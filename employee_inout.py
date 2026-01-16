class Employee:
    def __init__(self):
        print('Employee Created')
    def __del__(self):
        print('Destructor called')
def Create_obj():
    print('Making Object...')
    obj=Employee()
    print('function end...')
    return obj 
print('Calling Create.onj() function...')
obj=Create_obj()
print('program end...')           