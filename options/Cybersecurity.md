# Cybersecurity Career Roadmap — job-focused, 12–24 months

This roadmap is designed for **earning a living**, not just “learning hacking.” The safest entry strategy is:

> **Target first job:** SOC Analyst / Junior Cybersecurity Analyst / IT Security Analyst
> **Long-term direction:** Cloud Security, AppSec, Detection Engineering, GRC, or Incident Response

Cybersecurity has strong long-term demand: the U.S. BLS projects **29% growth for information security analysts from 2024–2034**, much faster than average. ([Bureau of Labor Statistics][1]) The NIST NICE Framework is also useful because it defines real cybersecurity work roles, skills, knowledge, and tasks used by employers. ([NIST][2])

---

## 0. Rule before starting

Only practice on:

* Your own lab machines
* Platforms like TryHackMe, Hack The Box, PortSwigger Academy, Blue Team Labs
* Authorized bug bounty programs
* Employer-approved environments

Do **not** attack real websites, Wi-Fi networks, accounts, or servers without permission.

---

# Phase 1 — Computer, networking, and Linux foundation

**Time:** 2–3 months
**Goal:** Become comfortable with how computers, networks, operating systems, and the internet work.

## Learn

### Computer fundamentals

You should understand:

* CPU, RAM, storage, processes
* Filesystems
* Virtual machines
* Command line basics
* How software runs
* Client-server model
* APIs
* Databases basics

## Best courses

### Free / low-cost

1. **Harvard CS50x**

   * Best for computer science thinking, programming basics, algorithms, memory, web basics, and problem solving.
   * CS50x is entry-level and teaches computational thinking, abstraction, algorithms, data structures, resource management, security, software engineering, and web development. ([Harvard University][3])

2. **Cisco Networking Academy — Introduction to Cybersecurity**

   * Good first cybersecurity overview.
   * Cisco lists Introduction to Cybersecurity as a beginner course. ([Cisco Networking Academy][4])

3. **Cisco Networking Academy — Networking Basics**

   * Learn OSI model, TCP/IP, IP addressing, DNS, DHCP, routing, switching, wireless, troubleshooting.
   * Cisco says the course covers networking foundations, devices, media, and protocols. ([Cisco Networking Academy][5])

4. **Linux Foundation — Introduction to Linux**

   * Best beginner Linux course.
   * It teaches Linux from both GUI and command-line perspectives across major Linux distributions. ([Linux Foundation - Education][6])

## Books

Read slowly; do not just collect books.

* **Computer Networking: A Top-Down Approach** — Kurose & Ross
* **How Linux Works** — Brian Ward
* **The Linux Command Line** — William Shotts
* **Code: The Hidden Language of Computer Hardware and Software** — Charles Petzold

## Practical tasks

Create a home lab:

* Install **VirtualBox** or **VMware Workstation Player**
* Install:

  * Ubuntu
  * Windows evaluation VM
  * Kali Linux only for labs
* Practice:

  * `cd`, `ls`, `cat`, `grep`, `find`, `chmod`, `chown`
  * `ip`, `netstat` / `ss`, `ping`, `traceroute`, `curl`, `wget`
  * users, permissions, services, logs
  * SSH into your Linux VM

## Portfolio deliverables

Publish these on GitHub:

* `linux-notes.md`
* `networking-notes.md`
* `tcp-ip-cheatsheet.md`
* Screenshots of your lab setup
* A short write-up: “How DNS works”

---

# Phase 2 — Python, scripting, SQL, and Git

**Time:** 2 months
**Goal:** Automate simple tasks, read logs, parse files, and use GitHub professionally.

## Learn

### Python

Focus on:

* Variables
* Loops
* Functions
* Files
* Regex
* JSON
* CSV
* Requests
* APIs
* Basic automation

### SQL

Focus on:

* SELECT
* WHERE
* JOIN
* GROUP BY
* INSERT / UPDATE / DELETE
* Basic database security
* SQL injection concept

### Git / GitHub

