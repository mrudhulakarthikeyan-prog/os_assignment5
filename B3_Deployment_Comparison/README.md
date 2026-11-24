# B3 – Compare Bare Metal, Virtual Machine and Container

This task requires the same web application to be run in three environments and
measured. The supplied app is in `../B2_Docker_Containerisation/app/app.py`.

## 1. Bare-metal / direct Linux deployment

On the Linux host, create a venv and install the app dependencies:

```bash
cd ../B2_Docker_Containerisation
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
cd app
gunicorn --bind 0.0.0.0:8000 --workers 2 app:app
```

In another terminal, test with `curl http://127.0.0.1:8000/health`.
Record start-up time and memory with `/usr/bin/time -v` and `ps`/`ps` RSS.

## 2. Virtual machine deployment

Create an Ubuntu VM using VirtualBox or KVM, install Python and Git inside it,
copy the same application and run the same Gunicorn command. Record VM RAM allocation,
virtual disk size, boot/start-up time and load-test result. Do not claim VM results
until this has actually been run.

## 3. Docker deployment

Follow B2. Record container start-up time, `docker stats`, image size and load-test result.

## 4. Load test

Install ApacheBench (`sudo apt install apache2-utils`). With the service running:

```bash
ab -n 1000 -c 20 http://127.0.0.1:8000/
```

Use the same request count and concurrency for all three environments. Save the
complete output, especially Requests per second, mean time per request and failed requests.

## 5. Kubernetes (minikube or kind)

Use `deployment.yaml` after building or loading an image available to your local cluster.
For Minikube, one option is to build inside its Docker daemon:

```bash
eval "$(minikube docker-env)"
docker build -t result-portal:assignment5 ../B2_Docker_Containerisation
```

Apply:

```bash
kubectl apply -f deployment.yaml
kubectl get deployments,pods,services
kubectl describe deployment result-portal
kubectl delete pod POD_NAME
kubectl get pods -w
kubectl scale deployment result-portal --replicas=6
kubectl get pods
```

For a local cluster, a LoadBalancer service may need:

```bash
minikube service result-portal --url
```

Save command outputs in `outputs/`. A cluster with three replicas is not proof of
multi-node resilience unless the cluster actually has multiple nodes.

## Measurement table

Fill only with actual results:

| Metric | Direct Linux | VM | Docker |
|---|---:|---:|---:|
| Start-up time (s) | | | |
| Memory used (MiB) | | | |
| Disk / image size (MiB) | | | |
| Requests per second | | | |
| Failed requests | | | |

## Engineering interpretation

Discuss measured results, isolation, operational overhead, recovery, portability,
and the suitability of each approach for the university portal.
