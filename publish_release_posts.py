import json
import urllib.request
import urllib.error
import subprocess
import sys

LI_AUTHOR = "urn:li:person:ZXkhXV9MAp"
LI_TOKEN_PATH = "/home/ubuntu/linkedin_token.json"

LINKEDIN_POST_TEXT = """STOP WASTING HOURS TRANSLATING LIGHTHOUSE AUDITS FOR AI AGENTS... 🤯

Lighthouse ka raw JSON ya accordion reports developers ke liye hain, AI coding agents (Claude Code, Hermes, Cursor) ke liye nahi.

So we built something legendary: Sanad Web Auditor (سند) 🧬

Ab kisi bhi live website ka PageSpeed performance and visual design DNA extract karein in 1-click and get a highly actionable, branded CLAUDE.md fix plan.

What makes it legendary:
⚡ Raw PageSpeed Insights → Actionable AI-ready markdown.
🛑 Injects Mandatory Brand Gates (No human faces, native Arabic RTL support, mobile-first kiosk constraints).
📦 Complete open-source design system token extractor.

Just run:
npx sanad-web-auditor <your-site-url>

Feed the CLAUDE.md straight to your agent and watch it cook! 

👉 Get started or contribute: https://github.com/Amz34/sanad-web-auditor

#SoftwareEngineering #DevOps #AI #WebPerformance #DesignTokens #OpenSource #FullStack #NodeJS"""

BLUESKY_POST_TEXT = """Stop wasting hours translating Lighthouse audits for AI agents. 🤯

Run one command:
npx sanad-web-auditor <your-site>

Get an instant, branded CLAUDE.md fix plan + design DNA injected with strict Brand Gates (RTL, abstract-only). 

100% free and open-source: 
https://github.com/Amz34/sanad-web-auditor"""

def publish_to_linkedin():
    print("\n--- PUBLISHING TO LINKEDIN ---")
    try:
        with open(LI_TOKEN_PATH) as f:
            tok = json.load(f)["access_token"]
    except Exception as e:
        print("Failed to read LinkedIn token:", e)
        return None

    # Construct the UGC Post payload with an ARTICLE media category
    payload = {
        "author": LI_AUTHOR,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": LINKEDIN_POST_TEXT},
                "shareMediaCategory": "ARTICLE",
                "media": [{
                    "status": "READY",
                    "description": {
                        "text": "Enterprise-level PageSpeed audit and AI-ready design system generator branded under Sanad (سند)."
                    },
                    "originalUrl": "https://github.com/Amz34/sanad-web-auditor",
                    "title": {
                        "text": "Sanad Web Auditor & Design Extractor"
                    }
                }]
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
    }

    req = urllib.request.Request(
        "https://api.linkedin.com/v2/ugcPosts",
        data=json.dumps(payload).encode(),
        headers={
            "Authorization": f"Bearer {tok}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0"
        },
        method="POST"
    )

    try:
        resp_raw = urllib.request.urlopen(req).read()
        resp = json.loads(resp_raw.decode())
        post_urn = resp["id"]
        post_url = f"https://www.linkedin.com/feed/update/{post_urn}"
        print(f"LinkedIn Published Successfully: {post_url}")
        return post_url
    except urllib.error.HTTPError as e:
        print("LinkedIn Post Fail:", e.code, e.read().decode())
        return None
    except Exception as e:
        print("LinkedIn Error:", e)
        return None

def publish_to_bluesky():
    print("\n--- PUBLISHING TO BLUESKY ---")
    cmd = [
        "/home/ubuntu/clients/invertio/bin/bsky-infra",
        "post",
        "--text", BLUESKY_POST_TEXT,
        "--link", "https://github.com/Amz34/sanad-web-auditor",
        "--link-title", "Sanad Web Auditor (Open-Source)",
        "--link-desc", "PageSpeed-to-CLAUDE.md performance audit and design DNA extraction."
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        out = json.loads(res.stdout.strip())
        if out.get("ok"):
            post_url = out.get("url")
            print(f"Bluesky Published Successfully: {post_url}")
            return post_url
        else:
            print("Bluesky post failed:", out)
            return None
    except Exception as e:
        print("Bluesky run error:", e)
        return None

if __name__ == "__main__":
    li_url = publish_to_linkedin()
    bsky_url = publish_to_bluesky()

    print("\n=== FINAL SUMMARY ===")
    print("LinkedIn Link:", li_url)
    print("Bluesky Link:", bsky_url)
