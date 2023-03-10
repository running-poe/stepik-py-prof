class StepikTestGenerator:

    # читаем из файлов
    def __init__(self, fname_input_test: str, fname_results: str, fname_pytest: str, main_module: str, method: str):
        self.__stream_input_in = []
        self.__stream_input_out = []
        self.__stream_result_in = []
        self.__stream_result_out = []

        with open(fname_input_test, 'r') as f:
            self.__stream_input_in = f.readlines()

        with open(fname_results, 'r') as f:
            self.__stream_result_in = f.readlines()

        self.__method = method
        self.fname_pytest = fname_pytest

        self.main_module = main_module

    # читаем из потоков (строк)
    #def set_input(self, stream_input_test: list, stream_results: list, method: str):
    #    self.__stream_input_test = stream_input_test
    #    self.__stream_result_test = stream_results
     #   self.__method = method

    def doit(self):
        self.__stream_input_out = self.__parse(True, self.__stream_input_in)
        self.__stream_result_out = self.__parse(False, self.__stream_result_in)
        self.__create_pytest()

    def __parse(self, is_input: bool, stream_in: list):
        reading_input: bool = False
        result = []
        curr_input = []
        check_str = '# INPUT DATA:' if is_input else '# OUTPUT DATA:'
        for s in stream_in:
            if s.strip() in [check_str, '']:
                continue

            if not reading_input and not s.strip().startswith('#'):
                reading_input = True
                curr_input.append(s.strip())
                continue

            if reading_input and s.strip().startswith('#'):
                reading_input = False
                result.append(curr_input)
                curr_input = []

            if reading_input and not s.strip().startswith('#'):
                curr_input.append(s.strip())
        return result

    def __create_pytest(self):
        with open(self.fname_pytest, 'w') as f:
            f.write(f'from {self.main_module} import func\n\n\n')
            for k, t_in in enumerate(self.__stream_input_out):
                s1 = f'{t_in}'.replace('[', '').replace(']', '')
                s2 = f'{self.__stream_result_out[k]}'.replace('[', '').replace(']', '')
                f.write(f"def test{k}():\n")
                f.write(f"    assert {self.__method}({s1}) == ({s2})\n\n\n")





''' 
    
'''









