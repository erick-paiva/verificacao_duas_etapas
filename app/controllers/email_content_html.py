
HTML = """
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;400;600;700&family=Lilita+One&display=swap" rel="stylesheet">
    <title>Verification - Follow Events</title>
    <style type="text/css">
      body{
        align-content: center;
        align-items: center;
        background: #FFFFFF;
        border-radius: 10px;
        box-shadow: 0px 4px 4px rgb(0 0 0 / 25%);
        display: flex;
        flex-direction: column;
        flex-wrap: nowrap;
        font-family: 'Inter', sans-serif;
        height: max-content;
        justify-content: space-evenly;
        margin-left: auto;
        margin-right: auto;
        margin-top: 30px;
        max-width: 850px;
        padding: 30px;
      }
      h2{
        font-family: 'Lilita One', cursive; 
        font-weight: normal;
      }
      img{
        width: 120px;
      }
      p, h2{
        margin: 15px;
      }
      #code{
        color: #514BF2;
        font-size: 3.5rem;
        font-family: 'Lilita One', cursive; 
      }
      .main-content__text{
        display: flex;
        flex-direction: column;
        font-size: 1.2rem;
        justify-content: space-evenly;
        line-height: 32px;
      }
      
      .regards p {  
        margin: 0 15px;
      }
      footer{
        align-self: flex-start;      
        font-size: 10px;
        width: 100%;
      }
    </style>
  </head>
  <body>
    <img
      src="https://i.ibb.co/ctKDHyW/follow-events-logo.png"
      alt="Follow Events - Logo"
    />
    <main>
      <h2>Código de acesso:</h2>
      <p id="code">1234</p>
      <div class="main-content__text">
        <p>Olá, [user]!</p>
        <p>
          Por favor, volte para a página de alteração de senha e coloque o código
          acima para verificar a sua identidade.
        </p>
      <div class='regards'>
        <p>Sinceramente,</p>
        <p>Time do Follow Events</p>
      </div>
      </div>
    </main>
    <footer>
      <p>Esse email é enviado automaticamente e não precisa receber respostas.</p>
      <p>Precisa de ajuda? Nos contate através do email followevents.corp@gmail.com</a></p>
    </footer>
  </body>
</html>
"""
