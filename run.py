from pytest_gen import StepikTestGenerator

print("Creating tests...")
t = StepikTestGenerator('input_test_3_6_6', 'output_test_3_6_6', 'test.py', 'main_3_6_6', 'func')
t.doit()
print("Tests created!")
