from pytest_gen import StepikTestGenerator

print("Creating tests...")
t = StepikTestGenerator('input_test_3.5.8', 'output_test_3.5.8', 'test.py', 'main_3_5_8', 'func')
t.doit()
print("Tests created!")
