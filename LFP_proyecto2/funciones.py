from socket import TCP_KEEPINTVL
from tkinter import  filedialog as FileDialog, messagebox
from tkinter import  ttk
from tkinter.ttk import Progressbar, Treeview
from tkinter import *
import os



from lexico import  analizadorl
from sintactico import analizadorS
from traduccion1 import transformar


class Funcion:
    def __init__(self):
        self.ruta=""
        self.nombre=""
        self.tokenlist=[]
        

    def nuevo(self,contenido):
        res=messagebox.askyesnocancel('Pregunta','¿Desea guardar el archivo?')
        if res==True:
            self.tokenlist=[]
            if self.ruta=="":
                self.salve_c(str(contenido),0)
            elif self.ruta!="":
                self.salve(str(contenido), 0)
            self.ruta=""
            self.nombre=""
        if res==False:
            self.tokenlist=[]
            self.ruta=""
            self.nombre=""

        return res
    
    def viewer(self):
        self.ruta = FileDialog.askopenfilename(initialdir='.',filetypes=( ("Ficheros de texto", "*.gpw"),),  title="Abrir un fichero.")
        # Si la ruta es válida abrimos el contenido en lectura
        contenido1=""
        cade=""
        if self.ruta != "":  
            self.tokenlist=[]
            nameent=os.path.split(self.ruta)
            nom=nameent[1].split(".")
            self.nombre=nom[0]
            archivo  = open(self.ruta, 'r',encoding= "utf-8")
            contenido =  archivo.read()
            archivo.close()
            listal=contenido.split("\n")
            for linea in listal:
                if linea!="":
                    if cade!="":
                        cade+="\n"
                    contesp=0
                    linesp=linea.split(" ")
                    for line in linesp:
                        if contesp==0:
                            if line!="":
                               cade+=line
                               contesp+=1
                        else:
                            if contesp==1:

                                cade+=" "+line

                    
                    contenido1+=linea+"\n"
            
            return cade
        else:
            return "ninguno"
   
    def salve(self, contenido, op):
        if self.ruta != "":
            archivo  = open(self.ruta, 'w+',encoding= "utf-8")
            archivo.write(contenido)
            archivo.close()
            if op==0:
                messagebox.showinfo(message="Se guardaron los cambios correctamente",title="Guardar")
        else:
            self.salve_c(contenido, op)  

    def salve_c(self,contenido,op):
        archivo = None
        archivo = FileDialog.asksaveasfile(title="Guardar como", mode="w", defaultextension=".gpw")

        if  archivo  is not None:
            self.ruta =  archivo.name
            nameent=os.path.split(self.ruta)
            nom=nameent[1].split(".")
            self.nombre=nom[0]
            archivo  = open(self.ruta, 'w+',encoding= "utf-8")
            archivo.write(contenido)
            archivo.close()
            if op==0:
                messagebox.showinfo(message="El archivo se guardo correctamente",title="Guardar como")
        else:
            self.ruta = ""   
            self.nombre=""

    def run(self,tv):
        #print("ruta",self.ruta)
        self.tokenlist=[]
        a=analizadorl()
        resp=a.compilador(self.ruta)
        if resp["error"]==None:
            self.tokenlist=resp["3"]
            b=analizadorS()
            resp1=b.compilador1(self.ruta,resp)
            if resp1["error"]==None:
                c=transformar()
                c.imprimir(resp1,self.nombre)
            else:
                #for registro in tv.get_children():
                 #   tv.delete(registro)
                tv.insert("",END,text=f'{resp1["error"]}',values=(f'{resp1["linea"]}',f'{resp1["columna"]}',f'{resp1["token"]}',f'{resp1["descrip"]}'))
        else:
            #for registro in tv.get_children():
             #       tv.delete(registro)
            tv.insert("",END,text=f'{resp["error"]}',values=(f'{resp["linea"]}',f'{resp["columna"]}',f'{resp["token"]}',f'{resp["descrip"]}'))

    def tokengenerate(self):
        if len(self.tokenlist)==0:
            messagebox.showinfo(message="No se ha compilado correctamente",title="Tokens")
        else:
            ventanat=Tk()
            l1T = Label(ventanat, bg='#413658', text="LISTA DE TOKENS",fg="#45f9cf")
            lst2=('Calibri (Body)',18)
            l1T.config(font=lst2)
            l1T.place(x=180, y=15)
            style_t= ttk.Style(ventanat)
            style_t.configure("Treeview", background="#140b1e", foreground="#45f9cf", fieldbackgrond="#140b1e")
            style_t.map('Treeview',background=[('selected','dark turquoise')])

            #Frame para tabla
            frame1t = Frame(ventanat)
            frame1t.place(x = 20, y = 50)
            frame1t.config(width = "650", height = "140", bg = "#140b1e")
            # tabla 
            tvk = Treeview(frame1t, columns=("col1","col2"),height=15)
            for registro in tvk.get_children():
                tvk.delete(registro)
            tvk.column("#0", width=186,anchor=CENTER )
            tvk.column("col1", width=186,anchor=CENTER)
            tvk.column("col2", width=186,anchor=CENTER)
            tvk.heading("#0",text="Numero correlativo",anchor=CENTER)
            tvk.heading("col1",text="Token",anchor=CENTER)
            tvk.heading("col2",text="Lexema",anchor=CENTER)
            listoken=["Token_barra","Token_asterisco","Token_mayor","Token_menor","Token_signoE","Token_guion","Token_pcoma","Token_punto","Token_pa","Token_pc","Token_coma","Token_comilla","Token_elemento","Token_E_Control","Token_E_Propiedad","Token_E_Colocar","Token_Control","Token_Propiedad","Token_P_valor","Token_parametro","Token_posicion","Token_Id","Token_numero","Token_texto","Token_textoC"]
            for t in self.tokenlist:
                tvk.insert("",END,text=f'{t[0]}',values=(f'{listoken[int(t[1])]}',f'{t[2]}'))

            tvk.pack()

            #Configuracion de ventana
            ventanat.title('Tokens leidos')
            ventanat.config(bg = "#413658") #181e36#413658
            ventanat.geometry('600x400+400+50')
            ventanat .iconbitmap('dmlogo.ico')
            ventanat.mainloop()
    

    """
    # en este fragmento de codigo se utiliza la libreria os para abrirlo con un 
    #lector de pdf en nuestra computadora por medio de cmd
    separador = os.path.sep
    dir_actual = os.path.dirname(os.path.abspath(__file__))
    dir = separador.join(dir_actual.split(separador)[:-1])
    path = f"{dir}/Documentacion/Manual_usuario.pdf"
    os.system(path)
    """                