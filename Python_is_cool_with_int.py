import pytest

def func_tests(x):
      for i in x:	
  	return "Test :" + str(i)

def test_answer():
	assert func_tests([1,2,3,4,5]) == "Test :1"
