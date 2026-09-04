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
        self.assertIn("statusCasasPorCampeonato: statusCasasPorCampeonato || {}", self.html)

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
