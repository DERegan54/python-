"""Word Finder: finds random words from a dictionary."""

from random import choice 

class WordFinder:
    """Finds random words in a file with a list of words.

    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """
  
    def __init__(self, path):
        """Read file and return number of items read"""
        file = open(path)
        self.words = self.parse(file)
        print(f"{len(self.words)} words read")   
      
    def __repr__(self):
        """ Displays representation"""
        return f"<WordFinder file=path> words=self.words"
    
    def parse(self, file):
        """Parse file to word list."""
        return [w.strip() for w in file] 
    
    def random(self):
        """Return a random word from word list."""
        return choice(self.words)



class SpecialWordFinder(WordFinder):
    """WordFinder that ingores blanks and #.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """ 

    def parse(self, file):
        """Parses the list of words in the file, igoring whitespace and #."""
        return [w.strip() for w in file 
                if w.strip() and not w.startswith("#")]
