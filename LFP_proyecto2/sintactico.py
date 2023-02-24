
class analizadorS:
    def __init__(self):
        self.cadena = ""
        self.anterior=0
        self.columna = 0
        self.lista_cadena = []
        self.lista=[]
        self.listamostrar=[]
        self.estado_actual =""
        self.estado_comentario ="q0"
        self.control_leido=""
        self.posicion_agregar=-1
        self.propiedad_leida=""
        self.multic=-1
        self.adds=0
        self.tokens = []
        self.ids=[]
        self.num=[]
        self.text=[]
    
    def verificartoken (self, entrada:str, token:str):
        cont=0
        for i in range(0,len(token)):
            if cont>=len(entrada):
                return{"result":None, "cont":cont}
            if entrada[i] != token[i]:
                return{"result":None, "cont":cont}
            cont+=1
        nueva_cadena=""
        count=0
        lista= entrada.split(token)
        for j in lista:
            if count==len(lista)-1:
                nueva_cadena +=j
            elif count>0:
                nueva_cadena +=j + token
            count+=1
        return{"result":nueva_cadena, "cont":cont}
            
    def leerestado(self):
        self.estado_actual="q0"

        for i in range(len(self.lista_cadena)):
            self.anterior=self.columna
            self.columna=0
            #fila leida actualmente
            self.cadena=self.lista_cadena[i]
           # print("---------------------------------")
            #print(i)
            #print(self.cadena)
            #print("---------------------------------")
            comentres=self.comentario(i)
            if comentres!=None:
                return comentres
            if self.multic==-1:
                while self.cadena!="":

                    #INICIO AUTOMATA 1
                    if self.estado_actual=="q0":
                        token="<"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se necesita simbolo de abertura de area"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="q1"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="q1":
                        token="!"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba el signo de admiracion"}
                            print("Error",token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="q2"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="q2":
                        token="-"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba el simbolo guion"}
                            print("Error",token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="q3"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="q3":
                        token="-"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba el simbolo guion"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="q4"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="q4":
                        token="Controles"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            token="controles"
                            res=self.verificartoken(self.cadena,token)
                            if res["result"]==None:
                                return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":"Controles, controles","descrip":"Se esperaba una de las etiquetas para abertura de area"}
                                print("Error", token)
                                break
                            
                            print(" | ",i," | ",self.columna," | ", token)
                            self.cadena=res["result"]
                            self.columna+=res["cont"]
                            self.estado_actual="q5"
                        else:
                            print(" | ",i," | ",self.columna," | ", token)
                            self.cadena=res["result"]
                            self.columna+=res["cont"]
                            self.estado_actual="q5"

                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres
                        
                    elif self.estado_actual=="q5":
                        token="Controles"
                        Tcadena="Controles"
                        res=self.verificartoken(self.cadena,token)
                        # Error
                        if res["result"]==None:
                            token="controles"
                            Tcadena+=", controles"
                            res=self.verificartoken(self.cadena,token)
                            if res["result"]==None:
                                tokens=["Etiqueta","Boton","Check","RadioBoton","Texto","AreaTexto","Clave","Contenedor"]
                                for t in tokens:
                                    
                                    res=self.verificartoken(self.cadena,t)
                                    if res["result"]!=None:
                                        token=t
                                        self.estado_actual="q6"
                                        break
                                    else:
                                        Tcadena+=f", {t}"
                                    
                            else:
                                self.estado_actual="q8"
                                
                        else:
                            self.estado_actual="q8"
                            

                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i,"columna":self.columna,"token":Tcadena,"descrip":"Se esperaba una etiqueta reservada valida para el area de controles"}
                            print("Error",token)
                            break

                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres
                    
                    # id
                    elif self.estado_actual=="q6":
                        cont=0
                        cadena=""
                        respuesta=[]
                        respuesta=self.verificarid()
                        for id in self.ids:
                            if (self.ids.index(id)%2)!=0:

                                if id==respuesta[0]:
                                    token=id
                                    self.lista.append([self.ids[self.ids.index(id)-1],id])
                                    self.estado_actual="q7"
                                    break
                                else:
                                    if cont==0:
                                        cadena+=id
                                    else:
                                        cadena+=", "+id
                                    if len(self.ids)-1==self.ids.index(id):
                                        return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":cadena,"descrip":"Se esperaba un identificador definido"}
                                    cont+=1
                            
                        print(" | ",i," | ",self.columna," | ", token)
                        self.columna+=respuesta[1]
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="q7":
                        token=";"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i,"columna":self.anterior,"token":token,"descrip":"Se esperaba el simbolo de termino de comando, punto y coma"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="q5"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="q8":
                        token="-"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba el simbolo guion"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="q9"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="q9":
                        token="-"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba el simbolo guion"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="q10"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="q10":
                        token=">"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se necesita simbolo de cierre de area"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="q11"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres
                        
                    elif self.estado_actual=="q11":
                        self.estado_actual="r0"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres
                
                    # Inicio automata 2
                    elif self.estado_actual=="r0":
                        token="<"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se necesita simbolo de abertura de area"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="r1"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="r1":
                        token="!"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba el signo de admiracion"}
                            print("Error",token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="r2"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="r2":
                        token="-"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba el simbolo guion"}
                            print("Error",token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="r3"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="r3":
                        token="-"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba el simbolo guion"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="r4"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="r4":
                        token="Propiedades"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            token="propiedades"
                            res=self.verificartoken(self.cadena,token)
                            if res["result"]==None:
                                return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":"Propiedades, propiedades","descrip":"Se esperaba una de las etiquetas para abertura de area"}
                                print("Error", token)
                                break
                            
                            print(" | ",i," | ",self.columna," | ", token)
                            self.cadena=res["result"]
                            self.columna+=res["cont"]
                            self.estado_actual="r5"
                        else:
                            print(" | ",i," | ",self.columna," | ", token)
                            self.cadena=res["result"]
                            self.columna+=res["cont"]
                            self.estado_actual="r5"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres    
                    
                    #id    
                    elif self.estado_actual=="r5":
                        ve=0
                        token="Propiedades"
                        Tcadena="Propiedades"
                        res=self.verificartoken(self.cadena,token)
                        # Error
                        if res["result"]==None:
                            token="propiedades"
                            Tcadena+=", propiedades"
                            res=self.verificartoken(self.cadena,token)
                            if res["result"]==None:
                                respuesta=[]
                                respuesta=self.verificarid()
                                for id in self.ids:
                                    if (self.ids.index(id)%2)!=0:
                                        
                                        if id==respuesta[0]:
                                            ve+=1
                                            token=id
                                            self.estado_actual="r6"
                                            for pl1 in range(len(self.lista)):
                                                try:
                                                    if self.lista[pl1][1]==id:
                                                        self.posicion_agregar=pl1
                                                except:
                                                    pass
                                            self.control_leido=self.ids[self.ids.index(id)-1]
                                            break
                                        else:
                                            Tcadena+=f", {id}"
                            else:
                                self.estado_actual="r24"
                                
                        else:
                            self.estado_actual="r24"
                            
                        # Error
                        if ve==0:
                            if res["result"]==None:
                                return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":Tcadena,"descrip":"Se esperaba una etiqueta reservada valida para el area de propiedades"}
                                print("Error",token)
                                break
                                
                        print(" | ",i," | ",self.columna," | ", token)
                        
                        if ve>0:
                            self.columna+=respuesta[1]
                        else:
                            self.cadena=res["result"]
                            self.columna+=res["cont"]

                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres
                    
                    elif self.estado_actual=="r6":
                        token="."
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba el simbolo para agregar propiedad al control"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="r7"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres
                
                    elif self.estado_actual=="r7":
                        token=""
                        if self.control_leido=="AreaTexto":
                            token="setTexto"
                            res=self.verificartoken(self.cadena,token)
                            if res["result"]==None:
                                return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba una propiedad reservada valida para el control"}
                                print("Error", token)
                                break
                            print(" | ",i," | ",self.columna," | ", token)
                            self.cadena=res["result"]
                            self.columna+=res["cont"]
                            self.estado_actual="r8"

                        if self.control_leido=="Etiqueta":
                            token="setTexto"
                            Tcadena="setTexto"
                            res=self.verificartoken(self.cadena,token)
                            # Error
                            if res["result"]==None:
                                token="setColorLetra"
                                Tcadena+=", setColorLetra"
                                res=self.verificartoken(self.cadena,token)
                                if res["result"]==None:
                                    token="setColorFondo"
                                    Tcadena+=", setColorFondo"
                                    res=self.verificartoken(self.cadena,token)
                                    if res["result"]==None:
                                        token="setAncho"
                                        Tcadena+=", setAncho"
                                        res=self.verificartoken(self.cadena,token)
                                        if res["result"]==None:
                                            token="setAlto"
                                            Tcadena+=", setAlto"
                                            res=self.verificartoken(self.cadena,token)
                                            if res["result"]!=None:
                                                self.estado_actual="r20"
                                                self.propiedad_leida=token
                                                
                                        else:
                                            self.estado_actual="r20"
                                            self.propiedad_leida=token

                                    else:
                                        self.estado_actual="r13"
                                        
                                else:
                                    self.estado_actual="r13"
                                    
                            else:
                                self.estado_actual="r8"
                                
                            # Error
                            if res["result"]==None:
                                return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":Tcadena,"descrip":"Se esperaba una propiedad reservada valida para el control"}
                                print("Error",token)
                                break
                            print(" | ",i," | ",self.columna," | ", token)
                            self.cadena=res["result"]
                            self.columna+=res["cont"]

                        if self.control_leido=="Contenedor":
                            token="setColorFondo"
                            Tcadena="setColorFondo"
                            res=self.verificartoken(self.cadena,token)
                            # Error
                            if res["result"]==None:
                                token="setAncho"
                                Tcadena+=", setAncho"
                                res=self.verificartoken(self.cadena,token)
                                if res["result"]==None:
                                    token="setAlto"
                                    Tcadena+=", setAlto"
                                    res=self.verificartoken(self.cadena,token)
                                    if res["result"]!=None:
                                        self.estado_actual="r20"
                                        self.propiedad_leida=token
                                        
                                else:
                                    self.estado_actual="r20"
                                    self.propiedad_leida=token
                            else:
                                self.estado_actual="r13"

                            # Error
                            if res["result"]==None:
                                return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":Tcadena,"descrip":"Se esperaba una propiedad reservada valida para el control"}
                                print("Error",token)
                                break
                            print(" | ",i," | ",self.columna," | ", token)
                            self.cadena=res["result"]
                            self.columna+=res["cont"]

                        if self.control_leido=="Boton" or self.control_leido=="Texto" or self.control_leido=="Clave":
                            
                            token="setTexto"
                            Tcadena="setTexto"
                            res=self.verificartoken(self.cadena,token)
                            # Error
                            if res["result"]==None:
                                token="setAlineacion"
                                Tcadena+=", setAlineacion"
                                res=self.verificartoken(self.cadena,token)
                                if res["result"]!=None:
                                    self.estado_actual="r20"
                                    self.propiedad_leida=token
                            else:
                                self.estado_actual="r8"

                            # Error
                            if res["result"]==None:
                                return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":Tcadena,"descrip":"Se esperaba una propiedad reservada valida para el control"}
                                print("Error",token)
                                break
                            print(" | ",i," | ",self.columna," | ", token)
                            self.cadena=res["result"]
                            self.columna+=res["cont"]

                        if self.control_leido=="Check" or self.control_leido=="RadioBoton":
                            token="setTexto"
                            Tcadena="setTexto"
                            res=self.verificartoken(self.cadena,token)
                            # Error
                            if res["result"]==None:
                                token="setMarcada"
                                Tcadena+=", setMarcada"
                                res=self.verificartoken(self.cadena,token)
                                if res["result"]==None:
                                    token="setGrupo"
                                    Tcadena+=", setGrupo"
                                    res=self.verificartoken(self.cadena,token)
                                    if res["result"]!=None:
                                        self.estado_actual="r20"
                                        self.propiedad_leida=token
                                    
                                else:
                                    self.estado_actual="r20"
                                    self.propiedad_leida=token
                            else:
                                self.estado_actual="r8"

                            # Error
                            if res["result"]==None:
                                return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":Tcadena,"descrip":"Se esperaba una propiedad reservada valida para el control"}
                                print("Error",token)
                                break
                            print(" | ",i," | ",self.columna," | ", token)
                            self.cadena=res["result"]
                            self.columna+=res["cont"]
                       
                        self.lista[self.posicion_agregar].append(token)
                        self.control_leido=""
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="r8":
                        token="("
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba el simbolo de apertura para ingreso de parametros"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="r9"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres
                    
                    elif self.estado_actual=="r9":
                        token="\""
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba comillas para ingresar texto"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="r10"

                    #texto
                    elif self.estado_actual=="r10":
                        cont=0
                        cadena=""
                        token=""
                        respuesta=[]
                        respuesta=self.verificartext(2)
                        for text in self.text:
                            
                            if text==respuesta[0]:
                                token=text
                                self.estado_actual="r11"
                                break
                            else:
                            
                                if len(self.text)-1==self.text.index(text):
                                    return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":"Token_texto","descrip":"Se esperaba parametro de tipo texto"}
                                
                        self.lista[self.posicion_agregar].append(token)
                        print(" | ",i," | ",self.columna," | ", token)
                        self.columna+=respuesta[1]
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="r11":
                        token="\""
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba comillas para cierre de area de texto"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="r12"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres
                    
                    elif self.estado_actual=="r12":
                        token=")"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba simbolo para cierre de propiedad"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="r23"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="r13":
                        token="("
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba simbolo de apertura para ingreso de parametros"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="r14"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres
                    
                    #numero
                    elif self.estado_actual=="r14":
                        token=""
                        respuesta=[]
                        respuesta=self.verificarnum()
                        for num in self.num:
                            if respuesta[0]==num:
                                token=num
                                self.estado_actual="r15"
                                break
                            else:
                            
                                if len(self.num)-1==self.num.index(num):
                                    return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":"Token_numero","descrip":"Se esperaba parametro numerico"}
                                
                        self.lista[self.posicion_agregar].append(token)
                        print(" | ",i," | ",self.columna," | ", token)
                        self.columna+=respuesta[1]
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="r15":
                        token=","
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba un separador de parametros"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="r16"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres
                    
                    #numero
                    elif self.estado_actual=="r16":
                        token=""
                        respuesta=[]
                        respuesta=self.verificarnum()
                        for num in self.num:
                            if respuesta[0]==num:
                                token=num
                                self.estado_actual="r17"
                                break
                            else:
                            
                                if len(self.num)-1==self.num.index(num):
                                    return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":"Token_numero","descrip":"Se esperaba parametro numerico"}
                                
                        self.lista[self.posicion_agregar].append(token)
                        print(" | ",i," | ",self.columna," | ", token)
                        self.columna+=respuesta[1]
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="r17":
                        token=","
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba un separador de parametros"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="r18"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    #numero
                    elif self.estado_actual=="r18":
                        token=""
                        respuesta=[]
                        respuesta=self.verificarnum()
                        for num in self.num:
                            if respuesta[0]==num:
                                token=num
                                self.estado_actual="r19"
                                break
                            else:
                            
                                if len(self.num)-1==self.num.index(num):
                                    return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":"Token_numero","descrip":"Se esperaba parametro numerico"}
                                
                        self.lista[self.posicion_agregar].append(token)
                        print(" | ",i," | ",self.columna," | ", token)
                        self.columna+=respuesta[1]
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres
                    
                    elif self.estado_actual=="r19":
                        token=")"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba simbolo para cierre de propiedad"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="r23"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres
                    
                    elif self.estado_actual=="r20":
                        token="("
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba el simbolo de apertura para ingreso de parametros"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="r21"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="r21":
                        token=""

                        #numero
                        if self.propiedad_leida=="setAlto" or self.propiedad_leida=="setAncho":
                            respuesta=[]
                            respuesta=self.verificarnum()
                            for num in self.num:
                                if respuesta[0]==num:
                                    token=num
                                    self.estado_actual="r22"
                                    break
                                else:
                                
                                    if len(self.num)-1==self.num.index(num):
                                        return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":"Token_numero","descrip":"Se esperaba parametro numerico"}
                                    

                            print(" | ",i," | ",self.columna," | ", token)
                            self.columna+=respuesta[1]

                        if self.propiedad_leida=="setAlineacion":
                            token="Derecho"
                            Tcadena="Derecho"
                            res=self.verificartoken(self.cadena,token)
                            # Error
                            if res["result"]==None:
                                token="Izquierdo"
                                Tcadena+=", Izquierdo"
                                res=self.verificartoken(self.cadena,token)
                                if res["result"]==None:
                                    token="Centro"
                                    Tcadena+=", Centro"
                                    res=self.verificartoken(self.cadena,token)
                                    if res["result"]!=None:
                                        self.estado_actual="r22"
                                        
                                else:
                                    self.estado_actual="r22"
                                    
                            else:
                                self.estado_actual="r22"
                                

                            # Error
                            if res["result"]==None:
                                print("entra error")
                                return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":Tcadena,"descrip":"Se esperaba un parametro reservado valido para la propiedad"}
                                print("Error",token)
                                break
                            print(" | ",i," | ",self.columna," | ", token)
                            self.cadena=res["result"]
                            self.columna+=res["cont"]

                        if self.propiedad_leida=="setMarcada":
                            token="true"
                            Tcadena="true"
                            res=self.verificartoken(self.cadena,token)
                            # Error
                            if res["result"]==None:
                                token="false"
                                Tcadena+=", false"
                                res=self.verificartoken(self.cadena,token)
                                if res["result"]!=None:
                                    self.estado_actual="r22"
                                    self.propiedad_leida=token
                                     
                            else:
                                self.estado_actual="r22"
                                
                            # Error
                            if res["result"]==None:
                                return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":Tcadena,"descrip":"Se esperaba un parametro reservado valido para la propiedad"}
                                print("Error",token)
                                break
                            print(" | ",i," | ",self.columna," | ", token)
                            self.cadena=res["result"]
                            self.columna+=res["cont"]
                        
                        #id
                        if self.propiedad_leida=="setGrupo":
                            Tcadena=""
                            cont=0
                            respuesta=[]
                            respuesta=self.verificarid()
                            for id in self.ids:
                                if (self.ids.index(id)%2)!=0:
                                    if id==respuesta[0]:
                                        token=id
                                        self.estado_actual="r22"
                                        break
                                    else:
                                        if cont==0:
                                            Tcadena+=f"{t}"
                                        else:
                                            Tcadena+=f", {t}"
                                        cont+=1
                                        if len(self.ids)-1==self.ids.index(id):
                                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":Tcadena,"descrip":"Se esperaba como parametro a un identificador definido"}
                            
                            print(" | ",i," | ",self.columna," | ", token)
                            self.columna+=respuesta[1]

                        self.lista[self.posicion_agregar].append(token)
                        self.propiedad_leida=""
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="r22":
                        token=")"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba simbolo para cierre de propiedad"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="r23"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="r23":
                        token=";"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i,"columna":self.anterior,"token":token,"descrip":"Se esperaba el simbolo de termino de comando, punto y coma"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="r5"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="r24":
                        token="-"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba el simbolo guion"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="r25"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres
                    
                    elif self.estado_actual=="r25":
                        token="-"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba el simbolo guion"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="r26"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="r26":
                        token=">"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se necesita simbolo de cierre de area"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="r27"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres
                        
                    elif self.estado_actual=="r27":
                        self.posicion_agregar=-1
                        self.estado_actual="s0"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres
                    
                    #INICIO AUTOMATA 3
                    elif self.estado_actual=="s0":
                        token="<"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se necesita simbolo de abertura de area"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="s1"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="s1":
                        token="!"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba el signo de admiracion"}
                            print("Error",token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="s2"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="s2":
                        token="-"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba el simbolo guion"}
                            print("Error",token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="s3"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="s3":
                        token="-"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba el simbolo guion"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="s4"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="s4":
                        token="Colocacion"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            token="colocacion"
                            res=self.verificartoken(self.cadena,token)
                            if res["result"]==None:
                                return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":"Colocacion, colocacion","descrip":"Se esperaba una de las etiquetas para apertura de area"}
                                print("Error", token)
                                break
                            
                            print(" | ",i," | ",self.columna," | ", token)
                            self.cadena=res["result"]
                            self.columna+=res["cont"]
                            self.estado_actual="s5"
                        else:
                            print(" | ",i," | ",self.columna," | ", token)
                            self.cadena=res["result"]
                            self.columna+=res["cont"]
                            self.estado_actual="s5"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres
                    
                    #id
                    elif self.estado_actual=="s5":
                        ve=0
                        token="Colocacion"
                        Tcadena="Colocacion"
                        res=self.verificartoken(self.cadena,token)
                        # Error
                        if res["result"]==None:
                            token="colocacion"
                            Tcadena+=", colocacion"
                            res=self.verificartoken(self.cadena,token)
                            if res["result"]==None:
                                token="this"
                                Tcadena+=", this"
                                res=self.verificartoken(self.cadena,token)
                                if res["result"]==None:
                                    respuesta=[]
                                    respuesta=self.verificarid()
                                    for id in self.ids:
                                        if (self.ids.index(id)%2)!=0:
                                            if id==respuesta[0]:
                                                ve+=1
                                                token=id
                                                self.estado_actual="s6"
                                                for pl1 in range(len(self.lista)):
                                                    try:
                                                        if self.lista[pl1][1]==id:
                                                            self.posicion_agregar=pl1
                                                    except:
                                                        pass
                                                break
                                            else:
                                                Tcadena+=f", {id}"
                                else:
                                    self.posicion_agregar=-1
                                    self.estado_actual="s13"
                            else:
                                self.estado_actual="s19"
                                
                        else:
                            self.estado_actual="s19"
                            

                        # Error
                        if ve==0:
                            if res["result"]==None:
                                return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":Tcadena,"descrip":"Se esperaba una etiqueta reservada valida para el area de colocacion"}
                                print("Error",token)
                                break
                        print(" | ",i," | ",self.columna," | ", token)
                        if ve>0:
                            self.columna+=respuesta[1]
                        else:
                            self.cadena=res["result"]
                            self.columna+=res["cont"]
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres
                    
                    elif self.estado_actual=="s6":
                        token="."
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba el simbolo para agregar posicion al control"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="s7"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres
                    
                    elif self.estado_actual=="s7":
                        token="setPosicion"
                        Tcadena="setPosicion"
                        res=self.verificartoken(self.cadena,token)
                        # Error
                        if res["result"]==None:
                            token="add"
                            Tcadena+=", add"
                            res=self.verificartoken(self.cadena,token)
                            if res["result"]!=None:
                                self.adds+=1
                                self.estado_actual="s15"
                                self.propiedad_leida=token
                                    
                        else:
                            self.estado_actual="s8"
                            

                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":Tcadena,"descrip":"Se esperaba una etiqueta de colocacion valida"}
                            print("Error",token)
                            break
                        self.lista[self.posicion_agregar].append(token)
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="s8":
                        token="("
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba el simbolo de apertura para ingreso de parametros"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="s9"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres
                    
                    #numero
                    elif self.estado_actual=="s9":
                        token=""
                        respuesta=[]
                        respuesta=self.verificarnum()
                        for num in self.num:
                            if respuesta[0]==num:
                                token=num
                                self.estado_actual="s10"
                                break
                            else:
                            
                                if len(self.num)-1==self.num.index(num):
                                    return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":"Token_numero","descrip":"Se esperaba parametro numerico"}
                                
                        self.lista[self.posicion_agregar].append(token)
                        print(" | ",i," | ",self.columna," | ", token)
                        self.columna+=respuesta[1]
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="s10":
                        token=","
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba un separador de parametros"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="s11"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    #numero
                    elif self.estado_actual=="s11":
                        token=""
                        respuesta=[]
                        respuesta=self.verificarnum()
                        for num in self.num:
                            if respuesta[0]==num:
                                token=num
                                self.estado_actual="s12"
                                break
                            else:
                            
                                if len(self.num)-1==self.num.index(num):
                                    return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":"Token_numero","descrip":"Se esperaba parametro numerico"}
                                
                        self.lista[self.posicion_agregar].append(token)
                        print(" | ",i," | ",self.columna," | ", token)
                        self.columna+=respuesta[1]
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="s12":
                        token=")"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba simbolo para cierre de propiedad"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="s18"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="s13":
                        token="."
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba el simbolo para agregar posicion al control"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="s14"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres
                    
                    elif self.estado_actual=="s14":
                        token="add"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba etiqueta para agregar a la pagina"}
                            print("Error", token)
                            break
                        
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="s15"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="s15":
                        token="("
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba el simbolo de apertura para ingreso de parametros"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="s16"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    #id
                    elif self.estado_actual=="s16":
                        Tcadena=""
                        cont=0
                        token=""
                        respuesta=[]
                        respuesta=self.verificarid()
                        for id in self.ids:
                            if (self.ids.index(id)%2)!=0:

                                if id==respuesta[0]:
                                    token=id
                                    self.estado_actual="s17"
                                    break
                                else:
                                    if cont==0:
                                        Tcadena+=f"{id}"
                                    else:
                                        Tcadena+=f", {id}"
                                    cont+=1
                                    if len(self.ids)-1==self.ids.index(id):
                                        return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":Tcadena,"descrip":"Se esperaba como parametro a un identificador definido"}
                        if self.posicion_agregar==-1:
                            self.listamostrar.append(token)
                        else:
                            self.lista[self.posicion_agregar].append(token)
                        print(" | ",i," | ",self.columna," | ", token)
                        self.columna+=respuesta[1]
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="s17":
                        token=")"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba simbolo para cierre de propiedad"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="s18"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="s18":
                        token=";"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i,"columna":self.anterior,"token":token,"descrip":"Se esperaba el simbolo de termino de comando, punto y coma"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="s5"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="s19":
                        token="-"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba el simbolo guion"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="s20"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres
                    
                    elif self.estado_actual=="s20":
                        token="-"
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se esperaba el simbolo guion"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="s21"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres

                    elif self.estado_actual=="s21":
                        token=">"
                        print("dfsdfsdfsintactico")
                        res=self.verificartoken(self.cadena,token)
                        
                        # Error
                        if res["result"]==None:
                            return {"error":"Sintactico","linea":i+1,"columna":self.columna,"token":token,"descrip":"Se necesita simbolo de cierre de area"}
                            print("Error", token)
                            break
                        print(" | ",i," | ",self.columna," | ", token)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_actual="s22"
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres
                        
                    elif self.estado_actual=="s22":
                        self.posicion_agregar=-1
                        comentres=self.comentario(i)
                        if comentres!=None:
                            return comentres
                        break

            if self.multic==0:
                self.multic=-1
    
    def verificarnum(self):
        self.Token_numero = ["0","1","2","3","4","5","6","7","8","9"]
        encuentra=True
        num=""
        columna=0
        while encuentra:
            listencuentra=[]
            for en in self.Token_numero:
                res=self.verificartoken(self.cadena,en)
                if res["result"]!=None:
                    
                    num+=f"{en}"
                    self.cadena=res["result"]
                    columna+=res["cont"]
                else:
                    listencuentra.append("false")

            if len(listencuentra)==len(self.Token_numero):
                encuentra=False
        if num=="":
            num=" "
        return [num,columna]

    def verificartext(self,op):
        self.Token_textoC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','#','|','!','<','>','{','}','@','$','&','?','¿','%','+','"','=','_',',','-','.',':',';','(',')','[',']','^']
        self.Token_texto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','#','|','$','&','?','¿','%','+','=','_',',','-','.',':',';','(',')','[',']','^']

        if op==1:
            coment=""
            columna=0
            while self.cadena!="":
                listencuentra=[]
                for en in self.Token_textoC:
                    res=self.verificartoken(self.cadena,en)
                    if res["result"]!=None:
                        coment+=f"{en}"
                        self.cadena=res["result"]
                        columna+=res["cont"]
                    else:
                        listencuentra.append("false")

                if len(listencuentra)==len(self.Token_textoC) or self.cadena=="":
                    break
            if coment=="":
                coment=" "
            return [coment,columna]

        else:
            encuentra=True
            text=""
            columna=0
            while encuentra:
                listencuentra=[]
                for ent in self.Token_texto:
                    res=self.verificartoken(self.cadena,ent)
                    if res["result"]!=None:
                        text+=f"{ent}"
                        self.cadena=res["result"]
                        columna+=res["cont"]
                    else:
                        listencuentra.append("false")

                if len(listencuentra)==len(self.Token_texto):
                    encuentra=False
            if text=="":
                text=" "
            return [text,columna]

    def verificarid(self):
        self.Token_Id = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','_']
        encuentra=True
        idg=""
        columna=0
        while encuentra:
            listencuentra=[]
            for e in self.Token_Id:
                res=self.verificartoken(self.cadena,e)
                if res["result"]!=None:
                    idg+=f"{e}"
                    self.cadena=res["result"]
                    columna+=res["cont"]
                else:
                    listencuentra.append("false")

            if len(listencuentra)==len(self.Token_Id):
                encuentra=False
        if idg=="":
            idg=" "
        return [idg,columna]

    def comentario(self,f):
        tokenc=""
        tokent=""
        if self.estado_comentario =="q0":

            tokenc="/"
            res=self.verificartoken(self.cadena,tokenc)
            if res["result"]!=None:
                print(" | ",f," | ",self.columna," | ", tokenc)
                self.cadena=res["result"]
                self.columna+=res["cont"]
                tokenc="/"
                res=self.verificartoken(self.cadena,tokenc)
                if res["result"]!=None:
                    print(" | ",f," | ",self.columna," | ", tokenc)
                    self.cadena=res["result"]
                    self.columna+=res["cont"]
                    respuesta=[]
                    respuesta=self.verificartext(1)
                    for text in self.text:
                        if text==respuesta[0]:
                            tokent=text
                            break
                        else:
                        
                            if len(self.text)-1==self.text.index(text):
                                return {"error":"Sintactico","linea":f+1,"columna":self.columna,"token":"Token_texto","descrip":"Se esperaba parametro de tipo texto"}
                            

                    print(" | ",f," | ",self.columna," | ", tokent)
                    self.columna+=respuesta[1]
                else:
                    cont=0
                    tokenc="*"
                    res=self.verificartoken(self.cadena,tokenc)
                    if res["result"]!=None:
                        self.multic=1
                        self.estado_comentario ="q4"
                        
                        print(" | ",f," | ",self.columna," | ", tokenc)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        respuesta=[]
                        respuesta=self.verificartext(1)
                        for text in self.text:
                            if text==respuesta[0]:
                                cont+=1
                                tokent=text
                                break
                        if cont>0:  
                            print(" | ",f," | ",self.columna," | ", tokent)
                            self.columna+=respuesta[1]
                    else:
                        return {"error":"Sintactico","linea":f+1,"columna":self.columna,"token":"* , /","descrip":"No se cumple con la sintaxis para los comentarios"}
        
        if self.estado_comentario =="q4":  
            cont=0  
            if self.cadena!=None :
                respuesta=[]
                respuesta=self.verificartext(1)
                for text in self.text:
                    if text==respuesta[0]:
                        cont+=1
                        tokent=text
                        break
                if cont>0:
                    print(" | ",f," | ",self.columna," | ", tokent)
                    self.columna+=respuesta[1]
                tokenc="*"
                res=self.verificartoken(self.cadena,tokenc)
                if res["result"]!=None:
                    print(" | ",f," | ",self.columna," | ", tokenc)
                    self.cadena=res["result"]
                    self.columna+=res["cont"]
                    tokenc="/"
                    res=self.verificartoken(self.cadena,tokenc)
                    if res["result"]!=None:
                        print(" | ",f," | ",self.columna," | ", tokenc)
                        self.cadena=res["result"]
                        self.columna+=res["cont"]
                        self.estado_comentario="q0"
                        self.multic=0
                    else:
                        return {"error":"Sintactico","linea":f+1,"columna":self.columna,"token":tokenc,"descrip":"No se cumple con la sintaxis para los comentarios"}
            
            if f == len(self.lista_cadena)-1 and self.multic!=0:
                return {"error":"Sintactico","linea":f+1,"columna":self.columna,"token":"*/","descrip":"Falta cierre de comentario multilinea"}

    def compilador1(self,dir,datos):
        
        self.ids=datos["0"]
        self.num=datos["1"]
        self.text=datos["2"]
        #Leer archivo
        archivo = open(dir, "r",encoding="utf-8")
        #archivo = open("Archivosprueba/prueba1.gpw", "r",encoding="utf-8")
        contenido = archivo.readlines()
        archivo.close()

        #Limpiar cadena
        for i in contenido:
            i=i.replace(" ","")
            i=i.replace("\n","")
            if i!='':
                self.lista_cadena.append(i)

        #mostrar lista de cadena
        print("")
        print("----------------------------------------------------------------")
        print("                   ANALIZADOR SINTACTICO")
        print("----------------------------------------------------------------")

        e=self.leerestado()
        
        print("********************************************")
        print(self.lista)
        print("********************************************")
        print(self.listamostrar)
        print("")
        print("")

        if e==None:
            return {"error":None,"0":self.lista,"1":self.listamostrar,"2":self.adds}
        else:
            print(e)
            return e

       

"""
id=['Contenedor', 'contlogin', 'Boton', 'cmdIngresar','RadioBoton', 'bot1']
numero=['190', '47', '79', '586', '110','40', '100']
texto=[ 'ijoijo', 'juihi', 'jjj1', 'jjj2', 'ijoijo2', 'juihi2', 'jjj3', 'Ingresar', 'cmdIngresar.setPosicion(40,100);', 'contlogin.add(cmdIngresar);', 'Colocacion-->']
listacl=[id,numero,texto]
a=analizadorS()
a.compilador1(listacl)

"""