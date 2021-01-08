from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion

class Execute(Instruccion):
    def __init__(self, id, parametros, strGram, linea, columna, strSent):
        Instruccion.__init__(self,None,linea,columna,strGram,strSent)
        self.id = id
        self.parametros = parametros

    def ejecutar(self, tabla, arbol):
        pass

    def traducir(self,tabla,arbol,cadenaTraducida):
        codigo = "\t" + self.id + "("
        if self.parametros is not None:
            for col in self.parametros:
                strSent = strSent + col.strSent + ","
            strSent = strSent[:-1]
        
        codigo += ")"
        return codigo