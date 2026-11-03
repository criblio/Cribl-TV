# README for MTTJ Episode 2: K8s the Great

This is the companion repo for MTTJ Episode 2, where Jeff Lawton and Leon Adato speedrun deploying Cribl Edge onto a Kubernetes cluster as a DaemonSet, collecting logs, metrics, and events straight from the cluster, then handing it downstream to the rest of the Cribl platform.

PLEASE USE COMMON SENSE! Don't connect code you don't know or trust (including THIS code) to a production cluster. Try it on a throwaway/dev cluster first!

## Set up the Cribl side (Fleet)

1. Head over to [https://cribl.io/try-cloud/](https://cribl.io/try-cloud/) and create a new account (or log into your existing account), or point at your own on-prem Leader
2. Go to the "Products" menu in the upper left corner, then "Edge"
3. On the left-hand menu, click "Fleets"
4. Click "New Fleet" and give it a name - this is the Fleet every node in your Kubernetes cluster is about to join, so config and upgrades stay predictable across the whole cluster
5. **If any Node you'll run is on Cribl Edge 4.8.2 or older:** open this Fleet's Settings > General Settings > API Server Settings > General, and change the listening interface from `127.0.0.1` to `0.0.0.0`. Skip this and health checks fail once the agent downloads its config - the Node won't even show up in the Leader UI.

## Set up the Kubernetes side (Helm)

Files in this folder:
- `speedrun-commands.sh` - the exact commands run on camera: add Cribl's Helm repo, install the `edge` chart as a DaemonSet pointed at your Leader and Fleet, confirm the Pods are up. Fill in every `<PLACEHOLDER>`.
- `values-override.yaml` - the Helm values override referenced in step 3 of `speedrun-commands.sh`. The chart already ships a working DaemonSet, ServiceAccount, read-only RBAC for the Kubernetes Sources, a host filesystem mount, and the `CRIBL_K8S_POD` Downward API wiring by default - this file only covers what you actually need to decide (certificate handling, and where the Leader URL/auth token lives).

Walk through `speedrun-commands.sh` top to bottom. By the end you'll have a Cribl Edge Pod running on every node in the cluster.

## Turn on the Kubernetes Sources

Back in the Cribl UI, on your new Fleet, go to Data > Sources, turn off "Configured Only", and enable each of these three (they're singleton System and Internal Sources - no need to create new ones):
- **Kubernetes Logs** - polls the Kubernetes API for Pod logs (not raw `/var/log/containers/` files)
- **Kubernetes Metrics** - cluster/Node/Pod/container status; optionally also scrapes kubelet and cAdvisor metrics (for full node-exporter-style coverage, pair it with a Prometheus Edge Scraper instead)
- **Kubernetes Events** - cluster-level events (Pod starts, failed jobs, etc.) via the Kubernetes Events API

**DO NOT FORGET TO CLICK THE COMMIT & DEPLOY BUTTON.**

## What's next: handing off to Stream

Once Cribl Edge is collecting at the node level, it can enrich, route, and forward that data downstream to Cribl Stream for further processing. If you're also running Stream on Kubernetes (via Cribl's own Helm chart for Worker Groups), keep a few things in mind: sizing isn't automatic - set `CRIBL_MAX_WORKERS` explicitly rather than relying on container CPU detection - and if you're using autoscaling (HPA) together with Persistent Queue, use shared PQ storage (not local-FS) and a StatefulSet rather than a plain Deployment, or a scale-down can kill a Worker while it's still holding queued data.
