# ============================================================
# config.py — Configuration centralisée
# ============================================================
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

# ── Hybrid Analysis (conservé pour référence) ──────────────
HYBRID_API_KEY    = os.getenv("HYBRID_ANALYSIS_API_KEY")
HYBRID_BASE_URL   = "https://www.hybrid-analysis.com/api/v2"
HYBRID_HEADERS    = {
    "api-key"     : HYBRID_API_KEY,
    "User-Agent"  : "Falcon Sandbox",
    "accept"      : "application/json"
}

# ── VirusTotal ─────────────────────────────────────────────
VIRUSTOTAL_API_KEY = os.getenv(
    "VIRUSTOTAL_API_KEY",
    "d7599862c774c3e02cb6332c9280eafa40ec4d4b9b36f23daf597cd7c2e1e502")
VT_BASE_URL        = "https://www.virustotal.com/api/v3"
VT_MAX_WAIT        = 120  # secondes max d'attente
VT_POLL_INTERVAL   = 15   # vérifier toutes les 15s

# ── MinIO ──────────────────────────────────────────────────
MINIO_ENDPOINT    = os.getenv("MINIO_ENDPOINT",
                               "localhost:9000")
MINIO_ACCESS_KEY  = os.getenv("MINIO_ACCESS_KEY",
                               "minioadmin")
MINIO_SECRET_KEY  = os.getenv("MINIO_SECRET_KEY",
                               "minioadmin")
MINIO_BUCKET      = os.getenv("MINIO_BUCKET",
                               "malware-benin")

# ── Chemins modèles et données ─────────────────────────────
MODEL_DIR         = os.getenv(
    "MODEL_DIR",
    r"C:\PFA_Malware\models")
PROCESSED_DIR     = os.getenv(
    "PROCESSED_DIR",
    r"C:\PFA_Malware\data\processed")

# ── Paramètres analyse ─────────────────────────────────────
MAX_FILE_SIZE_MB  = 200
ANALYSIS_TIMEOUT  = 600
POLLING_INTERVAL  = 30
SANDBOX_ENV       = 120

# ── Seuils Weighted Vote (depuis Phase 4) ──────────────────
THRESHOLDS = {
    'RF_malmem'  : 0.5,   'RF_ember'  : 0.5,
    'XGB_malmem' : 0.5,   'XGB_ember' : 0.5,
    'LGB_malmem' : 0.5,   'LGB_ember' : 0.5,
    'CNN_malmem' : 0.397, 'CNN_ember' : 0.478,
    'FT_malmem'  : 0.100, 'FT_ember'  : 0.414,
}

WEIGHTS_EMBER = {
    'RF'     : 0.9470, 'XGBoost': 1.0000,
    'LGB'    : 0.9851, 'CNN1D'  : 0.9641,
    'FT'     : 0.9481
}

WEIGHTS_MALMEM = {
    'RF'     : 0.9999, 'XGBoost': 1.0000,
    'LGB'    : 1.0000, 'CNN1D'  : 1.0000,
    'FT'     : 1.0000
}

# ── Poids réduits pour analyse dynamique VT ────────────────
# Moins fiables car features approximées depuis VT
# (pas de vraies features Volatility)
WEIGHTS_MALMEM_VT = {
    'RF'     : 0.5, 'XGBoost': 0.5,
    'LGB'    : 0.5, 'CNN1D'  : 0.5,
    'FT'     : 0.5
}

print("✅ Config chargée")