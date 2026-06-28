# Detection Logic Explanation

This project detects brute-force SSH attempts by analyzing Linux authentication logs.

## Detection Method

- Extract source IP addresses from failed SSH login attempts
- Count number of failures per IP
- Flag IPs with 3 or more failed attempts as potential brute-force attacks

## Why this matters

Brute-force SSH attacks are a common method used by attackers to gain unauthorized access to systems. Detecting repeated failed login attempts helps identify malicious activity early.

## SOC Analyst Perspective

A SOC analyst would:
- Investigate repeated failed login attempts
- Correlate IP addresses with threat intelligence
- Escalate high-frequency attack sources
- Monitor for lateral movement attempts
