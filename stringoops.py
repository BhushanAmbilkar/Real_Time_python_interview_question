class stringpractice:
    # constructor
    def __init__(self, str1):
        self.str1 = str1

    # Reverse String using For Loop
    def revstring(self):
        rev_str = ""
        for i in self.str1:
            rev_str = i+rev_str
        print(rev_str)
    # Python Reverse String using Slicing
    def revstring2(self):
        rev_str=self.str1[::-1]
        print(rev_str)
    # Reverse a String using While Loop
    def reverse_while_loop(self):
        s1 = ''
        length = len(self.str1) - 1
        while length >= 0:
            s1 = s1 + self.str1[length]
            length = length - 1
        print(s1)
str1 = "Mahesh Wagge"
obj = stringpractice(str1)
obj.revstring()
obj.revstring2()
obj.reverse_while_loop()