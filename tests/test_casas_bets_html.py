from pathlib import Path
import unittest


INDEX = Path(__file__).resolve().parents[1] / "index.html"


class CasasBetsHtmlTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = INDEX.read_text(encoding="utf-8")

    def test_aba_lista_todas_as_casas_e_expande_detalhes(self):
        self.assertIn('id="btn-casasbets"', self.html)
        self.assertIn('id="tab-casasbets"', self.html)
        self.assertIn("function renderCasasBets()", self.html)
        self.assertIn("function toggleCasaBets(indice)", self.html)
        self.assertIn("const nomes=[...BET_LIST]", self.html)
        self.assertIn("casasBetsAbertas", self.html)

    def test_aba_mostra_odds_e_motivo_da_ausencia(self):
        self.assertIn("detalheStatusCasa", self.html)
        self.assertIn("textoSemOddsCasaBet", self.html)
        self.assertIn("Não retornou odds válidas neste campeonato durante a captura.", self.html)
        self.assertIn("casa-bet-odd casa", self.html)
        self.assertIn("casa-bet-reason", self.html)


if __name__ == "__main__":
    unittest.main()
