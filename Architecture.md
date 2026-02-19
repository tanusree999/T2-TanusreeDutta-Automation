Tools & Frameworks Used:---------------------------------------------------------

Selenium WebDriver (Python) – For browser automation and web element interaction

Python 3.x – Programming language for writing scripts

Google Chrome + ChromeDriver – Browser and driver for test execution

ActionChains (Selenium module) – For advanced user interactions like clicks and hover actions

Development Environment:----------------

IDE: PyCharm 

Browser: Google Chrome

Operating System: Windows 

Code Base & Structure:-----------

Language: Python

Libraries: selenium, time, datetime

Modules/Steps:-

Login Automation

Generator Creation

Billing Information Entry

Latitude & Longitude Verification

Service Hours Setup

Route Assignment & Service Addition

Scope of Work (SOW) Configuration

Price Book Updates (SP1 & SP2)

Logout & Browser Cleanup

Execution Flow:-------------------

Launch Chrome and maximize window

Navigate to login page and perform authentication

Add new generator with required details

Fill billing and location information, including map coordinates

Configure service hours for weekdays; mark weekends as closed

Assign routes, add services, and select service frequency & weekdays

Perform Scope of Work (SOW) selections and remove existing entries if needed

Update Price Book values and toggle relevant options

Logout and close browser

Special Features & Verification:-------------

Dynamic date selection using datetime module

JavaScript clicks for hidden or obstructed elements

Implicit waits and time.sleep for reliable execution

Latitude & longitude display verification

Modular structure allows easy extension to additional generators or workflows

Outcome:--------------

Fully automated, reliable, and scalable testing for the OctopusSaaS platform

Reduces manual effort and ensures accuracy across multiple functionalities
