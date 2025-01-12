from typing import Sequence, Any, Callable


class Seq:
    
    """Sequence class"""
    
    def __init__(self, sequence: Sequence[Any]):
        """
        Initializes the Seq object with a sequence.

        Args:
            sequence (Sequence[Any]): An input sequence of elements to be stored in the Seq object.
        """
        self.sequence = list(sequence)
        
    def map(self, func: Callable[[Any], Any]):
        """
        Applies a given function to each element in the sequence and returns a new Seq object 
        containing the results.

        Args:
            func (Callable[[Any], Any]): A function that takes an element from the sequence and 
            returns a transformed element.

        Returns:
            Seq: A new Seq object containing the transformed elements.
        """

        mapped_sequence = []
        for item in self.sequence:
            mapped_sequence.append(func(item))
        return Seq(mapped_sequence)
    
    def filter(self, func: Callable[[Any], bool]):
        """
        Filters the elements in the sequence based on a given predicate and returns a new Seq object containing the filtered elements.

        Args:
            func (Callable[[Any], bool]): A function that takes an element from the sequence and returns a boolean value indicating whether the element should be included in the filtered sequence.

        Returns:
            Seq: A new Seq object containing the filtered elements.
        """
        filtred_sequence = []
        for item in self.sequence:
            if func(item) == True:
                filtred_sequence.append(item)
        return Seq(filtred_sequence)
    
    def take(self, count: int):
        """
        Takes a specified number of elements from the start of the sequence and returns a new Seq object containing the taken elements.

        Args:
            count (int): The number of elements to be taken from the start of the sequence.

        Returns:
            Seq: A new Seq object containing the taken elements.
        """
        return Seq(self.sequence[:count])
    
    def __str__(self):
        return str(self.sequence)
    
    
if __name__ == "__main__":
    seq = Seq([1, 2, 3, 4, 5])
    print(seq.map(lambda x: x * 2))
    print(seq.filter(lambda x: x % 2 == 0))
    print(seq.take(3))
    print(seq.take(3).map(lambda x: x * 2))
        