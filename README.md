
# Analyseur d'URL avec VirusTotal

Ce script Python permet d'analyser une liste d'URL en utilisant l'API de VirusTotal et de sauvegarder les résultats dans un fichier JSON.

## Prérequis

Avant d'exécuter ce script, vous devez installer les bibliothèques Python nécessaires. Vous pouvez les installer en utilisant `pip` :

```bash
pip install requests
```

## Configuration

1. **Clé API** : Obtenez une clé API de VirusTotal en créant un compte sur [VirusTotal](https://www.virustotal.com/).
2. **Fichier CSV** : Préparez un fichier CSV nommé `urls.csv` contenant les URL à analyser. Chaque URL doit être sur une nouvelle ligne.
3. **Chemins des fichiers** : Modifiez les variables `CSV_FILE_PATH` et `OUTPUT_FILE_PATH` si nécessaire.

## Utilisation

1. Ajoutez votre clé API dans la variable `API_KEY` du script.
2. Exécutez le script en utilisant la commande suivante :

```bash
python script.py
```

## Description du Script

Le script effectue les étapes suivantes :

1. Lit les URL à partir d'un fichier CSV.
2. Envoie chaque URL à VirusTotal pour obtenir un ID d'analyse.
3. Attend un certain intervalle de temps pour permettre à l'analyse de se compléter.
4. Récupère le rapport d'analyse pour chaque URL.
5. Sauvegarde les résultats dans un fichier JSON.

## Détails des Fonctions

### `read_urls_from_csv(file_path)`

Lit les URL à partir d'un fichier CSV et retourne une liste d'URL.

### `get_analysis_id(url, api_key)`

Soumet une URL à VirusTotal et retourne l'ID de l'analyse.

### `get_analysis_report(analysis_id, api_key)`

Récupère le rapport d'analyse à partir de l'ID de l'analyse.

### `main()`

La fonction principale qui orchestre l'exécution du script.

## Paramètres

- `API_KEY` : Votre clé API VirusTotal.
- `CSV_FILE_PATH` : Chemin vers le fichier CSV contenant les URL.
- `OUTPUT_FILE_PATH` : Chemin vers le fichier JSON où les résultats seront sauvegardés.
- `POLL_INTERVAL` : Intervalle de temps (en secondes) entre les requêtes pour éviter de dépasser les limites de l'API.

## Exemple de CSV

```csv
http://example.com
http://example.org
http://example.net
```

## Exemple de Résultat JSON

```json
[
    {
        "url": "http://example.com",
        "analysis_id": "example-analysis-id",
        "report": {
            "data": {
                "attributes": {
                    "last_analysis_stats": {
                        "harmless": 70,
                        "malicious": 1,
                        "suspicious": 0,
                        "undetected": 5
                    }
                }
            }
        }
    }
]
```

## Remarques

- Assurez-vous de respecter les limites de requêtes de l'API de VirusTotal.
- Ce script est conçu pour des fins éducatives et doit être utilisé de manière responsable.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
