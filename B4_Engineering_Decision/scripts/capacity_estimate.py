#!/usr/bin/env python3
import argparse
import math

parser = argparse.ArgumentParser(
    description="Rough capacity estimate from student count and measured instance throughput."
)
parser.add_argument("--students", type=int, default=150000)
parser.add_argument("--hours", type=float, default=2.0)
parser.add_argument("--rps-per-instance", type=float, required=True,
                    help="Measured sustainable requests per second for one instance")
parser.add_argument("--requests-per-student", type=float, default=1.0)
parser.add_argument("--headroom", type=float, default=1.30,
                    help="Capacity multiplier, e.g. 1.30 for 30 percent headroom")
args = parser.parse_args()

if min(args.students, args.hours, args.rps_per_instance,
       args.requests_per_student, args.headroom) <= 0:
    parser.error("All numeric inputs must be greater than zero.")

total_requests = args.students * args.requests_per_student
duration_seconds = args.hours * 3600
average_rps = total_requests / duration_seconds
target_rps = average_rps * args.headroom
instances = math.ceil(target_rps / args.rps_per_instance)

print(f"Students: {args.students}")
print(f"Requests per student (assumption): {args.requests_per_student:g}")
print(f"Total requests (estimated): {total_requests:,.0f}")
print(f"Window: {args.hours:g} hours ({duration_seconds:,.0f} seconds)")
print(f"Average required throughput: {average_rps:.2f} requests/second")
print(f"Target throughput with {((args.headroom - 1) * 100):.0f}% headroom: {target_rps:.2f} requests/second")
print(f"Measured throughput per instance: {args.rps_per_instance:.2f} requests/second")
print(f"Estimated instances required: {instances}")
print("Note: This is a simplified estimate; validate with realistic peak-load and database tests.")
