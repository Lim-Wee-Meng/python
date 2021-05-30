
import tkinter as tk
import time

master = tk.Tk()
master.title("NRIC CHECKER")


def clear():
    nric_input.delete(0,tk.END)
    veri_box.delete(0,tk.END)
    

def quit():
    master.destroy()
    raise SystemExit
    rootquit()

def verify():
    encryptedString =""
    veri_box.delete(0,tk.END)
    # nric = input("Enter your NRIC ? ")
    nric = str(nric_input.get())
    if len(nric)!=9:
        encryptedString="Invalid - Format Error"

    elif nric[0].upper() != "S" and  nric[0].upper() != "T" and  nric[0].upper() != "F" and  nric[0].upper() != "G":
        encryptedString ="Invalid - Not Singapore Issued"
    else:
        crunch()
    veri_box.insert(30,encryptedString)    
    

    
def crunch():
    encryptedString =""
    veri_box.delete(0,tk.END)
    nric=""
    M="2765432"
    # If the IC starts with S or T: 0=J, 1=Z, 2=I, 3=H, 4=G, 5=F, 6=E, 7=D, 8=C, 9=B, 10=A
    S="JZIHGFEDCBA"
    T="JZIHGFEDCBA"
    # If the IC starts with F or G: 0=X, 1=W, 2=U, 3=T, 4=R, 5=Q, 6=P, 7=N, 8=M, 9=L, 10=K
    F="XWUTRQPNMLK"
    G="XWUTRQPNMLK"
    dig_sum=0
    
    nric = str(nric_input.get())
    if nric[0].upper() == "S":
        for dig_count in range(0,7,1): # For loop variable in range(start'inclusive',stop'not included',step)
            digit =(int(nric[dig_count+1]))*(int(M[dig_count]))
            dig_sum = dig_sum + digit 
        modulus_11 = dig_sum % 11
        check_dig = S[modulus_11]
        if check_dig == nric[8].upper():
            encryptedString="Valid"
        else:
            encryptedString="Invalid - Checksum Error"
    if nric[0].upper() == "T":
        for dig_count in range(0,7,1): # For loop variable in range(start'inclusive',stop'not included',step)
            digit =(int(nric[dig_count+1]))*(int(M[dig_count]))
            dig_sum = dig_sum + digit 
        dig_sum = dig_sum + 4
        modulus_11 = dig_sum % 11
        check_dig = T[modulus_11]
        if check_dig == nric[8].upper():
            encryptedString="Valid"
        else:
            encryptedString="Invalid - Checksum Error"
    if nric[0].upper() == "F":
        for dig_count in range(0,7,1): # For loop variable in range(start'inclusive',stop'not included',step)
            digit =(int(nric[dig_count+1]))*(int(M[dig_count]))
            dig_sum = dig_sum + digit 
        modulus_11 = dig_sum % 11
        check_dig = F[modulus_11]
        if check_dig == nric[8].upper():
            encryptedString="Valid"
        else:
            encryptedString="Invalid - Checksum Error"
    if nric[0].upper() == "G":
        for dig_count in range(0,7,1): # For loop variable in range(start'inclusive',stop'not included',step)
            digit =(int(nric[dig_count+1]))*(int(M[dig_count]))
            dig_sum = dig_sum + digit 
        dig_sum = dig_sum + 4
        modulus_11 = dig_sum % 11
        check_dig = G[modulus_11]
        if check_dig == nric[8].upper():
            encryptedString="Valid"
        else:
            encryptedString="Invalid - Checksum Error"

    veri_box.insert(30,encryptedString) 
    

tk.Label(master,text="Enter NRIC ?").grid(row=0,column=0,sticky=tk.W, 
                                                            pady=4)

tk.Label(master,text="Result >>").grid(row=2,column=0,sticky=tk.W, 
                                                            pady=4)
tk.Button(master,text="Verify",command=verify).grid(row=1,column=1,sticky=tk.W, 
                                                            pady=4)

tk.Button(master,text="Clear",command=clear).grid(row=1,column=2,sticky=tk.W, 
                                                            pady=4)

tk.Button(master, text='Quit', command=quit).grid(row=3,column=2,sticky=tk.W, 
                                                            pady=4)

tk.Label(master,text="Programmed by Remy Lim 2020").grid(row=4,column=0,columnspan=3,
                                                      sticky=tk.W, 
                                                      pady=4)

nric_input=tk.Entry(master)
veri_box =tk.Entry(master)
nric_input.grid(row=0,column=1,sticky=tk.W,pady=4)
veri_box.grid(row=2,column=1,columnspan=3,sticky=tk.W,pady=4)
master.mainloop()

tk.destroy()