Learn:

* `git init`
* `git add`
* `git commit`
* `git push`
* branches
* README files
* Markdown documentation

## Best courses

1. **Python for Everybody — University of Michigan / Coursera**

   * Good beginner Python course.
   * The specialization teaches programming fundamentals, data retrieval, processing, and visualization using Python. ([Coursera][7])

2. **CS50’s Introduction to Programming with Python**

   * Good if you prefer Harvard-style structured assignments.
   * It teaches reading, writing, testing, and debugging Python code. ([edX][8])

3. **Google Cybersecurity Certificate**

   * Useful because it includes beginner-level Python, Linux, SQL, SIEM, IDS, communication, and portfolio activities. ([Coursera][9])

## Practical projects

Build:

1. **Log parser**

   * Input: Apache/Nginx log file
   * Output: top IPs, suspicious paths, 404 count, failed login count

2. **Password audit script**

   * Check password length and common weak patterns
   * Do not store real passwords

3. **Port scanner**

   * Only scan your own VM
   * Use Python sockets

4. **IOC checker**

   * Input: list of IPs/domains/hashes
   * Output: formatted CSV report

## Portfolio deliverables

GitHub repos:

* `python-log-analyzer`
* `basic-port-scanner-lab`
* `sql-injection-notes`
* `regex-for-security-logs.md`

---

# Phase 3 — Cybersecurity fundamentals

**Time:** 2–3 months
**Goal:** Understand core security concepts and prepare for entry-level security roles.

## Learn

### Core concepts

* CIA triad
* Authentication vs authorization
* MFA
* Encryption basics
* Hashing vs encryption
* Symmetric vs asymmetric crypto
* Public key infrastructure
* Firewalls
* VPNs
* IDS / IPS
* SIEM
* EDR
* Vulnerability management
* Risk
* Threats
* Vulnerabilities
* Controls
* Security policies
* Incident response
* Business continuity
* Disaster recovery

## Best courses

1. **Google Cybersecurity Professional Certificate — Coursera**

   * Very good beginner path.
   * Google describes it as beginner-friendly, no degree or experience required, and focused on job-ready cybersecurity skills. ([Coursera][9])

2. **ISC2 Certified in Cybersecurity Specialization — Coursera**

   * Good if you want to prepare for ISC2 CC.
   * Coursera lists this as a beginner-level ISC2 specialization. ([Coursera][10])

3. **Cisco Introduction to Cybersecurity**

   * Good free starting point.
   * Cisco Networking Academy offers beginner cybersecurity and networking courses. ([Cisco][11])

## Certifications for this phase

Choose **one** of these first:

### Option A — ISC2 Certified in Cybersecurity

Best if you are a complete beginner.

ISC2 says the CC proves foundational knowledge for entry-level or junior cybersecurity roles and has no work experience requirement. ([ISC2][12])

### Option B — CompTIA Security+

Best if you want a more recognized entry-level security certification.

The official Security+ SY0-701 objectives cover five domains: general security concepts; threats, vulnerabilities, and mitigations; security architecture; security operations; and security program management/oversight. ([Contentful][13])

### Option C — Google Cybersecurity Certificate

Best if you want structured beginner training plus portfolio activities.

Google’s certificate includes hands-on experience with Python, Linux, SQL, and SIEM tools. ([Google Skills][14])

## Recommended order

If you are starting from zero:

1. Google Cybersecurity Certificate
2. ISC2 CC
3. Security+

If money is limited:

1. Cisco free courses
2. Google Cybersecurity Certificate only if you can pay for Coursera
3. Security+ later when you can afford exam fees

---

# Phase 4 — SOC Analyst / Blue Team path

**Time:** 3–5 months
**Goal:** Become job-ready for SOC Analyst, Junior Security Analyst, or Cybersecurity Analyst roles.

This is the best first cybersecurity job target because it gives real-world exposure to alerts, logs, incidents, malware, phishing, SIEM, endpoint events, and escalation.

## Learn

