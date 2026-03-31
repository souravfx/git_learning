import subprocess

branch_name = "feature1"

# Fetch latest changes and prune deleted remote branches
subprocess.run(["git", "fetch", "--prune"])

# Delete the local branch
subprocess.run(["git", "branch", "-d", branch_name])
