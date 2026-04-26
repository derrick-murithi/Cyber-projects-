# Cybersecurity Projects Collection

> **Legal Disclaimer**: These tools are for educational purposes and authorized testing only. Unauthorized access to computer systems is illegal. Only use these tools on systems you own or have explicit written permission to test.

## Projects Overview

### 1. Password Strength Checker
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

### 2. Caesar Cipher Tool
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

### 3. Port Scanner
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

### 4. Hash Cracker (Dictionary Attack)
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

### 5. Network Packet Analyzer
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

### 6. Security Log Analyzer
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

### 7. XSS Payload Detector
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

### 8. Steganography Tool
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

### 9. File Integrity Monitor (FIM)
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

### 10. Subdomain Enumerator
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
