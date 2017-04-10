#!/usr/bin/env python

import sys
import subprocess as subp


cmd = '' if len(sys.argv) <= 1 else str(sys.argv[1])
steps = 1 if len(sys.argv) <= 2 else int(sys.argv[2])

if steps == 0:
    steps = 1

if cmd in ['first', 'latest', 'prev', 'next']:

    log = subp.check_output(['git', 'rev-list', '--all']).strip()
    log = [line.strip() for line in log.split('\n')]

    pos = subp.check_output(['git', 'rev-parse', 'HEAD']).strip()
    idx = log.index(pos)

    # First commit:
    if cmd == 'first':
        subp.call(['git', 'checkout', log[-1]])

    # Latest commit:
    elif cmd == 'latest':
        subp.call(['git', 'checkout', log[0]])

    # Next commit:
    elif cmd == 'next':
        if idx - steps >= 0:
            subp.call(['git', 'checkout', log[idx - steps]])
        else:
            subp.call(['git', 'checkout', log[0]])
            print("Now you're on the latest commit.")

    # Previous commit:
    elif cmd == 'prev':
        if idx + steps <= len(log) - 1:
            if steps == 1:
                subp.call(['git', 'checkout', 'HEAD^'])
            else:
                subp.call(['git', 'checkout', log[idx + steps]])
        else:
            subp.call(['git', 'checkout', log[-1]])
            print("Now you're on the first commit.")

else:
    print('Usage:')
    print('git walk latest')
    print('git walk first')
    print('git walk prev [int:n_commits]')
    print('git walk next [int:n_commits]')
