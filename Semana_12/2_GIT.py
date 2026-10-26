'''

REMOTE***

Un remote es básicamente una referencia que le dice a tu repositorio local:
"Existe otro repositorio Git en otro lugar con el que puedo comunicarme."

git remote add origin URL = “Git, guarda que existe un repositorio remoto llamado origin y que está en esta dirección.” 

PUSH***

git push origin master = “Envía los commits de mi rama local master al repositorio remoto identificado como origin.”

--------

Parte	Significado
git	usamos Git
push	enviar cambios al remoto
origin	nombre del remoto
master	rama que queremos enviar

-----

origin no es el servidor. Es el nombre que tiene guardado localmente la referencia al servidor/repositorio remoto.

PULL***

git pull origin master = Traer al repositorio local los cambios que están en el remoto.   


             🌐 GITHUB
              /     \
             /       \
        push ↑         ↓ pull
           /             \
          /               \
     💻 TU PC          💻 OTRO PC

-----------------------------------------
Conceptualmente, pull hace dos cosas:
git pull
   ↓
fetch
   ↓
integrar los cambios
----------------------------------------

CLONE***

git clone URL = Crea una copia local del repositorio y trae también su historial Git.

                    🌐 GITHUB
                       │
                 REPOSITORIO REMOTO
                       │
              ┌────────┴────────┐
              │                 │
           git pull          git clone
              ↓                 ↓
       💻 REPO LOCAL      💻 NUEVO PC
              │
              │ git push
              └──────────────→ 🌐

Y origin = nombre de la referencia al remoto


ORIGIN***

git remote -v = nos muestra los remotos configurados y sus URLs.

                Por ejemplo, podríamos ver:
                            origin  https://github.com/usuario/AI-Engineer-Bootcamp.git (fetch)
                            origin  https://github.com/usuario/AI-Engineer-Bootcamp.git (push)

FETCH VS PUSH ***

origin
 ├── fetch → traer información/cambios
 └── push  → enviar cambios    

 
la ruta exacta de la raíz de tu repositorio Git. ***

***git rev-parse --show-toplevel  == devuelve la ruta raíz del repositorio Git, es decir, donde está la carpeta .git.


***Get-ChildItem -Force = Muestra todos los archivos y carpetas.
   Ese d--h-- significa que .git es una carpeta oculta (d = directory, h = hidden).

*** Move-Item .git ..\..\ = Mueve la carpeta .git dos niveles hacia arriba.







'''