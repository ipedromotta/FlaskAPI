
class ResponseController():

    @staticmethod
    def get_response(status, nome_do_conteudo, conteudo, mensagem=False):
        try:
            body = {}
            body["status"] = status
            body[nome_do_conteudo] = conteudo

            if(mensagem):
                body["mensagem"] = mensagem
        except:
            body = {}

        return body