### SOC skills

* What a SOC does
* Alert triage
* Severity classification
* False positives vs true positives
* Incident lifecycle
* Escalation
* Ticket writing
* Basic malware behavior
* Phishing analysis
* Windows event logs
* Linux logs
* Authentication logs
* Network logs
* Firewall logs
* DNS logs
* Proxy logs
* EDR alerts
* SIEM searches
* Basic threat hunting

### Frameworks

* Cyber Kill Chain
* MITRE ATT&CK
* NIST CSF
* Incident response lifecycle

MITRE ATT&CK is a globally accessible knowledge base of adversary tactics and techniques based on real-world observations. ([MITRE ATT&CK][15]) NIST CSF 2.0 provides guidance for organizations to manage cybersecurity risk and communicate cybersecurity outcomes. ([NIST Publications][16])

## Best platforms

### TryHackMe — SOC Level 1

Use this after basic networking and Linux.

TryHackMe’s SOC Level 1 path introduces defensive security topics and real-world analysis scenarios. ([TryHackMe][17])

### LetsDefend — SOC Analyst Learning Path

Good simulated SOC experience.

LetsDefend says its SOC Analyst path teaches technical skills for a Security Operations Center career and includes topics like Cyber Kill Chain, MITRE ATT&CK, phishing analysis, and web attack detection. ([LetsDefend][18])

### Hack The Box Academy — SOC Analyst path

More technical and structured.

HTB Academy says its SOC Analyst Job Role Path is for newcomers who want to become professional SOC analysts and covers security monitoring, analysis concepts, adversary tactics, and tools. ([academy.hackthebox.com][19])

### Blue Team Labs Online

Good for defensive investigations.

Blue Team Labs Online provides gamified defensive labs covering incident response, digital forensics, security operations, reverse engineering, and threat hunting. ([blueteamlabs.online][20])

### CyberDefenders

Good for DFIR and SOC practice.

CyberDefenders says its labs are built around real SOC investigations, threat behaviors, and defensive workflows. ([CyberDefenders][21])

## Tools to learn

### SIEM

Learn at least one:

* Splunk
* Microsoft Sentinel
* Elastic Security
* Wazuh
* Security Onion

### Endpoint / logs

* Windows Event Viewer
* Sysmon
* PowerShell logs
* Linux `/var/log`
* Zeek logs
* Suricata alerts
* Wireshark

### Malware / phishing basics

* Email headers
* URLs
* Attachments
* Sandboxes
* VirusTotal-style analysis
* Hashes
* YARA basics

## Home lab projects

Build at least 4:

1. **Wazuh SIEM lab**

   * Install Wazuh
   * Add Ubuntu and Windows agents
   * Generate failed logins
   * Write an incident report

2. **Phishing analysis report**

   * Analyze a sample phishing email from a training dataset
   * Extract sender, headers, links, attachments, indicators

3. **Windows attack log lab**

   * Install Sysmon
   * Run safe simulated events
   * Detect suspicious PowerShell behavior

4. **Network traffic analysis**

   * Use Wireshark
   * Analyze DNS, HTTP, TLS handshake, suspicious traffic

5. **MITRE ATT&CK mapping**

   * Pick one attack scenario
   * Map behavior to ATT&CK tactics and techniques

## Portfolio deliverables

Create a GitHub folder:

```md
/cybersecurity-portfolio
  /soc-labs
  /phishing-analysis
  /wireshark-labs
  /wazuh-siem-lab
  /incident-reports
  /mitre-attack-mapping
```

Each project should include:

* Objective
* Lab setup
* Tools used
* Screenshots
* Findings
* MITRE mapping
* Remediation
* Lessons learned

---

# Phase 5 — Web security and AppSec foundation

**Time:** 2–4 months
**Goal:** Understand web vulnerabilities so you can work in SOC, AppSec, bug bounty, or junior pentesting later.

## Learn

