from pathlib import Path
import unittest


INDEX = Path(__file__).resolve().parents[1] / "index.html"


class StatusCasasXlsxTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = INDEX.read_text(encoding="utf-8")

    def test_importa_e_sincroniza_status_das_casas(self):
        self.assertIn("status das casas", self.html)
        self.assertIn("statusCasasPorCampeonato", self.html)
        self.assertIn("oddsData/statusCasasPorCampeonato", self.html)
        self.assertIn(".set(statusCasasPorCampeonato || [])", self.html)
        trecho_payload = self.html.split("const payload = {", 1)[1].split("};", 1)[0]
        self.assertNotIn("statusCasasPorCampeonato:", trecho_payload)
        self.assertIn("statusDoArquivo.push({casa,status", self.html)
        self.assertNotIn("statusDoArquivo[casa]", self.html)
        self.assertIn("function normalizarStatusCasas", self.html)
        self.assertIn("function statusCasaDoArquivo", self.html)

    def test_detalhe_diferencia_desativada_geladeira_e_sem_retorno(self):
        self.assertIn("'DESATIVADA'", self.html)
        self.assertIn("'GELADEIRA'", self.html)
        self.assertIn("const rotuloStatus=", self.html)
        self.assertIn("statusDesativada==='DESATIVADA'?'DESATIVADA':'-'", self.html)

    def test_lista_padrao_nao_remove_casas_desativadas_da_auditoria(self):
        self.assertIn("const SITES_PADRAO=BET_LIST;", self.html)
        self.assertNotIn("const SITES_PADRAO=BET_LIST.filter(casaEstaAtiva);", self.html)


if __name__ == "__main__":
    unittest.main()
