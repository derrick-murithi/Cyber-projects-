# 🛡️ Cybersecurity Projects Collection

A comprehensive collection of 10 educational cybersecurity tools covering cryptography, network security, incident response, and application security. Each project is fully documented and ready to use.

> ⚠️ **Legal Disclaimer**: These tools are for educational purposes and authorized testing only. Unauthorized access to computer systems is illegal. Only use these tools on systems you own or have explicit written permission to test.

## 📋 Projects Overview

### 1. 🔐 Password Strength Checker
**Location:** `01-password-strength-checker/`

Analyzes password security across multiple dimensions: length, character diversity, entropy, and common password detection. Provides actionable improvement suggestions.

- **Key Features:** Multi-factor scoring, entropy calculation, breach detection
- **Skills:** Password security, regex, entropy mathematics
- **Dependencies:** Python 3.7+ (no external libs)

```bash
cd 01-password-strength-checker
python password_checker.py
```

---

### 2. 🔑 Caesar Cipher Tool
**Location:** `02-caesar-cipher/`

Educational implementation of the classic Caesar cipher with encryption, decryption, brute-force cracking, and frequency analysis for cryptanalysis learning.

- **Key Features:** Encrypt/decrypt, try all 25 shifts, frequency-based guessing
- **Skills:** Classical cryptography, frequency analysis
- **Dependencies:** Python 3.7+ (no external libs)

```bash
cd 02-caesar-cipher
python caesar_cipher.py
```

---

### 3. 🔍 Port Scanner
**Location:** `03-port-scanner/`

Fast multi-threaded TCP port scanner identifies open ports on target hosts. Includes service mapping and configurable scan ranges.

- **Key Features:** Multi-threading, service detection, flexible ranges
- **Skills:** Network reconnaissance, socket programming, threading
- **Dependencies:** Python 3.7+
- **⚠️ Legal:** Only scan hosts you own or have permission to test

```bash
cd 03-port-scanner
python port_scanner.py
```

---

### 4. 💥 Hash Cracker (Dictionary Attack)
**Location:** `04-hash-cracker/`

Demonstrates how unsalted password hashes are vulnerable via dictionary attacks. Supports MD5, SHA1, SHA256, and SHA512 with performance metrics.

- **Key Features:** MD5/SHA1/SHA256/SHA512, wordlist-based cracking, hash identifier
- **Skills:** Hash functions, dictionary attacks, why salting matters
- **Dependencies:** Python 3.7+ (no external libs)

```bash
cd 04-hash-cracker
python hash_cracker.py
```

---

### 5. 📡 Network Packet Analyzer
**Location:** `05-packet-analyzer/`

Analyzes PCAP captures to summarize traffic, extract DNS queries, identify HTTP hosts, and flag suspicious network behavior.

- **Key Features:** Protocol breakdown, DNS/HTTP extraction, suspicious port detection
- **Skills:** Network forensics, PCAP analysis, traffic patterns
- **Dependencies:** `pip install scapy`
- **⚠️ Legal:** Only analyze traffic on networks you own or have permission to monitor

```bash
cd 05-packet-analyzer
pip install scapy
python packet_analyzer.py
```

---

### 6. 📋 Security Log Analyzer
**Location:** `06-log-analyzer/`

Parses web server access logs to detect brute force attempts, path scanning, suspicious file access, and generates security alerts.

- **Key Features:** Brute-force detection, scanner detection, sensitive path tracking
- **Skills:** Log parsing, regex, anomaly detection
- **Dependencies:** Python 3.7+ (no external libs)

```bash
cd 06-log-analyzer
python log_analyzer.py
```

---

### 7. 🛡️ XSS Payload Detector
**Location:** `07-xss-detector/`

Detects 15 different types of Cross-Site Scripting (XSS) attack patterns in user input. Includes HTML sanitization and severity ratings.

- **Key Features:** 15 XSS signatures, severity classification, auto-sanitization
- **Skills:** Web security, input validation, XSS attack types
- **Dependencies:** Python 3.7+ (no external libs)

```bash
cd 07-xss-detector
python xss_detector.py
```

---

### 8. 🔐 Steganography Tool
**Location:** `08-steganography/`

Hide secret messages inside images using LSB (Least Significant Bit) steganography. Messages are compressed and embedded in color channels.

- **Key Features:** LSB embedding, automatic compression, capacity calculator
- **Skills:** Steganography, image processing, compression
- **Dependencies:** `pip install Pillow`

```bash
cd 08-steganography
pip install Pillow
python steganography.py
```

---

### 9. 🔏 File Integrity Monitor (FIM)
**Location:** `09-file-integrity-monitor/`

Monitors files and directories by comparing cryptographic hashes. Detects unauthorized modifications, additions, and deletions.

- **Key Features:** Baseline snapshots, continuous monitoring, change detection
- **Skills:** File hashing, baseline comparison, system monitoring
- **Dependencies:** Python 3.8+ (walrus operator)

```bash
cd 09-file-integrity-monitor
python file_integrity_monitor.py
```

---

### 10. 🌐 Subdomain Enumerator
**Location:** `10-subdomain-enumerator/`

