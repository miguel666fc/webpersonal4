class Carro:
    def  __init__(self,request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        # Cuando el usuario se va de la pagina y vuelve no hay carro se crea entonces
        if not carro:
            carro=self.session["carro"]={}
        #else:  # aqui Cuando hay carro y el usuario sale de la pagina y vuelve y el carro funciona 
        self.carro=carro


      # aqui  se define para que le carrito pueda agregar productos
    def agregar(self,producto):
        # Aqui se agrega el producto por primera vez
        if(str(producto.id) not in self.carro.keys() ): # si no encuentras el  id del producto los agregas
            self.carro[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre_producto,
                "precio":str(producto.precio_venta),
                "cantidad":1,
                "imagen":producto.imagen.url,
            }
        else:
            for key,value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    break

        self.guardar_carro()

     # Guarda el producto en el carro   
    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True
    
    # Elimina lo que hay en el carrito
    def eliminar(self,producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
    
    # Resta los productos con los que hay en el carrito
    def restar_producto(self,producto):
         for key,value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]-1
                    if value["cantidad"]<1:
                        self.eliminar(producto)
                    break
         self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True








    







