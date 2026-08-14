import unittest
from pathlib import Path


class HistoricoExcelHtmlTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (Path(__file__).resolve().parents[1] / "index.html").read_text(encoding="utf-8")

    def test_interface_oferece_modelo_e_importacao(self):
        self.assertIn('href="modelo_importacao_historico.xlsx"', self.html)
        self.assertIn('id="input-historico-excel"', self.html)
        self.assertIn("prepararImportacaoHistoricoExcel(event)", self.html)

    def test_importacao_tem_previa_e_nao_substitui_historico(self):
        self.assertIn("function confirmarImportacaoHistoricoExcel()", self.html)
        self.assertIn("historicoData.apostas.push", self.html)
        trecho = self.html.split("function confirmarImportacaoHistoricoExcel()", 1)[1].split("function exportarHistoricoExcel()", 1)[0]
        self.assertNotIn("historicoData =", trecho)

    def test_importacao_detecta_duplicados(self):
        self.assertIn("function chaveApostaHistorico", self.html)
        self.assertIn("if (vistos.has(chave))", self.html)

    def test_exportacao_preserva_data_e_hora(self):
        self.assertIn("'Data/Hora': new Date(a.data).toLocaleString", self.html)


if __name__ == "__main__":
    unittest.main()
