import os

class ElementAna :
    """
     Class for elemental analysis based on a given pillar.

    Attributes:
    - pillar (tuple): A tuple representing elements.
    - life_determinant (str): The determined life determinant.
    - life_determinant_comment_gene (str): General comment related to the life determinant.
    - ld_interaction_comment (str): Elemental interaction comment based on the life determinant.
    - life_determinant_path_gene (str): File path for life determinant general comment.
    - element_stat (list): Element counts based on the pillar.
    - element_stat_balance (list): Categorized element counts as deficit or excess.
    - element_stat_comment (str): General comment based on element counts.
    - element_inter_path (str): File path for elemental interaction descriptions.
    - element_deficit_path (str): File path for element deficit descriptions.
    """
    life_determinant = None
    life_determinant_comment_gene = ''
    ld_interaction_comment = ''
    life_determinant_path_gene = "life_deter_gene.txt"
    
    element_stat = None
    element_stat_balance = None
    element_stat_comment = ''
    element_inter_path = 'element_interaction.txt'
    element_deficit_path = "element_deficit.txt"
    
    def __init__ (self, pillar):
        """
       Parameters:
       - pillar (list): A list representing elements.

        """
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

        
     
    def load_element_descriptions(self, file_path):
        """
        Load element descriptions from a file and return them as a dictionary.

        Parameters:
        - file_path (str): The path to the file containing element descriptions.

        Returns:
        dict: A dictionary where keys are element names and values are corresponding descriptions.

        Example:
        >>> obj = YourClass()
        >>> file_path = "path/to/descriptions.txt"
        >>> result = obj.load_element_descriptions(file_path)
        >>> print(result)
        {'Element1': 'Description of Element1', 'Element2': 'Description of Element2', ...}
        """
        # Initialize variables
        element_descriptions = {}
        current_element = None
        description_lines = []

        # Open the file and read its content
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Strip leading and trailing whitespaces from the line
                line = line.strip()

                # Check for empty lines to separate elements and descriptions
                if not line:
                    # If there is a current element and description lines, store them in the dictionary
                    if current_element and description_lines:
                        element_descriptions[current_element] = '\n'.join(description_lines)
                        description_lines = []
                    continue

                # Check if the line starts with a digit, indicating a new element
                if line[0].isdigit():
                    current_element = line[2:]
                    
                else:
                    # If not, it is part of the description for the current element
                    description_lines.append(line)
                    

        # Return the dictionary of element descriptions
        return element_descriptions

 
    def obtain_element(self):
        """
        Count the occurrences of elements in the 'pillar' attribute and update the 'element_stat' attribute.

        The 'pillar' attribute is assumed to be a nested list representing elements in a specific format.

        Elements are categorized into Wood, Fire, Earth, Metal, and Water based on specific characters.

        Returns:
        self: The instance with the updated 'element_stat' attribute.

        Example:
        >>> obj = YourClass()
        >>> obj.pillar = [['甲', '丙', '戊', '庚', '壬'], ['乙', '丁', '己', '辛', '癸']]
        >>> obj.obtain_element()
        >>> print(obj.element_stat)
        [['Wood', 2], ['Fire', 3], ['Earth', 2], ['Metal', 2], ['Water', 1]]
        """
        # Initialize a list to store the counts of each element
        element_stat = [['Wood', 0], ['Fire', 0], ['Earth', 0], ['Metal', 0], ['Water', 0]]

        # Iterate through each sublist in 'pillar'
        for i in self.pillar:
            for j in i:
                # Check the specific characters and update the corresponding element count
                if j in ["甲", "乙", "寅", "卯"]:
                    element_stat[0][1] += 1
                elif j in ["丙", "丁", "巳", "午"]:
                    element_stat[1][1] += 1
                elif j in ["戊", "己", "戌", "未"]:
                    element_stat[2][1] += 1
                elif j in ["庚", "辛", "申", "酉"]:
                    element_stat[3][1] += 1
                elif j in ["壬", "癸", "亥", "子"]:
                    element_stat[4][1] += 1

        # Update the 'element_stat' attribute with the calculated counts
        self.element_stat = element_stat

        # Return the instance with the updated 'element_stat' attribute
        return self

    def balance_analysis(self):
        """
        Analyze the balance of elements based on their counts in 'element_stat'.

        Elements are categorized into 'deficit' if their count is zero and 'excess' if their count is three or more.

        Updates the 'element_stat_balance' attribute with the analysis.

        Returns:
        self: The instance with the updated 'element_stat_balance' attribute.

        Example:
        >>> obj = YourClass()
        >>> obj.element_stat = [['Wood', 2], ['Fire', 3], ['Earth', 2], ['Metal', 2], ['Water', 1]]
        >>> obj.balance_analysis()
        >>> print(obj.element_stat_balance)
        [['deficit', 'Wood', 'Earth', 'Metal', 'Water'], ['excess', 'Fire']]
        """
        # Initialize a list to store elements with deficit and excess counts
        balance_lst = [['deficit'], ['excess']]

        # Iterate through each element in 'element_stat'
        for i in self.element_stat:
            # Check if the count is zero and categorize as 'deficit'
            if i[1] == 0:
                balance_lst[0].append(i[0])
            # Check if the count is three or more and categorize as 'excess'
            elif i[1] >= 3:
                balance_lst[1].append(i[0])

        # Update the 'element_stat_balance' attribute with the balance analysis
        self.element_stat_balance = balance_lst

        # Return the instance with the updated 'element_stat_balance' attribute
        return self

    
    def load_element_general_comment(self):
        """
        Load a general comment based on the counts of elements obtained from 'obtain_element'.

        Updates the 'element_stat_comment' attribute with the general comment.

        Returns:
        self: The instance with the updated 'element_stat_comment' attribute.

        Example:
        >>> obj = YourClass()
        >>> obj.load_element_general_comment()
        >>> print(obj.element_stat_comment)
        'You have 2 Wood elements. You have 3 Fire elements. ...'
        """
        # Initialize an empty string to store the general comment
        result = ''

        # Obtain element counts using the 'obtain_element' method
        self.obtain_element()

        # Iterate through each element in 'element_stat' and construct the comment
        for i in self.element_stat:
            result += f'You have {i[1]} {i[0]} element. '
            
       

        # Update the 'element_stat_comment' attribute with the constructed comment
        self.element_stat_comment += result

        # Return the instance with the updated 'element_stat_comment' attribute
        return self

        
    def load_element_deficit_comment(self):
        """
        Load comments related to element deficits based on the balance analysis.

        Updates the 'element_stat_comment' attribute with deficit-related comments.

        Returns:
        self: The instance with the updated 'element_stat_comment' attribute.

        Example:
        >>> obj = YourClass()
        >>> obj.load_element_deficit_comment()
        >>> print(obj.element_stat_comment)
        '[No Deficit]\n\nDescription for No Deficit\n\n[Lack Wood]\nDescription for Lack Wood\n...'
        """
        # Obtain element counts using the 'obtain_element' method
        self.obtain_element()

        # Perform balance analysis using the 'balance_analysis' method
        self.balance_analysis()

        # Initialize an empty string to store the deficit-related comments
        result = ''

        # Get the file path for element deficit descriptions
        deficit_path = self.get_path(self.element_deficit_path)

        # Load element deficit descriptions from the specified file
        dic = self.load_element_descriptions(deficit_path)
        

        # Check if there are no deficits and provide a default comment
        if len(self.element_stat_balance[0]) == 1:
            result = "\n" + '[No Deficit]' + '\n\n' + dic['No_Deficit']
            self.element_stat_comment += result
        else:
            # Iterate through deficit elements and append their descriptions to the comment
            for i in self.element_stat_balance[0][1:]:
                result = "\n" + f"[Lack {i}]" + "\n" + dic[i]
                self.element_stat_comment += result
                self.element_stat_comment += '\n'

        # Return the instance with the updated 'element_stat_comment' attribute
        return self

    
    def find_life_determinant(self):
        """
        Determine the life determinant based on the first character of the third element in the 'pillar'.

        The 'pillar' attribute is assumed to be a nested list representing elements.

        Updates the 'life_determinant' attribute with the determined life determinant.

        Returns:
        self: The instance with the updated 'life_determinant' attribute.
        """
        p = self.pillar[2][0]
        if p == '甲':
            self.life_determinant = "Wood α"
        elif p == '乙':
            self.life_determinant = 'Wood β'
        elif p == '丙':
            self.life_determinant = 'Fire ψ'
        elif p == '丁':
            self.life_determinant = 'Fire δ'
        elif p == '戊':
            self.life_determinant = 'Earth ε'
        elif p == '己':
            self.life_determinant = 'Earth φ'
        elif p == '庚':
            self.life_determinant = 'Metal γ'
        elif p == '辛':
            self.life_determinant = 'Metal η'
        elif p == '壬':
            self.life_determinant = 'Water ι'
        elif p == '癸':
            self.life_determinant = 'Water ξ'
        return self 
            
    def get_determinant_general_comment(self):
        """
        Get a general comment based on the life determinant obtained from 'find_life_determinant'.

        Updates the 'life_determinant_comment_gene' attribute with the general comment.

        Returns:
        self: The instance with the updated 'life_determinant_comment_gene' attribute.

        """
        # Find the life determinant using the 'find_life_determinant' method
        self.find_life_determinant()
       

        # Get the determined life determinant
        determinant = self.life_determinant
        

        # Get the file path for the life determinant general comment
        life_determinant_path = self.get_path(self.life_determinant_path_gene)

        # Load the life determinant general comment from the specified file
        dic = self.load_element_descriptions(life_determinant_path)
       
       
        # Update the 'life_determinant_comment_gene' attribute with the general comment
        self.life_determinant_comment_gene = dic[determinant]
        

        # Return the instance with the updated 'life_determinant_comment_gene' attribute
        return self


    
    def find_interactions(self):
        """
        Find and categorize elemental interactions based on the determined life determinant.

        Updates the 'ld_interaction_comment' attribute with the interactions.

        Returns:
        self: The instance with the updated 'ld_interaction_comment' attribute.
        """
        interaction_path = self.get_path(self.element_inter_path)
        dic = self.load_element_descriptions(interaction_path)
        result = ''
        self.find_life_determinant()
        if "Wood" in self.life_determinant:
            result += "[Supporting Elements:Wood and Water] \n\n[Counteracting Elements: Metal] \n\n"
            result += (dic["Wood"] + '\n')
        elif "Fire" in self.life_determinant:
            result += "[Supporting Elements: Wood and Fire] \n\n[Counteracting Elements: Water]\n\n"
            result += (dic["Fire"] + '\n')
        elif "Earth" in self.life_determinant:
            result += "[Supporting Elements:Fire and Earth] \n\n[Counteracting Elements: Wood]\n\n"
            result += (dic["Earth"] + '\n')
        elif "Metal" in self.life_determinant:
            result += "[Supporting Elements:Earth and Metal] \n\n[Counteracting Elements: Fire]\n\n"
            result += (dic["Metal"] + '\n')
        elif "Water" in self.life_determinant:
            dic["Water"] = 'In the realm of water, your essence flows,\nWith metal and water, a synergy grows.\nYet beware, for wood, fire, and earthly might,\nMay disrupt the harmony, casting shadows on your light.'
            result += "[Supporting Elements:Water and Metal] \n\n[Counteracting Elements: Wood]\n\n"
            result += (dic["Water"] + '\n')
            
        self.ld_interaction_comment += result 
        
        return self 