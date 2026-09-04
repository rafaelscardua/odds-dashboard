from pathlib import Path
import unittest


INDEX = Path(__file__).resolve().parents[1] / "index.html"


class BasqueteDashboardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = INDEX.read_text(encoding="utf-8")

    def test_seletor_publica_basquete_com_estilo_ativo(self):
        self.assertIn("basquete:{nome:'Basquete'", self.html)
        self.assertIn('.sport-option[data-esporte="basquete"].active', self.html)
        self.assertIn("if(esporte==='tenis')esporte='basquete'", self.html)

    def test_importador_usa_colunas_do_automatico_basquete(self):
        colunas = [
            "CAMPEONATO", "TIME 1", "TIME 2", "ODD TIME 1", "ODD TIME 2",
            "CASA(S) TIME 1", "CASA(S) TIME 2",
        ]
        for coluna in colunas:
            with self.subTest(coluna=coluna):
                self.assertIn(coluna, self.html)

    def test_firebase_salva_basquete_e_migra_dados_antigos(self):
        self.assertIn("basqueteData: tenisData || []", self.html)
        self.assertIn("val.basqueteData || val.tenisData || []", self.html)

    def test_interface_exibe_terminologia_de_basquete(self):
        self.assertIn("Comparativo de basquete", self.html)
        self.assertIn("Carregar basquete XLSX", self.html)
        self.assertIn("NBA 2026/27", self.html)
        self.assertIn("Odd time 1", self.html)
        self.assertIn("Odd time 2", self.html)


if __name__ == "__main__":
    unittest.main()
