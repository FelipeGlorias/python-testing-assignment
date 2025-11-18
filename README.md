# python-testing-assignment

# Homework
- Name: Felipe Glorias
## Question 1) Define the following unit, integration, regression tests and when you would use each?
- Unit test: Checks a single function isolated from the rest to verify its working. The utilization of this is done to make sure tha  sole function works without other funcitons. 
- Integration test: Checks multiple functions or pieces of code and how they work together. You would use this to make sure that these different parts work together when combined. 
- Regression test: These tests are used to make sure that a bug fix works as intended.  You would use this test  to make sure that the bug doesn't occur again 
## Question 2) Briefly explain pytest discovery (file/function naming) and what a fixture is.
Pytest locates test files and functions based on their names. A file must have test_###.py, funstions have to start with test_, and classes have to start with Test. Fixtures on the other hand are reusable code thst gives data for tests. It helps with setting up your code as well as cleaning it up, cutting a lot of repetition out. You can create these fixtures with the decorator @pytest.fixture, which then passes test functions as parameters.
