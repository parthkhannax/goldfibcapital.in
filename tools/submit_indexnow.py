#!/usr/bin/env python3
"""Submit all URLs from sitemap.xml to Bing and IndexNow-enabled search engines.

Usage:
    python3 tools/submit_indexnow.py
"""
import json
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITEMAP = ROOT / "sitemap.xml"
KEY = "goldfib8c20e549fb8172901a3cb24e6"
KEY_FILE = ROOT / f"{KEY}.txt"
HOST = "goldfibcapital.in"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

ENDPOINTS = [
    ("IndexNow API", "https://api.indexnow.org/indexnow"),
    ("Bing IndexNow", "https://www.bing.com/indexnow"),
]


def get_urls_from_sitemap():
    if not SITEMAP.exists():
        print(f"Error: {SITEMAP} not found.")
        sys.exit(1)

    tree = ET.parse(SITEMAP)
    root = tree.getroot()
    # Handle XML namespace
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = []
    for loc in root.findall(".//sm:loc", ns):
        if loc.text:
            urls.append(loc.text.strip())

    if not urls:
        # Fallback if namespace differs
        for loc in root.iter():
            if loc.tag.endswith("loc") and loc.text:
                urls.append(loc.text.strip())

    return urls


def submit(endpoint_name, endpoint_url, urls):
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        endpoint_url,
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "GoldfibCapital-IndexNow/1.0",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            status = resp.status
            reason = resp.reason
            print(f"[{endpoint_name}] Status {status} ({reason}): Successfully submitted {len(urls)} URLs.")
            return True, status
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"[{endpoint_name}] HTTPError {e.code} ({e.reason}): {body}")
        return False, e.code
    except Exception as e:
        print(f"[{endpoint_name}] Failed: {e}")
        return False, None


def main():
    if not KEY_FILE.exists():
        KEY_FILE.write_text(f"{KEY}\n")
        print(f"Created IndexNow key file: {KEY_FILE.name}")

    urls = get_urls_from_sitemap()
    print(f"Found {len(urls)} URLs in sitemap ({SITEMAP.name}).")
    articles = [u for u in urls if "/blog/" in u and u != f"https://{HOST}/blog/" and not u.endswith("/walkthrough/")]
    print(f"  - {len(articles)} research articles")
    print(f"  - {len(urls) - len(articles)} core site pages")

    print("\nSubmitting batch to search engines via IndexNow...")
    for name, endpoint in ENDPOINTS:
        submit(name, endpoint, urls)

    print("\nNote: Make sure to commit and push changes (including the key file and sitemap.xml) to GitHub Pages")
    print("so search engines can verify keyLocation if this is the first submission.")


if __name__ == "__main__":
    main()
