from rest_framework.response import Response
from utils.permissions import IsRememberAccount
from rest_framework import status
from utils.response import RememberResponse
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

class TermView(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def list(self, request, pk=None):
        body = {
            "title": "Os termos de Condições de Uso e Política de Privacidade",
            "items": [
                TermItem(
                    title="Um dos pontos mais importantes para nós da equipe Remember é manter viva os momentos que os nossos usuários possuem com as pessoas importantes da vida deles e para continuarmos fazendo isso, é necessário que você aceite os termos do Remember, para que continue compartilhando os momentos importantes com a sua familía."
                ).toJson(),
                TermItem(
                    title="Termos de Condiçõs de Uso",
                    description="Ao instalar ou ao utilizar o Remember, esses termos serão aplicados a você, é recomendado ler os termos antes de aceitar e continuar utilizando o aplicativo.\nNão é permitido copiar ou modificar o aplicativo ou apenas parte do aplicativo de forma alguma. É permitido fazer uma copia para fins de aprendizado, caso você for um desenvolvedor de aplicativos Mobile ou Web."
                ).toJson(),
                TermItem(
                    title="Idade para utilizar",
                    items= [
                        TermItem(
                            description="É necessário possuir 13 anos ou mais para utilizar o Remember, caso possuir menos que 13 anos não será possível criar uma conta."
                        ).toJson()
                    ],
                    type="Expandable"
                ).toJson(),
                TermItem(
                    title="Uso aceitável do Remember",
                    items= [
                        TermItem(
                            description="Nossos Serviços devem ser acessados e utilizados somente para fins lícitos, autorizados e aceitáveis. Você não usará (ou ajudará outras pessoas a usar) nossos Serviços: (a) de forma a violar, apropriar-se indevidamente ou infringir direitos do Remember, dos nossos usuários ou de terceiros, inclusive direitos de privacidade, de publicidade, de propriedade intelectual ou outros direitos de propriedade; (b) de forma ilícita, obscena, difamatória, ameaçadora, intimidadora, assediante, odiosa, ofensiva em termos raciais ou étnicos, ou que instigue ou encoraje condutas que sejam ilícitas ou inadequadas, como a incitação a crimes violentos, a exploração de crianças ou outras pessoas, a ação de colocá-las em perigo, ou a coordenação de danos reais; (c) envolvendo declarações falsas, incorretas ou enganosas; (d) para se passar por outra pessoa; (e) para enviar comunicações ilícitas ou não permitidas, mensagens em massa, mensagens automáticas, ligações automáticas e afins; ou (f) de forma a envolver o uso não pessoal dos nossos Serviços, a menos que esteja autorizado por nós."
                        ).toJson(),
                        TermItem(
                            description="Ao utilizar o remember de formas não aceitáveis, a equipe Remember vai analisar o caso e dependendo da gravidade, suspender ou até mesmo banir a conta do usuário."
                        ).toJson()
                    ],
                    type="Expandable"
                ).toJson(),
                TermItem(
                    title="\n\nPolítica de Privacidade"
                ).toJson(),
                TermItem(
                    title="Idade",
                    items=[
                        TermItem(
                            description="Para utilizar o remember é nessário ter uma idade mínima de 13 anos, caso não tiver essa idade mínima, é necessário que os seus pais ou responsáveis leiam e aceitam o termo."
                        ).toJson()
                    ],
                    type="Expandable"
                ).toJson(),
                TermItem(
                    title="Registro",
                    items=[
                        TermItem(
                            description="Para registrar uma conta no remember, é necessário passar poucas informações, essas que utilizamos apenas para entender os usuário que a rede Remember possui.\nCaso for a vontade do cliente, podemos remover quase todas essas informações, excluindo email e usuário."
                        ).toJson()
                    ],
                    type="Expandable"
                ).toJson(),
                TermItem(
                    title="Dados que coletamos",
                    items=[
                        TermItem(
                            description="O Remember coleta os dados necessários para que você possa utilizar as funcionalidades do aplicativo e dados sobre a sua utilização do nosso aplicativo, com fins de melhorar a experiência do Remember e poder mostrar anúncios que fazem sentido.\nEm seguida, mostraremos os dados que você nos fornece e os dados que coletamos automaticamente."
                        ).toJson(),
                        TermItem(
                            title="Dados fornecidos pelo usuário",
                            sub_title="Dados da sua conta:",
                            description="Para criar a sua conta, você precisa passar alguns dados como: nome, email, apelido, gênero, idade, senha e usuário.\nEssas informações ficam armazenadas no nosso sistema, a sua senha é armazenada já encriptografada e não temos acesso a ela, para ser utilizadas(exceto a senha) para mostrar anuncios que fazem sentido para os nossos usuários. "
                        ).toJson(),
                        TermItem(
                            sub_title="Comentários em momentos:",
                            description="Os comentários feitos em momentos são armazenados no nosso sistema apenas para serem mostrada para os usuários, não utilizamos esses textos para nenhuma outra objetivo."
                        ).toJson(),
                        TermItem(
                            sub_title="Momentos de Mídias:",
                            description="Quando o usuário cria um momento que possui uma mídia, como fotos, essas mídias são armazenadas no nosso sistema e os únicos individuos que tem acesso a essas mídias são os membros da memory line onde foi criado o momento. É feito acesso via aplicativo dessas imagens por uma url que serve apenas para uma mídia e que dura até 1 hora o acesso."
                        ).toJson(),
                        TermItem(
                            sub_title="Memory Lines e tipos de Memory Lines:",
                            description="Para o usuário criar uma memory line, é necessário ele criar um tipo de memory line. Quando um usuário cria uma memory line e um tipo de memory line, ele nos informa quais são os interesses deles e qual a prioridade do interesse dele ao ordenar os tipos, com essa informação utilizamos para mostrar anúncios que fazem sentido para o usuário. "
                        ).toJson(),
                        TermItem(
                            title="Dados que coletamos:",
                            sub_title="Dados de uso:",
                            description="Coletamos dados sobre sua atividade em nossos Serviços, como a quantidade de tempo que utiliza, os pontos onde mais e menos utiliza, quantidade de anuncios que assiste e se esse anúncio foi util para você. Também coletamos informações sobre as pessoas que você está conectado através das suas memory lines, os momentos que compartilham e a localização deles."
                        ).toJson(),
                        TermItem(
                            sub_title="Dados do dispositivo:",
                            description="Coletamos dados do sistema operacional que utiliza, de qual dispositivo está utilizando, o desempenho que o remember está tendo no seu aplicativo e em quais telas o desempenho está pior para melhorarmos a experiência do usuário."
                        ).toJson()
                    ],
                    type="Expandable"
                ).toJson(),
                TermItem(
                    title="Como utilizamos os dados",
                    items=[
                        TermItem(
                            description="Utilizamos os dados que você fornece e que coletamos apenas para melhorar a experiência do remember como um todo. Apenas utilizamos os dados com o seu consentimento."
                        ).toJson(),
                        TermItem(
                            sub_title="Nossos serviços:",
                            description="Coletamos os dados para poder continuar operando o Remember, que hoje é disponibilizado de forma gratuita. Coletamos também para continuar mantendo a qualidade do Remember e para sempre melhorar a experiência que o usuário tem com os nossos serviços."
                        ).toJson(),
                        TermItem(
                            sub_title="Segurança:",
                            description="Segurança é uma parte fundamental do Remember e utilizamos os dados coletados para proteger os nossos usuário. Através dos dados podemos verificar contas e atividades, localizar e combater condutas nocivas na nossa rede e proteger o usuário de experiências ruins.\nUtilizamos também para detectar usuários que violaram os termos do Remember e aplicar as punições definidas nos termos."
                        ).toJson(),
                    ],
                    type="Expandable"
                ).toJson()
            ]
        }
        return Response(body, status=status.HTTP_200_OK)

class TermItem:
    def __init__(self, title = None, sub_title = None, description = None, type = "Normal", items = []):
        self.title = title
        self.sub_title = sub_title
        self.description = description
        self.type = type
        self.items = items

    def toJson(self):
        return {
            "title": self.title,
            "sub_title": self.sub_title,
            "description": self.description,
            "type": self.type,
            "items": self.items
        }