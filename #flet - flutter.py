# flet - flutter

# Passo a passo

# botao de iniciar chat

# popup para entrar no site

# quando entrar no site 

# aparecer a mensagem que voce entrou

# o campo e o botao de enviar mensagem

# a cada mensagem que voce envia 

# nome: texto da mensagem

# so funcionara ao vivo

# flet -> backend / frontend

# importar flet

# cria a função

# criação da pagina principal

# dicionario do python = { "produto: "iphone", "preço": 6000}


import flet as ft

def main(pagina):

    texto = ft.Text("crischat")

    chat = ft.Column()

    nome_usuario = ft.TextField(label="Escreva seu nome")

    def enviar_mensagem_tune1 (mensagem):
        
        tipo = mensagem ["tipo"]

        if tipo == "mensagem": 

            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]

            # adicionar a mensagem no chat

            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))

        else: 
            usuario_mensagem = mensagem["usuario"]

            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat", size=12,
                                italic=True, color=ft.colors.BLUE_900))



        # limpar o campo de mensagem

        pagina.update()

    # PUBLISH
    # SUBSCRIBE

    pagina.pubsub.subscribe(enviar_mensagem_tune1)    


    def enviar_mensagem(evento):

        pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value, 
                                "tipo": "mensagem"})
                   
      # limpar o campo de mensagem                 

        campo_mensagem.value = ""

        pagina.update()

 
    nome_usuario = ft.TextField(label="Escreva seu nome")
    campo_mensagem = ft.TextField(label="Digite uma mensagem", on_submit= enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click= enviar_mensagem)


    def entrar_popup(evento):

        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})


        # add o chat
        pagina.add(chat)

        # fechar o popup
        popup.open = False 
        pagina.update()

        # remover o botao iniciar chat
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
    
        # criar o campo de mensagem do usuario
        pagina.add(campo_mensagem)
      
        # criar o botao de enviar mensagem do usuario
        pagina.add(botao_enviar_mensagem)

        pagina.update()


    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao Crischat"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)],
        )


    def entrar_chat(evento):

        pagina.dialog = popup
        popup.open = True
        pagina.update()

        texto_entrou = ft.Text("Entrou no chat")
        pagina.add(texto_entrou)
        
    botao_iniciar = ft.ElevatedButton("iniciar chat", 
    on_click=entrar_chat)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER, port=8000)

# ipcondig
# Endereço IPv4. . . . . . . .  . . . . . . . : 192.168.43.62
# deploy 

192.168.43.62 -> hashtagtreinamentos.com/
