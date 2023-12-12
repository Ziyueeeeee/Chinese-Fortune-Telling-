import my_module.Analyze_Element as ae 
import my_module.Analyze_Fate as af 
import my_module.Analyze_Zodiac as az
import my_module.Get_Lunar_Feast as lf
import my_module.Get_Natal_Chart as gnc
import my_module.Tools_for_Main as tfm


def main():
    print("\n------------- Fortune Teller Opened -------------\n")
    
    try:
        Input = tfm.input_birth()
        birthday = Input[0]
        sex = Input[1]
        pillar = gnc.combine_natal_chart(birthday)
    except:
        print("Error Occurs. Relaunch me!")
        return None 
   
    while True:
        user_input_1 = input(
                            "\n\nPlease enter an option and press enter:\n" +
                            "\t(1) See my Chinese Animal Zodiac\n" +
                            "\t(2) See my Element Analysis in my Natal Chart\n" +
                            "\t(3) See my Fate\n" +
                            "\t(4) Want to see the picture of my pillar\n"
                            "\t(5) Exit the Fortune Teller\n" +
                            "-------> "
                            )
    
    
        if user_input_1 == '1':
            print("\n------------- Fortune Teller : Zodiac -------------\n")
            user_zodiac = az.ZodiacAna(pillar)
            user_zodiac.update_zodiac()
            user_zodiac.obtain_zodiac_comment()
            
            print (f"Dear user, your Animal Zodiac is {user_zodiac.zodiac}\n\n")
            print ("Here is the Corresponding Description for your Zodiac:\n\n")
            print(user_zodiac.zodiac_comment)
            pass
            
            
        elif user_input_1 == '2':
            print("\n------------- Fortune Teller : Element Analysis -------------\n")
            user_element = ae.ElementAna(pillar)
            
            user_element.obtain_element().find_life_determinant().get_determinant_general_comment()
           
            user_element.find_interactions()
            
            user_element.load_element_general_comment().load_element_deficit_comment()
           
            while True:
                user_input_2 = input(
                            "\n\nPlease enter an option and press enter:\n" +
                            "\t(1) See my Life Determinant\n" +
                            "\t(2) See my how other elements influence life determinant\n "
                            "\t(3) See my Element Distribution \n" +
                            "\t(4) Exit the Element Analysis" +
                            "-------> "
                            )
                if user_input_2 == "1":
                    print("\n------------- Fortune Teller : Life Determinant-------------\n")
                    print (f"Dear user, your life determinant is {user_element.life_determinant}\n\n")
                    print (f"Here is the brief comment regarding your life determinant: \n\n")
                    print (user_element.life_determinant_comment_gene)
                    pass 
                  
                elif user_input_2 == "2":
                    print("\n------------- Fortune Teller : Life Determinant-------------\n")
                    print(user_element.ld_interaction_comment)
                    pass
                      
                elif user_input_2 == "3":
                    print("\n------------- Fortune Teller : Element Distribution -------------\n")
                    print("Dear user, here is your element distribution and potential deficits:")
                    print(user_element.element_stat_comment)
                    pass
                      
                elif user_input_2 == "4":
                    print("\nExiting the Element Analysis. Let's go ack!\n")
                    break
                
                else:
                    print("\nInvalid option. Please enter a valid option (1-4).\n")
                    pass
                
            pass
                    
                    
        elif user_input_1 == '3':
            user_fate = af.Fate(birthday,sex) 
            user_fate.get_combined_cycle()
            user_fate.gene_ten_gods().gene_fate_comment()
            
            while True:
                user_input_3 = input(
                            "\n\nPlease enter an option and press enter:\n" +
                            "\t(1) See my ages of inflection and corresponding pillar\n" +
                            "\t(2) See the prediction according to my ten_gods \n" +
                            "\t(3) Exit the Fate Analysis\n" +
                            "-------> "
                            )
                if user_input_3 == "1":
                    print("\n------------- Fate:Age of Inflection -------------\n")
                    print("Dear user, your ages of inflection is")
                    print(user_fate.age)
                    print("/n Pay attention to these ages, since they signal a great change in your life in every ten years.\n")
                    pass
                    
                elif user_input_3 == "2":
                    print("\n------------- Fate:Prediction per Ten Years-------------\n")
                    print("Dear user, here is the prediction per ten years:\n")
                    print(user_fate.fate_comment)
                    pass
                
                elif user_input_3 == "3":
                    print("\nExiting the Fate Analysis. Let's go ack!\n")
                    break
                
                else:
                    print("\nInvalid option. Please enter a valid option (1-3).\n")
                    pass
                
            pass
                
        elif user_input_1 == '4':
            print("\n------------- Fortune Teller : Plot Natal Chart -------------\n")
            gnc.plot_natal_chart(birthday)
            pass
            
        elif user_input_1 == '5':
            print("\nExiting the Fortune Teller. Goodbye!\n")
            break

        else:
            print("\nInvalid option. Please enter a valid option (1-4).\n")
            pass
        
    return None

main()