* HTTP / HTTPS
* Cookies
* Sessions
* JWT
* CORS
* Same-origin policy
* Authentication
* Authorization
* SQL injection
* XSS
* CSRF
* SSRF
* File upload vulnerabilities
* IDOR
* Access control issues
* Security headers
* API security
* Secure coding basics

OWASP Top 10 is the standard awareness document for developers and web application security, and the current released version is OWASP Top 10 2025. ([OWASP][22])

## Best resources

### PortSwigger Web Security Academy

This is one of the best free resources for web security.

PortSwigger describes Web Security Academy as a free online training center for web application security with interactive labs and learning materials. ([PortSwigger][23])

### OWASP Top 10

Use this as your checklist for web vulnerabilities.

### TryHackMe

Useful beginner rooms:

* Web Fundamentals
* OWASP Top 10
* Burp Suite
* Jr Penetration Tester path

### TCM Security — Practical Ethical Hacking

Good paid course if you want offensive basics.

TCM’s Practical Ethical Hacking course focuses on practical hacking techniques. ([TCM Security - Cyber Security][24])

### Hack The Box Academy — Penetration Tester path

Use this if you want to go deeper into pentesting.

HTB Academy says its Penetration Tester Job Role Path is for newcomers who want to become professional penetration testers and covers security assessment concepts, tools, attack tactics, and methodology. ([academy.hackthebox.com][25])

## Projects

Build:

1. **OWASP Top 10 notes**
2. **Burp Suite lab write-ups**
3. **SQL injection lab report**
4. **XSS lab report**
5. **Broken access control lab report**
6. **API security checklist**
7. **Secure login app**
8. **Vulnerable app remediation report**

## Warning

Do not start with pentesting as your only plan unless you are patient. Junior pentesting jobs are fewer and more competitive than SOC/GRC/IT-security roles. Learn web security, but use SOC or IT security as your first job target if you need income sooner.

---

# Phase 6 — Cloud security foundation

**Time:** 2–4 months
**Goal:** Become valuable for modern cybersecurity jobs.

## Learn

* Shared responsibility model
* IAM
* MFA
* Least privilege
* Cloud networking
* Security groups
* Logging
* Storage security
* Key management
* Cloud monitoring
* Cloud incident response
* Cloud misconfigurations

## Choose one cloud first

Pick **AWS** or **Microsoft Azure**.

### If targeting global startups / cloud-native companies

Choose AWS.

AWS Skill Builder has a Security Learning Plan designed to give beginners a guided path through cloud security topics. ([Amazon Web Services, Inc.][26])

### If targeting enterprises / Microsoft-heavy companies

Choose Azure / Microsoft Security.

Microsoft SC-900 demonstrates foundational knowledge of security, compliance, identity concepts, and related cloud-based Microsoft solutions. ([Microsoft Learn][27])

## Recommended cloud cert path

### AWS route

1. AWS Cloud Practitioner
2. AWS Security Learning Plan
3. AWS Certified Security — Specialty later, after real AWS experience

AWS says its Security Specialty prep plan is available through AWS Skill Builder. ([Amazon Web Services, Inc.][28])

### Microsoft route

1. SC-900
2. AZ-900
3. SC-200 or AZ-500 later

## Projects

Build:

1. **AWS IAM least privilege lab**
2. **S3 bucket security lab**
3. **CloudTrail logging lab**
4. **GuardDuty alert investigation**
5. **Azure Entra ID MFA policy notes**
6. **Microsoft Sentinel basic detection lab**

---

# Phase 7 — GRC, risk, and compliance

**Time:** 1–3 months
**Goal:** Open doors to less coding-heavy cybersecurity jobs.

GRC is useful if you are good at documentation, communication, policies, audits, and risk thinking.

## Learn

* Risk assessment
* Asset inventory
* Policies
* Standards
* Procedures
* Security controls
* ISO 27001 basics
* NIST CSF
* SOC 2 basics
* Vendor risk
* Business impact analysis
* Disaster recovery
* Incident response planning
* Access reviews
* Evidence collection

## Best resources

