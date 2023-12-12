import os

class ZodiacAna :# pillar is a list
    zodiac = None
    zodiac_comment = None
    zodiac_path = "animal_zodiac.txt"
    
    def __init__ (self, pillar):
        self.pillar = pillar 
        
   

    def get_path(self,filename):
        """
       Construct and return the absolute path for a file within the 'scripts' directory.
 
       Parameters:
       - filename (str): The name of the file to be included in the path.

       Returns:
       str: The absolute path to the specified file within the 'scripts' directory.

       Example:
       >>> obj = YourClass()
       >>> file_name = "example.txt"
       >>> result = obj.get_path(file_name)
       >>> print(result)
       "/path/to/current/directory/scripts/example.txt"
       """
        current_directory = os.getcwd()
        path = os.path.join(current_directory,'scripts', filename)
        return path


        
    
     
    def load_zodiac_descriptions(self):
        zodiac_descriptions = {}
        current_zodiac = None
        description_lines = []

        with open(self.get_path(self.zodiac_path), 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()

            # Check if the line is empty, indicating a new zodiac sign
                if not line:
                    if current_zodiac and description_lines:
                        zodiac_descriptions[current_zodiac] = '\n'.join(description_lines)
                        description_lines = []  # Reset for the next zodiac
                    continue

                # Check if the line starts with a number (indicating a zodiac sign)
                if line[0].isdigit():
                    current_zodiac = line[2:]
                else:
                    description_lines.append(line)

        return zodiac_descriptions   
  
  
    def obtain_zodiac_animal(self):
        """
        Obtain the zodiac animal based on the Earth stem of the birth year.

        Returns:
         The zodiac animal corresponding to the Earth stem of the birth year,
                 or None if the mapping is not available.

        Explanation:
        - Retrieves the Earth stem of the birth year from the pillar.
        - Maps the Earth stem to the corresponding zodiac animal using a predefined dictionary.
        - Returns the zodiac animal or None if the Earth stem is not found in the mapping.
        """
        year_earth_stem = self.pillar[0][1]
        zodiac_mapping = {
        '子': 'Rat',
        '丑': 'Ox',
        '寅': 'Tiger',
        '卯': 'Rabbit',
        '辰': 'Dragon',
        '巳': 'Snake',
        '午': 'Horse',
        '未': 'Goat',
        '申': 'Monkey',
        '酉': 'Rooster',
        '戌': 'Dog',
        '亥': 'Pig'
        }

        return zodiac_mapping.get(year_earth_stem)

    def update_zodiac(self):
        self.zodiac = self.obtain_zodiac_animal()
        return self 
    
    def obtain_zodiac_comment(self):
        """
        Obtain the zodiac comment based on the current zodiac sign.

        Updates the 'zodiac_comment' attribute with the comment corresponding to the current zodiac sign.

        Returns:
        self: The instance with the updated 'zodiac_comment' attribute.

        Explanation:
        - Calls 'update_zodiac' method to determine the current zodiac sign.
        - Retrieves the zodiac comment from the loaded zodiac descriptions using 'load_zodiac_descriptions' method.
        - Updates the 'zodiac_comment' attribute with the retrieved comment.

        """
        # Update the current zodiac sign using 'update_zodiac' method
        self.update_zodiac()

        # Get the current zodiac sign
        z = self.zodiac

        # Load zodiac descriptions into a dictionary using 'load_zodiac_descriptions' method
        dic = self.load_zodiac_descriptions()
        # Retrieve the zodiac comment from the loaded descriptions
        self.zodiac_comment = dic.get(z)

        return self