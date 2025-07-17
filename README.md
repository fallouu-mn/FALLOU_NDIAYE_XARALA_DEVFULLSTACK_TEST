![Diagramme d’architecture](./assets/diagramme.png)

## 🧭 Diagramme d’architecture

Ce schéma montre les interactions principales dans l’application.

```mermaid
graph TD
  Utilisateur((Utilisateur))
  Frontend[Frontend React.js]
  API[Backend API Django REST]
  DB[(Base de données SQLite)]

  Utilisateur -->|Navigateur| Frontend
  Frontend -->|fetch / axios| API
  API --> DB
