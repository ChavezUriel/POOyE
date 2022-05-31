from tkinter import *
import tkinter.font as font

class calculadora:
    def __init__(self, win):
        
        # COLORES DE BOTONES Y COLOR DE LETRAS
        color_nums = "#595959"
        color_fuente = "#e8e8e8"
        color_ops = "#4d4d4d"
        
        # VALORES INICIALES
        # ÚLTIMA RESPUESTA
        self.last_ans = ""
        # VARIABLES MEMORIA X, Y
        self.xmem = ""
        self.ymem = ""
        # SE PUEDE GUARDAR EN X, Y
        self.savable = False
        
        # DISPLAY
        self.display = Label(win, text="", bg="black", fg="white", font=myFont, height=2, width=1, anchor="e")
        self.display.grid(column=0, row=0, columnspan=4, sticky="we")

        # BOTONES DE NÚMEROS
        self.b0 = Button(win, text='0', width=3, bg=color_nums, fg=color_fuente, font=myFont, command = lambda: self.addDisplay("0"))
        self.b1 = Button(win, text='1', width=3, bg=color_nums, fg=color_fuente, font=myFont, command = lambda: self.addDisplay("1"))
        self.b2 = Button(win, text='2', width=3, bg=color_nums, fg=color_fuente, font=myFont, command = lambda: self.addDisplay("2"))
        self.b3 = Button(win, text='3', width=3, bg=color_nums, fg=color_fuente, font=myFont, command = lambda: self.addDisplay("3"))
        self.b4 = Button(win, text='4', width=3, bg=color_nums, fg=color_fuente, font=myFont, command = lambda: self.addDisplay("4"))
        self.b5 = Button(win, text='5', width=3, bg=color_nums, fg=color_fuente, font=myFont, command = lambda: self.addDisplay("5"))
        self.b6 = Button(win, text='6', width=3, bg=color_nums, fg=color_fuente, font=myFont, command = lambda: self.addDisplay("6"))
        self.b7 = Button(win, text='7', width=3, bg=color_nums, fg=color_fuente, font=myFont, command = lambda: self.addDisplay("7"))
        self.b8 = Button(win, text='8', width=3, bg=color_nums, fg=color_fuente, font=myFont, command = lambda: self.addDisplay("8"))
        self.b9 = Button(win, text='9', width=3, bg=color_nums, fg=color_fuente, font=myFont, command = lambda: self.addDisplay("9"))
        
        self.b0.grid(column=0, row=6)
        self.b1.grid(column=0, row=5)
        self.b2.grid(column=1, row=5)
        self.b3.grid(column=2, row=5)
        self.b4.grid(column=0, row=4)
        self.b5.grid(column=1, row=4)
        self.b6.grid(column=2, row=4)
        self.b7.grid(column=0, row=3)
        self.b8.grid(column=1, row=3)
        self.b9.grid(column=2, row=3)

        #BOTONES DE OPERADORES
        self.bdiv = Button(win, text='÷', width=3, bg=color_ops, fg=color_fuente, font=myFont, command = lambda: self.addDisplay(" ÷ "))
        self.bpor = Button(win, text='×', width=3, bg=color_ops, fg=color_fuente, font=myFont, command = lambda: self.addDisplay(" × "))
        self.bmas = Button(win, text='-', width=3, bg=color_ops, fg=color_fuente, font=myFont, command = lambda: self.addDisplay(" - "))
        self.bmenos = Button(win, text='+', width=3, bg=color_ops, fg=color_fuente, font=myFont, command = lambda: self.addDisplay(" + "))
        self.bpunto = Button(win, text='.', width=3, bg=color_ops, fg=color_fuente, font=myFont, command = lambda: self.addDisplay("."))
        self.bpot = Button(win, text='^', width=3, bg=color_ops, fg=color_fuente, font=myFont, command = lambda: self.addDisplay(" ^ "))
        self.bpari = Button(win, text='(', width=3, bg=color_ops, fg=color_fuente, font=myFont, command = lambda: self.addDisplay("("))
        self.bpard = Button(win, text=')', width=3, bg=color_ops, fg=color_fuente, font=myFont, command = lambda: self.addDisplay(")"))
        
        self.bdiv.grid(column=3, row=2)
        self.bpor.grid(column=3, row=3)
        self.bmas.grid(column=3, row=4)
        self.bmenos.grid(column=3, row=5)
        self.bpunto.grid(column=1, row=6)
        self.bpot.grid(column=2, row=2)
        self.bpari.grid(column=0, row=2)
        self.bpard.grid(column=1, row=2)
        
        # OTROS BOTONES
        self.bxmem = Button(win, text='x', width=3, bg=color_ops, fg=color_fuente, font=myFont, command = self.use_xmem)
        self.bymem = Button(win, text='y', width=3, bg=color_ops, fg=color_fuente, font=myFont, command = self.use_ymem)
        self.bborrar = Button(win, text='⌫', width=3, bg=color_ops, fg=color_fuente, font=myFont, command = self.backspace)
        self.bans = Button(win, text='ANS', width=3, bg=color_ops, fg=color_fuente, font=(myFont,12), command = lambda: self.addDisplay(self.last_ans))
        self.bdel = Button(win, text='C', width=3, bg=color_ops, fg=color_fuente, font=myFont, command = self.deleteDisplay)
        
        self.bxmem.grid(column=0, row=1)
        self.bymem.grid(column=1, row=1)
        self.bborrar.grid(column=3, row=1)
        self.bans.grid(column=2, row=6, sticky = "nswe")
        self.bdel.grid(column=2, row=1)
        
        # BOTON IGUAL
        self.bigual = Button(win, text='=', width=3, bg="#1b2d6e", fg=color_fuente, font=myFont, command = self.resolve)
        self.bigual.grid(column=3, row=6)


    # AGREGAR CARACTERES AL DISPLAY
    def addDisplay(self, character):
        self.display["text"] += character
        self.savable = False

    # BORRAR DISPLAY COMPLETO
    def deleteDisplay(self):
        self.display["text"] = ""
        self.savable = False
    
    # BORRA DISPLAY CARACTER POR CARACTER
    def backspace(self):
        if(self.display["text"][-1:] != " "):
            self.display["text"] = self.display["text"][:-1]
        else:
            self.display["text"] = self.display["text"][:-3]
        self.savable = False
    
    # RESOLUCIÓN DEL STRING EN EL DISPLAY CON JERARQUIA DE OPERACIONES
    def resolve(self, dis_in = ""):
        # SI RECIBE EL ARGUMENTO dis_in LO USA COMO LA STRING A TRATAR, 
        # SI NO, USARÁ EL TEXTO EN EL DISPLAY (ESTO SIRVE PARA USARLA 
        # ESTA FUNCIÓN RECURSIVAMENTE PARA LA RESOLUCIÓN DE PARÉNTESIS)
        if(dis_in == ""):
            dis_str = self.display["text"]
        else:
            dis_str = dis_in
        
        
        if(dis_str[1] == "-" ):
            dis_str = "0" + dis_str
        
        if(dis_str[0] == "-" ):
            dis_str = "0 + " + dis_str

        
        # LA RESOLUCIÓN DE LOS PARÉNTESIS SE HACE ANTES DEL RESTO DE OPERACIONES, 
        # EN ESTA SECCIÓN SE USA ESTA MISMA FUNCIÓN PARA RESOLVER LO QUE ESTÁ 
        # DENTRO DEL PARÉNTESIS 
        
        # RESOLUCIÓN DE PARÉNTESIS
        end_loop = False
        while(not end_loop):
            end_i_loop = False
            for i in range(len(dis_str)):
                if(dis_str[i] == "("):
                    count_pars = 1
                    for j in range(i+1,len(dis_str)):
                        if(dis_str[j] == "("):
                            count_pars += 1
                        elif(dis_str[j] == ")"):
                            count_pars += -1
                        if(count_pars == 0):
                            par_sol = self.resolve(dis_str[i+1:j])
                            if(dis_str[1] == "-" or dis_str[1] == "+"):
                                dis_str = "0" + dis_str
                            dis_str = dis_str[:i] + par_sol + dis_str[j+1:]
                            end_i_loop = True
                            break
                    if(count_pars != 0):
                        end_loop = True
                        end_i_loop = True
                if(end_i_loop):
                    break
            if(not "(" in dis_str):
                end_loop = True
        
        # SEPARAMOS CADA COMPONENTE DE LA OPERACION POR 
        # LOS ESPACIOS QUE HAY ENTRE ELLOS
        dis_sep = dis_str.split(" ")

        # CONVERTIMOS A FLOAT AQUELLOS ELEMENTOS QUE NO SEAN UN OPERADOR
        for i in range(len(dis_sep)):
            if(not dis_sep[i] in "+-×÷^"):
                dis_sep[i] = float(dis_sep[i])
        
        # RESOLUCIÓN DE POTENCIAS
        end_loop = False
        while(not end_loop):    
            for i in range(len(dis_sep)):
                if(dis_sep[i] == "^"):
                    dis_sep[i] = dis_sep[i-1]**dis_sep[i+1]
                    dis_sep.pop(i+1)
                    dis_sep.pop(i-1)
                    break
                if(i == len(dis_sep)-1):
                    end_loop = True
        
        # RESOLUCIÓN DE MULTIPLICACIONES Y DIVISIONES
        end_loop = False
        while(not end_loop):    
            for i in range(len(dis_sep)):
                if(dis_sep[i] == "×"):
                    dis_sep[i] = dis_sep[i-1]*dis_sep[i+1]
                    dis_sep.pop(i+1)
                    dis_sep.pop(i-1)
                    break
                elif(dis_sep[i] == "÷"):
                    dis_sep[i] = dis_sep[i-1]/dis_sep[i+1]
                    dis_sep.pop(i+1)
                    dis_sep.pop(i-1)
                    break
                if(i == len(dis_sep)-1):
                    end_loop = True

        # RESOLUCIÓN DE SUMAS Y RESTAS
        end_loop = False
        while(not end_loop):    
            for i in range(len(dis_sep)):
                if(dis_sep[i] == "+"):
                    dis_sep[i] = dis_sep[i-1]+dis_sep[i+1]
                    dis_sep.pop(i+1)
                    dis_sep.pop(i-1)
                    break
                elif(dis_sep[i] == "-"):
                    dis_sep[i] = dis_sep[i-1]-dis_sep[i+1]
                    dis_sep.pop(i+1)
                    dis_sep.pop(i-1)
                    break
                if(i == len(dis_sep)-1):
                    end_loop = True
        
        solucion = str(round(dis_sep[0],3))
        # SI EL INPUT ORIGINAL DE LA FUNCIÓN NO FUE NINGUNO, GUARDAMOS EN EL DISPLAY,
        # SI NO, LO REGRESAMOS COMO RETURN
        if(dis_in == ""):
            self.display["text"] = solucion
            self.last_ans = solucion
            # SOLO CUANDO SE DA UN RESULTADO EL ESTADO DE "SALVABILIDAD" EN LAS VARIABLES 
            # DE MEMORIA SE ACTIVA
            self.savable = True
        else: 
            return solucion
    
    # FUNCIONES DE USO DE LAS VARIABLES DE MEMORIA X, Y
    # CUANDO EL RESULTADO ES "SALVABLE" (SOLO DESPUÉS DE DAR UN RESULTADO)
    # SE PUEDE GUARDAR EL RESULTADO EN LAS VARIABLES DE MEMORIA X, Y, 
    # DE LO CONTRARIO, EL BOTÓN SERVIRÁ PARA INSERTAR EN EL DISPLAY LO QUE 
    # LA VARIABLE DE MEMORIA TENGA GUARDADO
    def use_xmem(self):
        if(self.savable):
            self.xmem = self.display["text"]
        else:
            self.addDisplay(self.xmem)
    
    def use_ymem(self):
        if(self.savable):
            self.ymem = self.display["text"]
        else:
            self.addDisplay(self.ymem)
        

window = Tk()
window.config(bg="black")
window.resizable(False, False)
myFont = font.Font(family='Helvetica')
window.title('Calculadora')
window.iconbitmap('calculator.ico')
mywin = calculadora(window)
window.mainloop()