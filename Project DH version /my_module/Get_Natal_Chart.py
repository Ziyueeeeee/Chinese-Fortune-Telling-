#Obtain Your Natal Chart 
__package__ 
import datetime
import os
from lunarcalendar import Lunar,Solar, Converter
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties



def isleap(year):
    """
    Check if a given year is a leap year.

    Parameters:
    - year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if (year % 100 == 0) and (year % 400 == 0):
      return True
    elif (year % 100 != 0) and (year % 4 == 0):
        return True 
    else:
        False 
        
def days_of_date(date):
    """
    Calculate the total number of days from the beginning of the year to a given date.

    Parameters:
    - date (tuple): A tuple representing the date in the format (year, month, day).

    Returns:
    int: The total number of days from the beginning of the year to the specified date.
    """
    days = 0
    days_normal = [31 , 28 , 31 , 30 , 31 , 30 , 31 ,31 ,30 ,31 , 30 ,31]
    days_leap = [31 , 29 , 31 , 30 , 31 , 30 , 31 ,31 ,30 ,31 , 30 ,31]

    # Check if the year is a leap year
    if isleap(date[0]) == True:
        # Calculate days for each month in a leap year
        for i in range(0,date[1]-1):
            days += days_leap[i]
    else:
        # Calculate days for each month in a non-leap year
        for i in range(0,date[1]-1):
            days += days_normal[i]
    # Add the day of the specified date
    days += date[2]
    return days 

def days_between_dates( date1: str, date2: str) -> int:
    """
    Calculate the number of days between two given dates.

    Parameters:
    - date1 (str): The first date in the format 'YYYY-MM-DD'.
    - date2 (str): The second date in the format 'YYYY-MM-DD'.

    Returns:
    int: The absolute number of days between the two dates.
    """
    # Convert the date strings to datetime objects
    a = datetime.datetime.strptime(date1, '%Y-%m-%d')
    b = datetime.datetime.strptime(date2, '%Y-%m-%d')

    # Calculate the absolute difference in days between the two dates
    result = abs((a - b).days)
   
    return result 

def solar_to_lunar(birth):
    """
    Convert a solar date to a lunar date.

    Parameters:
    - birth (list): A list representing a solar date in the format [year, month, day, hour].

    Returns:
    list: A list representing the corresponding lunar date in the format [year, month, day, hour].
    """
    # Extract the hour from the input
    hour = birth[3]
    # Create a Solar object using the provided year, month, and day
    solar_date = Solar(birth[0], birth[1], birth[2])
    # Convert the Solar date to Lunar using the provided Converter
    lunar_date = Converter.Solar2Lunar(solar_date)
    # Update the birth list with the Lunar date and hour
    birth = [lunar_date.year , lunar_date.month , lunar_date.day,hour]

    return birth

def gene_year_column(birth):
    """
    Generate the Tiangan and Dizhi for the year column based on the given birth year.

    Parameters:
    - birth (list): A list representing a birth date in the format [year, month, day, hour].

    Returns:
    list: A list containing the Tiangan and Dizhi for the year column.
    """
    # Define lists for Tiangan and Dizhi
    tiangan_1 = ['庚','辛','壬','癸','甲','乙','丙','丁','戊','己']
    dizhi_1 = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
    # Initialize counters
    a,b = 0,0
    # Extract the birth year from the input
    year = birth[0]
    # Normalize the year to a 60-year cycle starting from 1900
    year -= 1900
    year %= 60
    # Calculate Tiangan and Dizhi for the given year
    for _ in range(year):
        a += 1
        b += 1
    year_gx = a % 10
    year_zx = b % 12
    year_gan = tiangan_1[year_gx]
    year_zhi = dizhi_1[year_zx]
    # Return a list containing the Tiangan and Dizhi for the year column
    return [year_gan ,year_zhi]


def gene_month_column(birth):
    """
    Generate the Tiangan and Dizhi for the month column based on the given birth month.

    Parameters:
    - birth (list): A list representing a birth date in the format [year, month, day, hour].

    Returns:
    list: A list containing the Tiangan and Dizhi for the month column.
    """
    # Define lists for Tiangan and Dizhi
    tiangan_2 = ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
    dizhi_2 = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
    # Extract the last digit of the birth year
    year_end = str(birth[0])
    year_end = int(year_end[-1])
    # Calculate Tiangan and Dizhi for the month
    month_gx = (year_end + 2) * 2 + birth[1]
    month_gx = month_gx % 10 - 1 
    
    month_zx = (birth[1] + 2) % 12 - 1 
    
    # Return a list containing the Tiangan and Dizhi for the month column
    return [tiangan_2[month_gx] , dizhi_2 [month_zx]]




def gene_day_column(birth):
    """
    Generate the Tiangan and Dizhi for the day column based on the given birth date.

    Parameters:
    - birth (list): A list representing a birth date in the format [year, month, day, hour].

    Returns:
    list: A list containing the Tiangan and Dizhi for the day column.
    """
    # Define the Ganzhi table for the day
    day_ganzhi_table = ['甲子', '乙丑', '丙寅', '丁卯', '戊辰', '己巳', '庚午', '辛未', '壬申', '癸酉',
                        '甲戌', '乙亥', '丙子', '丁丑', '戊寅', '己卯', '庚辰', '辛巳', '壬午', '癸未',
                        '甲申', '乙酉', '丙戌', '丁亥', '戊子', '己丑', '庚寅', '辛卯', '壬辰', '癸巳',
                        '甲午', '乙未', '丙申', '丁酉', '戊戌', '己亥', '庚子', '辛丑', '壬寅', '癸卯',
                        '甲辰', '乙巳', '丙午', '丁未', '戊申', '己酉', '庚戌', '辛亥', '壬子', '癸丑',
                        '甲寅', '乙卯', '丙辰', '丁巳', '戊午', '己未', '庚申', '辛酉', '壬戌', '癸亥']

    # Extract year, month, and day from the birth date
    y = birth[0]
    m = birth[1]
    d = birth[2]

    # Calculate the difference in days between the birth date and a reference date
    date_now = str(y) + '-' + str(m) + '-' + str(d)
    diff = days_between_dates(date_now, "1943-12-6")

    # Calculate the index in the Ganzhi table for the day
    day_index = diff % 60
    day_column = day_ganzhi_table[day_index]

    # Return a list containing the Tiangan and Dizhi for the day column
    return [day_column[0], day_column[1]]

def gene_hour_column(birth):
    """
    Generate the Tiangan and Dizhi for the hour column based on the given birth hour.

    Parameters:
    - birth (list): A list representing a birth date and hour in the format [year, month, day, hour].

    Returns:
    list: A list containing the Tiangan and Dizhi for the hour column.
    """
    tiangan_4=['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
    dizhi_4=["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
  
    h = birth[3]
    if h % 2 == 0:
        hour_zx = h / 2
        hour_zx = int(hour_zx)
    else:
       hour_zx = (h + 1) / 2
       hour_zx =int(hour_zx)
       
    day_column = gene_day_column(birth)
    day_gx = tiangan_4.index(day_column[0]) 
    hour_gx = int(day_gx * 2 + (hour_zx + 1))
    
    if hour_gx > 10:
        hour_gx -= 10
        
    return [tiangan_4[(hour_gx - 1) % len(tiangan_4)] , dizhi_4[hour_zx]]

def combine_natal_chart(birth):
    """
    Combine the Tiangan and Dizhi columns for the year, month, day, and hour of a given birth.

    Parameters:
    - birth (list): A list representing a birth date and hour in the format [year, month, day, hour].

    Returns:
    list: A list containing lists representing the Tiangan and Dizhi columns for the year, month, day, and hour.
    """
    birth = solar_to_lunar(birth)
    result = []
    result.append(gene_year_column(birth))
    result.append(gene_month_column(birth))
    result.append(gene_day_column(birth))
    result.append(gene_hour_column(birth))
    return result 


def plot_natal_chart(birth):
    """
    Plot the Chinese Natal Chart using Matplotlib.

    Parameters:
    - birth (list): A list representing a birth date and hour in the format [year, month, day, hour].

    Returns:
    None
    """
    # Generate Tiangan and Dizhi columns for the year, month, day, and hour
    year_column = gene_year_column(birth)
    month_column = gene_month_column(birth)
    day_column = gene_day_column(birth)
    hour_column = gene_hour_column(birth)
    
    # Define columns and corresponding Tiangan and Dizhi values
    columns = ['Year Pillar', 'Month Pillar', 'Day Pillar', 'Hour  Pillar']
    tiangan_values = [year_column[0], month_column[0], day_column[0], hour_column[0]]
    dizhi_values = [year_column[1], month_column[1], day_column[1], hour_column[1]]
    
    # Define font properties
    fig, ax = plt.subplots(figsize=(10, 6))

    # Set the font path for displaying Chinese characters
    font_path = os.path.abspath("/home/ziz103/Final-Project/fonts/NotoSansTC-Black.ttf")  
    
    # Define font properties
    font_properties = FontProperties(fname = font_path , size = 20)
    # Iterate over Tiangan and Dizhi values and plot them on the axis
    for i, (tiangan, dizhi) in enumerate(zip(tiangan_values, dizhi_values)):
        ax.text(0.5, i * 0.8 , f'{tiangan}{dizhi}', ha ='center', va ='center', fontproperties = font_properties)
    
    # Set axis title and labels
    ax.set_title('Chinese Natal Chart')
    ax.set_xlabel('Celestial Stems and Earthly Branches')

    # Set y-axis ticks and labels
    ax.set_yticks(range(len(columns)))
    ax.set_yticklabels(columns, fontproperties = font_properties)
    
    # Display the plot
    plt.show()
