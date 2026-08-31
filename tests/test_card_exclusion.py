import unittest
from pathlib import Path


class CardExclusionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (Path(__file__).resolve().parents[1] / "index.html").read_text(
            encoding="utf-8"
        )

    def test_menu_contextual_e_restrito_ao_card(self):
        self.assertIn("const exclusoesPorCard=new Map()", self.html)
        self.assertIn("document.addEventListener('contextmenu'", self.html)
        self.assertIn("Eliminar esta casa", self.html)
        self.assertIn("Retirar exclusão desta casa", self.html)
        self.assertIn("somente neste card", self.html)
        self.assertIn("data-card-idx", self.html)
        self.assertIn("is-excluded", self.html)

    def test_substitutas_usam_todas_as_odds_e_recalculam_jogadores(self):
        self.assertIn("function prepararOpcoesResultado(", self.html)
        self.assertIn("casa_opcoes:casaOpcoes", self.html)
        self.assertIn("empate_opcoes:empateOpcoes", self.html)
        self.assertIn("fora_opcoes:foraOpcoes", self.html)
        self.assertIn("function atualizarCardAposExclusao(", self.html)
        self.assertIn("const totaisJogadores=[1,2,3].map", self.html)
        self.assertIn("recalcularTotaisCard(cardIdx)", self.html)


if __name__ == "__main__":
    unittest.main()
