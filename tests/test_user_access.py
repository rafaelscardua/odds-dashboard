import json
import unittest
from pathlib import Path


class UserAccessHtmlTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]
        cls.html = (cls.root / "index.html").read_text(encoding="utf-8")

    def test_admin_tem_gerenciador_de_usuarios(self):
        self.assertIn('id="btnGerenciarUsuarios"', self.html)
        self.assertIn('id="modal-gerenciar-usuarios"', self.html)
        self.assertIn("function abrirGerenciadorUsuarios()", self.html)
        self.assertIn("function alterarAcessoUsuario", self.html)

    def test_bloqueio_e_verificado_antes_de_exibir_app(self):
        trecho = self.html.split("function checkAdmin(user)", 1)[1].split(
            "function setupUIForRole", 1
        )[0]
        self.assertIn("blockedUsers[user.uid]", trecho)
        self.assertLess(trecho.index("acesso.blocked === true"), trecho.index("showApp()"))

    def test_sessao_aberta_monitora_bloqueio(self):
        self.assertIn("function iniciarMonitoramentoDeAcesso()", self.html)
        self.assertIn("config/blockedUsers/${currentUser.uid}", self.html)
        self.assertIn("bloquearSessaoAtual('Seu acesso foi bloqueado", self.html)

    def test_regras_negam_odds_para_usuario_bloqueado(self):
        regras = json.loads(
            (self.root / "firebase-database-rules.json").read_text(encoding="utf-8")
        )
        leitura = regras["rules"]["oddsData"][".read"]
        self.assertIn("blockedUsers", leitura)
        self.assertIn("auth.uid", leitura)


if __name__ == "__main__":
    unittest.main()