1. **NIST Cybersecurity Framework 2.0**

   * Official, free, highly respected.
   * NIST CSF 2.0 is designed to help organizations manage cybersecurity risk. ([NIST Publications][16])

2. **Coursera — GRC Approach to Managing Cybersecurity**

   * Covers governance, risk management, and compliance as part of cybersecurity management. ([Coursera][29])

3. **Coursera — Introduction to Cybersecurity & Risk Management**

   * Covers governance, compliance, foundational risk management, personnel security, and third-party security. ([Coursera][30])

## Projects

Build:

1. Risk register for a fake company
2. Security policy pack:

   * Password policy
   * Acceptable use policy
   * Incident response policy
   * Access control policy
3. Vendor risk questionnaire
4. NIST CSF gap assessment
5. Business impact analysis template

## Job titles

Apply for:

* GRC Analyst
* IT Risk Analyst
* Cyber Risk Analyst
* Compliance Analyst
* Security Analyst
* Third-Party Risk Analyst
* Information Security Analyst

---

# Phase 8 — Certifications roadmap

Do not collect certificates randomly. Use them to prove skills at each stage.

## Beginner

Choose 1–2:

* Google Cybersecurity Certificate
* ISC2 Certified in Cybersecurity
* CompTIA Security+

## Networking

Choose one only if needed:

* Cisco CCNA
* CompTIA Network+

CCNA is especially useful if your networking is weak or you want network security.

## SOC / blue team

Choose after labs:

* CompTIA CySA+
* Blue Team Level 1
* HTB Certified Defensive Security Analyst
* Microsoft SC-200 if going Microsoft Sentinel route

## Cloud security

Choose after cloud basics:

* Microsoft SC-900
* Microsoft AZ-900
* Microsoft AZ-500
* AWS Cloud Practitioner
* AWS Security Specialty later

## Pentesting / AppSec

Choose after strong hands-on practice:

* eJPT
* PNPT
* HTB CPTS
* Burp Suite Certified Practitioner

HTB describes CPTS as a hands-on certification assessing penetration testing skills. ([academy.hackthebox.com][31])

## GRC

Choose after fundamentals:

* ISC2 CC
* Security+
* ISO 27001 Foundation
* CISA later, after experience
* CISSP much later, after years of experience

ISC2 lists CISSP and CCSP as advanced certifications requiring significant work experience, while CC is entry-level with no work experience requirement. ([ISC2][32])

---

# Phase 9 — Best books by stage

## Beginner

* **Cybersecurity for Dummies**
* **Security+ Get Certified Get Ahead** — Darril Gibson
* **CompTIA Security+ Study Guide** — Mike Chapple / David Seidl

## Networking

* **Computer Networking: A Top-Down Approach**
* **CCNA 200-301 Official Cert Guide** — Wendell Odom

## Linux

* **How Linux Works**
* **The Linux Command Line**

## Blue team / SOC

* **Blue Team Handbook: SOC, SIEM & Threat Hunting**
* **The Practice of Network Security Monitoring** — Richard Bejtlich
* **Applied Incident Response** — Steve Anson

## Web security

* **Web Application Hacker’s Handbook**
* **Real-World Bug Hunting** — Peter Yaworski
* **Web Security for Developers** — Malcolm McDonald

## Cloud security

* **AWS Security Best Practices**
* **Azure Security Center / Microsoft Defender documentation**
* **Cloud Security and Privacy**

## GRC

* **How to Measure Anything in Cybersecurity Risk**
* **Information Security Policies Made Easy**
* **CISSP Official Study Guide** later, not at the beginning

---

# Phase 10 — Job-ready portfolio checklist

Before applying seriously, have these:

## Minimum portfolio

* 3 SOC incident reports
* 2 phishing analysis reports
* 2 Wireshark packet analysis write-ups
* 1 SIEM home lab
* 1 Linux hardening checklist
* 1 Windows logging/Sysmon lab
* 1 OWASP Top 10 web security write-up
* 1 cloud IAM/security lab
* 1 risk register or policy document

