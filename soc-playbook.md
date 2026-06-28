# SOC Incident Response Playbook

## Alert

Brute Force SSH Detection Alert

Severity: High

---

## Initial Triage Questions

1. Which source IP triggered the alert?

2. How many failed authentication attempts occurred?

3. Which usernames were targeted?

4. Were any successful logins observed?

5. Did the activity occur within a short time window?

---

## Investigation Steps

### Step 1 — Review authentication activity

Search:

```spl
index=linux_auth
```

Review:

- Failed password events
- Successful authentication events
- Authentication patterns

---

### Step 2 — Identify source IP activity

Determine:

- Frequency of login attempts
- Number of targeted accounts
- Whether activity is isolated or repeated

---

### Step 3 — Review account targeting

Accounts observed:

- admin
- root
- test

Determine whether privileged accounts are being targeted.

---

### Step 4 — Assess severity

Indicators:

- Repeated login failures
- Multiple account targets
- Rapid authentication attempts

Severity:

High

---

## Containment Actions

If production activity were confirmed:

1. Block malicious source IP addresses
2. Enforce password resets if compromise suspected
3. Review account lockout policies
4. Continue monitoring authentication logs

---

## Escalation Criteria

Escalate if:

- Successful suspicious logins are observed
- Multiple systems become affected
- Persistence behavior is identified

---

## MITRE ATT&CK

Technique:

T1110 — Brute Force
