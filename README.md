# Portfolio Chatbot - Valentin Dujour

## 📋 Description

Chatbot intelligent basé sur l'IA permettant de répondre aux questions sur mon parcours, mes compétences et mes projets. L'application utilise une base de données vectorielle Upstash et l'API Groq pour générer des réponses contextuelles et personnalisées.

---

## 🚀 Fonctionnalités

- ✨ **Chatbot conversationnel** avec interface Streamlit intuitive
- 💡 **Questions suggérées** pré-configurées pour faciliter l'interaction
- 🔢 **Limite de 5 questions** par session pour optimiser l'utilisation de l'API
- 🔍 **Recherche sémantique** dans une base de données vectorielle
- 🤖 **Réponses générées par IA** via l'API Groq (modèle gpt-oss-120b)

---

## 🛠️ Technologies utilisées

| Technologie | Usage |
|-------------|-------|
| **Python 3.12+** | Langage de programmation |
| **Streamlit** | Interface utilisateur interactive |
| **OpenAI Agents** | Framework pour l'orchestration de l'agent IA |
| **Groq API** | Modèle de langage (gpt-oss-120b) |
| **Upstash Vector** | Base de données vectorielle pour la recherche sémantique |
| **python-dotenv** | Gestion sécurisée des variables d'environnement |

---

## 📁 Structure du projet

```
projet-iut-potfolio/
├── data/ (Fichier poussés dans upstash)
│   ├── 01-presentation.md
│   ├── 02-alternance.md
│   ├── 03-projet.md
│   ├── 04-competence.md
│   └── 05-contact.md
├── src/ (Scripts python)
│   ├── agent.py
│   ├── app_streamlit.py
│   ├── instructions.txt
│   ├── load.py
│   ├── split.py
│   └── upstash.py
├── .env (Variables d'environnements)
├── requirements.txt (Dépendances pour le .venv)
└── README.md
```

## 🔧 Installation et configuration

### 1️⃣ Cloner le repository

```bash
git clone https://github.com/Vdujour/projet-iut-potfolio.git
cd projet-iut-potfolio
```

### 2️⃣ Créer un environnement virtuel

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

### 3️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4️⃣ Configuration des variables d'environnement

Créez un fichier `.env` à la racine du projet avec les variables suivantes :

```env
UPSTASH_VECTOR_REST_URL="votre_url_upstash"
UPSTASH_VECTOR_REST_TOKEN="votre_token_upstash"
GROQ_API_KEY="votre_clé_groq"
```

> **Note** : Le fichier `.env` est fourni par email et doit être placé à la racine du projet.

---

## 🗄️ Base de données vectorielle (Upstash)

### Création de l'index et chargement des données

Pour créer et alimenter la base de données Upstash Vector, exécutez simplement :

```bash
python src/upstash.py
```

**Ce script effectue automatiquement :**
1. 📂 **Chargement** des fichiers markdown via `load.py`
2. ✂️ **Découpage** en chunks via `split.py`
3. 📤 **Indexation** des données dans Upstash Vector

---

## 🤖 Fonctionnement de l'agent IA

### Configuration de l'agent

L'agent IA est configuré dans le fichier **`agent.py`**.

**Caractéristiques principales :**
- 🔧 **Modèle** : `openai/gpt-oss-120b` via l'API Groq
- 📝 **Instructions** : Définies dans `instructions.txt` pour contextualiser les réponses
- 🔍 **Outil** : Fonction `get_upstash_data()` pour interroger la base vectorielle

**Fonctionnement :**
1. L'utilisateur pose une question
2. L'agent utilise l'outil `get_upstash_data()` pour rechercher dans Upstash
3. Les informations pertinentes sont récupérées (top 5 résultats)
4. L'agent génère une réponse contextualisée avec mes données personnelles

---

## 💻 Lancement de l'application

### Mode développement (local)

Lancez l'application Streamlit avec la commande suivante :

```bash
streamlit run ./src/app_streamlit.py
```

L'application sera accessible à l'adresse : **http://localhost:8501**

### 🌐 Déploiement sur Streamlit Cloud

L'application est également déployée en ligne et accessible à l'adresse :

**🔗 https://chatbot-valentin-dujour.streamlit.app/**

---

## 📝 Utilisation

### Interface utilisateur

1. **Saisir une question** dans le champ de texte : *"Que veux-tu savoir ?"*
2. **Ou cliquer** sur l'une des questions suggérées

### Questions suggérées disponibles

- 📚 **Qui es-tu ?**
- 💼 **Parle-moi de ton alternance**
- 🚀 **Quels projets as-tu réalisés ?**
- 🛠️ **Quelles sont tes compétences ?**
- 📧 **Comment te contacter ?**
- 🌐 **Comment aller sur ton portfolio ?**

### ⚠️ Limitation des questions

- **5 questions maximum** par session
- Après la limite atteinte, l'agent redirige automatiquement vers mes informations de contact
- Cette limitation permet d'optimiser l'utilisation de la clé API et encourage le contact direct

---

## 🔐 Sécurité

- ✅ Les clés API sont stockées dans le fichier `.env` (non versionné sur Git)
- ✅ Les secrets sont configurés séparément sur Streamlit Cloud
- ✅ Aucune clé API n'est exposée dans le code source

---

## 👤 Auteur

**Valentin Dujour**  
Étudiant en 3ème année BUT Science des Données (BUT SD) en Alternance

- 📧 Email: [valentin.dujour@icloud.com](mailto:valentin.dujour@icloud.com)
- 💼 LinkedIn: [Valentin Dujour](https://www.linkedin.com/in/valentin-dujour-304b32279)
- 🌐 Portfolio: [vdujour.github.io](https://vdujour.github.io)

---