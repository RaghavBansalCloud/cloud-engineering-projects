import os
import datetime
import platform

print("=== CLOUD OPERATIONS LOG AUTO-GENERATOR ===")
print(f"Timestamp: {datetime.datetime.now()}")
print(f"Operating System inside container: {platform.system()} {platform.release()}")

# Simulating a basic system health check
print("\n[INFO] Checking directory status...")
if os.path.exists('/app'):
    print("[SUCCESS] Operational directory '/app' is healthy.")
else:
    print("[WARNING] Application directory not found.")

print("==========================================")