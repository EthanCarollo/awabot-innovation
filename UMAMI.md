<p align="center">
  <table>
    <tr>
      <td align="center" style="border: none;">
        <img src="website/public/umami.png" width="200" alt="Umami Logo"><br>
        <b>Umami Analytics</b>
      </td>
      <td align="center" style="border: none; padding: 0 40px;">
        <img src="https://img.icons8.com/ios-filled/50/FAC130/plus-math.png" alt="Plus Icon">
      </td>
      <td align="center" style="border: none;">
        <img src="website/public/logo_baseline.svg" width="200" alt="Awabot Logo"><br>
        <b>Awabot</b>
      </td>
    </tr>
  </table>
</p>

# Umami — Analytics respectueux de la vie privée

[Umami](https://umami.is/) est une solution d'analytics web **open-source** et **auto-hébergeable**, utilisée comme alternative à Google Analytics.

## Pourquoi Umami ?

| Critère | Google Analytics | Umami |
|---|---|---|
| **Vie privée** | Collecte de données utilisateur, cookies | Aucun cookie, conforme RGPD |
| **Hébergement** | Cloud Google | Auto-hébergé (souveraineté totale) |
| **Performance** | Script lourd (~45 KB) | Script léger (~2 KB) |
| **Complexité** | Interface surchargée | Interface simple et lisible |
| **Coût** | Gratuit (données = le produit) | Gratuit et open-source |

## Installation

### 1. Docker Compose (suggestion)

> L'exemple ci-dessous est une **suggestion de configuration** pour un deploiement rapide.
> Il n'est pas obligatoire d'utiliser Docker ; Umami peut etre installe de multiples facons
> (voir la [documentation officielle](https://umami.is/docs/install)).

Creer un fichier `docker-compose.yml` :

```yaml
version: '3'
services:
  umami:
    image: ghcr.io/umami-software/umami:postgresql-latest
    ports:
      - "3333:3000"
    environment:
      DATABASE_URL: postgresql://umami:umami@db:5432/umami
      DATABASE_TYPE: postgresql
      APP_SECRET: votre-secret-aleatoire
    depends_on:
      db:
        condition: service_healthy
    restart: always

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: umami
      POSTGRES_USER: umami
      POSTGRES_PASSWORD: umami
    volumes:
      - umami-db-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U umami"]
      interval: 5s
      timeout: 5s
      retries: 5
    restart: always

volumes:
  umami-db-data:
```

Lancer :

```bash
docker compose up -d
```

> Accessible sur [http://localhost:3333](http://localhost:3333)
> Login par défaut : `admin` / `umami`

### 2. Intégration dans Nuxt.js

Installer le module :

```bash
npm install nuxt-umami
```

Ajouter dans `nuxt.config.ts` :

```typescript
export default defineNuxtConfig({
  modules: ['nuxt-umami'],

  umami: {
    id: 'votre-website-id',       // ID du site dans Umami
    host: 'https://analytics.votredomaine.com',
    autoTrack: true,
    ignoreLocalhost: true,
  },
})
```

### 3. Récupérer l'ID du site

1. Se connecter à Umami (`http://localhost:3333`)
2. Aller dans **Settings > Websites > Add website**
3. Entrer le nom et le domaine du site
4. Copier le **Website ID** généré
5. Le coller dans la config Nuxt (`umami.id`)

## Ressources

- [Documentation officielle](https://umami.is/docs)
- [Repository GitHub](https://github.com/umami-software/umami)
- [Module nuxt-umami](https://github.com/ijkml/nuxt-umami)
