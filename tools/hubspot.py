#!/usr/bin/env python3
"""HubSpot CRM Integration Tool for Goldfib Capital.

Connects to HubSpot Portal 247824830 using the private app token configured
in HUBSPOT_TOKEN or ~/.config/goldfib/hubspot.env.

Usage:
    python3 tools/hubspot.py --test
    python3 tools/hubspot.py --info
    python3 tools/hubspot.py --contacts
    python3 tools/hubspot.py --create-contact email=lead@example.com firstname=Rajesh company="Mehta FO"
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path


def get_credentials():
    token = os.environ.get("HUBSPOT_TOKEN")
    portal_id = os.environ.get("HUBSPOT_PORTAL_ID", "247824830")

    env_file = Path.home() / ".config" / "goldfib" / "hubspot.env"
    if not token and env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("HUBSPOT_TOKEN="):
                token = line.split("=", 1)[1].strip().strip('"').strip("'")
            elif line.startswith("HUBSPOT_PORTAL_ID="):
                portal_id = line.split("=", 1)[1].strip().strip('"').strip("'")

    if not token:
        print("[!] Error: HUBSPOT_TOKEN not found in environment or ~/.config/goldfib/hubspot.env")
        print("    Run: export HUBSPOT_TOKEN=your_token")
        sys.exit(1)

    return token, portal_id


API_BASE = "https://api.hubapi.com"


def request(endpoint, method="GET", data=None):
    token, _ = get_credentials()
    url = f"{API_BASE}{endpoint}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "GoldfibCapital-HubSpotSync/1.0"
    }
    body = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode("utf-8")
            return json.loads(content) if content else {}
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        try:
            return {"error": True, "code": e.code, "details": json.loads(err_msg)}
        except Exception:
            return {"error": True, "code": e.code, "raw": err_msg}


def cmd_test():
    _, portal_id = get_credentials()
    print(f"[*] Testing connection to HubSpot Portal {portal_id}...")
    res = request("/account-info/v3/details")
    if res.get("error"):
        print(f"[!] Authentication failed: {res}")
        return False
    print(f"[✓] Connected successfully!")
    print(f"    Portal ID: {res.get('portalId')}")
    print(f"    Timezone:  {res.get('timeZone')}")
    print(f"    Hosting:   {res.get('dataHostingLocation')}")
    print(f"    Domain:    {res.get('uiDomain')}")
    return True


def cmd_contacts(limit=10):
    print(f"[*] Fetching recent contacts (limit {limit})...")
    res = request(f"/crm/v3/objects/contacts?limit={limit}&properties=email,firstname,lastname,company,createdate,hs_lead_status")
    if res.get("error"):
        print(f"[!] Error fetching contacts: {res}")
        return
    results = res.get("results", [])
    print(f"[✓] Found {len(results)} contacts:")
    for c in results:
        props = c.get("properties", {})
        print(f"    - {props.get('firstname', '')} {props.get('lastname', '')} <{props.get('email', 'no-email')}> | Company: {props.get('company', '—')} | Created: {props.get('createdate', '')}")


def cmd_create_contact(props):
    email = props.get("email")
    if not email:
        print("[!] Error: 'email' property is required.")
        return
    print(f"[*] Creating/updating contact for {email}...")
    payload = {"properties": props}
    res = request("/crm/v3/objects/contacts", method="POST", data=payload)
    if res.get("error"):
        print(f"[!] Creation error: {res}")
        return
    print(f"[✓] Contact successfully created with ID: {res.get('id')}")
    print(f"    URL: {res.get('url')}")


def main():
    parser = argparse.ArgumentParser(description="Goldfib Capital HubSpot Sync")
    parser.add_argument("--test", action="store_true", help="Test HubSpot API connection")
    parser.add_argument("--info", action="store_true", help="Show portal information")
    parser.add_argument("--contacts", action="store_true", help="List recent CRM contacts")
    parser.add_argument("--create-contact", nargs="*", help="Create contact key=val (e.g. email=x@y.com firstname=John company=Acme)")

    args = parser.parse_args()

    if args.test or args.info:
        cmd_test()
    elif args.contacts:
        cmd_contacts()
    elif args.create_contact:
        props = {}
        for item in args.create_contact:
            if "=" in item:
                k, v = item.split("=", 1)
                props[k] = v
        cmd_create_contact(props)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
