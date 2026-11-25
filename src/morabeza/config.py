"""Leitura da configuração do projeto (Sessão 3)."""
from pathlib import Path
from typing import Any

import yaml # pyright: ignore[reportMissingModuleSource]

CHAVES_OBRIGATORIAS = ("ficheiro_vendas", "moeda")


class ConfigInvalida(Exception):
    """O ficheiro de configuração não existe ou falta-lhe alguma chave obrigatória."""


def carregar_config(caminho: str | Path = "config.yaml") -> dict[str, Any]:
    ficheiro = Path(caminho)
    if not ficheiro.exists():
        raise ConfigInvalida(f"Ficheiro de configuração não encontrado: {caminho}")

    with open(ficheiro, mode="r", encoding="utf-8") as f:
        dados = yaml.safe_load(f) or {}

    em_falta = [chave for chave in CHAVES_OBRIGATORIAS if chave not in dados]
    if em_falta:
        raise ConfigInvalida(f"Chaves obrigatórias em falta: {', '.join(em_falta)}")

    return dados
    """Lê o ficheiro YAML e devolve um dicionário com a configuração."""
    # TODO 1: se o ficheiro não existir (Path(caminho).exists()), levanta ConfigInvalida.
    # TODO 2: abre o ficheiro com with open(...) e lê-o com yaml.safe_load(ficheiro).
    # TODO 3: vê que chaves de CHAVES_OBRIGATORIAS faltam (compreensão de lista)
    #         e, se faltar alguma, levanta ConfigInvalida com os nomes em falta.
    # TODO 4: devolve o dicionário.
    raise NotImplementedError("carregar_config ainda não está feita")
