from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QMessageBox, QComboBox, QRadioButton # Importa as classes necessárias do PyQt5
from PyQt5.uic import loadUi # Importae as funções PyQt5
import os

class ItemCadastroWindow(QMainWindow):# Define a classe ItemCadastroWindow, que herda de QMainWindow
    def __init__(self, stacked_widget, db_manager):
        super(ItemCadastroWindow, self).__init__()
        self.stacked_widget = stacked_widget
        self.db_manager = db_manager#iteração do banco de dados

        # Carregar o arquivo itemCadastro.ui da pasta registro
        ui_path = os.path.join(os.path.dirname(__file__), "itemCadastro.ui")
        loadUi(ui_path, self)

        # Conectar o botão menuButton ao método para voltar ao menu
        self.menuButton: QPushButton = self.findChild(QPushButton, "menuButton")
        if self.menuButton:
            self.menuButton.clicked.connect(self.go_to_menu)
        else:
            print("[ERRO] menuButton não encontrado no arquivo itemCadastro.ui")

        # Conectar o botão salvarButton ao método de salvar
        self.salvarButton: QPushButton = self.findChild(QPushButton, "salvarButton")
        if self.salvarButton:
            self.salvarButton.clicked.connect(self.salvar_item)
        else:
            print("[ERRO] salvarButton não encontrado no arquivo itemCadastro.ui")

        # Inputs
        self.editoraInput: QLineEdit = self.findChild(QLineEdit, "editoraInput")
        self.generoBox: QComboBox = self.findChild(QComboBox, "generoBox")
        self.titleInput: QLineEdit = self.findChild(QLineEdit, "titleInput")
        self.verdadeiroButton: QRadioButton = self.findChild(QRadioButton, "verdadeiroButton")
        self.falsoButton: QRadioButton = self.findChild(QRadioButton, "falsoButton")
        self.isbnInput: QLineEdit = self.findChild(QLineEdit, "isbnInput")
        self.tipoItemBox: QComboBox = self.findChild(QComboBox, "tipoItemBox")
        self.autorBox: QComboBox = self.findChild(QComboBox, "autorBox")

        # Carrega os autores no ComboBox ao abrir a janela
        self.carregar_autores()# Carrega os autores do banco de dados

    def carregar_autores(self):
        """Carrega os autores do banco de dados no ComboBox autorBox."""
        if not self.autorBox:
            print("[ERRO] autorBox não encontrado no arquivo itemCadastro.ui")
            return
        self.autorBox.clear()
        try:
            query = "SELECT idAutor, nome FROM autor" # Consulta todos os autores no banco de dados
            autores = self.db_manager.fetch_query(query)
            if autores:
                for autor in autores:
                    self.autorBox.addItem(autor["nome"], autor["idAutor"])
                    # Para cada autor encontrado, adiciona o nome do autor no ComboBox,
            else:
                self.autorBox.addItem("Nenhum autor cadastrado", None)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar autores: {e}")

    def go_to_menu(self):
        """Volta para a tela do menu."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.menu_window)

    def salvar_item(self):
        """Salva o item no banco de dados."""
        editora = self.editoraInput.text().strip() if self.editoraInput else ""
        genero = self.generoBox.currentText() if self.generoBox else ""
        titulo = self.titleInput.text().strip() if self.titleInput else ""
        isbn = self.isbnInput.text().strip() if self.isbnInput else ""
        tipo_item = self.tipoItemBox.currentText() if self.tipoItemBox else ""

        # Determina o valor booleano com base nos botões de rádio
        if self.verdadeiroButton and self.verdadeiroButton.isChecked():
            disponivel = True
        elif self.falsoButton and self.falsoButton.isChecked():
            disponivel = False
        else:
            disponivel = None

        id_autor = self.autorBox.currentData() if self.autorBox else None
        # currentData() retorna o dado associado ao item selecionado (que foi definido como idAutor em addItem).

        # Verifica se todos os campos obrigatórios estão preenchidos
        if not editora or not genero or not titulo or disponivel is None or not isbn or not tipo_item or not id_autor:
            QMessageBox.warning(self, "Atenção", "Preencha todos os campos!")
            return

        try:
            query = """
                INSERT INTO item (editora, genero, titulo, disponivel, isbn, tipo_item, idAutor)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            self.db_manager.execute_query(query, (editora, genero, titulo, disponivel, isbn, tipo_item, id_autor))
            QMessageBox.information(self, "Sucesso", "Item cadastrado com sucesso!")
            self.editoraInput.clear()
            self.titleInput.clear()
            self.isbnInput.clear()
            self.generoBox.setCurrentIndex(0)
            self.tipoItemBox.setCurrentIndex(0)
            
            if self.verdadeiroButton:
                self.verdadeiroButton.setChecked(False)
            if self.falsoButton:
                self.falsoButton.setChecked(False)
            if self.autorBox:
                self.autorBox.setCurrentIndex(0)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar item: {e}")