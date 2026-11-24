# Operating Systems Assignment 5 – CO5
**Register Number:** 192524335  
**Student Name:** K. Mrudhula  
**Platform:** Ubuntu on WSL2 (record the exact version used)  
**Compiler:** GCC (record the exact version used)

This repository is an implementation pack for Assignment 5. It contains source code,
scripts, Docker and Kubernetes configuration, and evidence-capture helpers.

> Important: Do not submit invented measurements. Run the experiments on your own
> Linux/WSL/Docker/Kubernetes environment and place the actual terminal outputs and
> screenshots in the corresponding `outputs/` and `screenshots/` folders.

## Repository structure

- `B1_Linux_Administration/` – system observation, log analysis, disk alerts, cron,
  systemd and Nginx configuration.
- `B2_Docker_Containerisation/` – Flask result portal, Dockerfile, Compose and
  resource-limit commands.
- `B3_Deployment_Comparison/` – deployment instructions, load-test helper,
  Kubernetes deployment/service manifest and evidence folders.
- `B4_Engineering_Decision/` – second service and capacity-estimation helper.
- `PartA_Design/` – report-writing checklist and comparison-table template.

## Environment preparation (Ubuntu/WSL)

```bash
sudo apt update
sudo apt install -y build-essential git curl wget procps sysstat nginx ufw \
  cron python3 python3-venv python3-pip apache2-utils
```

Check versions:

```bash
uname -a
lsb_release -a
gcc --version | head -n 1
git --version
docker --version
docker compose version
kubectl version --client
```

Docker and Kubernetes commands require those tools to be installed and running.
On WSL, Docker Desktop integration or a supported Linux Docker Engine is required.
A VM experiment requires VirtualBox or KVM and a separately provisioned guest.

## Recommended execution order

1. Complete `B1_Linux_Administration/README.md`.
2. Complete `B2_Docker_Containerisation/README.md`.
3. Complete `B3_Deployment_Comparison/README.md`.
4. Complete `B4_Engineering_Decision/README.md`.
5. Fill Part A design answers using `PartA_Design/REPORT_CHECKLIST.md`.
6. Save actual outputs and screenshots; update this README with exact versions and
   measured results before submission.

## Git workflow

Commit each task progressively, as required by the assignment:

```bash
git add B1_Linux_Administration
git commit -m "Complete B1 Linux administration implementation"
git add B2_Docker_Containerisation
git commit -m "Complete B2 Docker containerisation implementation"
git add B3_Deployment_Comparison
git commit -m "Complete B3 deployment comparison implementation"
git add B4_Engineering_Decision
git commit -m "Complete B4 engineering decision implementation"
git add PartA_Design README.md
git commit -m "Add Part A design and final documentation"
```

Create the GitHub repository named `CSA0405-192524335-Assignment5`, then connect it:

```bash
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Do not use a personal access token directly in a command or commit it to this repository.
