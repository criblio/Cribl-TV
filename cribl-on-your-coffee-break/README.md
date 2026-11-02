# Stupid-simple Cribl Data Generator Scripts
Welcome to the repository of files that are meant to be ridiculously simple (and therefore easy to understand) and generate vaguely useful data of various types. 

The scripts were originally written as part of the ["Cribl On Your Coffee Break"](https://www.youtube.com/watch?v=B8k1FLRYIvc&list=PLQemen2vk_As) series, but of course you're welcome to use it for any purpose you see fit. It's a simple script that generates random CPU values and sends them into a Cribl instance. 

PLEASE USE COMMON SENSE! Don't connect code you don't know or trust (including THIS code) to a production instance of anything you care about.

Each python script is broken down into it's own separate folder - Syslog, Prometheus, and OpenTelemetry. They all run by themselves - no container, pod, or other infrastructure; and they're all set up so you can use a virtual environment (venv) rather than installing things raw on your machine. Details for each generator appear below. 

## SYSLOG
There are two scripts in this folder - `syslogtest.py` generates a moderate amount of random messages. `syslogtest_sampling.py` generates significantly more messages with a large number of "INFO" types, intended to be used in the episode on sampling. 

Details on setting up both the script and also the receiver in Cribl can be found in [the Syslog script readme](./SYSLOGTEST/README.md).

## PROMETHEUS
This script - `promtest.py` generates a single metric (CPU % utilization) which is really just a randomized number.

Details on setting up both the script and also the receiver in Cribl can be found in [the Prometheus script readme](./PROMTEST/README.md)

## OPEN TELEMETRY (OTEL)
The main script - `oteltest.py` spins up a flask container that displays a webpage at [http://localhost:8080](http://localhost:8080) (or [http://127.0.0.1:8080](http://127.0.0.1:8080) if you're a networking weirdo or you've re-mapped localhost to something else.). 

You'll get some spans automatically, but you'll get more if you open the webpage and spam the "refresh" button. 

Details on setting up both the script and also the receiver in Cribl can be found in [the OTel script readme](./OTELTEST/README.md)
