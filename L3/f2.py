def say_hello(name, age):
    print('Hello ' + name)
    print('Your age is: ', age)

def main():
    name = input('Please - enter your name :')
    age = int(input('Please - enter your age : '))
    say_hello(name, age)

if __name__ == '__name__':
    main()
