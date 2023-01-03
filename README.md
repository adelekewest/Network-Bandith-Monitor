# Network-Bandith-Monitor
A simple python script to monitor network bandith.
This script uses the psutil module to get the current network statistics and calculates the difference in bytes sent and received since the last iteration. It then divides this difference by the time elapsed (1 second) to get the current send and receive rates in bytes per second. The script prints these rates to the console and updates the previous totals for the next iteration.

You should also know that this script will run indefinitely and will print the current send and receive rates to the console every second.




