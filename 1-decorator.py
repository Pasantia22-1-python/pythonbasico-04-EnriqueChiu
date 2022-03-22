PASSW = '12345'

def pass_required(func):
    def wrapper():
        password = input('What is your password? ')
        if password == PASSW:
            return func()
        else:
            print('The password is incorrect')

    return wrapper

@pass_required
def needs_pass():
    print('Password Correct')


def upper(func):
    def wrapper(*args, **kargs):
        result = func(*args, **kargs)
        
        return result.upper()

    return wrapper

@upper
def say_my_name(name):
    return ('Hola {}'.format(name))

if __name__ == '__main__':
    print(say_my_name('Julio'))


