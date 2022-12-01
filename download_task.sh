#!/usr/bin/env bash
set -Eeuo pipefail

day=$1
url="https://adventofcode.com/2022/day/$1"
session=$(cat ./session.txt)
mkdir -p ./$day

curl --output ./$day/task.html $url
curl --cookie $session --output ./$day/input.txt $url/input

