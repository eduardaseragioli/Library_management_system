import sys #importa o módulo sys para manipulação de argumentos e saída do programa
from PyQt5.QtWidgets import QApplication, QStackedWidget, QMessageBox # importa classes necessárias do PyQt5 para criar a interface gráfica
from PyQt5.QtGui import QFont # importa a classe QFont para definir fontes na interface gráfica
from capa import CapaWindow # importa a classe CapaWindow do módulo capa
from login import LoginWindow
from menu import MenuWindow
from show.cadastro import CadastroWindow
from show.leitura import LeituraWindow
from show.perfil import PerfilWindow
from show.funcionario import FuncionarioWindow
from show.leitor import LeitorWindow
from show.item import ItemWindow
from show.estatistica import EstatisticaWindow
from show.autor import AutorWindow
from show.emprestimo import EmprestimoWindow
from show.multa import MultaWindow
from registro.funcionarioCadastro import FuncionarioCadastroWindow
from registro.leitorCadastro import LeitorCadastroWindow
from registro.itemCadastro import ItemCadastroWindow
from registro.autorCadastro import AutorCadastroWindow
from registro.emprestimoCadastro import EmprestimoCadastroWindow
from registro.multaCadastro import MultaCadastroWindow
from databaseManager import DatabaseManager # Importa o gerenciador de banco de dados

class MainApp(QStackedWidget): # Define a Classe principal do aplicativo que herda de QStackedWidget
    def __init__(self): # Método construtor da classe MainApp

        """Inicializa o aplicativo e configura as telas."""
        super(MainApp, self).__init__() # Chama o construtor da classe pai QStackedWidget

        # Inicializa o gerenciador de banco de dados
        self.db_manager = DatabaseManager() # Cria uma instância do gerenciador de banco de dados
        self.connect_to_database()  

        # Inicializa as telas
        self.capa_window = CapaWindow(self) # Cria uma instância da CapaWindow
        self.login_window = LoginWindow(self, self.db_manager)  # Cria uma instância da LoginWindow com referência ao gerenciador de banco de dados
        self.menu_window = MenuWindow(self)
        self.cadastro_window = CadastroWindow(self)
        self.leitura_window = LeituraWindow(self)
        self.perfil_window = PerfilWindow(self, self.db_manager)
        self.funcionario_window = FuncionarioWindow(self, self.db_manager)
        self.leitor_window = LeitorWindow(self, self.db_manager)
        self.item_window = ItemWindow(self, self.db_manager)
        self.estatistica_window = EstatisticaWindow(self, self.db_manager)
        self.autor_window = AutorWindow(self, self.db_manager)
        self.emprestimo_window = EmprestimoWindow(self, self.db_manager)
        self.multa_window = MultaWindow(self, self.db_manager)
        self.funcionario_cadastro_window = FuncionarioCadastroWindow(self, self.db_manager)
        self.leitor_cadastro_window = LeitorCadastroWindow(self, self.db_manager)
        self.item_cadastro_window = ItemCadastroWindow(self, self.db_manager)
        self.autor_cadastro_window = AutorCadastroWindow(self, self.db_manager)
        self.emprestimo_cadastro_window = EmprestimoCadastroWindow(self, self.db_manager)
        self.multa_cadastro_window = MultaCadastroWindow(self, self.db_manager)

        # Adiciona as telas ao QStackedWidget
        # Para cada instância de janela criada, ela é adicionada ao QStackedWidget.

        self.addWidget(self.capa_window) # Adiciona a CapaWindow ao QStackedWidget
        self.addWidget(self.login_window)
        self.addWidget(self.menu_window)
        self.addWidget(self.cadastro_window)
        self.addWidget(self.leitura_window)
        self.addWidget(self.perfil_window)
        self.addWidget(self.funcionario_window)
        self.addWidget(self.leitor_window)
        self.addWidget(self.item_window)
        self.addWidget(self.estatistica_window)
        self.addWidget(self.autor_window)
        self.addWidget(self.emprestimo_window)
        self.addWidget(self.multa_window)
        self.addWidget(self.funcionario_cadastro_window)
        self.addWidget(self.leitor_cadastro_window)
        self.addWidget(self.item_cadastro_window)
        self.addWidget(self.autor_cadastro_window)
        self.addWidget(self.emprestimo_cadastro_window)
        self.addWidget(self.multa_cadastro_window)

        # Define a tela inicial como a CapaWindow
        self.setCurrentWidget(self.capa_window)

    def set_funcionario_logado(self, id_funcionario_logado):# Define um método para passar o ID do funcionário que logou para a tela de perfil.

        """Atualiza o ID do funcionário logado e recarrega os dados no PerfilWindow."""
        self.perfil_window.set_funcionario_id(id_funcionario_logado)

    def connect_to_database(self):#Define um método para lidar com a conexão ao banco de dados
        """Conecta ao banco de dados e exibe uma mensagem de sucesso ou erro."""
        try:
            self.db_manager.connect()
            print("Conexão com o banco de dados bem-sucedida!")
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            QMessageBox.critical(self, "Erro", f"Erro ao conectar ao banco de dados: {e}")
            sys.exit(1)  # Encerra o programa se a conexão falhar

if __name__ == "__main__":# Verifica se o script está sendo executado diretamente
    app = QApplication(sys.argv)# Cria uma instância da aplicação QApplication


    # Define o estilo global para o aplicativo
    app.setStyleSheet("""
        QMainWindow {
            background-color: #4A5A80;  /* Azul escuro */
        }
        QLabel, QLineEdit, QPushButton {
            color: white;  /* Texto branco */
        }
       
        QPushButton {
            background-color: #3A3A5F;  /* Botão azul escuro */
            border: 1px solid white;
            border-radius: 5px;
            padding: 5px;
        }
        QPushButton:hover {
            background-color: #505080;  /* Botão azul mais claro ao passar o mouse */
        }
    """)

    # Inicializa o QStackedWidget principal
    main_app = MainApp()# Cria uma instância da classe MainApp, que é um QStackedWidget, vai gerenciar as diferentes telas do aplicativo.

    id_funcionario_logado = 1  # Variável para armazenar o ID do funcionário logado
    main_app.set_funcionario_logado(id_funcionario_logado)


    # Ajusta o tamanho da janela para respeitar o tamanho do .ui
    main_app.resize(main_app.currentWidget().size())# Ajusta o tamanho da janela para o tamanho do widget atual
    main_app.show()# Exibe a janela principal do aplicativo

    sys.exit(app.exec_())# Encerra o aplicativo quando a janela é fechada