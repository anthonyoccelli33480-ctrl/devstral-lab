"""14 agents code — Devstral Small 2 + Codestral."""

from dataclasses import dataclass
from typing import Literal

ModelId = Literal["devstral-small-latest", "codestral-latest"]


@dataclass(frozen=True)
class AgentDef:
    id: str
    name: str
    tagline: str
    model: ModelId
    category: str
    icon: str
    placeholder: str
    system: str
    max_tokens: int = 2048
    temperature: float = 0.2


AGENTS: dict[str, AgentDef] = {}


def _register(a: AgentDef) -> AgentDef:
    AGENTS[a.id] = a
    return a


_register(AgentDef(
    id="review",
    name="Lab Review",
    tagline="Diff → review structurée",
    model="devstral-small-latest",
    category="agentic",
    icon="🔍",
    placeholder="Colle un diff ou un extrait de code…",
    system="""Tu es un reviewer senior. Réponds UNIQUEMENT en JSON :
{"summary":"<2 phrases>","score":<0-100>,"critical":[{"line":"...","issue":"...","fix":"..."}],
 "warnings":[{"issue":"...","suggestion":"..."}],"positives":["..."],"verdict":"ship|fix_first|rewrite"}
Français, concis.""",
))

_register(AgentDef(
    id="fix",
    name="Lab Fix",
    tagline="Stack trace → cause + patch",
    model="devstral-small-latest",
    category="agentic",
    icon="🔧",
    placeholder="Stack trace + code concerné…",
    system="""Débuggue. JSON uniquement :
{"error_type":"...","root_cause":"...","confidence":<0-1>,"fix_steps":["..."],
 "patch":"<code ou null>","prevention":"..."}""",
))

_register(AgentDef(
    id="impl",
    name="Lab Impl",
    tagline="Spec → plan d'implémentation agentique",
    model="devstral-small-latest",
    category="agentic",
    icon="🧭",
    placeholder="Décris la feature à implémenter (stack, contraintes)…",
    system="""Tu planifies comme un agent coding. JSON uniquement :
{"goal":"...","assumptions":["..."],"files":[{"path":"...","action":"create|edit","why":"..."}],
 "steps":[{"order":1,"task":"...","test":"..."}],"risks":["..."],"estimate_hours":<n>}""",
))

_register(AgentDef(
    id="refactor",
    name="Lab Refactor",
    tagline="Code smell → version propre",
    model="devstral-small-latest",
    category="agentic",
    icon="♻️",
    placeholder="Code à refactorer…",
    system="""Refactor. JSON :
{"smells":["..."],"refactored_code":"<code>","changes":["..."],"tests_to_add":["..."]}""",
))

_register(AgentDef(
    id="explain",
    name="Lab Explain",
    tagline="Code → explication claire",
    model="devstral-small-latest",
    category="agentic",
    icon="💡",
    placeholder="Colle du code obscur…",
    system="""Explique. JSON :
{"summary":"...","how_it_works":["..."],"complexity":"O(...)","gotchas":["..."],"analogy":"..."}""",
))

_register(AgentDef(
    id="test",
    name="Lab Test",
    tagline="Fonction → tests unitaires",
    model="devstral-small-latest",
    category="agentic",
    icon="🧪",
    placeholder="Fonction + framework de test (pytest, vitest…)…",
    system="""Génère des tests. JSON :
{"framework":"...","tests":"<code complet>","cases":[{"name":"...","covers":"..."}],"coverage_gaps":["..."]}""",
))

_register(AgentDef(
    id="secret",
    name="Lab Secret",
    tagline="Code/log → secrets détectés",
    model="devstral-small-latest",
    category="security",
    icon="🔐",
    placeholder="Code ou logs à scanner…",
    system="""Détecte les fuites. JSON :
{"found":<bool>,"secrets":[{"type":"api_key|password|token","location":"...","severity":"high|med|low","remediation":"..."}],
 "false_positives":["..."],"verdict":"clean|rotate_keys|block_merge"}""",
))

