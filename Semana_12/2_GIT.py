'''

REMOTE***

Un remote es básicamente una referencia que le dice a tu repositorio local:
"Existe otro repositorio Git en otro lugar con el que puedo comunicarme."

git remote add origin URL = “Git, guarda que existe un repositorio remoto llamado origin y que está en esta dirección.” 

git remote -v =  -v Significa verbose = mostrar información más detallada.
-----
git
Le dices a Git que vas a ejecutar un comando.
remote
Significa remoto. Trabaja con los repositorios externos conectados a tu repositorio local.
-----
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

*** Move-Item .git ..\.\ = Mueve la carpeta .git dos niveles hacia arriba.

*** git diff --cached --stat =  Ese comando no modifica nada. Solo nos muestra un resumen de lo que está preparado en staging. 


*** mkdir  = mkdir viene de make directory:

        mkdir Git-Prueba - 

*** cd ..\..\AI-Engineer-Bootcamp
        subimos:
            1. .. → Git-Prueba
            2. .. → Desktop
            3. AI-Engineer-Bootcamp → repositorio original
           
***pwd = confirma el camino donde estamos 

***New-Item README.md -ItemType File = crea nevo noead readme 

*** git diff muestra los cambios que tienes en tu working tree y que todavía NO están en staging.

*** git diff --cached
        ↓
Cambios que YA están staged

*** git diff  → comparar cambios.
            --cached → mirar lo que ya está en staging.
            --stat → mostrar solamente estadísticas/resumen.




como se ediaria ejemplo

        Editar archivo
     ↓
git diff              ← ¿qué cambié?
     ↓
git add
     ↓
git diff --cached     ← ¿qué voy a guardar?
     ↓
git commit
     ↓
git push

El + en git diff significa:
Esta línea existe en tu versión actual, pero no existía en la versión anterior que Git está comparando.

Y el otro símbolo importante es:
- línea eliminada
+ línea agregada


U  = Untracked
M  = Modified
staged = Changes to be committed






'''