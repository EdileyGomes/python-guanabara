import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QFrame, QSizePolicy, QSpacerItem
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont, QPixmap, QIcon

# --- CORES DO DESIGN ---
COR_PRIMARIA_AZUL = "#002B5B"  # Azul Marinho
COR_DESTAQUE_GRENÁ = "#8A0303"  # Grená para Alerta/Sair
COR_FUNDO_BRANCO = "#FFFFFF"  # Fundo Limpo
COR_FUNDO_SIDEBAR = "#F0F0F0"  # Cinza muito claro para Sidebar
COR_ATIVA_AZUL = "#1E90FF"  # Azul para Item Ativo


# --- CLASSE PRINCIPAL DA JANELA ---
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Gestão da Igreja - PyQt6")
        self.setGeometry(100, 100, 1200, 700)  # Tamanho da Janela

        # 1. Configurar Widget Central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 2. Criar e Adicionar Sidebar
        self.sidebar = self.create_sidebar()
        main_layout.addWidget(self.sidebar)

        # 3. Criar e Adicionar Conteúdo (Placeholder)
        self.content_area = self.create_content_area()
        main_layout.addWidget(self.content_area)

        # 4. Aplicar Estilos CSS
        self.apply_styles()

    # --- CRIAÇÃO DA SIDEBAR ---
    def create_sidebar(self):
        sidebar = QFrame()
        sidebar.setFixedWidth(250)
        sidebar.setObjectName("Sidebar")  # Usado para o CSS
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(15, 15, 15, 15)
        sidebar_layout.setSpacing(15)

        # 2.1. Seção de Perfil (FOTO / NOME / FUNÇÃO)
        perfil_frame = self.create_profile_section()
        sidebar_layout.addWidget(perfil_frame)

        # 2.2. Menu de Navegação
        menu_frame = self.create_menu_buttons()
        sidebar_layout.addWidget(menu_frame)

        # 2.3. Espaçador para empurrar o botão Sair para baixo
        sidebar_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # 2.4. Botão SAIR (Fica bem abaixo)
        btn_sair = QPushButton("Sair")
        btn_sair.setObjectName("BtnSair")
        btn_sair.setIcon(QIcon.fromTheme("application-exit"))  # Ícone de sair (depende do tema do sistema)
        btn_sair.setFixedHeight(40)
        sidebar_layout.addWidget(btn_sair)

        return sidebar

    # --- CRIAÇÃO DA SEÇÃO DE PERFIL ---
    def create_profile_section(self):
        profile_frame = QFrame()
        profile_layout = QHBoxLayout(profile_frame)
        profile_layout.setContentsMargins(0, 0, 0, 0)

        # Placeholder para Imagem (use um QLabel)
        lbl_foto = QLabel()
        lbl_foto.setFixedSize(QSize(60, 60))
        # Para carregar sua imagem real:
        # pixmap = QPixmap("caminho/para/sua/foto.png").scaled(60, 60, Qt.AspectRatioMode.KeepSmooth)
        # lbl_foto.setPixmap(pixmap)
        lbl_foto.setObjectName("ProfilePic")
        lbl_foto.setStyleSheet(f"""
            #ProfilePic {{
                background-color: {COR_ATIVA_AZUL};
                border-radius: 30px; /* Cria o efeito circular */
                border: 2px solid {COR_DESTAQUE_GRENÁ};
            }}
        """)
        profile_layout.addWidget(lbl_foto)

        # Nome/ID e Função
        info_widget = QWidget()
        info_layout = QVBoxLayout(info_widget)
        info_layout.setContentsMargins(10, 0, 0, 0)
        info_layout.setSpacing(2)

        lbl_nome = QLabel("Pr. Robimson (ID: 101)")
        lbl_nome.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        lbl_nome.setStyleSheet(f"color: {COR_PRIMARIA_AZUL};")

        lbl_funcao = QLabel("Pastor (València)\n2° Secretário Geral")
        lbl_funcao.setFont(QFont("Arial", 9))
        lbl_funcao.setStyleSheet(f"color: gray;")

        info_layout.addWidget(lbl_nome)
        info_layout.addWidget(lbl_funcao)
        profile_layout.addWidget(info_widget)
        profile_layout.addItem(
            QSpacerItem(1, 1, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))  # Empurra info para esquerda

        return profile_frame

    # --- CRIAÇÃO DOS BOTÕES DE MENU ---
    def create_menu_buttons(self):
        menu_frame = QFrame()
        menu_layout = QVBoxLayout(menu_frame)
        menu_layout.setContentsMargins(0, 0, 0, 0)
        menu_layout.setSpacing(5)

        menu_items = [
            ("Menu Principal", "home"),
            ("Membros", "people"),
            ("Financeiro", "wallet"),
            ("Relatórios", "bar-chart"),
            ("Configurações", "settings")
        ]

        # Cria os botões de menu
        for text, icon_name in menu_items:
            btn = QPushButton(text)
            btn.setObjectName(f"BtnMenu_{text.replace(' ', '')}")
            btn.setCheckable(True)
            btn.setFixedHeight(45)
            # Placeholder de Ícone (Substitua por QIcon.fromTheme se usar ícones SVG modernos)
            btn.setIcon(QIcon())
            btn.setStyleSheet(f"""
                QPushButton {{
                    text-align: left;
                    padding-left: 20px;
                    border: none;
                    background-color: transparent;
                    color: {COR_PRIMARIA_AZUL};
                    font-weight: 500;
                    border-radius: 8px; /* Cantos arredondados */
                }}
                QPushButton:checked {{
                    background-color: {COR_ATIVA_AZUL}; /* Azul Ativo */
                    color: {COR_FUNDO_BRANCO};
                }}
                QPushButton:hover:!checked {{
                    background-color: #E0E0E0; /* Efeito hover suave */
                }}
            """)
            menu_layout.addWidget(btn)

        # Define 'Relatórios' como o item ativo inicial
        # Encontre o botão correspondente e chame .setChecked(True)

        return menu_frame

    # --- CRIAÇÃO DA ÁREA DE CONTEÚDO (DIREITA) ---
    def create_content_area(self):
        content_frame = QFrame()
        content_frame.setObjectName("ContentArea")
        content_frame.setStyleSheet(f"background-color: {COR_FUNDO_BRANCO};")

        # Aqui você adicionaria o layout com o Título e a Tabela de Relatórios
        # ... (será implementado na próxima etapa)

        return content_frame

    # --- ESTILOS GLOBAIS ---
    def apply_styles(self):
        # Estilo da Janela Principal (Pode ser estendido para sombreamento da janela)
        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: {COR_FUNDO_BRANCO};
            }}
            #Sidebar {{
                background-color: {COR_FUNDO_SIDEBAR};
                border-right: 1px solid #D0D0D0; /* Linha de separação suave */
            }}
            #BtnSair {{
                background-color: {COR_DESTAQUE_GRENÁ};
                color: {COR_FUNDO_BRANCO};
                border-radius: 8px;
                font-weight: bold;
            }}
            #BtnSair:hover {{
                background-color: #103400; /* Grená mais escuro no hover */
            }}
        """)


# --- EXECUÇÃO DO APLICATIVO ---
if __name__ == '__main__':
    # Define a fonte global para um visual mais limpo (ex: Arial, Segoe UI, etc.)
    app = QApplication(sys.argv)
    font = QFont("Segoe UI", 10)
    app.setFont(font)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())