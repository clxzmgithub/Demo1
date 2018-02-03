# print 'hello world'
# print abs(-4)
# print abs(4)

# num = raw_input('Now enter a number:')
# print 'Doubling your number:%d' % (int(num)*2)
# help(raw_input)

# print -2*4+3**2
# print 2<4
# print 2!=3

# pystr = 'Python'
# iscool = 'is cool'
# print pystr[0]
# print pystr[2:5]
# print '_ ' * 20
# pystr='''python
# is cool'''
# print pystr

# aList = [1, 2, 3, 4]
# print aList
# print aList[0]
# print aList[2:]
# print aList[:3]
# aList[1] = 5
# print aList


# a = ('a', 'b', 'c', 'd')
# print a
# print a[:3]
# a[1] = 1

# x = -1
# if x < 0:
#     print 'x<0'
# elif x > 0:
#     print 'x>0'
# else:
#     print 'x=0'



# count = 0
# while count < 3:
#     print count
#     count += 1

# for item in ['a', 'b', 'c', 'd']:
#     print item
#     print


# foo = 'abc'
# for i in range(len(foo)):
#     print foo[i], '(%d)' % i


# foo = 'abc'
# for i, ch in enumerate(foo):
#     print ch, '(%d)' % i


# sequared = [x ** 2 for x in range(4)]
# for i in sequared:
#     print i


# sqdEvens = [x ** 2 for x in range(8) if not x % 2]
# for i in sqdEvens:
#     print i


# handle = open('/Users/xuzhongming/Desktop/bianlifeng/mystudy_project/PythonProject/Demo1/dir/corebook2.txt')
# filename = raw_input('Enter file name: ')
# fobj = open(filename, 'r')
# for eachLine in fobj:
#     print eachLine
# fobj.close()


# try:
#     filename = raw_input('Enter file name: ')
#     fobj = open(filename, 'r')
#     for eachLine in fobj:
#         print eachLine
#     fobj.close()
# except IOError, e:
#     print 'file open error:', e


# def addMe2Me(x):
#     'apply+operation to argument'
#     return (x + x)
#
#
# print addMe2Me([1, 'a'])





# def foo(debug=True):
#     'determine in debug model print debug'
#     if (debug):
#         print 'debug'
#     print 'clxzm'
#
#
# foo()
# foo(False)




###python3.6
# class FooClass(object):
#     """my first class:FooClass"""
#     version = 0.1  # class (data) attribute
#
#     # def __new__(self, nm='John Doe'):
#     #     """constructor"""
#     #     self.name = nm  # class instance (data) attribute
#     #     print('Created a class instance for', nm)
#
#     def __init__(self, nm='John Doe'):
#         self.name = nm  # class instance (data) attribute
#         print('Created a class instance for', nm)
#         print('Created a class instance for')
#
#     def show_name(self):
#         """display instance attribute and class name"""
#         print('Your name is', self.name)
#         print('My name is', self.__class__.__name__)
#
#     def show_version(self):
#         """display class(static) attribute"""
#         print(self.version)  # references FooClass.version
#
#     def addMe2Me(self, x):  # does not use 'self' """apply + operation to argument"""
#         return x + x

# foo1 = FooClass()
# foo1.show_name()
# print(foo1.addMe2Me(2))
# foo1.show_name()
# print(foo1.version)






# import sys
# print(sys.stdout)
# sys.stdout.write('clxzm')  # version 2.6 support,version 3.6 not support
# print(sys.platform)
# print(sys.version)
# print('aaa')
# print('aaa')



print type(42)
print type(type(42))
