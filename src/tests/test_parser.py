# -*- coding: utf-8 -*-
#
# Poio Tools for Linguists
#
# Copyright (C) 2009-2012 Poio Project
# Author: António Lopes <alopes@cidles.eu>
# URL: <http://www.cidles.eu/ltll/poio>
# For license information, see LICENSE.TXT
"""This module contains the tests to the class
PyGraphParser in module PyGraphParser.

This test serves to ensure the viability of the
methods of the class PyGraphParser in PyGraphParser.py.
"""
import codecs
import os

from graf import GraphParser

class TestGraphParser:
    """
    This class contains the test methods of the class GraphParser.

    """

    def setUp(self):
        self.gparser = GraphParser()

    def test_parse(self):
        """Raise an assertion if can't find a file.

        Return a PyGraph.

        Raises
        ------
        AssertionError
            If the can't find the file.

        """

        # Change directory
        # Opening the expected file result
        #file = os.path.dirname(__file__) + '/sample_files/' +\
        #       'balochi-graid1.xml'

        file = os.path.dirname(__file__) + '/sample_files/' +\
                      'balochi-header.hdr'

        file_stream = codecs.open(file, "r", "utf-8")

        g = self.gparser.parse(file_stream)

        expected_result = 624

        assert(len(g.nodes) == expected_result)