## Your GitHub should show

* Clear folder structure
* Clean README files
* Screenshots
* Commands used
* Findings
* Remediation steps
* What you learned
* No illegal targets
* No copied write-ups without understanding

---

# Phase 11 — Resume keywords

Use honest keywords only if you can explain them.

## Technical keywords

* Linux
* Windows
* Networking
* TCP/IP
* DNS
* HTTP
* SIEM
* IDS
* IPS
* EDR
* Wazuh
* Splunk
* Elastic
* Wireshark
* Sysmon
* MITRE ATT&CK
* Incident response
* Phishing analysis
* Log analysis
* Vulnerability management
* OWASP Top 10
* IAM
* MFA
* Cloud security
* Python
* SQL
* Git

## Soft skills

* Documentation
* Communication
* Analytical thinking
* Report writing
* Escalation
* Attention to detail
* Risk awareness
* Teamwork

---

# Phase 12 — Jobs to apply for

Do not only search “cybersecurity.” Search these titles:

## Best first jobs

* SOC Analyst Level 1
* Junior Security Analyst
* Cybersecurity Analyst
* Information Security Analyst
* IT Security Analyst
* Security Operations Analyst
* Threat Monitoring Analyst
* Incident Response Analyst — junior
* Vulnerability Management Analyst
* GRC Analyst
* IT Risk Analyst
* Compliance Analyst
* IAM Analyst
* NOC Analyst with security duties
* Help Desk / IT Support with security responsibilities

## Why include IT support and NOC?

Because cybersecurity is not always a direct first job. Many people enter through:

```md
IT Support → Sysadmin / Network Admin → SOC Analyst → Security Engineer
```

or:

```md
Web Developer → AppSec → Security Engineer
```

or:

```md
Compliance / Audit → GRC Analyst → Security Risk Manager
```

---

# 12-month study plan

## Months 1–2: Foundation

Learn:

* Computer basics
* Networking basics
* Linux basics
* Git/GitHub
* Basic Python

Resources:

* CS50x
* Cisco Networking Basics
* Linux Foundation Introduction to Linux
* Python for Everybody

Deliverables:

* Linux notes
* Networking notes
* Python scripts
* GitHub profile

---

## Months 3–4: Cybersecurity basics

Learn:

* Security concepts
* Threats
* Vulnerabilities
* Controls
* IAM
* Encryption
* SIEM basics
* Incident response

Resources:

* Google Cybersecurity Certificate
* ISC2 CC
* Security+ materials

Deliverables:

* Security+ notes
* Risk register
* Incident response notes
* Basic security glossary

---

## Months 5–7: SOC / blue team

Learn:

* Log analysis
* Alert triage
* Phishing analysis
* Wireshark
* SIEM
* MITRE ATT&CK
* Incident reports

Resources:

* TryHackMe SOC Level 1
* LetsDefend SOC Analyst path
* Blue Team Labs Online
* CyberDefenders
* HTB SOC Analyst path

Deliverables:

* 3 SOC reports
* 2 phishing reports
* 2 network analysis reports
* SIEM screenshots
* MITRE mapping

---

## Months 8–9: Web security

Learn:

* HTTP
* Burp Suite
* OWASP Top 10
* SQL injection
* XSS
* IDOR
* CSRF
* SSRF
* API security

Resources:

* PortSwigger Web Security Academy
* OWASP Top 10
* TryHackMe OWASP rooms
* TCM Practical Ethical Hacking if paid training is possible

Deliverables:

* 5 PortSwigger lab write-ups
* OWASP checklist
* Vulnerability remediation notes

---

## Months 10–11: Cloud + GRC

Learn:

* AWS or Azure basics
* IAM
* Logging
* Cloud security
* NIST CSF
* Risk management
* Policies

Resources:

* AWS Skill Builder Security Learning Plan
* Microsoft SC-900
* NIST CSF 2.0
* Coursera GRC course

Deliverables:

