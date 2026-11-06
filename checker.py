import requests

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy",
]

url = input("Enter website (e.g. example.com): ")

if not url.startswith("http"):
    url = "https://" + url

response = requests.get(url, timeout=10)

print(f"\nResults for {url}\n")

found = 0
for header in SECURITY_HEADERS:
    if header in response.headers:
        print(f"[PASS] {header}")
        found += 1
    else:
        print(f"[MISSING] {header}")

print(f"\nScore: {found}/{len(SECURITY_HEADERS)}")