from my_module.Get_Natal_Chart import combine_natal_chart
import my_module.Get_Lunar_Feast as lf
import os

class Fate:
      """
      Parameters:
      - birth (list): A tuple representing the birth information, including year month day and hour 
      - sex (str): A string representing the gender ('Male', 'Female').

      Attributes:
      - pillar (None): Placeholder for pillar attribute.
      - cycle (list): List to store cycle information.
      - age (list): List to store age information.
      - combined_cycle (list): List to store combined cycle information.
      - cycle_ten_gods (list): List to store cycle ten gods information.
      - fate_comment_path (str): File path for fate-related comments.
      - fate_comment (str): Placeholder for fate-related comments.
      - comment (str): Placeholder for comments.
      - day_ganzhi_table (list): List representing the day ganzhi table.
      - ten_gods_dict (dict): Dictionary mapping day ganzhi to ten gods.
      """
    
      pillar = None
      cycle = []
      age = []
      combined_cycle = []
      cycle_ten_gods = []
      fate_comment_path = 'ten_god_inter.txt'
      fate_comment = ''
      
      comment = ''
      day_ganzhi_table= [
        '甲子',  '乙丑' , '丙寅' , '丁卯' , '戊辰' , '己巳',  '庚午' , '辛未' , '壬申',  '癸酉',
        '甲戌',  '乙亥' , '丙子' , '丁丑' , '戊寅',  '己卯',  '庚辰',  '辛巳',  '壬午',  '癸未',
        '甲申',  '乙酉',  '丙戌' , '丁亥',  '戊子',  '己丑',  '庚寅',  '辛卯',  '壬辰',  '癸巳',
        '甲午',  '乙未',  '丙申',  '丁酉',  '戊戌',  '己亥',  '庚子',  '辛丑',  '壬寅',  '癸卯', 
        '甲辰',  '乙巳',  '丙午',  '丁未',  '戊申',  '己酉',  '庚戌',  '辛亥',  '壬子',  '癸丑',
        '甲寅',  '乙卯',  '丙辰',  '丁巳',  '戊午',  '己未',  '庚申',  '辛酉',  '壬戌',  '癸亥'
        ]
      
      ten_gods_dict = {
        '甲子': '比肩', '乙丑': '劫财', '丙寅': '正印', '丁卯': '正官', '戊辰': '正财',
        '己巳': '七杀', '庚午': '食神', '辛未': '偏财', '壬申': '比肩', '癸酉': '劫财',
        '甲戌': '伤官', '乙亥': '七杀', '丙子': '正印', '丁丑': '正官', '戊寅': '正财',
        '己卯': '偏印', '庚辰': '伤官', '辛巳': '七杀', '壬午': '食神', '癸未': '正官',
        '甲申': '正财', '乙酉': '劫财', '丙戌': '伤官', '丁亥': '七杀', '戊子': '比肩',
        '己丑': '劫财', '庚寅': '伤官', '辛卯': '七杀', '壬辰': '正印', '癸巳': '正官',
        '甲午': '正财', '乙未': '劫财', '丙申': '伤官', '丁酉': '七杀', '戊戌': '比肩',
        '己亥': '劫财', '庚子': '伤官', '辛丑': '七杀', '壬寅': '正印', '癸卯': '正官',
        '甲辰': '正财', '乙巳': '劫财', '丙午': '伤官', '丁未': '七杀', '戊申': '正印',
        '己酉': '正官', '庚戌': '偏财', '辛亥': '劫财', '壬子': '伤官', '癸丑': '七杀',
        '甲寅': '正印', '乙卯': '正官', '丙辰': '正财', '丁巳': '劫财', '戊午': '伤官',
        '己未': '七杀', '庚申': '正印', '辛酉': '正官', '壬戌': '偏财', '癸亥': '劫财'
    }

      def __init__(self,birth,sex):
        self.birth = birth
        self.sex = sex 
        
      def get_path(self,filename):
          """
          Construct and return the absolute path for a file within the 'scripts' directory.

          Parameters:
          - filename (str): The name of the file to be included in the path.

          Returns:
          str: The absolute path to the specified file within the 'scripts' directory.
          """
          current_directory = os.getcwd()
          path = os.path.join(current_directory,'scripts', filename)
          return path

      
      def update_pillar(self):
          """
          Update the 'pillar' attribute based on the birth information using the 'combine_natal_chart' function.

          Returns:
          self: The instance with the updated 'pillar' attribute.
          """
          self.pillar  = combine_natal_chart(self.birth)
          return self 
      
      def define_sequence(self):
          """
          Define a sequence based on the birth year's heavenly stem and the gender information.

          Updates the 'pillar' attribute using 'update_pillar' method.

          Returns:
          int: The determined sequence (1 or -1).

          Explanation:
          - The sequence is determined based on the heavenly stem of the birth year and the gender of the individual.
          - If the heavenly stem is one of ['甲', '丙', '戊', '庚', '癸']:
              - For males, the sequence is set to 1.
              - For females, the sequence is set to -1.
          - Otherwise (if the heavenly stem is not in the specified list):
              - For females, the sequence is set to 1.
              - For males, the sequence is set to -1.
          """
          sequence = None

          # Update the 'pillar' attribute using the 'update_pillar' method
          self.update_pillar()
          year_gan = self.pillar[0][0]

          # Determine sequence based on year's heavenly stem and gender information
          if year_gan in ['甲', '丙', '戊', '庚', '癸']:
              if self.sex == "Male":
                  sequence = 1  # Set sequence to 1 for males
              else:
                  sequence = -1  # Set sequence to -1 for females
          else:
              if self.sex == "Female":
                  sequence = 1  # Set sequence to 1 for females
              else:
                  sequence = -1  # Set sequence to -1 for males

          return sequence 
          
      def gene_cycle(self):
          """
          Generate a cycle of day ganzhi based on the defined sequence and the starting day ganzhi.

          Updates the 'sequence' attribute using 'define_sequence' method.
          Updates the 'pillar' attribute using 'update_pillar' method.

          Returns:
          self: The instance with the updated 'cycle' attribute.

          Explanation:
          - The cycle is generated based on the defined sequence (positive or negative) and the starting day ganzhi.
          - The starting day ganzhi is determined by combining the elements of the second element in the pillar.
          - The cycle is a list of day ganzhi representing a sequence of days.
          """
          sequence = self.define_sequence()

          # Update the 'pillar' attribute using the 'update_pillar' method
          self.update_pillar()

          # Determine the starting day ganzhi
          start = self.pillar[1][0] + self.pillar[1][1]
          start_index = self.day_ganzhi_table.index(start)

          result = []

          # Generate the cycle of day ganzhi based on the defined sequence
          for i in range(1, 10):
              if sequence == 1:
                  stop = self.day_ganzhi_table[(start_index + i) % len(self.day_ganzhi_table)]
                  result.append(stop)
              elif sequence == -1:
                  stop = self.day_ganzhi_table[start_index - i]
                  result.append(stop)

          # Update the 'cycle' attribute with the generated cycle
          self.cycle = result
          return self
          
          
      def get_age(self):
          """
          Calculate and set age milestones based on the birth information.

          Updates the 'age' attribute with a list of age milestones.

          Returns:
          self: The instance with the updated 'age' attribute.

          Explanation:
          - Calculates the number of days between the birth date and the reference date.
          - Divides the days into 3-year intervals to determine the starting year.
          - Generates a list of age milestones at 10-year intervals starting from the calculated starting year.
          """
          # Calculate the number of days between the birth date and the reference date
          day_diff = lf.get_days_diff(self.birth)

          # Calculate the starting year for age milestones based on 3-year intervals
          start_year = day_diff // 3

          result = []

          # Generate a list of age milestones at 10-year intervals
          for i in range(0, 9):
              inflection_age = start_year + i * 10
              result.append(inflection_age)

          # Update the 'age' attribute with the generated age milestones
          self.age = result
          return self

      def get_combined_cycle(self):
          """
          Combine age milestones and day ganzhi cycle into a list of tuples.

          Updates the 'combined_cycle' attribute with a list of tuples representing age milestones and corresponding day ganzhi.

          Returns:
          self: The instance with the updated 'combined_cycle' attribute.

          Explanation:
          - Calls 'get_age' method to calculate age milestones.
          - Calls 'gene_cycle' method to generate the day ganzhi cycle.
          - Combines age milestones and day ganzhi into a list of tuples.
          """
          result = []

          # Calculate age milestones using 'get_age' method
          self.get_age()

          # Generate day ganzhi cycle using 'gene_cycle' method
          self.gene_cycle()

          # Combine age milestones and day ganzhi into a list of tuples
          for i in zip(self.age, self.cycle):
              j = [i[0], i[1]]
              result.append(j)

          # Update the 'combined_cycle' attribute with the generated list of tuples
          self.combined_cycle = result
          return self
     
      def gene_ten_gods(self):
            """
            Generate the ten gods for each element in the combined cycle.

            This method retrieves the combined cycle, maps each element to its corresponding
            ten gods based on the 'ten_gods_dict', and updates the 'cycle_ten_gods' attribute.

            Returns:
            self: The instance with the updated 'cycle_ten_gods' attribute.
            """
            self.get_combined_cycle()
            result = self.combined_cycle 
            for i in result :
                i[1] = self.ten_gods_dict[i[1]]
            self.cycle_ten_gods = result 
            return self 
      
      def get_path(self,filename):
          """
          Construct and return the absolute path for a file within the 'scripts' directory.

          Parameters:
          - filename (str): The name of the file to be included in the path.

          Returns:
          str: The absolute path to the specified file within the 'scripts' directory.
          """
          current_directory = os.getcwd()
          path = os.path.join(current_directory,'scripts', filename)
          return path 
      
      def load_fate_descriptions(self):
          """
          Load fate descriptions from a file and organize them into a dictionary.

          Reads the fate descriptions from the specified file path and organizes them into a dictionary
          where keys are zodiac signs or god signs and values are the corresponding descriptions.

          Returns:
          dict: A dictionary containing fate descriptions.

          Explanation:
          - Opens the fate file at the specified path using 'get_path' method.
          - Iterates through each line in the file and organizes fate descriptions into a dictionary.
          - Each god sign or zodiac sign is used as a key, and the corresponding description is the value.
          """
          fate_descriptions = {}
          current_god = None
          description_lines = []

          # Get the file path for fate descriptions using 'get_path' method
          fate_path = self.get_path(self.fate_comment_path)

          with open(fate_path, 'r', encoding='utf-8') as file:
              for line in file:
                  line = line.strip()

                  # Check if the line is empty, indicating a new god sign
                  if not line:
                      if current_god and description_lines:
                          # Store the collected description lines for the current god sign
                          fate_descriptions[current_god] = '\n'.join(description_lines)
                          description_lines = []  # Reset for the next god
                      continue

                  # Check if the line starts with a number (indicating a zodiac sign)
                  if line[0].isdigit():
                      current_god = line[2:]
                  else:
                      description_lines.append(line)

          return fate_descriptions
      
     

      def gene_fate_comment(self):
          """
          Generate fate comments based on the loaded descriptions and the cycle of ten gods.

          Loads fate descriptions using 'load_fate_descriptions' method.
          Generates fate comments based on the cycle of ten gods and age milestones.

          Returns:
          self: The instance with the updated 'fate_comment' attribute.

          Explanation:
          - Loads fate descriptions into a dictionary using 'load_fate_descriptions' method.
          - Generates the cycle of ten gods using 'gene_ten_gods' method.
          - Iterates through the cycle of ten gods, retrieving the corresponding age and fate description.
          - Appends the age and fate description to the 'fate_comment' attribute.
          """
          # Load fate descriptions into a dictionary using 'load_fate_descriptions' method
          dic = self.load_fate_descriptions()

          # Generate the cycle of ten gods using 'gene_ten_gods' method
          self.gene_ten_gods()
          table = self.cycle_ten_gods

          for i in table:
              sign = i[1]
              # Append age and fate description to the 'fate_comment' attribute
              self.fate_comment += ('\n\n' + f" Age [{self.age[table.index(i)]}] " + "\n\n" + dic[sign])

          return self