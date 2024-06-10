# Importa a biblioteca win32com.client, que permite automação de tarefas do Windows, como interagir com o Outlook
import win32com.client as win32

# Cria um objeto que representa o aplicativo Outlook
outlook = win32.Dispatch('outlook.application')

# Cria um novo item de email no Outlook
emailOutlook = outlook.CreateItem(0)

email = "ana@gmail.com"
nome = "Ana"

# Define o destinatário do email
emailOutlook.To = email

# Define o assunto do email
emailOutlook.Subject = "Meu primeiro email usando Python e Outlook"


# Define o corpo do email em formato HTML
emailOutlook.HTMLBody = f"""
<p>Boa noite <b>{nome}</b>.</p>
<p><font color="red"><b><u>Esse é apenas um email de teste.</b></u></font></p>
<p><a href="https://www.google.com/">Clique aqui para acessar o nosso site.</a></p>
<p><img src="C:\\python_com_rpa_e_criacao_de_projeto_reais\\tech.jpg"></p>
<p>Atenciosamente.</p>
"""

# Salva o email no Outlook sem enviar
emailOutlook.save() # use emailOutlook.Send() para enviar o email

# emailOutlook.Send()# Enviar o email

