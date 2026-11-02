## README for Promtest.py
This script was originally written as part of the "Cribl On Your Coffee Break" series, but of course you're welcome to use it for any purpose you see fit. It's a simple script that captures traces from a simple flask application and sends them into a Cribl instance. 

In order for this to work, you need to set up the following items:
1. Head over to [https://cribl.io/try-cloud/](https://cribl.io/try-cloud/) and create a new account (or log into your existing account)

PLEASE USE COMMON SENSE! Don't connect code you don't know or trust (including THIS code) to a production instance. Set up a new workspace first!

2. IF you're using production (SEE NOTE ABOVE. WE DO NOT WANT ANY OOPSIES!), first do the following:
    1. Open the "Products" menu in the upper left corner
    2. Go to "Workspace"
    3. On the left-hand menu, click "Manage Workspaces"
    4. Click "Add Workspace"
    5. Set up your workspace a name and ID, pick a region, and click "Next"
    6. Set your data retention and click "Next"
    7. Select your release channel and click "Save"

OK, now that we've ensured we won't mess up prod, let's set up this script.

3. Go to the "Products" menu in the upper left corner
4. Under "Stream", click "Worker Groups"
5. Click the default worker group
6. Open the "Data" menu at the top and select "Sources"
7. Make sure the "Configured Only" toggle is off
8. Find and click the tile for the "OpenTelemetry" source
9. Click "Add Source"
10. Make sure the "enabled" toggle is turned on
11. Put a name in the "Input ID" field
12. Make sure the OTLP version 1.3.1 is selected
13. Note the port - it should be 4317
14. On the left-hand menu, click "Connected Destinations"
15. Click "QuickConnect"
16. A modal box will pop up confirming the choice. Click "Yes"
17. In the Destination dropdown, select devnull:devnull
18. Click "Save"

## **DO NOT FORGET TO CLICK THE COMMIT & DEPLOY BUTTON.**

Now we need to update the script with your Cribl information. Before we start, make sure you know two things:
* the port (it should be 4317)
* The Cribl URL. You can get that by doing the following:
    1. Go to the "Products" menu in the upper left corner
    2. Go to "Workspace"
    3. On the left-hand menu, click "Data Sources"
    From this window, you're looking for the Cribl URL. It's going to be in the form of ***default.main.WORD-WORD-RANDOM.cribl.cloud***. 

Now that you have that information, you need to:
1. open up oteltest.py
2. Edit the line that reads `endpoint="https://CRIBL-URL-GOES-HERE:4317",` by putting the Cribl URL and port (4317) in their respective places. 
3. Save the file

To run the script, you might first need to set up a virtual environment and install some dependencies. In a terminal window in the directory where these files are located, you should:
1. Set up the virtual environment:  `python3 -m venv venv` 
Enable the virtual environment: `source venv/bin/activate`
Install additional python libraries: `pip install -r requirements.txt`

Now, you should be able to run the command `python3 oteltest.py`. This will spin up a flask container that displays a webpage at [http://localhost:8080](http://localhost:8080) (or [http://127.0.0.1:8080](http://127.0.0.1:8080) if you're a networking weirdo or you've re-mapped localhost to something else.). 

You'll get some spans automatically, but you'll get more if you open the webpage and spam the "refresh" button.
