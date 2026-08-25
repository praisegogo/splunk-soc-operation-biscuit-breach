# Final Report

## Operation Biscuit Breach

This report summarises the findings from the Splunk SOC investigation conducted as part of Operation Biscuit Breach. The project involved onboarding simulated web access logs into Splunk and analysing the data from IT Operations, DevOps, Business Analytics and Security perspectives before conducting SOC escalation and incident response activities.

## 1. What data was onboarded into Splunk?

A simulated web server access log dataset containing **10,000 HTTP request events** was onboarded into Splunk.

The data was indexed in the `main` index using the `access_combined` sourcetype. The dataset contained fields relating to web application activity, including timestamps, client IP addresses, HTTP request methods, requested URI paths, HTTP status codes and user-agent information.

These fields enabled the dataset to be analysed from IT Operations, DevOps, Business Analytics and Security perspectives.

## 2. What is the purpose of `sourcetype=access_combined`?

The `access_combined` sourcetype identifies the uploaded data as web server access log data in Splunk.

It allows Splunk to interpret and organise the events consistently and extract useful fields such as client IP addresses, HTTP methods, requested URI paths, status codes and user-agent information.

This makes it easier to search, filter and analyse web activity throughout the investigation.

## 3. What did IT Operations learn from the status codes?

IT Operations learned that the website generated a mixture of successful requests, redirects, client errors and server errors.

HTTP 200 was the most common status code, with **3,905 requests**, indicating that a large proportion of requests were processed successfully.

However, there were also substantial numbers of HTTP 400, 401, 403 and 404 client errors, as well as HTTP 500 and 503 server errors.

This showed that although the website was processing many requests successfully, recurring request, access and server-side issues were present and would require monitoring and investigation.

## 4. What did DevOps learn from browser and operating system analysis?

DevOps learned that the web application was accessed across several operating systems and browsers.

The analysis helped identify which platforms generated significant traffic and which browsers were associated with the highest numbers of failed requests.

Browser failure analysis identified:

- **Chrome:** 955 failed requests
- **Safari:** 917 failed requests
- **Android Browser:** 910 failed requests
- **Firefox:** 901 failed requests
- **Mobile Safari:** 876 failed requests

The analysis also identified an issue in the original platform-classification logic because Android user-agent strings contained the term `Linux`. The SPL logic was subsequently improved by evaluating Android before Linux, preventing Android traffic from being incorrectly classified as Linux.

This demonstrates how user-agent analysis can help DevOps identify compatibility issues and improve monitoring logic.

## 5. What did Business Analytics learn from failed purchases?

Business Analytics identified **612 failed purchase requests** in the web application.

Using the scenario assumption that each failed purchase represented **£25 in potential revenue**, the estimated lost revenue was:

**£15,300**

Analysis of failed purchases over time also showed fluctuations and periods of increased failure activity.

These findings demonstrate the potential business impact of web application failures and highlight why purchase-related errors should be monitored and investigated.

The revenue figure is an estimate because a failed request does not necessarily mean that a genuine customer would have completed a £25 purchase.

## 6. What suspicious activity was identified?

The security analysis identified repeated failed web requests from several source IP addresses.

`8.8.8.8` generated the highest overall number of HTTP errors, with **706 failed requests**.

Further investigation identified repeated HTTP 401 Unauthorized, HTTP 403 Forbidden and HTTP 404 Not Found responses associated with the source.

The combination of authentication failures, access-denied responses and requests resulting in unavailable resources was treated as potentially suspicious activity consistent with possible reconnaissance or authentication abuse.

The available evidence justified further investigation but was not sufficient to classify the activity as a confirmed attack.

## 7. What activity was escalated to SOC Level 2?

The suspicious web activity associated with `8.8.8.8` was escalated to SOC Level 2 for further investigation.

The source generated **1,459 total web events**, including **354 combined HTTP 401, 403 and 404 responses**:

- **132 HTTP 401 responses**
- **117 HTTP 403 responses**
- **105 HTTP 404 responses**

The combination of repeated authentication failures, access-denied responses and requests for unavailable resources was considered sufficient to warrant deeper analysis.

SOC Level 2 subsequently enriched the evidence by examining timestamps, HTTP methods, requested URI paths, status codes and user-agent information associated with the source IP.

## 8. What dashboards were created?

Five Splunk dashboards were created during the project:

1. **IT Operations Dashboard**  
   Website health and HTTP status-code monitoring.

2. **DevOps Dashboard**  
   Browser, operating-system and platform analysis.

3. **Business Analytics Dashboard**  
   Failed purchases and estimated lost revenue.

4. **Security and Fraud Dashboard**  
   Suspicious source IPs and failed web requests.

5. **Executive Web Operations Dashboard**  
   Overall operational, business and security overview for senior management.

Together, these dashboards demonstrate how the same web access dataset can provide useful information to different organisational stakeholders.

## 9. What improvements would be made in a real enterprise environment?

In a real enterprise environment, the monitoring solution could be improved by collecting logs from additional sources such as:

- Firewalls
- Web Application Firewalls (WAFs)
- Authentication systems
- Endpoint security platforms
- Application servers
- Identity and access-management systems

Splunk alerts and correlation rules could be configured to automatically detect patterns such as repeated HTTP 401, 403 and 404 responses, unusually high request volumes and increases in server-side errors.

Threat-intelligence sources could also be integrated to enrich suspicious IP addresses and provide additional context during investigations.

Other improvements would include:

- Real-time alerting
- Automated incident ticket creation
- Role-Based Access Control (RBAC)
- Appropriate log-retention policies
- Improved business transaction data
- Additional authentication telemetry
- Documented incident-response procedures
- Correlation across multiple security data sources

These improvements would provide greater visibility, improve detection accuracy and make the Splunk environment more suitable for real-world SOC operations.

## Conclusion

Operation Biscuit Breach demonstrated how Splunk can be used to transform web access logs into operational, business and security intelligence.

The project covered log ingestion, SPL analysis, dashboard development, business-impact analysis, suspicious activity detection, SOC Level 1 escalation and SOC Level 2 incident investigation.

The investigation also demonstrated the importance of interpreting security events within context rather than treating individual HTTP errors as definitive evidence of malicious activity.