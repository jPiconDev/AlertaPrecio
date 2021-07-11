# AlertaPrecio
Script que envía a telegram notificaciones de precios de un producto en seguimiento.

### ¿Que es AlertaPrecio?

AlertaPrecio es un pequeño script *(en fase de desarrollo)* que a partir de una url de un producto a la venta, éste nos avisa cuando se produce una bajada de precio por debajo de un importe determinado, enviándonos mensaje de telegram a un canal previamente configurado.

### ¿Cómo funciona?

Mediante python y web scrapping obtenemos datos de un determinado producto.

Luego nos comunicamos con la api de telegram para enviar dicha información.

### Pasos a seguir:

1. Obtener el token de nuestra cuenta de Telegram y el chat_id de un chat en el que recibir los mensajes.
2. Modificar el fichero .env con el token y chat_id obtenidos.
3. Modificar el script con la url del producto en cuestión. 
4. Ejecutar el script en un terminal.

### Detalle de lo pasos:

1. #### Obtener el token:

   Primero debemos buscar **BotFather** en la aplicación Telegram e iniciar un chat con él enviando **/start** , BotFather nos  responderá con una lista de comandos (que empiezan con **/**) que podemos utilizar. Ahora, al enviarle **/newbot**, nos guiará a través del proceso  de creación de un nuevo bot proporcionándole un nombre y @username (como un usuario humano de Telegram). Después de eso, BotFather nos  felicitará por crear un nuevo bot y nos enviará un token que se  utilizará junto con la API de Telegram Bot para controlar el  comportamiento de nuestro bot, debemos mantener este token en secreto porque quien tenga este código controla el bot .

   Ahora que hemos creado un bot, debemos hacerle saber quiénes somos.  Busque el bot usando el nombre de usuario del bot e inicia una  conversación con él, envíale un mensaje aleatorio como 'hola'.

   Luego usaremos el token proporcionado por BotFather para acceder a la  API de Telegram **/getUpdates** para recuperar nuestra identificación de  chat.

   ```
   # Envía una solicitud GET a la siguiente URL, o simplemente accede a ellos en el navegador
   https://api.telegram.org/bot<INSERT-TOKEN-HERE>/getMe
   
   # Después de eso, recibiremos una respuesta JSON como esta.
   {"ok":true,"result":{"id":0123456789,"is_bot":true,"first_name":"AlertaPrecioBot","username":"AlertaPrecio","can_join_groups":true,"can_read_all_group_messages":false,"supports_inline_queries":false}}
   
   # Nuestro id del chat es response.result.id
   En este caso sería 0123456789
   ```

2. #### Modificar el fichero .env

   Ahora necesitamos asignar a las variables correspondientes (**TOKEN** y **CHAT_ID**) los valores obtenidos anteriormente. El archivo .env mantiene guardada la información sensible para aislarla del código del script.

3. #### Modificar el script con la url del producto.

   Mediante web scrapping obtendremos una ruta a los datos que nos interesen. Necesitamos para ello instalar un script de Python que se encargará de ello.

   Lo instalamos con el siguiente comando:

   ```
   pipenv install requests python-dotenv beautifulsoup4
   ```

   Luego en el código asignamos a la constante **BASE_URL** como string la cabecera http, en este caso 'https://www.' y en la variable **items** la url  por cada producto copiada de la barra de direcciones del navegador. Como se trata de una lista separaremos cada artículo (string) con comas.

4. #### Ejecutar el script en un terminal.

   Ahora tan solo necesitamos ejecutar el script en un terminal. Mientras el script esté en ejecución estará consultando los precios y enviando un mensaje si es necesario.

   Podemos lanzar el script en segundo plano para dejar el terminal libre.

   ```shell
   jorge@jorge-Mint:~/Documentos/repos/AlertaPrecio_Public$ python3 AlertaPrecio/src/main.py &
   ```



### Fuentes e información útil.

- https://codeburst.io/price-tracking-with-telegram-bot-691d66ec7a37
- https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- https://core.telegram.org/bots/api#authorizing-your-bot

El script está configurado (parser) para la web de amazon pero puede utilizarse para cualquier web, solo es necesario ajustar el dato que necesitamos con BeutifulSoup a la web en cuestion.