# Project 3: Phishing Awareness Analysis

**Track:** Threat Detection-Social Engineering Defense
**Skills:** Threat analysis, red-flag identification, triage decision-making

## Objective

Analyze sample phishing emails to identify deceptive tactics, apply a structured red-flag checklist, and reach a clear triage verdict (Safe / Suspicious / Malicious) for each — mirroring real Tier-1 SOC email-triage work.

## Methodology

A 9-point Red Flag Checklist (sender-domain mismatch, urgency language, suspicious links, generic greetings, credential requests, unexpected attachments, grammar issues, mismatched reply-to, too-good-to-be-true offers) was applied to 5 sample emails, followed by a decision tree:

- **0–1 flags** → Safe → Close
- **2–3 flags** → Suspicious → Warn User
- **4+ flags or any critical flag** → Malicious → Block & Escalate

## Samples Analyzed

| # | Type | Verdict |
|---|---|---|
| 1 | Fake Microsoft account suspension (mass phishing) | 🔴 Malicious |
| 2 | CEO wire transfer request (Business Email Compromise) | 🔴 Malicious |
| 3 | Fake MFA re-enrollment via QR code (Quishing) | 🔴 Malicious |
| 4 | LinkedIn engagement notification | ✅ Safe |
| 5 | GitHub SSH key security alert | ✅ Safe |

Full checklist scoring, reasoning, and decision tree are documented in the report.

## Files

- [`Phishing_Triage_Report.docx`](./Phishing_Triage_Report.docx) — full report: checklist, decision tree, and 5 worked sample analyses with verdicts and reasoning
