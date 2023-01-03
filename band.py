import psutil
import time

# Initialize variables
previous_total_bytes_sent = 0
previous_total_bytes_received = 0

# Continuously monitor network bandwidth usage
while True:
  # Get current network stats
  current_bytes_sent = psutil.net_io_counters().bytes_sent
  current_bytes_received = psutil.net_io_counters().bytes_recv

  # Calculate the difference in bytes sent and received since the last iteration
  bytes_sent_diff = current_bytes_sent - previous_total_bytes_sent
  bytes_received_diff = current_bytes_received - previous_total_bytes_received

  # Calculate the current send and receive rates in bytes per second
  send_rate = bytes_sent_diff / time.sleep(1)
  receive_rate = bytes_received_diff / time.sleep(1)

  # Print the current send and receive rates
  print("Send rate: {} bytes/s".format(send_rate))
  print("Receive rate: {} bytes/s".format(receive_rate))

  # Update the previous totals
  previous_total_bytes_sent = current_bytes_sent
  previous_total_bytes_received = current_bytes_received