_register(AgentDef(
    id="migrate",
    name="Lab Migrate",
    tagline="Stack A → plan migration B",
    model="devstral-small-latest",
    category="agentic",
    icon="🚚",
    placeholder="Ex: Express → FastAPI, JS → TS…",
    system="""Plan de migration. JSON :
{"from":"...","to":"...","phases":[{"name":"...","tasks":["..."],"rollback":"..."}],
 "breaking_changes":["..."],"effort_days":<n>,"priority_order":["..."]}""",
))

_register(AgentDef(
    id="commit",
    name="Lab Commit",
    tagline="Diff → Conventional Commits",
    model="codestral-latest",
    category="codestral",
    icon="📝",
    placeholder="Git diff…",
    system="""Conventional Commits. JSON :
{"commit_type":"feat|fix|refactor|docs|test|chore","commit_subject":"<72 chars>",
 "commit_body":"...","pr_title":"...","pr_description":"...","breaking_change":<bool>}""",
))

_register(AgentDef(
    id="regex",
    name="Lab Regex",
    tagline="Description → regex testée",
    model="codestral-latest",
    category="codestral",
    icon="⚡",
    placeholder="Ce que tu veux matcher…",
    system="""Expert regex. JSON :
{"pattern":"...","flags":"...","explanation":"...","matches":["..."],"non_matches":["..."],"edge_cases":["..."]}""",
))

_register(AgentDef(
    id="sql",
    name="Lab SQL",
    tagline="Question + schéma → requête",
    model="codestral-latest",
    category="codestral",
    icon="🗄️",
    placeholder="Schéma SQL + question en français…",
    system="""SQL. JSON :
{"dialect":"postgres|mysql|sqlite","query":"<SQL>","explanation":"...","indexes_suggested":["..."],"warnings":["..."]}""",
))

_register(AgentDef(
    id="dockerfile",
    name="Lab Docker",
    tagline="Stack → Dockerfile minimal",
    model="codestral-latest",
    category="codestral",
    icon="🐳",
    placeholder="Stack (ex: FastAPI + React, Node 22…)…",
    system="""Dockerfile prod-ready minimal. JSON :
{"dockerfile":"<content>","dockerignore":["..."],"build_cmd":"...","run_cmd":"...","notes":["..."]}""",
))

_register(AgentDef(
    id="openapi",
    name="Lab OpenAPI",
    tagline="Endpoints → spec OpenAPI",
    model="codestral-latest",
    category="codestral",
    icon="📡",
    placeholder="Liste d'endpoints ou description API…",
    system="""OpenAPI 3.1. JSON :
{"openapi_yaml":"<yaml>","endpoints":[{"method":"GET","path":"...","summary":"..."}],"auth":"..."}""",
))

_register(AgentDef(
    id="api-design",
    name="Lab API Design",
    tagline="Besoin métier → design REST",
    model="codestral-latest",
    category="codestral",
    icon="🏗️",
    placeholder="Décris le produit et les ressources…",
    system="""Design API REST. JSON :
{"resources":[{"name":"...","endpoints":[{"method":"...","path":"...","body":"..."}]}],
 "errors":[{"code":400,"when":"..."}],"versioning":"...","pagination":"..."}""",
))


def get_agent(agent_id: str) -> AgentDef:
    if agent_id not in AGENTS:
        raise KeyError(agent_id)
    return AGENTS[agent_id]


def list_agents() -> list[dict]:
    from .guides import get_guide

    out = []
    for a in AGENTS.values():
        g = get_guide(a.id)
        out.append({
            "id": a.id,
            "name": a.name,
            "tagline": a.tagline,
            "model": a.model,
            "category": a.category,
            "icon": a.icon,
            "placeholder": a.placeholder,
            "requires_image": False,
            "max_images": 0,
            "how_to": g["how_to"],
            "next_steps": g["next_steps"],
        })
    return out