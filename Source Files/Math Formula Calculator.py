import math
import mformulae

def initial_menu():
    print()
    print("Welcome!")
    print("Pick a Category")
    print("a: Unit Conversions")
    print("b: Surface Area")
    print("c: Volume")
    print("d: Trigonometry")
    print("e: Other")
    print("q: Quit")
    print()

def top_menu():
    print()
    print("a: Unit Conversions")
    print("b: Surface Area")
    print("c: Volume")
    print("d: Trigonometry")
    print("e: Other")
    print("q: Quit")
    print()

def conv_menu():
    print()
    print("What would you like to convert?")
    print("a: Metres -> Yards")
    print("b: Yards -> Metres")
    print("c: Centimetres -> Inches")
    print("d: Inches -> Centimetres")
    print("e: Kilometres -> Miles")
    print("f: Miles -> Kilometres")
    print("g: Back")
    print()

def sa_menu():
    print()
    print("a: Sphere")
    print("b: Cone")
    print("c: Cylinder")
    print("d: Rectangular Prism")
    print("e: Triangular Prism ")
    print("f: Square Pyramid")
    print("g: Triangular Pyramid")
    print("h: back")
    print()

def vol_menu():
    print()
    print("a: Sphere")
    print("b: Cone")
    print("c: Cylinder")
    print("d: Rectangular Prism")
    print("e: Triangular Prism ")
    print("f: Square Pyramid")
    print("g: Triangular Pyramid")
    print("h: back")
    print()

def trig_menu():
    print()
    print("a: Tangent (Degrees)")
    print("b: Sine (Degrees)")
    print("c: Cosine (Degrees)")
    print("d: Tangent (Radians)")
    print("e: Sine (Radians)")
    print("f: Cosine (Radians)")
    print("g: Find Angle with Tangent")
    print("h: Find Angle with Sine")
    print("i: Find angle with Cosine")
    print("j: Back")
    print()
    
def other_menu():
    print()
    print("a: Mass to Energy")
    print("b: Density")
    print("c: Pressure")
    print("d: Find Watts")
    print("e: Find Amps")
    print("f: Find Volts")
    print("g: Back")
    print()