* Cloud IAM lab
* Cloud logging lab
* NIST CSF gap assessment
* Policy templates

---

## Month 12: Job application sprint

Do:

* Finalize resume
* Clean GitHub
* Create LinkedIn
* Apply daily
* Practice interviews
* Message recruiters
* Join cybersecurity communities
* Do mock interviews

Apply to:

* SOC Analyst
* Junior Security Analyst
* IT Security Analyst
* GRC Analyst
* Vulnerability Analyst
* IAM Analyst
* NOC Analyst with security tasks

---

# Weekly schedule

If you can study **3 hours/day**:

```md
Monday: Networking/Linux
Tuesday: Python/Scripting
Wednesday: Cybersecurity theory
Thursday: Labs
Friday: Labs + write-up
Saturday: Long project session
Sunday: Review + resume/GitHub update
```

If you can study **6 hours/day**:

```md
2 hours: course
2 hours: hands-on lab
1 hour: notes
1 hour: GitHub/write-up/interview practice
```

---

# Interview preparation

Prepare answers for:

## Technical

* What is DNS?
* What is TCP vs UDP?
* What happens when you visit a website?
* What is the CIA triad?
* What is a hash?
* What is MFA?
* What is phishing?
* What is SIEM?
* What is an IDS?
* What is the difference between vulnerability, threat, and risk?
* What is MITRE ATT&CK?
* What is SQL injection?
* What is XSS?
* What is least privilege?
* How do you investigate a failed login alert?
* How do you analyze a phishing email?
* How would you handle a malware alert?

## Behavioral

* Tell me about a time you solved a difficult problem.
* How do you handle pressure?
* How do you document your work?
* How do you learn new tools?
* What cybersecurity project are you proud of?
* What would you do if you were unsure whether an alert is malicious?

---

# The strongest “earning a living” strategy

Do not try to become an elite hacker first. Become employable first.

Best practical route:

```md
Networking + Linux + Python
→ Google Cybersecurity / Security+
→ SOC labs
→ SIEM portfolio
→ Apply for SOC / Junior Security Analyst jobs
→ Add cloud security
→ Specialize after first job
```

Your first target should be:

> **SOC Analyst / Junior Cybersecurity Analyst**

Your long-term specialization should be one of:

```md
SOC Analyst → Incident Responder → Detection Engineer
SOC Analyst → Cloud Security Engineer
Web Developer → AppSec Engineer
Security Analyst → GRC Analyst → Security Manager
SOC Analyst → Threat Hunter
Pentesting labs → Junior Pentester → AppSec / Red Team
```

# Final priority list

If you want the most efficient path, follow this order:

1. **Cisco Networking Basics**
2. **Linux Foundation Introduction to Linux**
3. **Python for Everybody**
4. **Google Cybersecurity Certificate**
5. **Security+ or ISC2 CC**
6. **TryHackMe SOC Level 1**
7. **LetsDefend SOC Analyst**
8. **Blue Team Labs / CyberDefenders**
9. **PortSwigger Web Security Academy**
10. **AWS or Microsoft SC-900**
11. **Build portfolio**
12. **Apply aggressively**

This is the safest roadmap for getting employable without wasting years.

