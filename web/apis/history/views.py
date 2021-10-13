from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

class HistoryView(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def list(self, request, pk=None):
        bandtecMoment = {
            "id": "28fa0453-eb1323239-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/bandtec.jpg",
            "description": "A História do Remember se iniciou na Bandtec, uma faculdade brasileira de Tecnologia.",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        groupOneMoment = {
            "id": "28fa0453-eb19-44a73-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg",
            "description": "Cada semestre da faculdade, temos um projeto do semestre e a partir do terceiro semestre, os alunos podem escolher os integrantes do grupo e obviamente eu e meus amigos montamos um grupo.",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        rememberOneMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/remember_1.jpeg",
            "description": "E o nosso amigo, Rodolfo, carinhosamente apelidado de idoso",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        rememberTwoMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/remember_2.PNG",
            "description": "Teve a ideia de criar uma rede social diferente das demais, onde você poderia guardar os momentos da sua vida e compartilhar com as pessoas que realmente importam.",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        rememberThreeMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/remember_3.PNG",
            "description": "Esses momentos ficariam em linhas do tempo, e o usuário iria poder ter quantas linhas do tempo quiser, ajudando a guardar os momentos que teve e ainda poderia convidar pessoas para participar das linhas do tempo e construírem junto.",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        rememberFourMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/remember_4.PNG",
            "description": "E pensamos em chamar essa rede social de Remember",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        rememberFiveMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/remember_5.jpeg",
            "description": "E ficamos apaixonados pela ideia, porque a gente sempre tirou fotos nos nossos roles e as fotos acabavam ficando perdidas nas nossas galerias.",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        groupTwoMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_2.jpeg",
            "description": "Antes de continuamos, não poderíamos deixar de falar de cada um dos nossos integrantes fodas, sem eles, o Remember não seria possível.",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        ruizOneMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/ruiz_1.jpeg",
            "description": "O Ruiz, nosso programador que mexe com tudo e manja demais.",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        ruizTwoMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/ruiz_2.jpeg",
            "description": "Até mesmo quando ele está conversando a gente, ele ainda continuava focado na programação...",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        rodolfoOneMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/rodolfo_1.jpg",
            "description": "O Rodolfo, como disse antes, o nosso querido idoso do Time, programador fullstack que ama Django(a Framework, não o Filme)",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        rodolfoTwoMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/rodolfo_2.PNG",
            "description": "O Rei do Xadrez e Dama, que não ficou feliz quando perdeu para a Juliana no Xadrez",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        yudiOneMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/pp.jpg",
            "description": "Temos o nosso mestre do PowerPoint e Design, Yudi, nosso DBA e Frontend Web junto com o Ruiz",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        yudiTwoMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/yudi_2.PNG",
            "description": "E uma das poucas coisas que ele gosta mais que o Seinenkai, é o Ep 19 do Kimetsu no Yaiba.",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        juOneMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/ju_1.PNG",
            "description": "Temos também a Juliana, QA do Time, que manja bastante de testes. E também sabe desenhar bastante",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        juTwoMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/ju_2.PNG",
            "description": "Ela é muito viciada em games, principalmente League of Legends e formos nós que a incentivamos para entrar nesse mundo que o League of Legends",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        lucasOneMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/lucas_1.jpeg",
            "description": "Temos o Lucas, que apesar de não poder participar da criação do Remember na Faculdade(já que ele era de outra sala), é um grande amigo nosso e que sempre deu feedback sobre como está o App e o Site do Remember.",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        lucasTwoMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/lucas_2.png",
            "description": "E ele tem a cachorra mais fofa que existe",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        viniOneMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/vinicius_1.jpg",
            "description": "E por último, tem eu, o Vinicius, sou o desenvolvedor Android do Time e sim, se você tiver um problema com o App, pode colocar a culpa em mim.",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        viniTwoMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/vinicius_2.jpg",
            "description": "Até hoje tento achar alguém que já leu Mistborn no brasil e até agora não achei. Caso você já tenha lido, vamos criar uma Linha do Tempo junto e compartilhas os momentos incríveis dessa saga de livros",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        developmentOneMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/desenvolvimento_1.jpg",
            "description": "E agora vamos falar do desenvolvimento do Remember",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        developmentTwoMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/desenvolvimento_2.jpeg",
            "description": "Posso dizer que teve muita programação.",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        developmentThreeMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/desenvolvimento_3.jpeg",
            "description": "Muitas discussões das nossas ideias para o projeto",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        developmentFourMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/desenvolvimento_4.PNG",
            "description": "Muito design também das telas",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        developmentFiveMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/desenvolvimento_5.PNG",
            "description": "E não só Mobile, Web também.",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        developmentSixMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/desenvolvimento_6.jpeg",
            "description": "E quando acabou o semestre, tínhamos uma versão alpha do Remember funcionando na Web.",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        developmentSevenMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/desenvolvimento_7.jpg",
            "description": "E no quarto semestre, iriamos melhorar o que já tínhamos construído, principalmente a versão do App(que estava bem feia naquela época).",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        groupThreeMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_3.jpeg",
            "description": "E no quarto semestre(último da faculdade e que aconteceu no começo da pandemia), fizemos isso, melhoramos o que já tínhamos e terminamos a faculdade com algo que realmente nos dava orgulho.",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        continuedMoment = {
            "id": "28fa0453-eb139-44a7-a569-c5ed2e97a868",
            "file": "https://remember-history.s3.amazonaws.com/memory-line-history/continue.jpg",
            "description": "Agora que acabou a faculdade, temos planos bem grandes para o Remember e espero que a história do Remember só esteja começando.",
            "owner": {
                "id": "lsajkdlaks",
                "photo": "https://remember-history.s3.amazonaws.com/memory-line-history/grupo_1.jpg"
            },
            "comments_count": 0,
            "memory_line": "b5f962f1-8fe7-45d7-a665-4eb8346b2bcf",
            "pub_date": "2020-06-15T22:17:47.303153-03:00",
            "updated_at": "2020-06-15T22:17:47.303153-03:00"
        }

        body = [
            bandtecMoment, groupOneMoment, rememberOneMoment, rememberTwoMoment, rememberThreeMoment, rememberFourMoment, rememberFiveMoment,
            groupTwoMoment, ruizOneMoment, ruizTwoMoment, rodolfoOneMoment, rodolfoTwoMoment, yudiOneMoment, yudiTwoMoment, juOneMoment, juTwoMoment, lucasOneMoment, lucasTwoMoment,
            viniOneMoment, viniTwoMoment, developmentOneMoment, developmentTwoMoment, developmentThreeMoment, developmentFourMoment, developmentFiveMoment, developmentSixMoment,
            developmentSevenMoment, groupThreeMoment, continuedMoment
        ]
        return Response(body, status=status.HTTP_200_OK)

class HistoryParticipantsView(viewsets.ViewSet):
    """
    """
    permission_classes = (AllowAny,)

    def list(self, request, pk=None):
    
        vini = {
            "id": "asdsadsadsadsadasd",
            "owner": False,
            "participant": {
                "id": "lsajdlas",
                "photo": "https://remember-history.s3.amazonaws.com/participants-history/vinicius.jpeg",
                "nickname": "Vinicius",
                "name": "Vinicius",
                "birth_date": "1997-09-05",
                "username": "Vinicius",
                "email": "asjdhakjdask@hotmail.com"
            },
            "created_at": "2020-04-06T22:21:36.681497-03:00",
            "updated_at": "2020-04-06T22:21:36.681497-03:00"
        }

        rodolfo = {
            "id": "asdsadsadsadsadasd",
            "owner": False,
            "participant": {
                "id": "lsajdlas",
                "photo": "https://remember-history.s3.amazonaws.com/participants-history/rodolfo.jpg",
                "nickname": "Rodolfo",
                "name": "Rodolfo",
                "birth_date": "1997-09-05",
                "username": "Rodolfo",
                "email": "asjdhakjdask@hotmail.com"
            },
            "created_at": "2020-04-06T22:21:36.681497-03:00",
            "updated_at": "2020-04-06T22:21:36.681497-03:00"
        }

        ruiz = {
            "id": "asdsadsadsadsadasd",
            "owner": False,
            "participant": {
                "id": "lsajdlas",
                "photo": "https://remember-history.s3.amazonaws.com/participants-history/ruiz.jpg",
                "nickname": "Vinicius Ruiz",
                "name": "Vinicius Ruiz",
                "birth_date": "1997-09-05",
                "username": "Vinicius Ruiz",
                "email": "asjdhakjdask@hotmail.com"
            },
            "created_at": "2020-04-06T22:21:36.681497-03:00",
            "updated_at": "2020-04-06T22:21:36.681497-03:00"
        }

        ju = {
            "id": "asdsadsadsadsadasd",
            "owner": False,
            "participant": {
                "id": "lsajdlas",
                "photo": "https://remember-history.s3.amazonaws.com/participants-history/ju.PNG",
                "nickname": "Juliana",
                "name": "Juliana",
                "birth_date": "1997-09-05",
                "username": "Juliana",
                "email": "asjdhakjdask@hotmail.com"
            },
            "created_at": "2020-04-06T22:21:36.681497-03:00",
            "updated_at": "2020-04-06T22:21:36.681497-03:00"
        }

        yudi = {
            "id": "asdsadsadsadsadasd",
            "owner": False,
            "participant": {
                "id": "lsajdlas",
                "photo": "https://remember-history.s3.amazonaws.com/participants-history/yudi.jpg",
                "nickname": "Yudi",
                "name": "Yudi",
                "birth_date": "1997-09-05",
                "username": "Yudi",
                "email": "asjdhakjdask@hotmail.com"
            },
            "created_at": "2020-04-06T22:21:36.681497-03:00",
            "updated_at": "2020-04-06T22:21:36.681497-03:00"
        }

        lucas = {
            "id": "asdsadsadsadsadasd",
            "owner": False,
            "participant": {
                "id": "lsajdlas",
                "photo": "https://remember-history.s3.amazonaws.com/participants-history/lucas.jpg",
                "nickname": "Lucas",
                "name": "Lucas",
                "birth_date": "1997-09-05",
                "username": "Lucas",
                "email": "asjdhakjdask@hotmail.com"
            },
            "created_at": "2020-04-06T22:21:36.681497-03:00",
            "updated_at": "2020-04-06T22:21:36.681497-03:00"
        }

        body = [
            vini, rodolfo, ruiz, ju, yudi, lucas
        ]
        return Response(body, status=status.HTTP_200_OK)