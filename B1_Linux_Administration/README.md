# B1 – Administer the Linux Server

## B1.1 Observe the system

Run the following from this folder and save the output:

```bash
bash scripts/observe_system.sh | tee outputs/system_observation.txt
```

The script records process, CPU/load, memory, virtual-memory, disk, filesystem and
network-socket information using `ps`, `top`, `free`, `vmstat`, `iostat`, `df` and `ss`.
If `iostat` is unavailable, install `sysstat`.

## B1.2 Automate

```bash
bash scripts/log_analysis.sh | tee outputs/log_analysis.txt
bash scripts/disk_space_alert.sh | tee outputs/disk_alert.txt
```

The log-analysis script creates its own small, clearly labelled test access log. The
expected counts are 200:4, 302:1, 403:1, 404:1; busiest client 10.0.0.5:4; total bytes
43200. It does not read a real Nginx log unless you edit `LOG_SOURCE`.

To schedule the scripts hourly, edit your crontab:

```bash
crontab -e
```

Add (replace the path with the absolute path printed by `pwd`):

```cron
0 * * * * /bin/bash /ABSOLUTE/PATH/B1_Linux_Administration/scripts/log_analysis.sh >> /ABSOLUTE/PATH/B1_Linux_Administration/outputs/hourly_log_analysis.log 2>&1
0 * * * * /bin/bash /ABSOLUTE/PATH/B1_Linux_Administration/scripts/disk_space_alert.sh >> /ABSOLUTE/PATH/B1_Linux_Administration/outputs/hourly_disk_alert.log 2>&1
```

Verify with `crontab -l`. Keep the actual output in `outputs/`.

## B1.3 Services and network

A sample Flask portal is supplied in B2. The systemd unit and Nginx reverse-proxy
configuration are templates in `config/`. Review and adapt paths before installing.
System-wide service installation requires sudo and may not behave exactly the same
inside WSL as on a full Linux machine.

Example firewall plan (only run after confirming SSH access and the correct SSH port):

```bash
sudo ufw allow OpenSSH
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
sudo ufw status verbose
```

Do not enable a firewall remotely until SSH access is allowed, or you may lock yourself out.

## B1.4 Compare with design

In `outputs/design_comparison.md`, record what was actually implemented, differences
from Part A, reasons, and limitations.
