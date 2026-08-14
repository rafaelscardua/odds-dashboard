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

    def test_tres_tipos_de_aposta_estao_disponiveis(self):
        self.assertIn('<option value="Arbitragem">Arbitragem</option>', self.html)
        self.assertIn('<option value="Individual">Individual</option>', self.html)
        self.assertIn('<option value="Bônus">Bônus</option>', self.html)

    def test_arbitragem_exige_tres_odds(self):
        self.assertIn('id="arb-casa-odd"', self.html)
        self.assertIn('id="arb-empate-odd"', self.html)
        self.assertIn('id="arb-fora-odd"', self.html)

    def test_data_nao_exibe_horario(self):
        self.assertIn('type="date" id="form-data-v2"', self.html)
        self.assertIn("const dataHora=dataJogo;", self.html)

    def test_bonus_nao_usa_investimento_proprio(self):
        self.assertIn("const bonus=tipo==='Bônus'?digitado:0,valor=tipo==='Bônus'?0:digitado;", self.html)

    def test_dados_antigos_migram_para_individual(self):
        self.assertIn("const tipo=a.tipo||'Individual';", self.html)

    def test_interface_usa_nome_arbitragem(self):
        self.assertNotIn("aposta holandesa", self.html.lower())
        self.assertNotIn("distribuição automática por dutching", self.html.lower())


if __name__ == "__main__":
    unittest.main()
