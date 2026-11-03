#!/usr/bin/env bash
# MTTJ Episode 1 - "OTel On the Go" - speedrun commands
#
# Launches an EC2 instance, installs the OpenTelemetry Collector, points it
# at a Cribl Stream OTel Source, and restarts the service.
#
# Replace every <PLACEHOLDER> below with values from your own AWS account
# and Cribl Cloud workspace before running.

# 1. Launch an EC2 instance
aws ec2 run-instances \
  --image-id <YOUR_AMI_ID> \
  --instance-type t3.micro \
  --region <YOUR_REGION> \
  --key-name <YOUR_KEY_PAIR_NAME> \
  --security-group-ids <YOUR_SECURITY_GROUP_ID> \
  --subnet-id <YOUR_SUBNET_ID>

# 2. Confirm it's up and grab its public DNS name
aws ec2 describe-instances --region <YOUR_REGION>

# 3. SSH in
ssh -i /path/to/<YOUR_KEY_PAIR_NAME>.pem ec2-user@<YOUR_EC2_PUBLIC_DNS>

# 4. Install the OpenTelemetry Collector (amd64 - matches any current AWS Linux AMI, 64-bit)
wget https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v0.161.0/otelcol_0.161.0_linux_amd64.rpm
sudo rpm -ivh otelcol_0.161.0_linux_amd64.rpm

# 5. Swap in the Cribl-pointed config (see otelcol-config.yaml in this folder)
cd /etc/otelcol/
sudo cp config.yaml configbak.yaml
sudo chmod 644 config.yaml   # avoid 777 - the collector only needs to read this file
vim config.yaml
# ggdG   <- vim: jump to top, delete to end of file, then paste in otelcol-config.yaml

# 6. Restart the collector to pick up the new config
sudo systemctl restart otelcol.service
