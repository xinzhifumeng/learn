
def display_targets(networks, security_type):
    print("Select a target: \n")
    
    rows, columns = os.popen('stty size', 'r').read().split()
    for i in range(len(networks)):
        width = len(str(str(i+1)+". "+networks[i]+security_type[i]))+2
        spacer = " "
        
        if (int(columns) >= 100):
            calc = int((int(columns)-int(width))*0.75)
        else:
                calc = int(columns)-int(width)
        
        for index in range(calc):
            spacer += "."
            if index == (calc-1):
                spacer += " "
            
        print(str(i+1)+". "+networks[i]+spacer+security_type[i])


