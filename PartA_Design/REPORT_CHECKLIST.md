# Part A – Design Report Checklist

Use the exact task organization from the assignment.

## A1 – Evaluate Linux System Components (7 marks)
- A1.1 Linux architecture: kernel, system libraries, shell/utilities, process/memory/file/device/network management.
- A1.2 CFS, page cache, swapping, `/proc` and `/sys`.
- A1.3 directory hierarchy, VFS, owner/group/others, setuid and sudo.
- Alternative: Windows Server comparison covering base memory/disk, automation time and licensing cost.

## A2 – Design System Administration (5 marks)
- A2.1 user accounts/groups, systemd services and log monitoring.
- A2.2 IP addressing, DNS, Nginx, firewall and SSH keys.
- A2.3 shell and cron automation for backups, log rotation and disk alerts.
- Alternative: Ansible versus scripts for one and twenty servers, configuration drift and maintenance.

## A3 – Evaluate Virtualisation (5 marks)
- A3.1 type-1/type-2 hypervisors, full/para-virtualisation, Intel VT-x and AMD-V.
- A3.2 isolation, consolidation, snapshots, live migration, overhead, VM memory and licensing.
- Alternative: VirtualBox versus KVM for CPU/I/O overhead, host memory and production suitability.

## A4 – Evaluate Containerisation (4 marks)
- A4.1 namespaces, cgroups and layered images.
- A4.2 start-up, memory, isolation/security and portal/database placement.
- Alternative: separate VMs versus containers for start-up, memory and isolation.

## A5 – Cloud Deployment and Orchestration (4 marks)
- A5.1 IaaS/PaaS/SaaS and result-day cloud design.
- A5.2 pods, deployments, services, replicas, requests/limits and HPA.
- Alternative: fixed VMs versus Kubernetes autoscaling for peak response, idle resources and cost.

## Required comparisons
For every alternative concept, explain the changed design and compare time/space
complexity or operational effort as relevant. Use Big-O where an algorithm is involved;
for infrastructure choices, compare measurable resource/time/cost dimensions rather
than forcing an inappropriate Big-O expression.

## Report evidence checklist
- Architecture/network/deployment diagrams.
- Comparison tables.
- Actual command outputs and screenshots from Part B.
- Exact Linux distribution, version, compiler and tool versions.
- GitHub repository URL on cover page and in submission.
