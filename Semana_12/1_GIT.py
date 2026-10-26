''' 

GIT

Git guarda la historia de los cambios de tu proyecto
para que puedas saber qué cambió y volver a una versión anterior cuando sea necesario.


----------------------


Pero hay una distinción MUY importante
Git ≠ GitHub


Git → herramienta que controla/versiona tu código localmente.
GitHub → plataforma donde puedes almacenar y compartir repositorios Git remotamente.

GIT
📓 = historial/versiones de tu proyecto

GITHUB
☁️ = lugar remoto donde puedes guardar ese repositorio

git init

"Inicializa Git en esta carpeta."


Es decir, le estás diciendo a Git:
"Desde ahora quiero que empieces a controlar las versiones de este proyecto." 📓



Primero inicializas el repositorio. Después veremos cómo decirle a Git:
"Quiero que este cambio forme parte de la próxima versión."


git init
git status
git add -- pasar a staging “Este cambio lo quiero meter en el carrito para el próximo commit.” 
git commit -- “Ahora sí, guarda esta versión.”
---git commit -m "Primer commit"  - el -m significa message → mensaje 
---git commit -a "la opción -a significa --all." "Incluye automáticamente en el commit los archivos que Git ya está siguiendo y que fueron modificados."
---              "git commit -a -m "Actualizo (archivo)" e puedes saltar el git add
---git commit --amend - corregir ulimo commit para mensaje

---                 git add
                    → "quiero preparar estos cambios"
                    
                    git commit
                    → "guarda lo que está preparado"
                    
                    git commit -a
                    → "prepara automáticamente cambios de archivos YA SEGUIDOS
                    y luego haz el commit"

git push
git log --oneline  -----git log = muestra el historial de commits.
-                      -oneline = le dice a Git: Muéstramelo de forma resumida, una línea por commit."
-                      -consulta el historial
git log --oneline --graph --all ------ consulta el arbol de ramas ***

HEAD -> master ---  HEAD señala la versión/commit en la que estás actualmente parado.
--                  master → la rama en la que estoy , 
--                  git branch -- confirmar branches 
--                      -- ejemplo git branch prueba  - crea rama
--                      -- git checkout prueba     → me cambio a esa rama

git merge -  “Estoy en master y quiero incorporar los cambios que existen en branch.”
--           produce Fast-forward.

M = merge commit.

Hash =  es un identificador único que se le asigna a cada confirmación (commit) o cambio guardado en el repositorio

.gitignore = "Estos archivos/carpetas existen en mi computadora, pero NO quiero subirlos al repositorio."



'''



