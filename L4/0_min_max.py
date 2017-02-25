#  аналоги функций min и max
def my_max(l):
    m = float(l[0])
    for i in l:
        if float(i) > m:
            m = float(i)
    return m

def my_min(l):
    m = float(l[0])
    for i in l:
        if float(i) < m:
            m = float(i)
    return m

def main():
    s = input('Enter list of numbers (separate is ","): ')
    l = s.split(',')
    #l = [ 1, 45, 55, 789 ]
    print(l)
    _max = my_max(l)
    _min = my_min(l)
    print('Минимальное значение: ',_max)
    print('Максимальное значение: ', _min)

main()