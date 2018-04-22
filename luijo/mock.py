#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by pat on 4/21/18
"""
.. currentmodule:: testing
.. moduleauthor:: Pat Daburu <pat@daburu.net>

Say something descriptive about the 'testing' module.
"""
import luigi
import luigi.mock


class MockTask(luigi.Task):

    def requires(self):
        """
        This task has no requirements.

        :return: an empty iteration
        """
        return []

    def output(self) -> luigi.mock.MockTarget:
        """
        This implementation returns a mock target.

        :return: a mock target
        """
        return luigi.mock.MockTarget()

    def run(self):
        """
        Running the task has no effect.
        """
        pass
