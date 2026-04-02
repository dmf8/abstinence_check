#!/usr/bin/env python3
import os
import subprocess
from datetime import datetime
import re
from pathlib import Path
import argparse


def getComments() -> str:
    path = Path(".git")/"COMMIT_EDITMSG"
    if not path.exists():
        return ""
    try:
        content = path.read_text(encoding="utf-8").strip()
        first_line = content.split("\n", 1)[0].strip()
        return first_line if first_line else ""
    except Exception:
        return ""


def tryMatch(lines, pattern) -> int:
    for i in range(len(lines)):
        if re.match(pattern, lines[i]):
            return i
    return -1


yyyy = datetime.now().strftime("%Y")
mm = datetime.now().strftime("%m")
dd = datetime.now().strftime("%d")
file = f"{yyyy}/{yyyy}_{mm}.md"
title = f"# {yyyy}-{mm}-{dd}"
author = subprocess.getoutput("git config user.name").strip() or "Unknown"
parser = argparse.ArgumentParser()
parser.add_argument("msg")
parser.add_argument("-n", "--name", default=author)
args = parser.parse_args()

# comments = getComments()
comments = args.msg
author = args.name
# print(comments)
# print(author)


if not os.path.exists(f"{yyyy}/"):
    os.makedirs(yyyy)
if not os.path.exists(file):
    with open(file, 'w') as f:
        pass

lines = []
with open(file, 'r') as f:
    lines = f.readlines()

line_id = tryMatch(lines, title)
if line_id < 0:
    lines.append("\n")
    lines.append(f"{title}\n")
    line_id = len(lines)-1

new_lines = []
new_lines.append(f"- @{author}\n")
new_lines.append("\n")
new_lines.append(f"    {comments}\n")

print("new commit")
print(title)
print(new_lines[0])
print(new_lines[2])

for i in range(len(new_lines), 0, -1):
    lines.insert(line_id+1, new_lines[i-1])

with open(file, "w") as f:
    f.writelines(lines)