Discovers subdomains for a target domain via DNS resolution against a wordlist. Identifies live subdomains and their IP addresses.

- **Key Features:** Multi-threaded enumeration, custom wordlist support, results export
- **Skills:** OSINT, DNS reconnaissance, attack surface mapping
- **Dependencies:** Python 3.7+
- **⚠️ Legal:** Only enumerate domains you own or have explicit permission to test

```bash
cd 10-subdomain-enumerator
python subdomain_enumerator.py
```

---

## 🚀 Quick Start

### 1. Clone or Download This Repository

```bash
# Navigate to the projects directory
cd cybersec-projects
```

### 2. Install Optional Dependencies

Some projects require external libraries:

```bash
pip install scapy Pillow
```

### 3. Explore Each Project

Each project has its own `README.md` with detailed documentation:

```bash
cd 01-password-strength-checker
cat README.md
python password_checker.py
```

---

## 📚 Learning Path

**Beginner:**
1. Password Strength Checker — understand password security metrics
2. Caesar Cipher — learn classical cryptography
3. XSS Detector — understand web vulnerabilities
4. Steganography — explore hidden communication

**Intermediate:**
5. Hash Cracker — learn why unsalted hashes fail
6. Port Scanner — network reconnaissance fundamentals
7. Log Analyzer — incident response basics
8. File Integrity Monitor — system hardening

**Advanced:**
9. Packet Analyzer — network forensics
10. Subdomain Enumerator — OSINT and attack surface mapping

---

## 🛠️ Technology Stack

| Skill | Projects |
|-------|----------|
| **Cryptography** | Caesar Cipher, Hash Cracker, Steganography |
| **Network Security** | Port Scanner, Packet Analyzer, Subdomain Enumerator |
| **Web Security** | XSS Detector, Log Analyzer |
| **System Security** | File Integrity Monitor |
| **Python Fundamentals** | All projects |
| **Threading** | Port Scanner, Subdomain Enumerator |
| **Regex** | Password Checker, Log Analyzer, XSS Detector |

---

## 📖 Concepts Covered

- ✅ Password entropy and strength metrics
- ✅ Classical and modern cryptography
- ✅ Hash functions and their vulnerabilities
- ✅ Network reconnaissance techniques
- ✅ Steganography and covert communication
- ✅ Web application security (XSS)
- ✅ Incident response and log analysis
- ✅ File integrity and change detection
- ✅ DNS and subdomain enumeration
- ✅ Multi-threading and performance optimization
- ✅ Regular expression pattern matching
- ✅ Security best practices

---

## ⚖️ Legal & Ethical Guidelines

**These tools are for authorized use only:**

- ✅ **Allowed:** Testing systems you own, authorized penetration testing with written consent
- ❌ **Illegal:** Unauthorized network scanning, cracking passwords on systems you don't own, monitoring traffic without consent

**Responsible disclosure:**
- Always have written permission before testing
- Report vulnerabilities responsibly
- Never exploit vulnerabilities for malicious purposes

---

## 🔗 GitHub Setup

To add these projects to GitHub:

```bash
git init
git add .
git commit -m "Add 10 cybersecurity educational tools"
git remote add origin https://github.com/YOUR_USERNAME/cybersec-projects
git push -u origin main
```

### Suggested GitHub Repository Description:
```
🛡️ Educational cybersecurity tools collection: password strength 
checker, port scanner, XSS detector, hash cracker, and more. 
Learn network security, cryptography, and incident response.
```

### Suggested GitHub Topics:
```
cybersecurity, security-tools, educational, python, hacking, 
penetration-testing, network-security, cryptography, xss, 
incident-response
```

---

## 📞 Support & Contributions

Each project is self-contained with:
- ✅ Fully documented code with docstrings
- ✅ Interactive CLI interface
- ✅ Comprehensive README with examples
- ✅ No dependencies (except optional Scapy and Pillow)

### Extending Projects

Suggested improvements:
- Add `--output` and `--format` flags for exporting results
- Implement `--config` file support for tool settings
- Add unit tests with pytest
- Create Docker containers for each tool
- Add REST API wrappers with Flask
- Build web dashboard for results visualization

---

## 📄 License

All projects are released under the **MIT License**. See individual project READMEs for details.

---

## 🎓 Educational Resources

### Learn More About:
- **Cryptography:** Try the Caesar Cipher, then move to modern crypto libraries
- **Network Security:** Start with Port Scanner, advance to packet analysis
- **Web Security:** XSS Detector teaches OWASP top vulnerabilities
- **Incident Response:** Log Analyzer + File Integrity Monitor for forensics
- **OSINT:** Subdomain Enumerator for reconnaissance

### Recommended Next Steps:
1. Modify these tools to add new features
2. Combine multiple tools into an integrated security suite
3. Create automated versions with cron jobs or systemd timers
4. Build a REST API around these tools
5. Contribute improvements back to this repo

---

## ⭐ Credits

Built as a comprehensive educational resource for cybersecurity learning and authorized security testing.

Happy hacking! 🚀

---

**Last Updated:** 2024
**Total Projects:** 10
**Lines of Code:** 2,500+
**Documentation:** 100%
