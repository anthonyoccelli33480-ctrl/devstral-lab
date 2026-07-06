import { useState } from "react";
import { saveApiKey } from "../lib/api";

interface Props {
  onComplete: () => void;
  hasKey?: boolean;
}

export default function Onboarding({ onComplete, hasKey = false }: Props) {
  const [step, setStep] = useState<"welcome" | "key" | "done">("welcome");
  const [apiKey, setApiKey] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleSave() {
    setLoading(true);
    setError(null);
    try {
      await saveApiKey(apiKey);
      setStep("done");
    } catch (e) {
      setError(e instanceof Error ? e.message : "Erreur");
    } finally {
      setLoading(false);
    }
  }

  function finish() {
    localStorage.setItem("devstral-lab-onboarding", "1");
    onComplete();
  }

  return (
    <div className="ob-overlay">
      <div className="ob-card">
        {step === "welcome" && (
          <>
            <h1>🧪 Devstral Lab</h1>
            <p>
              Vitrine <strong>code agentique</strong> sur{" "}
              <a href="https://docs.mistral.ai" target="_blank" rel="noreferrer">
                La Plateforme Mistral
              </a>
              . 14 agents one-shot · Devstral Small 2 + Codestral · zéro 429.
            </p>
            <ul>
              <li>Devstral → review, debug, impl plan, tests</li>
              <li>Codestral → SQL, regex, Docker, OpenAPI</li>
              <li>Rate-gate par modèle (30s / 20s)</li>
            </ul>
            <button onClick={() => (hasKey ? setStep("done") : setStep("key"))}>
              {hasKey ? "Entrer →" : "Configurer la clé →"}
            </button>
          </>
        )}
        {step === "key" && (
          <>
            <h1>Clé La Plateforme</h1>
            <p>
              Stockée dans <code>devstral-lab/.env</code> (gitignoré).{" "}
              <a href="https://console.mistral.ai" target="_blank" rel="noreferrer">
                console.mistral.ai →
              </a>
            </p>
            <input
              type="password"
              placeholder="MISTRAL_API_KEY"
              value={apiKey}
              onChange={(e) => setApiKey(e.target.value)}
            />
            {error && <div className="ob-err">{error}</div>}
            <button disabled={apiKey.length < 20 || loading} onClick={handleSave}>
              {loading ? "Validation…" : "Enregistrer"}
            </button>
          </>
        )}
        {step === "done" && (
          <>
            <h1>✓ Prêt</h1>
            <p>Commence par <strong>Lab Review</strong> ou <strong>Lab Impl</strong>.</p>
            <button onClick={finish}>Lancer le Lab →</button>
          </>
        )}
      </div>
      <style>{`
        .ob-overlay { position:fixed; inset:0; z-index:100; background:#0c0c10ee;
          display:flex; align-items:center; justify-content:center; padding:1.5rem; }
        .ob-card { max-width:480px; background:var(--surface); border:1px solid var(--border);
          border-radius:14px; padding:2rem; }
        .ob-card h1 { margin-bottom:.75rem; font-size:1.4rem; }
        .ob-card p, .ob-card li { color:var(--muted); line-height:1.6; margin-bottom:.75rem; }
        .ob-card a { color:var(--accent); }
        .ob-card ul { padding-left:1.2rem; margin-bottom:1rem; }
        .ob-card input { width:100%; padding:.75rem; border-radius:8px; border:1px solid var(--border);
          background:var(--bg); color:var(--text); font-family:var(--mono); margin-bottom:1rem; }
        .ob-card button { padding:.7rem 1.2rem; border-radius:8px; border:none; background:var(--accent);
          color:#fff; font-weight:600; cursor:pointer; }
        .ob-card button:disabled { opacity:.4; cursor:not-allowed; }
        .ob-err { color:var(--red); font-size:.85rem; margin-bottom:.75rem; }
      `}</style>
    </div>
  );
}