#import SummerProjects

class EquationMethods:
    def print_solution(s):
        return print(str(format(s, '.4f')).replace('j', 'i').replace('+0.0000i', '').replace('-0.0000i', '').replace('-0.0000', '0')
                 .replace('0.0000', '0').replace('.0000', '').replace('1i', 'i'))