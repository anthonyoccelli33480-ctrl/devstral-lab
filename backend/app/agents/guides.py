GUIDES: dict[str, dict[str, list[str]]] = {
    "review": {
        "how_to": ["Colle un diff Git ou un fichier", "Vise < 500 lignes pour la latence", "Le verdict ship/fix_first guide la merge"],
        "next_steps": ["Applique les fix critical", "Relance Lab Review sur le patch"],
    },
    "fix": {
        "how_to": ["Inclus stack trace complète + snippet", "Mentionne langage et version"],
        "next_steps": ["Copie le patch", "Ajoute un test de non-régression"],
    },
    "impl": {
        "how_to": ["Décris stack, contraintes, critères de done", "Idéal pour specs issues GitHub"],
        "next_steps": ["Suis les steps dans l'ordre", "Valide chaque test suggéré"],
    },
    "refactor": {"how_to": ["Un module à la fois"], "next_steps": ["Run tests", "Lab Review sur le diff"]},
    "explain": {"how_to": ["Code obscur ou legacy"], "next_steps": ["Documente avec le summary"]},
    "test": {"how_to": ["Donne la fonction + framework"], "next_steps": ["Colle les tests dans le fichier spec"]},
    "secret": {"how_to": ["Scan avant commit"], "next_steps": ["Rotate keys si verdict rotate_keys"]},
    "migrate": {"how_to": ["Sois explicite sur from/to"], "next_steps": ["Exécute phase 1 seule d'abord"]},
    "commit": {"how_to": ["git diff staged"], "next_steps": ["git commit -m", "Ouvre la PR"]},
    "regex": {"how_to": ["Décris en langage naturel"], "next_steps": ["Teste matches/non_matches"]},
    "sql": {"how_to": ["Colle le schéma CREATE TABLE"], "next_steps": ["EXPLAIN la query en prod"]},
    "dockerfile": {"how_to": ["Liste runtime + build steps"], "next_steps": ["docker build", "Scan image"]},
    "openapi": {"how_to": ["Liste routes ou user stories API"], "next_steps": ["Importe dans Swagger UI"]},
    "api-design": {"how_to": ["Décris ressources et règles métier"], "next_steps": ["Impl avec Lab Impl"]},
}


def get_guide(agent_id: str) -> dict[str, list[str]]:
    return GUIDES.get(agent_id, {"how_to": ["Colle ton input", "Clique Run"], "next_steps": ["Itère"]})