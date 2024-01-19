Setting Up Datadog Monitoring

Introduction
This README provides step-by-step instructions for setting up Datadog monitoring, installing the Datadog agent on a server, creating an application key, and configuring monitors and dashboards. Follow these guidelines to monitor and visualize system metrics using Datadog.

Prerequisites
Access to https://app.datadoghq.com (US region - US1)
A server (e.g., web-01) to install the Datadog agent
Basic knowledge of API keys and dashboard creation in Datadog

Step 1: Sign Up for Datadog
Navigate to Datadog and sign up for a free account.
During the signup process, choose the statistics you want Datadog to monitor from your current stack.

Step 2: Install Datadog Agent
Follow the instructions provided on the Datadog website to install the Datadog agent on your server (e.g., web-01).

Step 3: Create Application Key
Log in to Datadog.
Navigate to the "Integrations" section and create an application key.

Step 4: Intranet User Profile Configuration
Copy your Datadog API key and application key.
Paste these keys into your Intranet user profile.

Step 5: Verify Server Visibility
Ensure your server (web-01) is visible in Datadog under the hostname XX-web-01.
Validate server visibility using Datadog's API.

Step 6: Set Up Monitors
Explore System Check Metrics.
Create monitors in the Datadog dashboard to alert you based on specific system metrics.

Step 7: Create a Dashboard
Create a new dashboard in Datadog.
Add at least four widgets of any type to your dashboard, monitoring the metrics of your choice.

Step 8: Dashboard ID Retrieval
Use Datadog's API to retrieve the ID of your newly created dashboard.

Step 9: Create Answer File
Create a file named 2-setup_datadog.
Place the dashboard ID on the first line of the file.

Conclusion
By following these steps, you have successfully set up Datadog monitoring, installed the Datadog agent, created an application key, configured monitors, and created a dashboard with visualizations. This monitoring setup allows you to keep track of system metrics and receive alerts when needed.