option = "x"
initial_menu()
while option != "q":
    option = input("Choice: ")
    if option == "a":
        option = "x"
        conv_menu()
        while option != "q":
            option = input("Choice: ")
            if option == "a":
                m = float(input("Metres: "))
                print("Yards:", mformulae.m2yd(m))
            elif option == "b":
                yd = float(input("Yards: "))
                print("Metres:", mformulae.yd2m(yd))
            elif option == "c":
                cm = float(input("Centimetres: "))
                print("Inches:", mformulae.cm2in(cm))
            elif option == "d":
                inch = float(input("Inches: "))
                print("Centimetres:", mformulae.in2cm(inch))
            elif option == "e":
                km = float(input("Kilometres: "))
                print("Miles:", mformulae.km2mi(km))
            elif option == "f":
                mi = float(input("Miles: "))
                print("Kilometres:", mformulae.mi2km(mi))
            elif option == "g":
                top_menu()
                break
    if option == "b":
        option = "x"
        sa_menu()
        while option != "h":
            option = input("Choice: ")
            if option == "a":
                rad = float(input("Radius: "))
                unit = input("Unit: ")
                print(mformulae.areasphere(rad), unit, "^2")
            elif option == "b":
                rad = float(input("Radius: "))
                slant = float(input("Slant: "))
                unit = input("Unit: ")
                print(mformulae.areacone(rad, slant), unit, "^2")
            elif option == "c":
                rad = float(input("Radius: "))
                hght = float(input("Height: "))
                unit = input("Unit: ")
                print(mformulae.areacyl(rad, hght), unit, "^2")
            elif option == "d":
                l = float(input("Length: "))
                w = float(input("Width: "))
                h = float(input("Height: "))
                unit = input("Unit: ")
                print(mformulae.arearecprism(l, w, h), unit, "^2")
            elif option == "e":
                b = float(input("Base: "))
                h = float(input("Height: "))
                s = float(input("Slant: "))
                l = float(input("Length: "))
                unit = input("Unit: ")
                print(mformulae.areatriprism, unit, "^2")
            elif option == "f":
                slant = float(input("Slant: "))
                sl = float(input("Side Length: "))
                unit = input("Unit: ")
                print(mformulae.areasqrpyramid(slant, sl), unit, "^2")
            elif option == "g":
                sl = float(input("Side Length: "))
                slant = float(input("Slant: "))
                bth = float(input("Height of base Triangle: "))
                unit = input("Unit: ")
                print(mformulae.areatripyramid(sl, slant, bth), unit, "^2")
            elif option == "h":
                top_menu()
                break
    if option == "c":
        option = "x"
        vol_menu()
        while option != "h":
            option = input("Choice: ")
            if option == "a":
                rad = float(input("Radius: "))
                unit = input("Unit: ")
                print(mformulae.volsphere(rad), unit, "^3")
            elif option == "b":
                rad = float(input("Radius: "))
                hght = float(input("Height: "))
                unit = input("Unit: ")
                print(mformulae.volcone(rad, hght), unit, "^3")
            elif option == "c":
                rad = float(input("Radius: "))
                hght = float(input("Height: "))
                unit = input("Unit: ")
                print(mformulae.volcyl(rad, hght), unit, "^3")
            elif option == "d":
                l = float(input("Length: "))
                w = float(input("Width: "))
                h = float(input("Height: "))
                unit = print("Unit: ")
                print(mformulae.volrecprism(l, w, h), unit, "^3")
            elif option == "e":
                b = float(input("Base :"))
                h = float(input("Height: "))
                l = float(input("Length: "))
                unit = input("Unit: ")
                print(mformulae.voltriprism(b, h, l), unit, "^3")
            elif option == "f":
                hght = float(input("Height: "))
                sl = float(input("Side Length: "))
                unit = input("Unit: ")
                print(mformulae.volsqrpyramid(hght, sl), unit, "^3")
            elif option == "g":
                hght = float(input("Height: "))
                sl = float(input("Side Length: "))
                bth = float(input("Height of Base Triangle: "))
                unit = input("Unit: ")
                print(mformulae.voltripyramid(hght, sl, bth), unit, "^3")
            elif option == "h":
                top_menu()
                break
    if option == "d":
        option = "x"
        trig_menu()
        while option != "j":
            option = input("Choice: ")
            if option == "a":
                n = float(input("Degrees: "))
                print(mformulae.tangent_deg(n))
            elif option == "b":
                n = float(input("Degrees: "))
                print(mformulae.sine_deg(n))
            elif option == "c":
                n = float(input("Degrees: "))
                print(mformulae.cosine_deg(n))
            elif option == "d":
                n = float(input("Radians: "))
                print(mformulae.tangent_rad(n))
            elif option == "e":
                n = float(input("Radians: "))
                print(mformulae.sine_rad(n))
            elif option == "f":
                n = float(input("Radians: "))
                print(mformulae.cosine_rad(n))
            elif option == "g":
                opp = float(input("Opposite: "))
                adj = float(input("Adjacent: "))
                print(mformulae.findangletan(opp, adj), "°")
            elif option == "h":
                opp = float(input("Opposite: "))
                hyp = float(input("Hypotenuse: "))
                print(mformulae.findanglesin(opp, hyp,), "°")
            elif option == "i":
                adj = float(input("Adjacent: "))
                hyp = float(input("Hypotenuse: "))
                print(mformulae.findanglecos(adj, hyp), "°")
            elif option == "j":
                top_menu()
                break
    if option == "e":
        option = "x"
        other_menu()
        while option != "g":
            option = input("Choice: ")
            if option == "a":
                mass = float(input("Mass: "))
                velocity = float(input("Velocity: "))
                print(mformulae.masstoenergy(mass, velocity), "joules")
            elif option == "b":
                mass = float(input("Mass: "))
                vol = float(input("Volume: "))
                unitm = input("Mass Unit: ")
                unitv = input("Volume Unit: ")
                print(mformulae.density(mass, vol), unitm , "/", unitv)
            elif option == "c":
                force = float(input("Force: "))
                area = float(input("Area: "))
                unitf = input("Force Unit: ")
                unita = input("Area Unit: ")
                print(mformulae.pressure(force, area), unitf , "/", unita)
            elif option == "d":
                amps = float(input("Amps: "))
                volts = float(input("Volts: "))
                print(mformulae.getwatts(amps, volts), "Watts")
            elif option == "e":
                watts = float(input("Watts: "))
                volts = float(input("Volts: "))
                print(mformulae.getamps(watts, volts), "Amps")
            elif option == "f":
                watts = float(input("Watts: "))
                amps = float(input("Amps: "))
                print(mformulae.getvolts(watts, amps), "Volts")
            elif option == "g":
                top_menu()
                break
    if option == "q":
        print(" ",end="")
        
                          
                
                      
                      
                
