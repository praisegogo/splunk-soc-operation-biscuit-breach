# Incident Response Mini-Playbook

## Suspicious Web Activity

This mini-playbook documents the response process used to investigate suspicious web activity identified during the SOC Level 1 investigation. The purpose is to validate the activity, enrich the available evidence, classify the behaviour, recommend appropriate containment actions, and document the case.

## Step 1: Validate the Alert

The first step is to validate the suspicious activity identified during the SOC Level 1 investigation.

The investigation identified `8.8.8.8` as a source IP generating a significant number of failed web requests. The activity included HTTP 401, 403 and 404 responses, which warranted further investigation.

The initial validation considered:

- Source IP address
- HTTP status codes
- Time period of the activity
- Requested web pages and resources
- Frequency of failed requests

Based on the volume and type of failed requests observed, the activity was escalated from SOC Level 1 to SOC Level 2 for further investigation.

## Step 2: Enrich the Evidence

To obtain additional context about the activity associated with the identified source IP, the following SPL search was performed:

```spl
index=main sourcetype=access_combined clientip="8.8.8.8"
| table _time clientip method uri_path status useragent
```

The search returned **1,459 events** associated with `8.8.8.8`.

The investigation exposed the following fields:

- Event timestamp (`_time`)
- Source IP (`clientip`)
- HTTP request method (`method`)
- Requested resource (`uri_path`)
- HTTP response status (`status`)
- User agent (`useragent`)

These fields provided additional context for evaluating the behaviour of the source IP and examining the individual web requests associated with it.

## Step 3: Classify the Activity

The activity was classified as **possible reconnaissance / suspicious web activity**.

The source generated repeated failed requests across different HTTP status codes and accessed multiple application resources. In particular, the presence of repeated 404 responses may indicate attempts to discover available or unavailable resources within the web application.

The 401 and 403 responses also indicate unsuccessful attempts to access resources requiring authentication or appropriate permissions.

The available evidence is therefore consistent with activity that warrants further investigation, although the web access logs alone do not conclusively establish malicious intent.

## Step 4: Containment Recommendation

Based on the available evidence, the following containment and response actions are recommended:

- Continue monitoring activity originating from `8.8.8.8`.
- Review the frequency and sequence of requests from the source IP.
- Investigate requests targeting authentication or restricted resources.
- Review requested URI paths for evidence of systematic resource discovery.
- Consider rate-limiting requests if the activity becomes excessive or disruptive.
- Temporarily block the source IP if further investigation confirms malicious activity.
- Notify the web/application team if application-related issues are identified.
- Raise an incident ticket if the activity is confirmed to represent a security incident.

Immediate permanent blocking is not recommended solely on the available evidence because further validation would be required to distinguish malicious behaviour from legitimate or misconfigured traffic.

## Step 5: Document the Case

### Who detected it?

The suspicious activity was identified during the SOC Level 1 investigation of web access logs in Splunk.

### What happened?

Repeated failed web requests were identified from source IP `8.8.8.8`. The activity included HTTP 401, 403 and 404 responses and was considered sufficiently suspicious to warrant escalation for deeper SOC Level 2 investigation.

### When did it happen?

The relevant activity investigated during the SOC analysis occurred between **22 June 2026 and 24 June 2026**.

### Which systems were affected?

The activity affected the monitored web application represented by the `access_combined` web access logs ingested into Splunk.

### What evidence was collected?

The investigation collected web access events containing:

- Timestamps
- Source IP addresses
- HTTP request methods
- Requested URI paths
- HTTP response status codes
- User-agent information

The SOC Level 2 enrichment search returned **1,459 events** associated with the investigated source IP.

### What action was recommended?

The recommended response was to continue monitoring the source IP and investigate its request pattern in greater depth. Rate-limiting or temporary blocking should be considered if further analysis confirms malicious or disruptive behaviour. An incident ticket should also be raised if the activity is confirmed as a security incident.

## Conclusion

The incident response investigation demonstrated how suspicious activity identified during initial SOC monitoring can be escalated and analysed using Splunk. The investigation of `8.8.8.8` revealed a substantial number of web requests, including repeated failed requests that justified additional analysis.

By examining the source IP, HTTP methods, requested resources, status codes and user-agent information, SOC Level 2 can obtain additional context before determining whether containment is necessary. This approach reduces the risk of responding to activity without sufficient evidence while ensuring potentially malicious behaviour is appropriately investigated.