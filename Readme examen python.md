# **Sistema de Gestión de Inventario para la Cafetería de Campuslands**

## 📝 **Descripción del Proyecto**

Este proyecto implementa un sistema de gestión de inventario para la  cafetería de Campuslands, enfocado en la administración de ingredientes  para la preparación de hamburguesas. El objetivo principal es solucionar los desafíos críticos relacionados con la gestión de ingredientes, como la falta de stock, el desperdicio de productos y la inconsistencia en  el servicio.

La implementación de este sistema automatizado busca proporcionar a los  chefs un control preciso y en tiempo real del inventario, optimizar la  toma de decisiones para la reposición de productos y, en consecuencia,  mejorar la eficiencia operativa, reducir costos y garantizar una  experiencia de alta calidad para los clientes.

## 🎯 **Problema a Solucionar**

La falta de un sistema de gestión de inventario eficiente y automatizado dificulta la capacidad de los Chefs para:

- 
- Satisfacer la demanda de los clientes de manera constante y oportuna.
- Mantener un seguimiento preciso de los ingredientes y su fecha de vencimiento.
- Minimizar el desperdicio de ingredientes y costos innecesarios.
- Tomar decisiones informadas sobre cuándo realizar pedidos de reposición.
- Garantizar una experiencia de cliente consistente y de alta calidad en sus platos.

## 🛠️ **Funcionalidades del Sistema**

El sistema está organizado en los siguientes módulos, cada uno con  funcionalidades específicas para la gestión integral de la cafetería.

### **Módulo de Ingredientes**

- 
- **Gestión Completa (CRUD):** Permite crear, leer, actualizar y eliminar ingredientes.
- **Información Detallada:** Almacena nombre, descripción, precio y stock de cada ingrediente.
- **Seguimiento de Historial:** Registra el uso de ingredientes para un mejor control.

### **Módulo de Categorías**

- 
- **Gestión Completa (CRUD):** Permite crear, leer, actualizar y eliminar las categorías de hamburguesas.
- **Información Detallada:** Almacena el nombre y la descripción de cada categoría (ej. "Clásica", "Vegetariana").

### **Módulo de Chefs**

- 
- **Gestión Completa (CRUD):** Permite crear, leer, actualizar y eliminar perfiles de los chefs.
- **Información Detallada:** Almacena el nombre y la especialidad de cada chef.

### **Módulo de Hamburguesas**

- 
- **Gestión Completa (CRUD):** Permite crear, leer, actualizar y eliminar hamburguesas del menú.
- **Información Detallada:** Almacena su nombre, categoría, lista de ingredientes, precio y el chef que la prepara.

## 🗃️ **Estructura de Datos (Archivos JSON)**

El sistema utiliza archivos JSON para almacenar la información de manera  organizada y persistente. A continuación se muestran ejemplos de la  estructura de datos:

**Ingredientes (ingredientes.json)**

Generated json



```
      [
    {
        "nombre": "Pan",
        "descripcion": "Pan de hamburguesa clásico",
        "precio": 2.5,
        "stock": 500
    },
    {
        "nombre": "Carne de res",
        "descripcion": "Carne de res jugosa y sabrosa",
        "precio": 8,
        "stock": 300
    },
    {
        "nombre": "Queso cheddar",
        "descripcion": "Queso cheddar derretido",
        "precio": 1.5,
        "stock": 200
    }
]
    
```

IGNORE_WHEN_COPYING_START



 Use code [with caution](https://support.google.com/legal/answer/13505487). Json

IGNORE_WHEN_COPYING_END

**Categorías (categorias.json)**

Generated json



```
      [
    {
        "nombre": "Clásica",
        "descripcion": "Hamburguesas clásicas y sabrosas"
    },
    {
        "nombre": "Vegetariana",
        "descripcion": "Hamburguesas sin carne, perfectas para vegetarianos"
    }
]
    
```

IGNORE_WHEN_COPYING_START



 Use code [with caution](https://support.google.com/legal/answer/13505487). Json

IGNORE_WHEN_COPYING_END

**Hamburguesas (hamburguesas.json)**

Generated json



```
      [
    {
        "nombre": "Clásica",
        "categoria": "Clásica",
        "ingredientes": ["Pan", "Carne de res", "Queso cheddar", "Lechuga", "Tomate"],
        "precio": 10,
        "chef": "ChefA"
    },
    {
        "nombre": "Doble Carne",
        "categoria": "Gourmet",
        "ingredientes": ["Pan de sésamo", "Doble carne de res", "Queso cheddar", "Bacon"],
        "precio": 12,
        "chef": "ChefC"
    }
]
    
```

IGNORE_WHEN_COPYING_START



 Use code [with caution](https://support.google.com/legal/answer/13505487). Json

IGNORE_WHEN_COPYING_END

**Chefs (chefs.json)**

Generated json



```
      [
    {
        "nombre": "ChefA",
        "especialidad": "Carnes"
    },
    {
        "nombre": "ChefB",
        "especialidad": "Cocina Vegetariana"
    }
]
    
```

IGNORE_WHEN_COPYING_START



 Use code [with caution](https://support.google.com/legal/answer/13505487). Json

IGNORE_WHEN_COPYING_END

## 📊 **Módulo de Reportes y Consultas**

Este módulo permite realizar consultas específicas sobre los datos  almacenados para facilitar la toma de decisiones estratégicas.

1. 
2. Encontrar todos los ingredientes con **stock menor a 400**.
3. Encontrar todas las hamburguesas de la categoría **“Vegetariana”**.
4. Encontrar todos los chefs que se especializan en **“Carnes”**.
5. Aumentar en **1.5** el precio de todos los ingredientes.
6. Encontrar todas las hamburguesas preparadas por **“ChefB”**.
7. Encontrar el **nombre y la descripción** de todas las categorías.
8. Eliminar todos los ingredientes que tengan un **stock de 0**.
9. Agregar un **nuevo ingrediente** a la hamburguesa “Clásica”.
10. Encontrar todas las hamburguesas que contienen **“Pan integral”** como ingrediente.
11. Cambiar la especialidad del “ChefC” a **“Cocina Internacional”**.
12. Encontrar el ingrediente **más caro**.
13. Encontrar las hamburguesas que **no contienen “Queso cheddar”** como ingrediente.
14. Incrementar el stock de “Pan” en **100 unidades**.
15. Eliminar las hamburguesas que contienen **menos de 5 ingredientes**.
16. Agregar un nuevo chef con especialidad en **“Cocina Asiática”**.
17. Listar las hamburguesas en **orden ascendente según su precio**.
18. Encontrar todos los ingredientes cuyo precio esté **entre $2 y $5**.
19. Actualizar la descripción del “Pan” a **“Pan fresco y crujiente”**.
20. Encontrar la hamburguesa más cara preparada por un chef especializado en **“Gourmet”**.
21. Listar todos los ingredientes junto con el **número de hamburguesas** que los contienen.