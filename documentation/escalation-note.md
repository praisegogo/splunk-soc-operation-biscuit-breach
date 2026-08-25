# SOC Level 1 Escalation Note

## Incident Title

Possible Web Activity from 8.8.8.8

## Summary

The source IP 8.8.8.8 generated repeated failed requests against the web application. The activity includes repeated HTTP 401, 403 and 404 responses, which may indicate reconnaissance or repeated attempts to access unauthorised resources.

## Evidence

- **Source IP:** 8.8.8.8
- **Number of failed requests:** 354 identified across HTTP 401, 403 and 404 events
- **Status codes observed:** 401, 403 and 404
- **Time period:** 22 June 2026 – 24 June 2026
- **Affected pages:** Not established by the Task 8 investigation SPL

## Initial Assessment

The combination of repeated 404 responses and authentication/access-denied responses from the same source may indicate suspicious scanning, attempted access to restricted resources, or abnormal user behaviour. The volume and variety of failed requests warrant further investigation.

## Recommended Action

Escalate to SOC Level 2 / Incident Response for deeper analysis. SOC Level 2 should investigate the requested URLs, event timestamps, request frequency and authentication activity associated with 8.8.8.8 to determine whether the behaviour is malicious.