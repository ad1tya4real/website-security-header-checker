
# Website Security Header Checker

A beginner-friendly Python tool that checks whether a website uses important HTTP security headers.

## Headers checked
- Strict-Transport-Security
- Content-Security-Policy
- X-Frame-Options
- X-Content-Type-Options
- Referrer-Policy
- Permissions-Policy

## How to run
1. Install Python 3.10 or newer
2. Install the library: `pip install requests`
3. Run: `python checker.py`
4. Enter a website, for example `github.com`

## Planned features
- Colored output and risk ratings
- Explanations and fixes for each missing header
- Simple web interface

## Note
Only test websites you own or public sites. This tool only reads headers that every browser already receives.
