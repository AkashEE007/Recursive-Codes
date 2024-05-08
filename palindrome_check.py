class PalindromeCheck:
    """Checks whether a given string is a palindrome or not."""

    def __init__(self):
        self.input_str = input("Enter a string: ")

    def _remove_punct(self):
        """The method removes any spaces, punctuations and special characters in the string.
        Returns a string of lower case characters."""

        self.input_str = self.input_str.lower()
        punctuations = ''' ''!@#$%^&*()_-+=/*.?<>:;""'''
        for char in self.input_str:
            if char in punctuations:
                self.input_str = self.input_str.replace(char,"")
        return self.input_str
     
    def _string_reversal(self,input_str):
        """The method reverses the string recursively.
        Returns a reversed string."""

        reverse_str = ""

        if len(input_str) < 1:  #Base case of recursion
            return input_str
    
        else:
            reverse_str = self._string_reversal(input_str[1:]) + input_str[0]
            return reverse_str
        
    def palindrome_check(self):
        """The method checks whether the input string matches reversed string or not.
        Returns a Boolean value."""
        
        self._remove_punct()
        if self.input_str == self._string_reversal(self.input_str):
            return True
        
        else:
            return False
        
if __name__ == '__main__':
    check = PalindromeCheck()
    print(check.palindrome_check())