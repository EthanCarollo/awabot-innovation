<div align="center">
  <img src="../../../website/public/logo_baseline.svg" alt="Awabot Logo" height="80" />
</div>

# Voxtral ASR Server (Mistral API Mode)

Ce serveur fournit un service de transcription (ASR) temps réel utilisant le modèle **Voxtral**.

## Mode de fonctionnement

Contrairement aux autres services de ce dépôt, ce backend **n'utilise pas de runtime local** (comme vLLM) pour exécuter le modèle Voxtral Realtime.

### Raison technique
Les cartes graphiques des postes utilisés pour le développement ne disposaient pas d'une mémoire vidéo (VRAM) suffisante pour charger et faire tourner le modèle **Voxtral-Mini-4B-Realtime** en local de manière fluide.

### Solution adoptée
Pour garantir les performances et la stabilité, nous utilisons le même modèle (**Voxtral Mini**) mais via l'**API Realtime de Mistral AI**. Cela permet de bénéficier de la puissance du modèle sans les contraintes matérielles locales.

## Configuration

Assurez-vous d'avoir une clé d'API valide dans le fichier `.env` :
```env
MISTRAL_API_KEY=votre_cle_ici
VOXTRAL_PORT=8082
VOXTRAL_MODEL=voxtral-mini-latest
```

## Installation

```bash
pip install -r requirements.txt
python server.py
```
