from sintactico import analizadorS
from traduccion1 import transformar

class analizadorl:
    def __init__(self):
        self.cadena = ""
        self.columna = 0
        self.lista_cadena = []
        self.tokens_usados = []
        self.ids=[]
        self.num=[]
        self.text=[]

        #Tokens
        self.Token_barra = "/"
        self.Token_textoC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','#','|','!','<','>','{','}','@','$','&','?','¿','%','+','"','=','_',',','-','.',':',';','(',')','[',']','^']
        self.Token_texto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','#','|','$','&','?','¿','%','+','=','_',',','-','.',':',';','(',')','[',']','^']
        self.Token_asterisco = "*"
        self.Token_mayor = ">"
        self.Token_menor = "<"
        self.Token_signoE = "!"
        self.Token_guion = "-"
        self.Token_E_Control = ["Controles","controles"] 
        self.Token_E_Propiedad = ["Propiedades","propiedades"]
        self.Token_E_Colocar = ["Colocacion","colocacion"]
        self.Token_Control = ["Etiqueta","Boton","Check","RadioBoton","Texto","AreaTexto","Clave","Contenedor"]
        self.Token_Id = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','_']
        self.Token_pcoma = ";"
        self.Token_punto = "."
        self.Token_Propiedad = ["setColorLetra","setTexto","setAlineacion","setColorFondo","setMarcada","setGrupo","setAncho","setAlto"]
        self.Token_pa = "("
        self.Token_pc = ")"
        self.Token_coma = ","
        self.Token_comilla = "\""
        self.Token_numero = ["0","1","2","3","4","5","6","7","8","9"]
        self.Token_P_valor = ["Centro","Izquierdo","Derecho"]
        self.Token_parametro = ["true","false"]
        self.Token_elemento = [self.Token_Id,"this"]
        self.Token_posicion = ["setPosicion","add"]
        self.tokens = [self.Token_barra,self.Token_asterisco,self.Token_mayor,self.Token_menor,self.Token_signoE,self.Token_guion,self.Token_pcoma,self.Token_punto,self.Token_pa,self.Token_pc,self.Token_coma,self.Token_comilla,self.Token_elemento,self.Token_E_Control,self.Token_E_Propiedad,self.Token_E_Colocar,self.Token_Control,self.Token_Propiedad,self.Token_P_valor,self.Token_parametro,self.Token_posicion]
        self.tokens2 =[]
    
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
        #print("----->nuevacadena")
        #print(nueva_cadena)
        return{"result":nueva_cadena, "cont":cont}
            
    def analisis(self):
        area=-1
        numtoken=0
        cota=0
        Ercol=0
        Erpr=0
        multic=-1
        for i in range(len(self.lista_cadena)):
            if multic==0:
                multic=-1
            #fila leida actualmente
            ve=0
            vp=0
            self.columna=0
            self.cadena=self.lista_cadena[i]
            """
            print("---------------------------------")
            print("+++++++++++++++++")
            print(self.cadena)
            print("+++++++++++++++++")
            """
            while self.cadena!="":
                cont=0
                Erid=0
                Erthis=""
                if multic==1:
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

                        if self.cadena=="":
                            numtoken+=1
                            try:
                                self.text.index(coment)            
                            except:
                                self.text.append(coment)
                            self.tokens_usados.append([numtoken,24,coment])
                            print(" | ",i," | ",self.columna," | ", coment)
                            self.columna+=columna
                        res=self.verificartoken(self.cadena,"*")
                        if res["result"]!=None:
                                print(" | ",i," | ",self.columna," | ", "*")
                                self.tokens_usados.append([numtoken,1,"*"])
                                self.cadena=res["result"]
                                self.columna+=res["cont"]
                                res=self.verificartoken(self.cadena,"/")
                                if res["result"]!=None:
                                    print(" | ",i," | ",self.columna," | ", "/")
                                    self.tokens_usados.append([numtoken,0,"/"])
                                    self.cadena=res["result"]
                                    self.columna+=res["cont"]
                                    multic=0
                                    
                       
                if multic==-1:   
                    if area==1 or area==2 or area==0:
                        if area==0:
                            res=self.verificartoken(self.cadena,"Controles")
                            if res["result"]!=None:
                                print(" | ",i," | ",self.columna," | ", "Controles")
                                self.cadena=res["result"]
                                self.columna+=res["cont"]
                                area=-1
                            else:
                                ret=self.verificartoken(self.cadena,"controles")
                                if ret["result"]!=None:
                                    print(" | ",i," | ",self.columna," | ", "controles")
                                    self.cadena=ret["result"]
                                    self.columna+=ret["cont"]
                                    area=-1
                                else:
                                    Ercont=1
                        if area==1:
                            rest=self.verificartoken(self.cadena,"Propiedades")
                            if rest["result"]!=None: 
                                print(" | ",i," | ",self.columna," | ", "Propiedades")
                                self.cadena=res["result"]
                                self.columna+=res["cont"]
                                area=-1
                            else:
                                ret=self.verificartoken(self.cadena,"propiedades")
                                if ret["result"]!=None:
                                    print(" | ",i," | ",self.columna," | ", "propiedades")
                                    self.cadena=ret["result"]
                                    self.columna+=ret["cont"]
                                    
                                    area=-1
                                else:
                                    cadenatemp=self.cadena
                                    for tep in "Ppropiedades":
                                        resio=self.verificartoken(cadenatemp,tep)
                                        if resio["result"]!=None:
                                            cadenatemp=resio["result"]
                                        
                                    for ts in "-->":
                                        res=self.verificartoken(cadenatemp,ts)
                                        if res["result"]!=None:
                                            Erpr=1
                        if area==2:
                            res=self.verificartoken(self.cadena,"Colocacion")
                            if res["result"]!=None:
                                print(" | ",i," | ",self.columna," | ", "Colocacion")
                                self.cadena=res["result"]
                                self.columna+=res["cont"]
                                area=-1
                            else:
                                ret=self.verificartoken(self.cadena,"colocacion")
                                if ret["result"]!=None:
                                    print(" | ",i," | ",self.columna," | ", "colocacion")
                                    self.cadena=ret["result"]
                                    self.columna+=ret["cont"]
                                    area=-1
                                else:
                                    cadenatemp=self.cadena
                                    for tep in "Ccolocacion":
                                        resio=self.verificartoken(cadenatemp,tep)
                                        if resio["result"]!=None:
                                            cadenatemp=resio["result"]
                                        
                                    for ts in "-->":
                                        res=self.verificartoken(cadenatemp,ts)
                                        if res["result"]!=None:
                                            Ercol=1
                    
                        if area==1 or area==2:
                            if Erpr==0 or Ercol==0:
                                if len(self.ids)>0:
                                    for aid in self.ids:
                                        res=self.verificartoken(self.cadena,aid)
                                        if res["result"]!=None:
                                            print(" | ",i," | ",self.columna," | ", aid)
                                            self.cadena=res["result"]
                                            self.columna+=res["cont"]
                                        elif res["result"]==None and area==2 and vp==0:
                                            Erid=1
                                        elif res["result"]==None:
                                            Erid=1
                                else:
                                    Erid=2  
               
                    for t in self.tokens:

                        if cont==0:
                            
                            indext=self.tokens.index(t)
                            #print("---->index ",indext)
                            if indext<12:
                                res=self.verificartoken(self.cadena,t)
                                
                                if res["result"]!=None:
                                    numtoken+=1
                                    try:
                                        #self.tokens_usados.index(indext)
                                        self.tokens_usados.append([numtoken,indext,t])
                                    except:
                                        self.tokens_usados.append(indext)
                                    print(" | ",i," | ",self.columna," | ", t)
                                    self.cadena=res["result"]
                                    self.columna+=res["cont"]
                                    Erid=0
                                    Erthis=""
                                    Ercont=0
                                    Erpr=0
                                    Ercol=0
                                    if indext==0:

                                        res=self.verificartoken(self.cadena,"/")
                                        if res["result"]!=None:
                                            self.tokens_usados.append([numtoken,0,"/"])
                                            print(" | ",i," | ",self.columna," | ", "/")
                                            self.cadena=res["result"]
                                            self.columna+=res["cont"]
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
                                                        Erid=0
                                                    else:
                                                        listencuentra.append("false")

                                                if len(listencuentra)==len(self.Token_numero) or self.cadena=="":
                                                    numtoken+=1
                                                    self.tokens_usados.append([numtoken,24,coment])
                                                    print(" | ",i," | ",self.columna," | ", coment)
                                                    try:
                                                        self.text.index(coment)            
                                                    except:
                                                        self.text.append(coment)
                                                    self.columna+=columna
                                        res=self.verificartoken(self.cadena,"*")
                                        if res["result"]!=None:
                                            print(" | ",i," | ",self.columna," | ", "*")
                                            self.tokens_usados.append([numtoken,1,"*"])
                                            self.cadena=res["result"]
                                            self.columna+=res["cont"]
                                            multic=1
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
                                                        Erid=0
                                                    else:
                                                        listencuentra.append("false")

                                                if len(listencuentra)==len(self.Token_numero) or self.cadena=="":
                                                    numtoken+=1
                                                    self.tokens_usados.append([numtoken,24,coment])
                                                    try:
                                                        self.text.index(coment)            
                                                    except:
                                                        self.text.append(coment)
                                                    print(" | ",i," | ",self.columna," | ", coment)
                                                    self.columna+=columna
                                    if indext==8 or indext==10 :
                                        if vp!=1 and vp!=2 and vp!=3 and vp!=4:
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
                                                        Erid=0
                                                    else:
                                                        listencuentra.append("false")
                                                        Ernum=1

                                                if len(listencuentra)==len(self.Token_numero):
                                                    numtoken+=1
                                                    self.tokens_usados.append([numtoken,22,num])
                                                    print(" | ",i," | ",self.columna," | ", num)
                                                    self.columna+=columna
                                                    encuentra=False
                                            try:
                                                self.num.index(num)            
                                            except:
                                                self.num.append(num)
                                        if indext==8 and vp==2:
                                                ve=0
                                                for en in self.Token_parametro:
                                                    res=self.verificartoken(self.cadena,en)
                                                    if res["result"]!=None:
                                                        ve+=1
                                                        numtoken+=1
                                                        try:
                                                            #self.tokens_usados.index(indext)
                                                            self.tokens_usados.append([numtoken,19,en])
                                                        except:
                                                            #print("no hay")
                                                            self.tokens_usados.append(indext)
                                                        print(" | ",i," | ",self.columna," | ", en)
                                                        self.cadena=res["result"]
                                                        self.columna+=res["cont"]
                                                        Erid=0
                                                        Erthis=""
                                                        Ercont=0
                                                        Erpr=0
                                                        Ercol=0
                                                    else:
                                                        if self.Token_parametro.index(en)==1 and ve==0:
                                                            return {"error":"Lexico","linea":i+1,"columna":self.columna,"token":"true, false","descrip":"Errores de ortografia en palabras reservadas"}
                                        if indext==8 and vp==1:
                                            ve=0
                                            encuentra=True
                                            idg=""
                                            columna=0
                                            while encuentra:
                                                listencuentra=[]
                                                for e in self.Token_Id:
                                                    res=self.verificartoken(self.cadena,e)
                                                    if res["result"]!=None:
                                                        ve+=1
                                                        idg+=f"{e}"
                                                        self.cadena=res["result"]
                                                        columna+=res["cont"]
                                                        Erid=0
                                                    else:
                                                        listencuentra.append("false")

                                                if len(listencuentra)==len(self.Token_Id):
                                                    numtoken+=1
                                                    self.tokens_usados.append([numtoken,21,idg])
                                                    print(" | ",i," | ",self.columna," | ", idg)
                                                    self.columna+=columna
                                                    Eriddef=1
                                                    encuentra=False
                                            try:
                                                self.ids.index(idg)            
                                            except:
                                                self.ids.append("Grupo")
                                                self.ids.append(idg)
                                            Erid=0
                                            Erthis=""
                                            Ercont=0
                                            Erpr=0
                                            Ercol=0
                                            cont+=1
                                        if indext==8 and vp==3:
                                            ve=0
                                            for en in self.Token_P_valor:
                                                res=self.verificartoken(self.cadena,en)
                                                if res["result"]!=None:
                                                    ve+=1
                                                    numtoken+=1
                                                    try:
                                                        #self.tokens_usados.index(indext)
                                                        self.tokens_usados.append([numtoken,18,en])
                                                    except:
                                                        #print("no hay")
                                                        self.tokens_usados.append(indext)
                                                    print(" | ",i," | ",self.columna," | ", en)
                                                    self.cadena=res["result"]
                                                    self.columna+=res["cont"]
                                                    Erid=0
                                                    Erthis=""
                                                    Ercont=0
                                                    Erpr=0
                                                    Ercol=0
                                                else:
                                                    if self.Token_P_valor.index(en)==2 and ve==0:
                                                        return {"error":"Lexico","linea":i+1,"columna":self.columna,"token":"Derecho, Izquierdo, Centro","descrip":"Errores de ortografia en palabras reservadas"}
                                    
                                    if indext==11 and vp==4:
                                        encuentra=True
                                        text=""
                                        columna=0
                                        while encuentra:
                                            listencuentra=[]
                                            for ent in self.Token_texto:
                                                res=self.verificartoken(self.cadena,ent)
                                                if res["result"]!=None:
                                                    #try:
                                                    #    self.tokens_usados.index(23)
                                                    #except:
                                                        #print("no hay")
                                                    #    self.tokens_usados.append(23)
                                                    text+=f"{ent}"
                                                    self.cadena=res["result"]
                                                    columna+=res["cont"]
                                                    Erid=0
                                                else:
                                                    listencuentra.append("false")
                                                    Ertext=1

                                            if len(listencuentra)==len(self.Token_texto):
                                                numtoken+=1
                                                self.tokens_usados.append([numtoken,23,text])
                                                print(" | ",i," | ",self.columna," | ", text)
                                                self.columna+=columna
                                                vp=0
                                                encuentra=False
                                        try:
                                            self.text.index(text)            
                                        except:
                                            self.text.append(text)
                                    cont+=1
                            
                            else:
                               
                                if indext==12:
                                    res=self.verificartoken(self.cadena,t[1])
                                    if res["result"]!=None:
                                        numtoken+=1
                                        try:
                                            #self.tokens_usados.index(indext)
                                            self.tokens_usados.append([numtoken,indext,t[1]])
                                        except:
                                            #print("no hay")
                                            self.tokens_usados.append(indext)
                                        print(" | ",i," | ",self.columna," | ", t[1])
                                        self.cadena=res["result"]
                                        self.columna+=res["cont"]
                                        cont+=1
                                        Erid=0
                                        Erthis=""
                                        Ercont=0
                                        Erpr=0
                                        Ercol=0
                                    else:
                                        cot=0
                                        cadenatemp=self.cadena
                                        for p in "this":
                                            ret=self.verificartoken(cadenatemp,p)
                                            if ret["result"]!=None:
                                                cadenatemp=ret["result"]
                                        ret=self.verificartoken(cadenatemp,".")
                                        if ret["result"]!=None:
                                            cadenatemp=ret["result"]
                                            ret=self.verificartoken(cadenatemp,"add")
                                            if ret["result"]!=None:
                                                Erthis=t[1]
                                                Ercont=0
                                                Erpr=0
                                                Ercol=0
        
                                else:
                                    #for veces in range(len(t)-1):
                                    #   print(veces)
                                    if area==-1:
                                        
                                        if indext==13 or indext==14 or indext==15:
                                            
                                            for j in t:
                                                ve+=1
                                                res=self.verificartoken(self.cadena,j)
                                                if res["result"]!=None:
                                                    cota+=1
                                                    numtoken+=1
                                                    try:
                                                        #self.tokens_usados.index(indext)
                                                        self.tokens_usados.append([numtoken,indext,j])
                                                    except:
                                                        #print("no hay")
                                                        self.tokens_usados.append(indext)
                                                    print(" | ",i," | ",self.columna," | ", j)
                                                    self.cadena=res["result"]
                                                    self.columna+=res["cont"]
                                                    Erid=0
                                                    Erthis=""
                                                    Ercont=0
                                                    Erpr=0
                                                    Ercol=0
                                                    if indext==13:
                                                        area=0
                                                    if indext==14:
                                                        area=1
                                                    if indext==15:
                                                        area=2
                                                    cont+=1
                                                else:
                                                    if t.index(j)==1:
                                                        if cota==0 and area==-1:
                                                            return {"error":"Lexico","linea":i+1,"columna":self.columna,"token":"Controles, controles","descrip":"Errores de ortografia en palabras reservadas"}
                                                        if cota==2 and area==-1 and ve==6:
                                                            return {"error":"Lexico","linea":i+1,"columna":self.columna,"token":"Colocacion, colocacion","descrip":"Errores de ortografia en palabras reservadas"}
                                                        if cota==1 and area==-1 and ve==4 :
                                                            return {"error":"Lexico","linea":i+1,"columna":self.columna,"token":"Propiedades, propiedades","descrip":"Errores de ortografia en palabras reservadas"}
                                                    
                                    if area==0:
                                        if indext==16:
                                            ve=0
                                            for j in t:
                                                res=self.verificartoken(self.cadena,j)
                                                if res["result"]!=None:
                                                    ve+=1
                                                    numtoken+=1
                                                    try:
                                                        #self.tokens_usados.index(indext)
                                                        self.tokens_usados.append([numtoken,indext,j])
                                                    except:
                                                        #print("no hay")
                                                        self.tokens_usados.append(indext)
                                                    print(" | ",i," | ",self.columna," | ", j)
                                                    self.cadena=res["result"]
                                                    self.columna+=res["cont"]
                                                    Erid=0
                                                    Erthis=""
                                                    Ercont=0
                                                    Erpr=0
                                                    Ercol=0
                                                    if  indext==16:
                                                        encuentra=True
                                                        id=""
                                                        columna=0
                                                        while encuentra:
                                                            listencuentra=[]
                                                            
                                                            for e in self.Token_Id:
                                                                res=self.verificartoken(self.cadena,e)
                                                                if res["result"]!=None:
                                                                    
                                                                    id+=f"{e}"
                                                                    self.cadena=res["result"]
                                                                    columna+=res["cont"]
                                                                    Erid=0
                                                                else:
                                                                    listencuentra.append("false")

                                                            if len(listencuentra)==len(self.Token_Id):
                                                                numtoken+=1
                                                                self.tokens_usados.append([numtoken,21,id])
                                                                print(" | ",i," | ",self.columna," | ", id)
                                                                self.columna+=columna
                                                                Eriddef=1

                                                                encuentra=False
                                                        self.ids.append(j)
                                                        self.ids.append(id)
                                                    cont+=1
                                                else:
                                                    if t.index(j)==7 and ve==0:
                                                        return {"error":"Lexico","linea":i+1,"columna":self.columna,"token":"Etiqueta, Boton, Check, RadioBoton, Texto, AreaTexto, Clave, Contenedor","descrip":"Errores de ortografia en palabras reservadas"}
                                                    
                                    if area==1:
                                        if  indext==17 :
                                            ve=0
                                            for j in t:
                                                res=self.verificartoken(self.cadena,j)
                                                if res["result"]!=None:
                                                    numtoken+=1
                                                    ve+=1
                                                    try:
                                                        #self.tokens_usados.index(indext)
                                                        self.tokens_usados.append([numtoken,indext,j])
                                                    except:
                                                        #print("no hay")
                                                        self.tokens_usados.append(indext)
                                                    print(" | ",i," | ",self.columna," | ", j)
                                                    self.cadena=res["result"]
                                                    self.columna+=res["cont"]
                                                    Erid=0
                                                    Erthis=""
                                                    Ercont=0
                                                    Erpr=0
                                                    Ercol=0
                                                    if indext==17:
                                                        if j=="setGrupo":
                                                            vp=1
                                                        elif j=="setMarcada":
                                                            vp=2
                                                        elif j=="setAlineacion":
                                                            vp=3
                                                        elif j=="setTexto":
                                                            vp=4
                                                    cont+=1
                                                else:
                                                    if t.index(j)==7 and ve==0:
                                                        return {"error":"Lexico","linea":i+1,"columna":self.columna,"token":"setColorLetra, setTexto, setAlineacion, setColorFondo, setMarcada, setGrupo, setAncho, setAlto","descrip":"Errores de ortografia en palabras reservadas"}
                                                
                                    if area == 2:
                                        if  indext==20:
                                            ve=0
                                            for j in t:
                                                res=self.verificartoken(self.cadena,j)
                                                if res["result"]!=None:
                                                    ve+=1
                                                    numtoken+=1
                                                    try:
                                                        #self.tokens_usados.index(indext)
                                                        self.tokens_usados.append([numtoken,indext,j])
                                                    except:
                                                        #print("no hay")
                                                        self.tokens_usados.append(indext)
                                                    print(" | ",i," | ",self.columna," | ", j)
                                                    self.cadena=res["result"]
                                                    self.columna+=res["cont"]
                                                    Erid=0
                                                    Erthis=""
                                                    Ercont=0
                                                    Erpr=0
                                                    Ercol=0
                                                    if j=="add":
                                                            vp=1
                                                    cont+=1
                                                else:
                                                    if t.index(j)==1 and ve==0:
                                                        return {"error":"Lexico","linea":i+1,"columna":self.columna,"token":"setPosicion, add","descrip":"Errores de ortografia en palabras reservadas"}
                
                if len(self.lista_cadena)==i+1 and multic==1:
                    return {"error":"Lexico","linea":i+2,"columna":self.columna,"token":"*/","descrip":"Cadena incorrecta de caracteres"} 

                if Erid==2:
                    return {"error":"Lexico","linea":i+1,"columna":self.columna,"token":" ","descrip":"El Id no se encuentra definido"}                            
                                            
                if Erid==1:
                    if Ercol==1:
                        return {"error":"Lexico","linea":i+1,"columna":self.columna,"token":"Colocacion, colocacion","descrip":"Errores de ortografia en palabras reservadas"}
                    elif Erpr==1:
                        return {"error":"Lexico","linea":i+1,"columna":self.columna,"token":"Propiedades, propiedades","descrip":"Errores de ortografia en palabras reservadas"}
                    elif Erthis!="" :
                        return {"error":"Lexico","linea":i+1,"columna":self.columna,"token":Erthis,"descrip":"Errores de ortografia en palabras reservadas"}
                    else:
                        cadenaid=""
                        contcadena=0
                        for idc in self.ids:
                            if (self.ids.index(idc)%2)!=0:
                                if contcadena==0:
                                    cadenaid+=idc
                                else:
                                    cadenaid+=f", {idc}"
                                contcadena+=1
                        return {"error":"Lexico","linea":i+1,"columna":self.columna,"token":cadenaid,"descrip":"El ID no se encuentra definido"}
                if Ercont==1:
                    return {"error":"Lexico","linea":i+1,"columna":self.columna,"token":"Controles, controles","descrip":"Errores de ortografia en palabras reservadas "}
                       
        print("-------------------------------------------------------------")
        print("")

    def compilador(self,dir):
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
        print("----------------------------------------------------------------")
        print("                     ANALIZADOR LEXICO")
        print("----------------------------------------------------------------")

        e=self.analisis()
        
        if e==None:
            return {"error":None,"0":self.ids, "1":self.num, "2":self.text, "3":self.tokens_usados}
            #analizadorS.compilador1(self.ids, self.num, self.text)
        else:
            print(e)
            return e
            

        #return self.tokens_usados

"""
a=analizadorl()
resp=a.compilador("h")
if resp["error"]==None:
    b=analizadorS()
    resp1=b.compilador1("h",resp)
   
    if resp1["error"]==None:
        c=transformar()
        c.imprimir(resp1,"prueba1")
"""