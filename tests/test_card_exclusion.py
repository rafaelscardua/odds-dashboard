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

    def test_unifica_variantes_de_cienciano_e_city_torque(self):
        self.assertIn("'club cienciano':'cienciano'", self.html)
        self.assertIn("'torque':'montevideo city torque'", self.html)
        self.assertIn("function nomeExibicaoJogo(", self.html)
        self.assertIn("normalizeJogo(r.jogo_limpo||r.jogo||'')", self.html)

    def test_unifica_variantes_da_champions(self):
        for alias in (
            "'psv eindhoven':'psv'",
            "'fc shakhtar donetsk':'shakhtar donetsk'",
            "'sk slavia praga':'slavia prague'",
            "'rc lens':'lens'",
            "'ssc napoli':'napoli'",
            "'arsenal fc':'arsenal'",
            "'sporting':'sporting lisboa'",
        ):
            self.assertIn(alias, self.html)

    def test_login_nao_exibe_status_dos_campeonatos(self):
        self.assertNotIn('id="loginUpdatesStatus"', self.html)
        self.assertNotIn("renderizarStatusAtualizacoes('loginUpdatesStatus')", self.html)

    def test_aba_jogos_revalida_jogo_limpo_com_aliases_atuais(self):
        render_jogos = self.html.split("function renderJogos(){", 1)[1].split(
            "function toggleExpandGame", 1
        )[0]
        self.assertIn(
            "normalizeJogo(r.jogo_limpo||normalizarNomeJogo(r.jogo))",
            render_jogos,
        )
        self.assertIn("jogo:nomeExibicaoJogo(r.jogo,jogoNorm)", render_jogos)


if __name__ == "__main__":
    unittest.main()
