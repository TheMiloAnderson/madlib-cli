# MadLib CLI

**Author**: Milo Anderson
**Version**: 0.1.0

## Overview
A function that generates MadLibs by combining user input with a text template file.

## Getting started
This project uses Python 3.6; testing is done with pytest. Set your environment accordingly.

## Architecture
madlib.py reads text from a file; it then uses the 're' Python library to find all input substitution instances in the text, and replace them with user input. The substituted text is saved to a file, output to the console, and returned by the function (for testing purposes)

## Change Log
02-20-2019 5:00pm - App & tests are working the way they're supposed to
