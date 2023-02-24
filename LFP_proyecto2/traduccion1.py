import webbrowser

class transformar():
    def __init__(self):
        self.leidos=[]
        self.contenedor=[]
        self.leidos12=[]
        self.cadenahtml=""
        self.cadenacss=""
        self.mostrar=[]
        self.listcontrol=[]
        self.agregardo=[]
        self.adds=0

    def imprimir(self,datos,archivoentrada):
        
        print("_______________________________________________________________________")
        #print("listo")
        self.mostrar=datos["1"]
        self.listcontrol=datos["0"]
        self.adds=datos["2"]
        
        self.leers()
        self.Addcontrol()

        
        for m in self.mostrar:
           # print("listo", m)
            for lei in self.leidos:
                if m == lei[0]:
                    self.cadenahtml+=lei[1]
                    self.cadenacss+=lei[2]
                    print("======================================================")
                    print(lei)
        
        print("________________________________________________________________________")   
        self.construircss(self.cadenacss,archivoentrada)
        self.construirhtml(self.cadenahtml,archivoentrada)

    def Addcontrol(self):
        print("")
        print("==========================================================")

        for c1 in self.listcontrol:
            add1=0
            for elem1 in c1:
                if elem1=="add":
                    add1=1
            
            if add1==1:
                self.contenedor.append(c1)
        completo=False    
        while completo==False:
            print("<<<<<<<<<<<<<<<<AÑADIENDO A CONTENEDORES >>>>>>>>>>>>>>>>>>")
            contw=0
            for contenedor1 in self.contenedor:
                print("-------CONTENEDOR------------------",contenedor1[1])
                respuesta1=self.comprobarc(contenedor1)
                if respuesta1=="no":
                    respuesta2=self.comprobarl(contenedor1[1])
                    if respuesta2=="no":
                        self.leer(contenedor1)
                else:
                    print(respuesta1)
                    contres=0
                    for resen1 in respuesta1:
                        print("----->",resen1)
                        respuesta2=self.comprobarl(resen1)
                        print(respuesta2)
                        if respuesta2=="no":
                            contres+=1

                    if contres==0:
                        self.leer(contenedor1)
                    else:
                        contw+=1
            
            #print("contenedores sin leer ",contw)
            if contw==0:
                completo=True


        print("=========================================================")
    
    def comprobarc(self,conten1):
        listelem=[]
        for elem1 in conten1:
            if conten1.index(elem1)!=1:
                for conten2 in self.contenedor:
                    if elem1==conten2[1]:
                        listelem.append(elem1)
                        
        
        if len(listelem)!=0:
            return listelem
        else:
            return "no"
    
    def comprobarl(self,conten1):
        for leido in  self.leidos:
            if leido[0] == conten1:
                return "si"
        
        return "no"

    def leers(self):

        adds=0
        for lis in self.listcontrol:
            for elem in lis:
                if elem=="add":
                    adds+=1
                    break
        
        while adds!=0:
            for lis in self.listcontrol:
                for elem in lis:
                    if elem=="add" and adds>0:
                        self.listcontrol.insert(len( self.listcontrol),lis)
                        self.listcontrol.remove(lis) 
            adds-=1
                
        for c in  self.listcontrol:
            cadenac=""
            cadenah=""
            add=0
            fue_agregado=0
            contener=0
            alto="25"
            ancho="100"
            grupo=""
            marcada=""
            fondo=""
            letra=""
            alineacion="left"
            texto=""
            posicionx=""
            posiciony=""
            cont=0
            contan=0
            contal=0

            for elem in c:
                if elem=="add":
                    add=1
            
            for leido in  self.leidos:
                
                #  print("leidos1",leido)
                if leido[0] == c[1]:
                    
                    fue_agregado=1
            # print("listo1", c,fue_agregado)
            if fue_agregado==0 and add==0:
                for p in c:
                    
                    if cont==0:
                        for propiedades in c:
                            # print("lectura", propiedades)
                            if propiedades=="setAlto":
                                alto=f"{c[c.index(propiedades)+1]}"
                                c[c.index(propiedades)+1]=c[c.index(propiedades)+1]+"A"
                            elif propiedades=="setAncho":
                                ancho=f"{c[c.index(propiedades)+1]}"
                                c[c.index(propiedades)+1]=c[c.index(propiedades)+1]+"B"
                            elif propiedades=="setGrupo":
                                grupo=f"{c[c.index(propiedades)+1]}"
                            elif propiedades=="setMarcada":
                                if c[c.index(propiedades)+1]=="true":
                                    marcada=f"checked=\"checked\""
                            elif propiedades=="setColorFondo":
                                fondo=f"{int(c[c.index(propiedades)+1])}, {int(c[c.index(propiedades)+2])}, {int(c[c.index(propiedades)+3])}"
                                c[c.index(propiedades)+1]=c[c.index(propiedades)+1]+"C"
                                c[c.index(propiedades)+2]=c[c.index(propiedades)+2]+"D"
                                c[c.index(propiedades)+3]=c[c.index(propiedades)+3]+"E"
                            elif propiedades=="setAlineacion":
                                if c[c.index(propiedades)+1]=="Centro":
                                    alineacion="center"
                                elif c[c.index(propiedades)+1]=="Derecho":
                                    alineacion="right"
                            elif propiedades=="setTexto":
                                texto=f"{c[c.index(propiedades)+1]}"
                            elif propiedades=="setColorLetra":
                                letra=f"{int(c[c.index(propiedades)+1])}, {int(c[c.index(propiedades)+2])}, {int(c[c.index(propiedades)+3])}"
                                c[c.index(propiedades)+1]=c[c.index(propiedades)+1]+"F"
                                c[c.index(propiedades)+2]=c[c.index(propiedades)+2]+"G"
                                c[c.index(propiedades)+3]=c[c.index(propiedades)+3]+"H"
                            elif propiedades=="setPosicion":
                                posicionx=f"{c[c.index(propiedades)+1]}"
                                posiciony=f"{c[c.index(propiedades)+2]}"
                                c[c.index(propiedades)+1]=c[c.index(propiedades)+1]+"I"
                                c[c.index(propiedades)+2]=c[c.index(propiedades)+2]+"J"
                            
                            
                                
                        cont+=1
                    if p=="Contenedor":
                        # print("entro")
                        cadenac+="#"+c[1]+"{\n"
                        cadenah+=f"<div id=\"{c[1]}\">\n"#contener mas cosas
                        contener=1
                    elif p=="Etiqueta":
                        contener=2
                        cadenac+="#"+c[1]+"{\n"
                        cadenah+=f"<label id=\"{c[1]}\"> {texto} </label>\n" #contener mas cosas
                    elif p=="Boton":
                        cadenac+="#"+c[1]+"{\n"+f"width: {ancho}px;\nheight: {alto}px;\n"
                        cadenah+=f"<input type=\"submit\" id=\"{c[1]}\" value=\"{texto}\" style=\"text-align: {alineacion}\"/>\n"
                    elif p=="Check":
                        cadenac+="#"+c[1]+"{\n"+f"width: {ancho}px;\nheight: {alto}px;\n"
                        if grupo=="":
                            cadenah+=f"<input type=\"checkbox\" id=\"{c[1]}\" {marcada} />{texto}\n"
                        else:
                            cadenah+=f"<input type=\"checkbox\" name=\"{grupo}\" id=\"{c[1]}\" {marcada} />{texto}\n"
                    elif p=="RadioBoton":
                        cadenac+="#"+c[1]+"{\n"+f"width: {ancho}px;\nheight: {alto}px;\n"
                        if grupo=="":
                            cadenah+=f"<input type=\"radio\"  id=\"{c[1]}\" {marcada} />{texto}\n"
                        else:
                            cadenah+=f"<input type=\"radio\" name=\"{grupo}\" id=\"{c[1]}\" {marcada} />{texto}\n"
                    elif p=="Texto":
                        cadenac+="#"+c[1]+"{\n"+f"width: {ancho}px;\nheight: {alto}px;\n"
                        cadenah+=f"<input type = \"text\" id=\"{c[1]}\" value=\"{texto}\" style=\"text-align:  {alineacion}\" />\n"
                        
                    elif p=="AreaTexto":
                        cadenac+="#"+c[1]+"{\n"+"width: 150px;\nheight: 150px;\n"
                        cadenah+=f"<textarea id=\"{c[1]}\">{texto}</textarea>\n" 
                    elif p=="Clave":
                        cadenac+="#"+c[1]+"{\n"+f"width: {ancho}px;\nheight: {alto}px;\n"
                        cadenah+=f"<input type = \"password\" id=\"{c[1]}\"value=\"{texto}\" style=\"text-align: {alineacion}\"/>\n"
                    
                    
                    elif p=="setAncho":
                        # print("ancho",ancho)
                        contan=1
                        cadenac+=f"width: {ancho}px;\n"
                    elif p=="setAlto":
                        # print("alto",alto)
                        contal=1
                        cadenac+=f"height: {alto}px;\n"
                    elif p=="setColorFondo":
                        # print("fondo",fondo)
                        cadenac+=f"background-color: rgb({fondo});\n"
                    elif p=="setColorLetra":
                        #   print("letra",letra)
                        cadenac+=f"color: rgb({letra});\n"
                    elif p=="setPosicion":
                        # print("posicion", posicionx,posiciony)
                        cadenac+=f"position:absolute;\nleft: {posicionx}px;\ntop: {posiciony}px;\n"
                   
                    elif len(c)-1==c.index(p):
                        if contan==0:
                            if contener==1 or contener==2 :
                                cadenac+=f"width: {ancho}px;\n"
                        if contal==0:
                            if contener==1 or contener==2 :
                                cadenac+=f"height: {alto}px;\n"
                        cadenac+="}\n"
                        if contener==1:
                            cadenah+="</div>\n"
                            contener=0
                        self.leidos.append([c[1],cadenah,cadenac])
        
    def leer(self,control):
        print("")
        print("++++++++++++++++++++++++++++++++")
        print("Agregando control")


        cadenaAdd=""
        cadenaCs1=""
        fue_agregado1=0
        contener1=0
        alto1="25"
        ancho1="100"
        grupo1=""
        marcada1=""
        fondo1=""
        letra1=""
        alineacion1="left"
        texto1=""
        posicionx1=""
        posiciony1=""
        agregar1=""
        agregar2=""
        contan1=0
        cont1=0
        contal1=0
            
        for leido1 in self.leidos:
            
            if leido1[0] == control[1]:
                
                fue_agregado1=1

        if fue_agregado1==0:
            
            for p1 in control:
                if cont1==0:
                    for propiedades1 in control:
                        if propiedades1=="setAlto":
                            alto1=f"{control[control.index(propiedades1)+1]}"
                            control[control.index(propiedades1)+1]=control[control.index(propiedades1)+1]+"A"
                        elif propiedades1=="setAncho":
                            ancho1=f"{control[control.index(propiedades1)+1]}"
                            control[control.index(propiedades1)+1]=control[control.index(propiedades1)+1]+"B"
                        elif propiedades1=="setGrupo":
                            grupo1=f"{control[control.index(propiedades1)+1]}"
                        elif propiedades1=="setMarcada":
                            if control[control.index(propiedades1)+1]=="true":
                                marcada1=f"checked=\"checked\""
                        elif propiedades1=="setColorFondo":
                            fondo1=f"{int(control[control.index(propiedades1)+1])}, {int(control[control.index(propiedades1)+2])}, {int(control[control.index(propiedades1)+3])}"
                            control[control.index(propiedades1)+1]=control[control.index(propiedades1)+1]+"C"
                            control[control.index(propiedades1)+2]=control[control.index(propiedades1)+2]+"D"
                            control[control.index(propiedades1)+3]=control[control.index(propiedades1)+3]+"E"
                        
                        elif propiedades1=="setAlineacion":
                            if control[control.index(propiedades1)+1]=="Centro":
                                alineacion1="center"
                            elif control[control.index(propiedades1)+1]=="Derecho":
                                alineacion1="right"
                        elif propiedades1=="setTexto":
                            texto1=f"{control[control.index(propiedades1)+1]}"
                        elif propiedades1=="setColorLetra":
                            letra1=f"{int(control[control.index(propiedades1)+1])}, {int(control[control.index(propiedades1)+2])}, {int(control[control.index(propiedades1)+3])}"
                            control[control.index(propiedades1)+1]=control[control.index(propiedades1)+1]+"F"
                            control[control.index(propiedades1)+2]=control[control.index(propiedades1)+2]+"G"
                            control[control.index(propiedades1)+3]=control[control.index(propiedades1)+3]+"H"
                        elif propiedades1=="setPosicion":
                            posicionx1=f"{control[control.index(propiedades1)+1]}"
                            posiciony1=f"{control[control.index(propiedades1)+2]}"
                            control[control.index(propiedades1)+1]=control[control.index(propiedades1)+1]+"I"
                            control[control.index(propiedades1)+2]=control[control.index(propiedades1)+2]+"J"
                        elif propiedades1=="add":
                            for l in self.leidos:
                                #[c[1],cadenah,cadenac]
                                if control[control.index(propiedades1)+1]==l[0]:
                                    agregar1+=l[1]
                                    agregar2+=l[2]
                            control[control.index(propiedades1)]=control[control.index(propiedades1)]+"I"
                            
                    cont1+=1        

                if p1=="Contenedor":
                    cadenaCs1+="#"+control[1]+"{\n"
                    cadenaAdd+=f"<div id=\"{control[1]}\">\n"#contener mas cosas
                    contener1=1
                elif p1=="Etiqueta":
                    contener1=2 
                    cadenaCs1+="#"+control[1]+"{\n"
                    cadenaAdd+=f"<label id=\"{control[1]}\"> {texto1} </label>\n" #contener mas cosas
                elif p1=="Boton":
                    cadenaCs1+="#"+control[1]+"{\n"+f"width: {ancho1}px;\nheight: {alto1}px;\n"
                    cadenaAdd+=f"<input type=\"submit\" id=\"{control[1]}\" value=\"{texto1}\" style=\"text-align: {alineacion1}\"/>\n"
                elif p1=="Check":
                    cadenaCs1+="#"+control[1]+"{\n"+f"width: {ancho1}px;\nheight: {alto1}px;\n"
                    if grupo1=="":
                        cadenaAdd+=f"<input type=\"checkbox\" id=\"{control[1]}\" {marcada1} />{texto1}\n"
                    else:
                        cadenaAdd+=f"<input type=\"checkbox\" name=\"{grupo1}\" id=\"{control[1]}\" {marcada1} />{texto1}\n"
                elif p1=="RadioBoton":
                    cadenaCs1+="#"+control[1]+"{\n"+f"width: {ancho1}px;\nheight: {alto1}px;\n"
                    if grupo1=="":
                        cadenaAdd+=f"<input type=\"radio\" id=\"{control[1]}\" {marcada1} />{texto1}\n"
                    else:
                        cadenaAdd+=f"<input type=\"radio\" name=\"{grupo1}\" id=\"{control[1]}\" {marcada1} />{texto1}\n"
                elif p1=="Texto":
                    cadenaCs1+="#"+control[1]+"{\n"+f"width: {ancho1}px;\nheight: {alto1}px;\n"
                    cadenaAdd+=f"<input type = \"text\" id=\"{control[1]}\" value=\"{texto1}\" style=\"text-align:  {alineacion1}\" />\n"
                elif p1=="AreaTexto":
                    cadenaCs1+="#"+control[1]+"{\n"+"width: 150px;\nheight: 150px;\n"
                    cadenaAdd+=f"<TEXTAREA id=\"{control[1]}\">{texto1}</TEXTAREA>\n" #contener mas cosas
                elif p1=="Clave":
                    cadenaCs1+="#"+control[1]+"{\n"+f"width: {ancho1}px;\nheight: {alto1}px;\n"
                    cadenaAdd+=f"<input type = \"password\" id=\"{control[1]}\"value=\"{texto1}\" style=\"text-align: {alineacion1}\"/>\n"
                
                
                elif p1=="setAncho":
                    contan1=1
                    cadenaCs1+=f"width: {ancho1}px;\n"
                elif p1=="setAlto":
                    contal1=1
                    cadenaCs1+=f"height: {alto1}px;\n"
                elif p1=="setColorFondo":
                    cadenaCs1+=f"background-color: rgb({fondo1});\n"
                elif p1=="setColorLetra":
                    cadenaCs1+=f"color: rgb({letra1});\n"
                elif p1=="setPosicion":
                    cadenaCs1+=f"position:absolute;\nleft: {posicionx1}px;\ntop: {posiciony1}px;\n"

                elif len(control)-1==control.index(p1):
                    if contan1==0:
                        if contener1==1  or contener1==2 :
                            cadenaCs1+=f"width: {ancho1}px;\n"
                    if contal1==0:
                        if contener1==1 or contener1==2 :
                            cadenaCs1+=f"height: {alto1}px;\n"
                    cadenaCs1+="}\n"
                    if agregar1!="":
                        cadenaAdd+=agregar1
                    if agregar2!="":
                        cadenaCs1+=agregar2

                    if contener1==1:
                        cadenaAdd+="</div>\n"
                        contener1=0
                    self.leidos.append([control[1],cadenaAdd,cadenaCs1])

        print("++++++++++++++++++++++++++++++++")
        print(cadenaAdd)
        print("++++++++++++++++++++++++++++++++")
        
        print("")

    def construirhtml(self,datohtml,nameentrada):
        print("---> CONSTRUYENDO HTML")
        
        file =open(f"{nameentrada}"+".html","w",encoding= "utf-8")
        contenido ="<!doctype html>\n" \
                "<html lang=\"es\">\n" \
                "<head>\n" \
                "\n" \
                "  <meta charset=\"UTF-8\">\n" \
                f"  <link href=\"{nameentrada}.css\" rel=\"stylesheet\"type=\"text/css\" />\n" \
                "\n" \
                "</head>\n" \
                "<body> \n" \
                "\n" 
        contenido+=datohtml
        contenido+="\n" \
                "</body>\n" \
                "</html>"
        file.write(contenido)
        file.close()
        print("       completado")
        webbrowser.open_new_tab(f"{nameentrada}"+".html")

    def construircss(self,datosccs,namecss):
        print("--->CONSTRUYENDO CSS")
        filec =open(f"{namecss}"+".css","w",encoding= "utf-8")
        filec.write(datosccs)
        filec.close()
        print("       completado")
        
        #webbrowser.open_new_tab(f"{namecss}"+".html")  