Postmortem Report: Web Application Outage

# Issue Summary:
    >> Duration: 
    January 15, 2024, 08:30 AM - 11:45 AM (UTC)

    >> Impact: 
    During the outage, the student dashboard and classroom chat features were inaccessible. Approximately 30% of users experienced slow responsiveness, and 15% were completely unable to access critical academic information or communicate.

    >> Root Cause:
    The root cause of the outage was identified as an unforeseen spike in database queries triggered by a misconfigured database connection pool. This resulted in a cascading effect, causing excessive load on the database server, leading to delayed responses and, in some cases, service unavailability.

# Timeline:
    08:30 AM: Issue detected as users reported slow dashboard loading times.
    08:45 AM: Datadog monitoring alerts triggered, indicating increased response times and errors.
    09:00 AM: Engineering team initiated investigation into server logs and database performance.
    09:30 AM: Misleading assumption that the issue was related to recent frontend changes led to unnecessary debugging efforts on the client side.
    10:00 AM: Issue escalated to the database team after identifying abnormal query patterns.
    11:00 AM: Root cause determined – misconfigured database connection pool causing excessive open connections.
    11:30 AM: Database connection pool settings adjusted to prevent further incidents.
    11:45 AM: Services fully restored, and users reported normal functionality.

# Root Cause and Resolution:
    >> Root Cause: 
    The misconfiguration of the database connection pool settings caused a rapid increase in open connections, overwhelming the database server.

    >> Resolution: 
    Database connection pool settings were adjusted to limit the number of simultaneous open connections, preventing the overload and ensuring stable performance.



# Corrective and Preventative Measures:
    >> Improvements/Fixes:
    Implement Additional Monitoring: Enhance monitoring systems to provide real-time alerts for abnormal database query patterns and connection pool usage.

    >> Automated Scaling: 
    Implement automated scaling solutions to dynamically adjust resource allocation based on the application's demand.

    >> Regular Load Testing: 
    Conduct regular load testing to simulate high traffic scenarios and identify potential bottlenecks in the system.

# Tasks to Address the Issue:
    >> Update Documentation: 
    Clearly document database connection pool configurations and guidelines for future reference.

    >>  Training Sessions:
    Conduct training sessions for the engineering team on interpreting and responding to monitoring alerts effectively.

    >> Incident Response Plan: 
    Develop a comprehensive incident response plan that outlines escalation procedures and responsibilities during outages.


CONCLUSION
This incident highlighted the critical need for robust monitoring and timely response to abnormalities. Moving forward, the implementation of automated scaling, enhanced monitoring, and regular load testing will fortify the system's resilience to unforeseen spikes in user activity. The adjustments made to the database connection pool settings have been documented to prevent similar issues in the future. The incident served as a valuable learning experience, reinforcing the importance of proactive measures to ensure the continued reliability of the "My Learning Hub" platform.

