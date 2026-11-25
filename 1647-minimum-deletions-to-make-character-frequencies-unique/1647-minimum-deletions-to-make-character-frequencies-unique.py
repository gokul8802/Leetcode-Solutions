# Define a class called Solution.
class Solution:
    # Define a method called minDeletions within the Solution class.
    # This method takes a string 's' as input and returns an integer.
    def minDeletions(self, s: str) -> int:
        # Create a Counter object 'char_count' to count the frequency of each character in the input string 's'.
        char_count = Counter(s)
        # Initialize a variable 'deletions' to keep track of the number of deletions needed.
        deletions = 0
        # Create an empty set 'unique_frequencies' to store unique frequencies encountered.

        unique_frequencies = set()

        # Iterate through each character and its frequency in 'char_count'.
        for char, freq in char_count.items():
            # Enter a loop while the current frequency 'freq' is greater than 0 and it is already in 'unique_frequencies'.
            while freq > 0 and freq in unique_frequencies:
                # Decrement 'freq' by 1, indicating that we are considering deleting one occurrence of this character.
                freq -= 1
                # Increment 'deletions' by 1, as we are performing a deletion operation.
                deletions += 1
            # Add the current 'freq' to 'unique_frequencies' to mark it as seen.
            unique_frequencies.add(freq)
            
        # After processing all characters, return the total number of deletions needed.
        return deletions