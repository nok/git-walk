#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import subprocess as subp
from unittest import TestCase


class Test(TestCase):

    def setUp(self):
        cmds = [
            'mkdir .test_env',
            'cd .test_env',
            'touch nums.txt',
            'git init --quiet',
            'echo "0" > nums.txt',
            'git add nums.txt',
            'git commit -m "Add 0" --quiet',
            'echo "1" > nums.txt',
            'git add nums.txt',
            'git commit -m "Add 1" --quiet',
            'echo "2" > nums.txt',
            'git add nums.txt',
            'git commit -m "Add 2" --quiet',
            'echo "3" > nums.txt',
            'git add nums.txt',
            'git commit -m "Add 3" --quiet',
            'echo "4" > nums.txt',
            'git add nums.txt',
            'git commit -m "Add 4" --quiet',
            'echo "5" > nums.txt',
            'git add nums.txt',
            'git commit -m "Add 5" --quiet'
        ]
        cmd = ' && '.join(cmds)
        subp.call(cmd, shell=True)
        sleep(0.01)
        # cmds = [
        #     'cd .test_env',
        #     'git reset --hard --quiet',
        # ]
        # cmd = ' && '.join(cmds)
        # subp.call(cmd, shell=True, stdout=True)
        # sleep(0.01)

    def tearDown(self):
        subp.call('rm -rf .test_env', shell=True)
        sleep(0.01)

    def _exec_cmd(self, cmd):
        p = subp.Popen(cmd, shell=True, stdout=subp.PIPE,
                       stderr=subp.STDOUT, stdin=subp.PIPE)
        while p.poll() is None:
            out = str(p.stdout.read().strip())
        p.stdout.close()
        p.stdin.close()
        sleep(0.01)
        return out

    def test_first(self):
        cmds = [
            'cd .test_env',
            'python ./../script.py first',
            'cat nums.txt'
        ]
        cmd = ' && '.join(cmds)
        out = self._exec_cmd(cmd)
        self.assertEqual(str(0), out)

    def test_oldest(self):
        cmds = [
            'cd .test_env',
            'python ./../script.py oldest',
            'cat nums.txt'
        ]
        cmd = ' && '.join(cmds)
        out = self._exec_cmd(cmd)
        self.assertEqual(str(0), out)

    def test_last(self):
        cmds = [
            'cd .test_env',
            'python ./../script.py last',
            'cat nums.txt'
        ]
        cmd = ' && '.join(cmds)
        out = self._exec_cmd(cmd)
        self.assertEqual(str(5), out)

    def test_latest(self):
        cmds = [
            'cd .test_env',
            'python ./../script.py latest',
            'cat nums.txt'
        ]
        cmd = ' && '.join(cmds)
        out = self._exec_cmd(cmd)
        self.assertEqual(str(5), out)

    def test_prev(self):
        cmds = [
            'cd .test_env',
            'python ./../script.py prev',
            'cat nums.txt'
        ]
        cmd = ' && '.join(cmds)
        out = self._exec_cmd(cmd)
        self.assertEqual(str(4), out)

    def test_prev_prev(self):
        cmds = [
            'cd .test_env',
            'python ./../script.py prev',
            'python ./../script.py prev',
            'cat nums.txt'
        ]
        cmd = ' && '.join(cmds)
        out = self._exec_cmd(cmd)
        self.assertEqual(str(3), out)

    def test_prev_1(self):
        cmds = [
            'cd .test_env',
            'python ./../script.py prev 1',
            'cat nums.txt'
        ]
        cmd = ' && '.join(cmds)
        out = self._exec_cmd(cmd)
        self.assertEqual(str(4), out)

    def test_prev_2(self):
        cmds = [
            'cd .test_env',
            'python ./../script.py prev 2',
            'cat nums.txt'
        ]
        cmd = ' && '.join(cmds)
        out = self._exec_cmd(cmd)
        self.assertEqual(str(3), out)

    def test_prev_3(self):
        cmds = [
            'cd .test_env',
            'python ./../script.py prev 3',
            'cat nums.txt'
        ]
        cmd = ' && '.join(cmds)
        out = self._exec_cmd(cmd)
        self.assertEqual(str(2), out)

    def test_prev_10(self):
        cmds = [
            'cd .test_env',
            'python ./../script.py prev 10',
            'cat nums.txt'
        ]
        cmd = ' && '.join(cmds)
        out = self._exec_cmd(cmd)
        self.assertEqual(str(0), out)

    def test_next(self):
        cmds = [
            'cd .test_env',
            'python ./../script.py first',
            'python ./../script.py next',
            'cat nums.txt'
        ]
        cmd = ' && '.join(cmds)
        out = self._exec_cmd(cmd)
        self.assertEqual(str(1), out)

    def test_next_next(self):
        cmds = [
            'cd .test_env',
            'python ./../script.py first',
            'python ./../script.py next',
            'python ./../script.py next',
            'cat nums.txt'
        ]
        cmd = ' && '.join(cmds)
        out = self._exec_cmd(cmd)
        self.assertEqual(str(2), out)

    def test_next_1(self):
        cmds = [
            'cd .test_env',
            'python ./../script.py first',
            'python ./../script.py next 1',
            'cat nums.txt'
        ]
        cmd = ' && '.join(cmds)
        out = self._exec_cmd(cmd)
        self.assertEqual(str(1), out)

    def test_next_2(self):
        cmds = [
            'cd .test_env',
            'python ./../script.py first',
            'python ./../script.py next 2',
            'cat nums.txt'
        ]
        cmd = ' && '.join(cmds)
        out = self._exec_cmd(cmd)
        self.assertEqual(str(2), out)

    def test_next_3(self):
        cmds = [
            'cd .test_env',
            'python ./../script.py first',
            'python ./../script.py next 3',
            'cat nums.txt'
        ]
        cmd = ' && '.join(cmds)
        out = self._exec_cmd(cmd)
        self.assertEqual(str(3), out)

    def test_next_10(self):
        cmds = [
            'cd .test_env',
            'python ./../script.py first',
            'python ./../script.py next 10',
            'cat nums.txt'
        ]
        cmd = ' && '.join(cmds)
        out = self._exec_cmd(cmd)
        self.assertEqual(str(5), out)
