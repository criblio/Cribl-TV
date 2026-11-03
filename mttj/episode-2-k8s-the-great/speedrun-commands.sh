#!/usr/bin/env bash
# MTTJ Episode 2 - "K8s the Great" - speedrun commands
#
# Deploys Cribl Edge onto every node of a Kubernetes cluster as a DaemonSet,
# using Cribl's official Helm chart, then wires it into a dedicated Fleet.
#
# Replace every <PLACEHOLDER> below with your own cluster/Cribl values.

# 1. Add the Cribl Helm repo
helm repo add cribl https://criblio.github.io/helm-charts/
helm repo update

# 2. In the Cribl UI: create (or select) a Fleet for these Kubernetes nodes
#    under Fleets > New Fleet, and note its name - you'll pass it as the
#    `group` query param below so every Node in this cluster lands in it.
#
#    If any Node in this Fleet is running Cribl Edge 4.8.2 or older: go to
#    Fleet Settings > General Settings > API Server Settings > General and
#    change the listening interface from 127.0.0.1 to 0.0.0.0. Skipping
#    this makes health checks fail and Nodes never show up in the Leader UI.

# 3. Install Cribl Edge as a DaemonSet via Helm, pointed at your Leader and
#    Fleet (see values-override.yaml for what this already sets up for you).
helm install --repo "https://criblio.github.io/helm-charts/" \
  --version "<CHART_VERSION>" \
  --create-namespace -n <YOUR_NAMESPACE> \
  --set "cribl.leader=tls://<YOUR_AUTH_TOKEN>@<YOUR_LEADER_HOST>:4200?group=<YOUR_FLEET_NAME>" \
  -f values-override.yaml \
  <YOUR_DEPLOYMENT_NAME> edge

# 4. Confirm there's a Pod running on every node
kubectl get pods -n <YOUR_NAMESPACE> -o wide

# 5. Back in the Cribl UI, on this Fleet, enable the "Kubernetes Logs",
#    "Kubernetes Metrics", and "Kubernetes Events" Sources (under System
#    and Internal Sources), then COMMIT & DEPLOY.
