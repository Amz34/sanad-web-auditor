# Sanad Web Auditor & Design System Extractor (سند)

```
   ____                       _     _ _       _   _             
  / ___|  __ _ _ __   __ _  __| |   | (_) __ _| | | |_ _ __ ___  
  \___ \ / _` | '_ \ / _` |/ _` |___| | |/ _` | |_| | '_ ` _ \ \ 
   ___) | (_| | | | | (_| | (_| |___| | | (_| |  _  | | | | | | |
  |____/ \__,_|_| |_|\__,_|\__,_|   |_|_|\__, |_| |_|_| |_| |_| |
                                         |___/                  
```

**Sanad Web Auditor** is an enterprise-grade web optimization and AI-ready design extractor built for high-performance deployment. It takes any URL, audits it against Google's PageSpeed Insights (Lighthouse), and spits out a **highly actionable `CLAUDE.md` fix plan** injected with **Sanad Brand Gates**.

This is perfect for feeding directly to AI coding agents like Claude Code, Hermes, Cursor, or ChatGPT to implement instant web fixes without human overhead.

---

## 🚀 Direct Product & Resource Links

To extract designs or run audits directly on your laptop or mobile:

- **Official Web App (Design Extraction)**: [visual-dna.live](https://visual-dna.live/) (Reverse-engineer any design system in 1 click)
- **VisualDNA Extension (Design Extraction)**: [VisualDNA Chrome Web Store](https://chromewebstore.google.com/detail/visualdna-%E2%80%93-design-system/ljilnejdgkedledpbhncgfdojfmnnaib)
- **Web App (Performance Audits)**: [lighthouse-md.com](https://lighthouse-md.com/) (Generate CLAUDE.md online)
- **Lighthouse-MD Extension**: [Lighthouse-MD Chrome Web Store](https://chromewebstore.google.com/detail/lighthouse-md-pagespeed-a/cphchklbbkhglppapokhdbhnkhghhhnk)

---

## 🛠️ Installation & CLI Usage

### Instant Run (NPX)
No local installation required! Simply run:

```bash
npx @sanad-io/web-auditor https://imaa-kiosk.pages.dev
```

This generates a branded `CLAUDE.md` in your current workspace directory. Feed it straight to Claude Code and say:
> *"Read CLAUDE.md and fix the failing audits."*

### Options
```bash
# Audits with desktop strategy instead of mobile
npx @sanad-io/web-auditor https://imaa-kiosk.pages.dev --strategy desktop

# Outputs to a custom file path
npx @sanad-io/web-auditor https://imaa-kiosk.pages.dev --output AUDIT.md
```

---

## 🔒 Sanad Brand Gates (Injected into CLAUDE.md)
Every generated fix plan automatically embeds **Sanad's Core Guidelines**:
- 🛑 **No Living Beings / Faces**: Keep all layouts clean, abstract, and architectural. No human photography.
- 🛑 **Bilingual RTL Support**: Fully support RTL alignment and native script-specific Arabic font stacks.
- 🛑 **AI-Free English Copy**: Pure, concise English copywriting with zero emojis or filler.

---

## 💎 GitHub Push & Cron Automation
To ensure continuous delivery and prevent performance regressions, add this workflow as `.github/workflows/sanad-audit.yml` to your repositories:

```yaml
name: Sanad Performance & QA Audit

on:
  push:
    branches: [ main ]
  schedule:
    - cron: '0 0 * * 0' # Weekly on Sundays

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20

      - name: Run Sanad Web Auditor
        run: npx @sanad-io/web-auditor https://imaa-kiosk.pages.dev

      - name: Commit and Push Audit Plan
        run: |
          git config --global user.name "Sanad Auditor"
          git config --global user.email "auditor@sanad.io"
          git add CLAUDE.md
          git diff-index --quiet HEAD || git commit -m "chore(audit): auto-update CLAUDE.md performance fix plan [skip ci]"
          git push
```

---
*Developed with ❤️ by Aamir Zahran (Sanad AI).*
