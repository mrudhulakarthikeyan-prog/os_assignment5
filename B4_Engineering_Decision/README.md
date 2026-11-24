# B4 – Final Engineering Decision

## B4.1 Practical extension

The Compose file in B2 includes two independently limited services:
- `portal`: 0.50 CPU and 256 MiB memory.
- `database`: 0.50 CPU and 512 MiB memory.

Run and record:

```bash
cd ../B2_Docker_Containerisation
docker compose up --build -d
docker compose ps
docker stats --no-stream
docker compose down
```

If using Kubernetes instead, create a second Deployment and Service for a separate
learning-management sample service, and give it its own resource requests and limits.
Do not state it was deployed unless you ran it.

## B4.2 Capacity estimate

The helper `scripts/capacity_estimate.py` estimates the request rate from 150,000
students over two hours and derives a rough instance count from a measured per-instance
requests/second value. The estimate is a planning approximation, not a production
capacity guarantee. It assumes one request per student unless you specify otherwise.

```bash
python3 scripts/capacity_estimate.py --students 150000 --hours 2 --rps-per-instance 50
```

Replace 50 with your measured sustainable per-instance throughput. Consider peak
concurrency, multiple requests per student, database bottlenecks, safety headroom,
and load-test failure rates.

## B4.3 Production decision

Complete `outputs/decision_template.md` using actual measurements and cost quotes.
Consider hybrid deployment: baseline services on university infrastructure and
temporary result-day capacity in public cloud. Address student-data governance,
network connectivity, backup, disaster recovery, security and operational skills.
