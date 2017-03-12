""" run only FROM cli"""
import sys
text = sys.argv[1]
# text = 'test    test   test'
print(sys.argv)
print('*' * (len(text)+2))
print('*',text,'*', sep='')
print('*' * (len(text)+2))
print()
print(__name__)