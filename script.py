#!/usr/bin/env python

import sys
import subprocess as subp


cmd = '' if len(sys.argv) <= 1 else str(sys.argv[1])

if cmd in ['prev', 'next']:

    log = subp.check_output(['git', 'rev-list', '--all']).strip()
    log = [line.strip() for line in log.split('\n')]

    pos = subp.check_output(['git', 'rev-parse', 'HEAD']).strip()
    idx = log.index(pos)

    # Next commit:
    if cmd == 'next':
        if idx > 0:
            subp.call(['git', 'checkout', log[idx - 1]])
        else:
            print("You're already on the latest commit.")

    # Previous commit:
    else:
        if idx + 1 <= len(log) - 1:
            subp.call(['git', 'checkout', 'HEAD^'])
        else:
            print("You're already on the first commit.")

else:
    print('Usage: git walk prev|next')
