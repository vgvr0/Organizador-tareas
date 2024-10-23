# 📝 PyTaskMaster

Una aplicación de gestión de tareas moderna y elegante construida con Python y Tkinter. Organiza tus tareas con categorías, prioridades y seguimiento de estado.

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## ✨ Características

- 📋 Gestión completa de tareas (Crear, Leer, Actualizar, Eliminar)
- 🎨 Categorización por tipos (Personal, Trabajo, Estudio, Hogar)
- 🚨 Sistema de prioridades (Alta, Normal, Baja)
- 📅 Seguimiento de fechas de creación
- 💾 Guardado automático en formato JSON
- 🎯 Estado de tareas (Pendiente/Completada)
- 🎨 Interfaz gráfica moderna con Tkinter
- 📱 Diseño responsive

## 🚀 Instalación

1. **Clona el repositorio**
```bash
git clone https://github.com/TU_USUARIO/pytaskmaster.git
cd pytaskmaster
```

2. **Verifica tu versión de Python**
```bash
python --version  # Debe ser 3.6 o superior
```

3. **Ejecuta la aplicación**
```bash
python taskmaster.py
```

## 💻 Uso

1. **Agregar una nueva tarea:**
   - Ingresa el título de la tarea
   - Selecciona la prioridad
   - Elige una categoría
   - Click en "Agregar Tarea"

2. **Gestionar tareas:**
   - Marca tareas como completadas
   - Elimina tareas no necesarias
   - Visualiza todas tus tareas organizadas

3. **Filtrar y ordenar:**
   - Ordena por cualquier columna
   - Filtra por estado o categoría
   - Busca tareas específicas

## 🛠️ Tecnologías

- **Python 3.6+**
- **Tkinter** - GUI toolkit
- **JSON** - Almacenamiento de datos
- **datetime** - Manejo de fechas

## 📁 Estructura del Proyecto

```
pytaskmaster/
│
├── taskmaster.py        # Archivo principal
├── tareas.json         # Almacenamiento de datos
├── README.md           # Documentación
└── LICENSE            # Licencia MIT
```

## 🤝 Contribuir

Las contribuciones son bienvenidas y apreciadas! Aquí está cómo puedes contribuir:

1. **Fork** el proyecto
2. Crea tu **Feature Branch** (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la Branch (`git push origin feature/AmazingFeature`)
5. Abre un **Pull Request**

## 📝 TODO

- [ ] Añadir fechas de vencimiento
- [ ] Implementar subtareas
- [ ] Agregar etiquetas personalizadas
- [ ] Sistema de recordatorios
- [ ] Temas visuales (claro/oscuro)
- [ ] Exportación a diferentes formatos
- [ ] Sincronización en la nube
- [ ] Filtros avanzados

## 🐛 Reporte de Bugs

Si encuentras un bug o tienes una sugerencia, por favor abre un issue:
[Crear Issue](https://github.com/TU_USUARIO/pytaskmaster/issues)

## 📜 Licencia

Este proyecto está bajo la licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 🙏 Agradecimientos

- Inspirado en metodologías de gestión de tareas como GTD
- Gracias a todos los contribuidores
- Comunidad Python/Tkinter por recursos y documentación
