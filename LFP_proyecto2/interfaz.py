from tkinter import messagebox, ttk
from tkinter.font import ITALIC
from tkinter.ttk import Progressbar, Treeview
from tkinter import *

#libreria propia
from funciones import Funcion

def ventanaprincipal():
    #Creando ventana
    q = Tk()

    #Frame de editor de texto
    frame3 = Frame()#55o  455
    frame3.config(width = "1150", height = "455", bg = "#140b1e")
    frame3.place(x = 20, y = 20)
    # Caja de texto 
    texto = Text(frame3)
    texto.place(x = 0, y = 0)
    texto.config(padx = 6, pady = 2, width="95", height = "19", bg = "#140b1e")
    texto.config( insertbackground = "white", foreground = "#45f9cf", font = ("Consolas", 16))
    
    """
    #scrooll
    frame_scrool=Frame(frame3)
    frame_scrool=pack(fill=BOTH, expand=1)
    my_canvas =Canvas()
    my_canvas.pack(side=LEFT,fill=BOTH, expand=1)
    my_scroollbar=Scrollbar(frame_scrool, orient=VERTICAL, Command=my_canvas.yview)
    my_scroollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scroollbar.set)
    my_canvas.bind('<Configure>',lambda e: my_canvas.configure(Scrollregion =my_canvas.bbox("all")))
    """

    ind=texto.index("insert")
    list=ind.split(".")

    l1 = Label(q, bg='#140b1e', text="fila:",fg="#45f9cf")
    l2 = Label(q, bg='#140b1e', text="columna:",fg="#45f9cf")
    l1.place(x=970, y=480)
    l2.place(x=1060, y=480)
    l3 = Label(q, bg='#140b1e', text=f" {list[0]}",fg="#45f9cf")
    l4 = Label(q, bg='#140b1e', text=f" {list[1]}",fg="#45f9cf")
    l3.config(width=7)
    l4.config(width=7)
    l3.place(x=995, y=480)
    l4.place(x=1114, y=480)
   
    q.bind("<Key>", lambda e:actualizar_index(texto,l3,l4))
    q.bind("<Button-1>", lambda e:actualizar_index(texto,l3,l4))

    style_t= ttk.Style()
    style_t.configure("Treeview", background="#140b1e", foreground="#45f9cf", fieldbackgrond="#140b1e")
    style_t.map('Treeview',background=[('selected','dark turquoise')])

    #Frame para tabla
    frame1 = Frame()
    frame1.place(x = 20, y = 515)
    frame1.config(width = "1150", height = "140", bg = "#140b1e")
     # tabla 
    tv = Treeview(frame1, columns=("col1","col2","col3","col4"),height=6)
    tv.column("#0", width=140,anchor=CENTER )
    tv.column("col1", width=80,anchor=CENTER)
    tv.column("col2", width=80,anchor=CENTER)
    tv.column("col3", width=250,anchor=CENTER)
    tv.column("col4", width=600,anchor=CENTER)
    tv.heading("#0",text="Tipo de Error",anchor=CENTER)
    tv.heading("col1",text="Linea",anchor=CENTER)
    tv.heading("col2",text="Posicion",anchor=CENTER)
    tv.heading("col3",text="Token Esperado",anchor=CENTER)
    tv.heading("col4",text="Descripcion de Error",anchor=CENTER)
    tv.pack()
    
    # BARRA DE MENU
    barra_menus = Menu()
    # MENU DE ARCHIVO
    menu_archivo = Menu(barra_menus, tearoff=False)
    menu_archivo.add_command(
        label="Nuevo",
        accelerator="Ctrl+N",
        command=lambda: nuevo(texto),
        compound=LEFT
    )
    menu_archivo.add_command(
        label="Abrir",
        accelerator="Ctrl+A",
        command=lambda: abrir(texto),
        compound=LEFT
    )
    menu_archivo.add_command(
        label="Guardar",
        accelerator="Ctrl+G",
        command=lambda: guardar(texto),
        compound=LEFT
    )
    menu_archivo.add_command(
        label="Guardar como",
        accelerator="Ctrl+S",
        command=lambda: guardar_como(texto),
        compound=LEFT
    )
    menu_archivo.add_separator()
    menu_archivo.add_command(
        label="Salir",command=lambda:q.destroy()
    )
    q.bind_all("<Control-n>", lambda x:nuevo(texto))
    q.bind_all("<Control-a>", lambda x:abrir(texto))
    q.bind_all("<Control-g>", lambda x:guardar(texto))
    q.bind_all("<Control-s>", lambda x:guardar_como(texto))
    barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
    
     # MENU DE ANALISIS
    menu_analisis= Menu(barra_menus, tearoff=False)
    menu_analisis.add_command(
        label="Generar página web",
        accelerator="Ctrl+W",
        command=lambda: generar(texto,tv),
        compound=LEFT
    )
    q.bind_all("<Control-w>", lambda x:generar(texto))
    barra_menus.add_cascade(menu=menu_analisis, label="Análisis")
    
     # MENU DE TOKEN
    menu_token= Menu(barra_menus, tearoff=False)
    menu_token.add_command(
        label="Ver Tokens",
        accelerator="Ctrl+T",
        command=lambda: g_tokens(),
        compound=LEFT
    )
    q.bind_all("<Control-t>", lambda x:g_tokens())
    barra_menus.add_cascade(menu=menu_token, label="Token")


    
    #Configuracion de ventana
    q.title('Traductor HTML')
    q.config(bg = "#413658") #181e36#413658
    q.geometry('1190x700+80+0')
    q.iconbitmap('dmlogo.ico')
    q.config(menu=barra_menus)
    q.mainloop()


