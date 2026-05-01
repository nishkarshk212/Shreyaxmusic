#!/bin/bash
cd /root/Shreyaxmusic
export PATH=$HOME/.deno/bin:$PATH
exec .venv/bin/python3 -m shreya >> shreya_log.txt 2>&1
