
import datetime
current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

import facade_estimate_area
import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.basicConfig(level=logging.DEBUG, filename='data.log',filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

name = input("Please enter Your name:")
logging.info(f"{name} has logged in successfully!")
company_name = input("Please enter Your company name:")
logging.info(f"{name} has entered company:{company_name}")



def get_choice_figure() -> int:
    print("Please choice figure from list: \n1. Rectangle\n2. Trapezoid\n3. Double_trapezoid")
    while True:
        choice_figure= input("Please enter number of figure(1/2/3):")
        if choice_figure in ["1", "2", "3"]:
            return choice_figure
        else:
            print(f"Received invalid figure choice: {choice_figure}")


def get_valid_input(user_enter_something):
    while True:
        user_input = input(user_enter_something)
        try:
            float_input = float(user_input) 
        except ValueError as e:
            print(f'Error: {e}')
            continue
        if float_input > 0:
            return float_input
        else:
            print("Error: Input must be greater than 0")



L = "Please enter lenght, m: "


def iniciate_figure_parameter():    

    if choice_figure == '1':
        lenght = get_valid_input(L)
        height = get_valid_input("Please enter height, m: ")
        rectangle_area = facade_estimate_area.Rectangle(lenght, height).calculate_area_rectangle()
        return rectangle_area

    elif choice_figure == '2':
        lenght = get_valid_input(L)
        height_l = get_valid_input("Please enter height from left, m:")
        height_r = get_valid_input("Please enter height from right, m:")
        trapezoid_area = facade_estimate_area.Trapezoid(lenght, height_l, height_r).calculate_area_trapezoid()
        return trapezoid_area

    elif choice_figure == '3':
        lenght = get_valid_input(L)
        height_l = get_valid_input("Please enter height from left, m:")
        height_mid = get_valid_input("Please enter height to the ridge of the roof, m:")
        height_r = get_valid_input("Please enter height from right, m:")
        double_trapezoid_area = facade_estimate_area.DoubleTrapezoid(lenght, height_l, height_mid, height_r).calculate_area_double_trapezoid()
        return double_trapezoid_area

    else:
        print("Invalid choice!")


def get_valid_quant_input(user_enter_something):
    while True:
        user_input = input(user_enter_something)
        try:
            int_input = int(user_input) 
        except ValueError:
            print("Error: input must be integer")
            continue
        if int_input > 0:
            return int_input
        else:
            print("Error: Input must be greater than 0")


figure_quantity = get_valid_quant_input("Please enter how many figures on one side facade:")

area = 0

figure_num = 1

while figure_num <= figure_quantity:
        
    choice_figure = get_choice_figure()
       
    figure_area = iniciate_figure_parameter()

    area += figure_area 

    figure_num += 1

area = round(area, 2)

print("Estimated area saved to estimated_area.txt file")

# generate answer in output.txt file
with open('estimated_output.txt', 'a') as f:
    print (f" {formatted_time} One side facade esimated area: {area} m2", file=f)




# cia ateityje reikia surasyti langus


# The measurement of the facade must be taken from the drawing. 
# Exmpl.: input "Please enter height from left:" mean that measure must be done from the facade drawing left.



# Pseudokodas(kad pripliusuoti figuras):

# input user kiek figuru bus
## inicijuoti sumos variable (susijes su punktu "susumuoti su esamu")

# loopint per figuru skaiciu:
    # user pasirenka figura
    # user inicijuoja figura su parametrais
    # skaiciuoju plota
    # susumuoti su esamu 
# grazinti suma

