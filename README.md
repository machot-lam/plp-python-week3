# plp-python-week3
# Python Loops and Debugging Assignment

* `grade_reporter.py` - Evaluates student scores, assigns letter grades, calculates pass/fail counts, and computes the class average using a single consolidated loop.
* `bug_hunt.py` - A debugging exercise featuring a while loop designed to calculate the sum of numbers from 1 to 5, with multiple errors successfully corrected.

### Reflection on Debugging Part B

The hardest bug to find in Part B was the logic/boundary error (`count < 5` instead of `count <= 5`), because it did not trigger a syntax or type error and the program ran without crashing. I knew something was wrong when the program successfully executed but printed a total of 10 instead of the expected 15, which signaled that the final iteration (the number 5) was being skipped entirely.
