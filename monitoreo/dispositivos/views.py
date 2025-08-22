from django.shortcuts import render

# Create your views here.
def inicio(request):
    contexto = {"nombre": "dilan cortes"}
    productos = [{"nombre": "Sensor1", "Valor": 100},
                 {"nombre": "Sensor2", "Valor": 200},
                 {"nombre": "Sensor3", "Valor": 300}
    ]
    
    return render(request, "dispositivos/inicio.html", contexto)