def actualizar_index(texto,l3,l4):
    ind=texto.index("insert")
    list=ind.split(".")
    l3.configure(text=f" {list[0]}")
    l4.configure(text=f" {list[1]}")
    list.pop()
    list.pop()

def nuevo(texto):
    res=True
    contenido=""
    contenido = texto.get(1.0,'end-1c')
    if contenido!="":
        res=fm.nuevo(contenido)
    if res!=None:
        texto.delete(1.0, 'end')          

def abrir(texto):
    contenido=fm.viewer()
    if contenido!="ninguno":
        texto.delete(1.0, 'end')           # Nos aseguramos de que esté vacío
        texto.insert('insert', contenido)  

def guardar(texto):
    contenido = texto.get(1.0,'end-1c')
    fm.salve(contenido,0) 

def guardar_como(texto):
    contenido = texto.get(1.0,'end-1c')
    fm.salve_c(contenido,0)

def generar(texto,tvg):
    print("Generando")
    contenido = texto.get(1.0,'end-1c')
    op=fm.salve(contenido,1)
    fm.run(tvg)
    

def g_tokens():
    print("generar tokens")
    fm.tokengenerate()



if __name__ == "__main__":
    fm=Funcion()
    #ventanaprincipal()
    
    w = Tk()
    width_of_window = 427
    height_of_window = 250
    screen_width = w.winfo_screenwidth()
    screen_height = w.winfo_screenheight()
    x_coordinate = (screen_width/2)-(width_of_window/2)
    y_coordinate = (screen_height/2)-(height_of_window/2)
    w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

    w.overrideredirect(1)

    s = ttk.Style()
    s.theme_use('clam')
    s.configure("red.Horizontal.TProgressbar", foreground='red', background='#249794')
    progress=Progressbar(w,style = "red.Horizontal.TProgressbar",orient = HORIZONTAL)
    progress.config(length = 500,mode='determinate')

   #PANTALLA FLOTANTE PARA INICIO DE PROGRAMA
    def bar():
        l4=Label(w,text='Espere...',fg='white',bg=a)
        lst4=('Calibri (Body)',10)
        l4.config(font=lst4)
        l4.place(x=18,y=210)
        
        import time
        r = 0
        for i in range(100):
            progress['value'] = r
            w.update_idletasks()
            time.sleep(0.03)
            r = r+1
        
        w.destroy()
        ventanaprincipal()
               
    progress.place(x = -10,y = 235)

    # frame 
    a='#140b1e'#249794=celeste
    Frame(w,width=427,height=241,bg=a).place(x=0,y=0)  
    b1=Button(w,width=10,height=1,text='Comenzar',command=bar)
    b1.config(border="0", fg = "white", bg ="#249794")
    b1.place(x=170,y=200)

    ######## Label
    l1=Label(w,text='TRADUCTOR',fg='#45f9cf',bg=a)
    lst1=('Calibri (Body)',18,'bold')
    l1.config(font=lst1)
    l1.place(x=50,y=80)

    l2=Label(w,text='HTML',fg='#45f9cf',bg=a)
    lst2=('Calibri (Body)',18)
    l2.config(font=lst2)
    l2.place(x=210,y=82)

    l3=Label(w,text='PROYECTO 2',fg='#45f9cf',bg=a)
    lst3=('Calibri (Body)',13)
    l3.config(font=lst3)
    l3.place(x=50,y=110)

    w.mainloop()
    
#def info():
  #  messagebox.showinfo(message= f"Informacion del desarollador:\nDamaris Julizza Muralles Veliz\nCarnet: 202100953\nCurso: LFP\nSeccion: B-",title="Temas de ayuda")
    