# Incident Timeline

## Security Event Timeline

| Time | Event | Notes |
|-------|--------|-------|
| 10:12:01 | Failed SSH login attempt detected | User: admin |
| 10:12:05 | Failed SSH login attempt detected | User: admin |
| 10:12:09 | Failed SSH login attempt detected | User: admin |
| 10:13:14 | Successful authentication observed | User: royce |
| 10:14:20 | Failed SSH login attempt detected | User: root |
| 10:14:25 | Failed SSH login attempt detected | User: root |
| 10:14:30 | Failed SSH login attempt detected | User: root |
| 10:15:01 | Privileged command executed | apt update |
| 10:16:44 | Failed SSH login attempt detected | User: test |
| 10:17:01 | Successful authentication observed | User: admin |

---

## Timeline Assessment

Repeated failed login attempts occurred in a short time period from the same source systems.

Multiple privileged usernames were targeted:

- admin
- root
- test

Observed activity is consistent with password guessing and brute-force authentication behavior.

No confirmed malicious successful authentication events were identified.

---

## Analyst Recommendation

Escalate activity for continued monitoring and validate account security controls if this were a production environment.
