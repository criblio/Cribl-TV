# README for MTTJ Episode 1: OTel On the Go

This is the companion repo for MTTJ Episode 1, where Jeff Lawton and Leon Adato speedrun getting OpenTelemetry trace data into and back out of Cribl Stream, using the standalone OpenTelemetry Collector running on a plain EC2 instance.

PLEASE USE COMMON SENSE! Don't connect code you don't know or trust (including THIS code) to a production instance of anything you care about. Set up a new workspace first!

## Set up the Cribl side (OTel Source)

1. Head over to [https://cribl.io/try-cloud/](https://cribl.io/try-cloud/) and create a new account (or log into your existing account)
2. Go to the "Products" menu in the upper left corner
3. Under "Stream", click "Worker Groups"
4. Click the default worker group (or whichever group you want to use)
5. Open the "Data" menu at the top and select "Sources"
6. Make sure the "Configured Only" toggle is off
7. Find and click the tile for the "OpenTelemetry" source
8. Click "Add Source"
9. Make sure the "enabled" toggle is turned on
10. Put a name in the "Input ID" field
11. Pick your OTLP version
12. Note the port - gRPC is 4317. **HTTP on 4318 is NOT available on Cribl-managed Worker Groups in Cribl.Cloud, so this speedrun uses gRPC.**
13. On the left-hand menu, click "Connected Destinations"
14. Click "QuickConnect", confirm "Yes" on the popup, pick a destination (even `devnull:devnull` works just to watch data arrive), and click "Save"

## **DO NOT FORGET TO CLICK THE COMMIT & DEPLOY BUTTON.**

Now grab your Cribl URL: "Products" menu > "Workspace" > "Data Sources" (left-hand menu). It'll look like ***default.main.WORD-WORD-RANDOM.cribl.cloud***.

## Set up the EC2 side (OpenTelemetry Collector)

Files in this folder:
- `speedrun-commands.sh` - the exact commands run on camera: launch an EC2 instance, install the OpenTelemetry Collector, drop in the Cribl-pointed config, restart the service. Fill in every `<PLACEHOLDER>` with your own AWS/Cribl values.
- `otelcol-config.yaml` - the Collector config referenced in step 5 of `speedrun-commands.sh`. Replace `<YOUR_CRIBL_OTEL_ENDPOINT>` with the Cribl URL you just grabbed above (the full hostname, already ending in `.cribl.cloud` - don't append it twice) and `<YOUR_CLUSTER_LABEL>` with whatever tag you want to identify this host's traffic.

Walk through `speedrun-commands.sh` top to bottom. By the end you'll have a live EC2 host running the OpenTelemetry Collector, shipping traces, host metrics, and logs straight into your Cribl OTel Source over gRPC.
