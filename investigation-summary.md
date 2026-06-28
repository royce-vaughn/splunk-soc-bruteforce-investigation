# Security Investigation Summary

## Alert Information

**Alert Name:** Brute Force SSH Detection Alert

**Alert Severity:** High

**Detection Time Window:** Last 15 Minutes

**Detection Logic:**
- Alert triggers when a source IP generates 3 or more failed SSH login attempts.

---

## Incident Overview

Multiple failed SSH login attempts were detected from external source IP addresses against Linux authentication services.

Repeated authentication failures within a short period indicate behavior consistent with a brute-force login attempt.

---

## Evidence Collected

### Source IPs Identified

- 45.33.12.89
- 185.220.101.77
- 103.21.244.55

### Failed Login Counts

| Source IP | Failed Attempts |
|------------|----------------|
| 45.33.12.89 | 3 |
| 185.220.101.77 | 3 |
| 103.21.244.55 | 1 |

### Targeted Usernames

- admin
- root
- test

---

## Investigation Findings

Observed repeated failed authentication attempts from the same source IPs targeting privileged accounts.

Indicators suggest password guessing behavior associated with brute-force activity.

No evidence of successful malicious authentication was identified within the analyzed dataset.

---

## Threat Assessment

**Classification:** Potential Brute Force Activity

**Risk Level:** High

**MITRE ATT&CK Mapping:**

Technique:
T1110 — Brute Force

---

## Recommended Actions

1. Block identified malicious IP addresses
2. Continue monitoring authentication events
3. Reset credentials if compromise is suspected
4. Review account lockout policies
5. Investigate additional indicators of persistence

---

## Analyst Notes

This investigation was conducted in a simulated SOC lab environment using Splunk and Python.

All log data and IP addresses were generated for educational and portfolio purposes.
