<div align="center">

![Logotipo de PalworldSaveTools](https://github.com/deafdudecomputers/PalworldSaveTools/blob/main/resources/PalworldSaveTools_Blue.png)

# __TECNOLOGÍA_16__

**Un completo kit de herramientas de edición de archivos guardados para Palworld**

[![Descargas](https://img.shields.io/github/downloads/deafdudecomputers/PalworldSaveTools/total)](https://github.com/deafdudecomputers/PalworldTools/releases/latest)
[![Licencia](https://img.shields.io/github/license/deafdudecomputers/PalworldSaveTools)](LICENSE)
[![Discord](https://img.shields.io/badge/Discord-Join_for_support-blue)](https://discord.gg/sYcZwcT4cT)
[![NexusMods](https://img.shields.io/badge/NexusMods-Download-orange)](https://www.nexusmods.com/palworld/mods/3190)

[English](https://github.com/deafdudecomputers/PalworldSaveTools/blob/main/README.md) | [zh-CN](https://github.com/deafdudecomputers/PalworldSaveTools/tree/main/resources/readme/README.zh_CN.md) | [de-DE](https://github.com/deafdudecomputers/PalworldSaveTools/tree/main/resources/readme/README.de_DE.md) | [es-ES](https://github.com/deafdudecomputers/PalworldSaveTools/tree/main/resources/readme/README.es_ES.md) | [fr-FR](https://github.com/deafdudecomputers/PalworldSaveTools/tree/main/resources/readme/README.fr_FR.md) | [ru-RU](https://github.com/deafdudecomputers/PalworldSaveTools/tree/main/resources/readme/README.ru_RU.md) | [ja-JP](https://github.com/deafdudecomputers/PalworldSaveTools/tree/main/resources/readme/README.ja_JP.md) | [ko-KR](https://github.com/deafdudecomputers/PalworldSaveTools/tree/main/resources/readme/README.ko_KR.md)

---

### **Download the standalone version from [Lanzamientos GitHub](https://github.com/deafdudecomputers/PalworldSaveTools/releases/latest)**

---

</div>

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Tools Overview](#tools-overview)
- [Guides](#guides)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Features

### Funcionalidad principal

| Característica | Descripción |
| --------- | ------------- |
| **Análisis de guardado rápido** | Uno de los lectores de archivos guardados más rápidos disponibles |
| **Gestión de jugadores** | Ver, editar, cambiar nombre, cambiar nivel, desbloquear tecnologías y administrar jugadores |
| **Gestión del gremio** | Crea, cambia el nombre, mueve jugadores, desbloquea investigaciones de laboratorio y gestiona gremios. |
| **Amigo editor** | Editor completo para estadísticas, habilidades, IV, rango, almas, género, jefe/cambio de suerte |
| **Herramientas del campamento base** | Exportar, importar, clonar, ajustar radios y gestionar bases |
| **Visor de mapas** | Mapa interactivo de base y jugador con coordenadas y detalles. |
| **Transferencia de personaje** | Transferir personajes entre diferentes mundos/servidores (guardado cruzado) |
| **Guardar conversión** | Convertir entre formatos Steam y GamePass |
| **Configuración mundial** | Editar la configuración de WorldOption y LevelMeta |
| **Herramientas de marca de tiempo** | Corregir marcas de tiempo negativas y restablecer los tiempos de los jugadores. |

### Herramientas todo en uno

El paquete **Herramientas todo en uno** proporciona una gestión integral de guardado:

- **Herramientas de eliminación**
  - Eliminar Players, bases o gremios
  - Eliminar jugadores inactivos según los umbrales de tiempo
  - Elimina jugadores duplicados y gremios vacíos.
  - Eliminar datos sin referencia/huérfanos

- **Herramientas de limpieza**
  - Eliminar elementos no válidos/modificados
  - Eliminar amigos inválidos y pasivos
  - Corregir amigos ilegales (límite máximo de estadísticas legales)
  - Eliminar estructuras no válidas
  - Restablecer torretas antiaéreas
  - Desbloquear cofres privados

- **Herramientas del gremio**
  - Reconstruir todos los gremios
  - Mover jugadores entre gremios
  - Hacer líder del gremio de jugadores
  - Cambiar el nombre de los gremios
  - Nivel máximo de gremio
  - Desbloquear toda la investigación de laboratorio

- **Herramientas del jugador**
  - Editar estadísticas y habilidades de amigos jugadores
  - Desbloquear todas las tecnologías
  - Desbloquear la jaula de visualización
  - Subir/bajar jugadores de nivel
  - Cambiar el nombre de los jugadores

- **Guardar utilidades**
  - Restablecer misiones
  - Reiniciar mazmorras
  - Corregir marcas de tiempo
  - Recortar inventarios sobresaturados
  - Generar comandos PalDefender

### Herramientas adicionales

| Herramienta | Descripción |
| ------ | ------------- |
| **Editar amigos jugadores** | Editor de amigos completo con estadísticas, habilidades, IV, talentos, almas, rango y género. |
| **SteamID Convertidor** | Convierta los ID de Steam a Palworld UIDs |
| **Reparar el guardado del host** | Intercambiar UIDs entre dos jugadores (por ejemplo, para intercambio de host) |
| **Intercambiar jugador UIDs** | Intercambia UIDs entre dos jugadores |
| **Inyector de ranura** | Aumentar espacios de palbox por jugador |
| **Restaurar mapa** | Aplicar el progreso del mapa desbloqueado en todos los mundos/servidores. |
| **Cambiar nombre del mundo** | Cambiar nombre mundial en LevelMeta |
| **WorldOption Editor** | Editar ajustes y configuración del mundo |
| **LevelMeta Editor** | Editar metadatos mundiales (nombre, host, nivel) |
| **Convertidor de coordenadas** | Convertir coordenadas en el juego |

---

## Installation

### Requisitos previos

**Para independiente (Windows):**
- __TECNOLOGÍA_10__ 10/11
- [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#latest-microsoft-visual-c-redistributable-version) (2015-2022)

**Para ejecutar desde el código fuente (Linux o desarrollo):**
- Python 3.10 o superior
- pip (Python administrador de paquetes)

### Independiente (Windows - Recomendado)

1. Descargue la última versión de [GitHub Releases](https://github.com/deafdudecomputers/PalworldSaveTools/releases/latest)
2. Extrae el archivo zip
3. Ejecute `PalworldSaveTools.exe`

### De la fuente (Linux o para desarrollo)

```bash
git clone https://github.com/deafdudecomputers/PalworldSaveTools.git
cd PalworldSaveTools
pip install -r requirements.txt
python start.py
```

---

## Quick Start

1. **Carga tu guardado**
   - Haga clic en **Archivo → Cargar Guardar**
   - Navegue a su carpeta de guardado Palworld
   - Seleccione `Level.sav`

2. **Explore sus datos**
   - Utilice las pestañas para ver Players, gremios, bases o el mapa.
   - Busque y filtre para encontrar entradas específicas

3. **Hacer cambios**
   - Seleccionar elementos para editar, eliminar o modificar
   - Utilice menús contextuales para opciones adicionales

4. **Guarde sus cambios**
   - Haga clic en **Archivo → Guardar cambios**
   - Las copias de seguridad se crean automáticamente

---

## Descripción general de las herramientas

### Herramientas todo en uno (AIO)

La interfaz principal para una gestión integral de guardados con tres pestañas:

**Players Tab** - Ver y administrar todos los jugadores en el servidor
- Editar nombres de jugadores, niveles y recuentos de amigos.
- Eliminar jugadores inactivos
- Ver gremios de jugadores y el último tiempo en línea

**Pestaña Gremios** - Administrar gremios y sus bases
- Cambiar el nombre de los gremios, cambiar los líderes
- Ver ubicaciones y niveles de bases
- Eliminar gremios vacíos o inactivos

**Pestaña Bases** - Ver todos los campamentos base
- Exportar/importar planos base
- Clonar bases a otros gremios.
- Ajustar el radio de la base

### Visor de mapas

Visualización interactiva de tu mundo:
- Ver todas las ubicaciones de las bases y posiciones de los jugadores.
- Filtrar por gremio o nombre de jugador
- Haga clic en los marcadores para obtener información detallada.
- Generar comandos `killnearestbase` para PalDefender

### Transferencia de personajes

Transferir personajes entre diferentes mundos/servidores (guardado cruzado):
- Transferir uno o todos los jugadores
- Conserva personajes, amigos, inventario y tecnología.
- Útil para migrar entre cooperativo y dedicated servers

### Reparar host Guardar

Intercambia UIDs entre dos jugadores:
- Transferir el progreso de un jugador a otro
- Esencial para transferencias de host/co-op al servidor
- Útil para intercambiar roles de anfitrión entre jugadores.
- Útil para cambios de plataforma (Xbox ↔ Steam)
- Resuelve problemas de asignación de host/servidor UID
- **Nota:** Affected player must have a character created on the target save first

---

## Guías

### Guardar ubicaciones de archivos

**Anfitrión/Cooperativo:**
```
%localappdata%\Pal\Saved\SaveGames\YOURID\RANDOMID\
```

**Servidor Dedicado:**
```
steamapps\common\Palworld\Pal\Saved\SaveGames\0\RANDOMSERVERID\
```

### Desbloqueo del mapa

<detalles>
<summary>Haga clic para ampliar las instrucciones de desbloqueo del mapa</summary>

1. Copia `LocalData.sav` de `src\resources\`
2. Encuentra tu carpeta de guardado de servidor/mundo
3. Reemplace el `LocalData.sav` existente con el archivo copiado
4. Inicie el juego con un mapa completamente desbloqueado.

> **Nota:** Utilice la opción **Herramientas → Restaurar mapa** en PST para aplicar el mapa desbloqueado a TODOS sus mundos/servidores a la vez con copias de seguridad automáticas.

</detalles>

### Host → Transferencia de servidor

<detalles>
<summary>Haga clic para expandir la guía de transferencia de host a servidor</summary>

1. Copie las carpetas `Level.sav` y `Players` desde el guardado del host
2. Pegar en la carpeta de guardado dedicated server
3. Iniciar servidor, crear un nuevo personaje.
4. Espere a que se guarde automáticamente y luego cierre
5. Utilice **Fix Host Save** para migrar GUIDs
6. Copie los archivos y ejecútelos

**Utilizando Fix Host Save:**
- Seleccione `Level.sav` de su carpeta temporal
- Elija el **carácter antiguo** (del guardado original)
- Elige el **nuevo personaje** (que acabas de crear)
- Haga clic en **Migrar**

</detalles>

### Intercambio de host (cambio de host)

<detalles>
<summary>Haga clic para expandir la guía de intercambio de host</summary>

**Fondo:**
- El anfitrión siempre usa `0001.sav`: el mismo UID para quien sea el anfitrión
- Cada cliente utiliza un guardado UID único y regular (por ejemplo, `123xxx.sav`, `987xxx.sav`)

**Requisitos previos:**
Ambos jugadores (antiguo anfitrión y nuevo anfitrión) deben generar sus partidas guardadas habituales. Esto sucede al unirse al mundo del anfitrión y crear un nuevo personaje.

**Pasos:**

1. **Asegúrese de que existan guardados regulares**
   - El jugador A (antiguo anfitrión) debe tener un guardado regular (por ejemplo, `123xxx.sav`)
   - El jugador B (nuevo anfitrión) debe tener un guardado regular (por ejemplo, `987xxx.sav`).

2. **Cambiar el guardado del host anterior al guardado normal**
   - Utilice PalworldSaveTools **Fix Host Save** para intercambiar:
   - `0001.sav` del antiguo host → `123xxx.sav`
   - (Esto mueve el progreso del antiguo anfitrión del puesto de anfitrión al puesto de jugador habitual)

3. **Cambiar el guardado habitual del nuevo anfitrión por el guardado del anfitrión**
   - Utilice PalworldSaveTools **Fix Host Save** para intercambiar:
   - `987xxx.sav` → `0001.sav` del nuevo host
   - (Esto mueve el progreso del nuevo anfitrión al espacio de anfitrión)

**Resultado:**
- El jugador B ahora es el anfitrión con su propio personaje y amigos en `0001.sav`
- El jugador A se convierte en cliente con su progreso original en `123xxx.sav`

</detalles>

### Exportación/Importación básica

<detalles>
<summary>Haga clic para expandir la guía básica de exportación/importación</summary>

**Exportando una Base:**
1. Carga tu guardado en PST
2. Ir a la pestaña Bases
3. Haga clic derecho en una base → Exportar base
4. Guardar como archivo `.json`

**Importando una base:**
1. Vaya a la pestaña Bases o al Visor de mapas base
2. Haga clic derecho en el gremio al que desea importar la base.
3. Seleccione Importar base
4. Seleccione su archivo `.json` exportado

**Clonación de una base:**
1. Haga clic derecho en una base → Clonar base
2. Seleccionar gremio objetivo
3. La base se clonará con posicionamiento desplazado.

**Ajuste del radio de la base:**
1. Haga clic derecho en una base → Ajustar radio
2. Ingrese un nuevo radio (50% - 1000%)
3. Guarde y cargue el guardado en el juego para las estructuras que se van a reasignar.

</detalles>

---

## Troubleshooting

### "No se encontró VCRUNTIME140.dll"

**Solution:** Install [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#latest-microsoft-visual-c-redistributable-version)

### `struct.error` when parsing save

**Causa:** Formato de archivo guardado desactualizado

**Solución:**
1. Cargue el guardado en el juego (modo Solo, Cooperativo o Servidor Dedicado)
2. Esto desencadena una actualización automática de la estructura.
3. Asegúrate de que el guardado se haya actualizado a partir del último parche del juego.

### El convertidor GamePass no funciona

**Solución:**
1. Cierre la versión GamePass de Palworld
2. Espera unos minutos
3. Ejecute el convertidor Steam → GamePass
4. Inicie Palworld en GamePass para verificar

---

## Construyendo desde la fuente

```bash
# Clone the repository
git clone https://github.com/deafdudecomputers/PalworldSaveTools.git

# Install dependencies
pip install -r requirements.txt

# Run the application
python start.py
```

Para crear el ejecutable independiente, utilice el script de compilación:
```bash
python scripts/build.py
```

---

## Contributing

¡Las contribuciones son bienvenidas! No dude en enviar una solicitud de extracción.

1. Bifurcar el repositorio
2. Crea tu rama de funciones (`git checkout -b feature/AmazingFeature`)
3. Confirme sus cambios (`git commit -m 'Agregar alguna característica increíble'`)
4. Empujar a la rama (`git push origin feature/AmazingFeature`)
5. Abrir una solicitud de extracción

---

## Descargo de responsabilidad

**Utilice esta herramienta bajo su propia responsabilidad. Siempre haga una copia de seguridad de sus archivos guardados antes de realizar modificaciones.**

Los desarrolladores no son responsables de ninguna pérdida de datos guardados o problemas que puedan surgir al utilizar esta herramienta.

---

## Apoyo

- **__TECNOLOGÍA_20__:** [Join us for support, base builds, and more!](https://discord.gg/sYcZwcT4cT)
- **GitHub Problemas:** [Report a bug](https://github.com/deafdudecomputers/PalworldSaveTools/issues)
- **Documentación:** [Wiki](https://github.com/deafdudecomputers/PalworldSaveTools/wiki) *(Currently in development)*

---

## Licencia

Este proyecto tiene la licencia MIT License; consulte el archivo [LICENSE](LICENSE) para obtener más detalles.

---

## Agradecimientos

- **__TECNOLOGÍA_29__** developed by Pocketpair, Inc.
- Gracias a todos los contribuyentes y miembros de la comunidad que han ayudado a mejorar esta herramienta.

---

<div align="center">

**Hecho con ❤️ para la comunidad Palworld**

⬆ Volver arriba

</div>