[1]: https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm?utm_source=chatgpt.com "Information Security Analysts"
[2]: https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center?utm_source=chatgpt.com "NICE Framework Resource Center"
[3]: https://pll.harvard.edu/course/cs50-introduction-computer-science?utm_source=chatgpt.com "CS50: Introduction to Computer Science | Harvard University"
[4]: https://www.netacad.com/courses/introduction-to-cybersecurity?utm_source=chatgpt.com "Introduction to Cybersecurity by Cisco: Free Online Course"
[5]: https://www.netacad.com/courses/networking-basics?courseLang=en-US&utm_source=chatgpt.com "Networking Basics"
[6]: https://training.linuxfoundation.org/training/introduction-to-linux/?utm_source=chatgpt.com "Introduction to Linux (LFS101)"
[7]: https://www.coursera.org/specializations/python?utm_source=chatgpt.com "Python for Everybody Specialization"
[8]: https://www.edx.org/learn/python/harvard-university-cs50-s-introduction-to-programming-with-python?utm_source=chatgpt.com "HarvardX: CS50's Introduction to Programming with Python"
[9]: https://www.coursera.org/professional-certificates/google-cybersecurity?utm_source=chatgpt.com "Google Cybersecurity Professional Certificate"
[10]: https://www.coursera.org/specializations/certified-in-cybersecurity?utm_source=chatgpt.com "Certified in Cybersecurity Specialization"
[11]: https://www.cisco.com/site/us/en/learn/training-certifications/training/netacad/index.html?utm_source=chatgpt.com "Cisco Networking Academy"
[12]: https://www.isc2.org/certifications/cc?utm_source=chatgpt.com "CC Certified in Cybersecurity Certification"
[13]: https://assets.ctfassets.net/82ripq7fjls2/6TYWUym0Nudqa8nGEnegjG/0f9b974d3b1837fe85ab8e6553f4d623/CompTIA-Security-Plus-SY0-701-Exam-Objectives.pdf?utm_source=chatgpt.com "CompTIA Security+ Certification Exam Objectives"
[14]: https://www.skills.google/paths/2268?utm_source=chatgpt.com "Google Cybersecurity Certificate"
[15]: https://attack.mitre.org/?utm_source=chatgpt.com "MITRE ATT&CK®"
[16]: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf?utm_source=chatgpt.com "The NIST Cybersecurity Framework (CSF) 2.0"
[17]: https://tryhackme.com/path/outline/soclevel1?utm_source=chatgpt.com "SOC Level 1 Training"
[18]: https://app.letsdefend.io/path/soc-analyst-learning-path?utm_source=chatgpt.com "SOC Analyst Learning Path"
[19]: https://academy.hackthebox.com/path/preview/soc-analyst?utm_source=chatgpt.com "SOC Analyst Job Role Path | HTB Academy - Hack The Box"
[20]: https://blueteamlabs.online/?utm_source=chatgpt.com "Blue Team Labs Online - Cyber Range"
[21]: https://cyberdefenders.org/?utm_source=chatgpt.com "CyberDefenders: Blue Team Training for SOC Analysts & DFIR"
[22]: https://owasp.org/www-project-top-ten/?utm_source=chatgpt.com "OWASP Top Ten Web Application Security Risks"
[23]: https://portswigger.net/web-security?utm_source=chatgpt.com "Web Security Academy: Free Online Training from ..."
[24]: https://tcm-sec.com/academy/practical-ethical-hacking/?utm_source=chatgpt.com "Practical Ethical Hacking"
[25]: https://academy.hackthebox.com/path/preview/penetration-tester?utm_source=chatgpt.com "Penetration Tester Job Role Path - HTB Academy"
[26]: https://aws.amazon.com/training/learn-about/security/?utm_source=chatgpt.com "Security - Digital and Classroom Training"
[27]: https://learn.microsoft.com/en-us/credentials/certifications/security-compliance-and-identity-fundamentals/?utm_source=chatgpt.com "Security, Compliance, and Identity Fundamentals"
[28]: https://aws.amazon.com/certification/certified-security-specialty/?utm_source=chatgpt.com "AWS Certified Security - Specialty"
[29]: https://www.coursera.org/learn/grc-approach-to-managing-cybersecurity?utm_source=chatgpt.com "The GRC Approach to Managing Cybersecurity"
[30]: https://www.coursera.org/specializations/information-security?utm_source=chatgpt.com "Introduction to Cybersecurity & Risk Management"
[31]: https://academy.hackthebox.com/preview/certifications/htb-certified-penetration-testing-specialist?utm_source=chatgpt.com "HTB Certified Penetration Testing Specialist (HTB CPTS)"
[32]: https://www.isc2.org/certifications?utm_source=chatgpt.com "Leading Cybersecurity Certifications from ISC2"
