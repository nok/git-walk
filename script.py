#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import subprocess as subp


def read_commit_ids():
    cmd = 'git rev-list --all'
    log = subp.check_output(cmd.split()).strip()
    log = [line.strip() for line in log.split('\n')]
    return log


def read_active_commit_id():
    cmd = 'git rev-parse HEAD'
    id = subp.check_output(cmd.split()).strip()
    return id


n_args = len(sys.argv) - 1
cmd = str(sys.argv[1]) if n_args >= 1 else ''

if cmd in ['first', 'oldest', 'last',
           'latest', 'prev', 'next']:

    log = read_commit_ids()
    target_id = None

    # First commit:
    if cmd in ['first', 'oldest']:
        target_id = log[-1]

    # Latest commit:
    elif cmd in ['latest', 'newest']:
        target_id = log[0]

    # Either next or prev commit:
    else:
        try:
            steps = int(sys.argv[2]) if n_args >= 2 else 1
            if steps < 1:
                steps = 1
        except ValueError:
            steps = 1

        current_commit_id = read_active_commit_id()
        current_index = log.index(current_commit_id)

        # Next commit:
        if cmd == 'next':
            try:
                target_id = log[current_index - steps - 1]
            except IndexError:
                target_id = log[0]

        # Previous commit:
        elif cmd == 'prev':
            try:
                target_id = log[current_index + steps]
            except IndexError:
                target_id = log[-1]

    if target_id:
        checkout_cmd = 'git checkout {} --quiet'.format(target_id)
        subp.call(checkout_cmd.split())

else:
    print('Usage:')
    print('git walk (last|latest)')
    print('git walk (first|oldest)')
    print('git walk prev [n_commits]')
    print('git walk next [n_commits]')
