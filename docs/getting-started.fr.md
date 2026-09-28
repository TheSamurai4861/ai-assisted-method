# Bien démarrer avec la méthode d'ingénierie assistée par IA

[English](getting-started.md) · [Présentation du projet](../README.md) · [Méthode de référence](../.ai/METHOD.md)

Ce guide vous accompagne de l'installation à votre premier changement vérifié. La méthode fonctionne avec un agent de code capable de lire les instructions du dépôt. Vous n'avez pas besoin d'utiliser tous les modèles dès le premier jour.

> **L'idée :** l'agent peut inspecter, proposer, implémenter et vérifier rapidement. Vous gardez la main sur les choix importants, les risques acceptés et la décision finale.

## 1. Installer la méthode dans votre projet

Ouvrez un terminal **à la racine du projet qui utilisera la méthode**. Installez [`uv`](https://docs.astral.sh/uv/getting-started/installation/) pour l'installation en une commande. Le paquet nécessite Python 3.10 ou plus récent ; `uv` peut utiliser un interpréteur déjà installé ou en gérer un.

```sh
uvx --from "git+https://github.com/TheSamurai4861/ai-assisted-method.git" ai-assisted-method
```

Pour prévisualiser un mode d'installation sans modifier de fichier, ajoutez `--dry-run` et le mode. Si des fichiers diffèrent, l'installateur interactif propose **Update**, **Separate**, **Replace** ou **Cancel**. Dans un terminal non interactif, indiquez `--mode` explicitement.

| Situation | Option | Effet |
|---|---|---|
| Nouveau projet, aucun conflit | aucune | Installe `AGENTS.md`, `.ai/` et `prompts/` |
| Méthode AI-Assisted déjà présente | `--mode update` | Sauvegarde et actualise les règles ; conserve vos `PROJECT_MAP.md`, `VERIFICATION.md` et `RESOURCES.md` |
| Autre méthode ou conflit incertain | `--mode separate` | Place une copie à comparer dans `.ai/ai-assisted-method/` ; conserve les fichiers existants |
| Réinitialisation volontaire | `--mode replace` | Sauvegarde et remplace les fichiers correspondants, y compris les modèles propres au projet |

Par exemple, pour prévisualiser une mise à jour :

```sh
uvx --from "git+https://github.com/TheSamurai4861/ai-assisted-method.git" ai-assisted-method --mode update --dry-run
```

L'installateur préserve les instructions situées hors de son bloc géré dans un `AGENTS.md` existant. Il ne fusionne pas automatiquement des règles contradictoires. Les sauvegardes des modes Update et Replace se trouvent dans `.ai/ai-assisted-method-backups/` et sont ignorées par Git dans ce dossier. Relisez les règles de sécurité et les paramètres du projet qui ont changé avant de vous y fier.

Si vous n'utilisez pas `uv`, clonez ce dépôt et lancez `python /chemin/vers/ai-assisted-method/scripts/install.py` depuis la racine de votre projet. Les mêmes options `--mode` et `--dry-run` sont disponibles.

## 2. Adapter la méthode à votre projet réel

L'installation apporte une méthode réutilisable, pas une connaissance de votre code. Donnez à votre agent [`prompts/bootstrap-new-project.md`](../prompts/bootstrap-new-project.md), ou demandez-lui :

> Lis `AGENTS.md` et `prompts/bootstrap-new-project.md`. Inspecte ce dépôt, puis renseigne la carte de l'état actuel du projet et ses vraies commandes de vérification. Préserve les règles existantes. Ne modifie pas le code produit.

Relisez ensuite deux fichiers avec l'agent :

- [`.ai/PROJECT_MAP.md`](../.ai/PROJECT_MAP.md) doit décrire **l'état actuel observé** : stack, points d'entrée, frontières importantes et contraintes confirmées. Les inconnues doivent rester indiquées comme telles.
- [`.ai/VERIFICATION.md`](../.ai/VERIFICATION.md) doit contenir des commandes qui fonctionnent vraiment dans ce projet. Exécutez-les une fois. Un modèle copié ne prouve pas que les contrôles existent.

Le [registre de ressources](../.ai/RESOURCES.md) est vide au départ. Le bootstrap ne doit ni inventer des références, ni en ajouter sans votre accord.

## 3. Lancer une vraie tâche

Décrivez le résultat voulu avec vos mots, puis indiquez [`prompts/start-task.md`](../prompts/start-task.md) à l'agent. Par exemple :

> Utilise `prompts/start-task.md`. Corrige le total des factures lorsque la remise est appliquée deux fois. Conserve l'API publique. Montre le cas qui échoue, puis vérifie la correction.

L'agent identifie d'abord **l'intention**, le type de tâche et le risque S/M/H. Il comprend le comportement actuel avant tout changement significatif. Pour un risque moyen ou élevé, il rédige des critères d'acceptation et un plan concis avec [`.ai/TASK_TEMPLATE.md`](../.ai/TASK_TEMPLATE.md). Si la direction est claire et les étapes réversibles, il peut avancer sans demander votre accord à chaque modification.

| Risque | Démarche habituelle | Votre rôle |
|---|---|---|
| **S** : local et facile à annuler | Comprendre, modifier, vérifier | Examiner le résultat |
| **M** : comportement significatif ou plusieurs composants | Critères d'acceptation, plan, vérification, revue | Trancher les choix de produit ou de conception importants, puis accepter le résultat |
| **H** : sécurité, données, architecture ou impact difficile à annuler | Plan progressif, preuves renforcées, revue indépendante | Approuver les actions sensibles et accepter explicitement les risques restants |

Le risque dépend de **l'impact d'une erreur**, pas du nombre de lignes modifiées. La [méthode](../.ai/METHOD.md) fait autorité pour le déroulement précis.

## 4. Examiner le résultat

Demandez un résumé de ce qui a changé, du choix effectué, des critères satisfaits et des preuves correspondantes. Exécutez ou examinez les contrôles utiles. Des tests au vert aident, mais ne prouvent pas automatiquement que le choix produit est bon.

Si une hypothèse importante s'avère fausse, renvoyez l'agent à `PLAN` ou `SPEC`. Si le résultat soulève un choix conséquent, prenez cette décision vous-même. Vous seul donnez l'acceptation finale.

L'[exemple de fonctionnalité](../examples/FEATURE_EXAMPLE.md) illustre une tâche de risque moyen, de l'intention à l'acceptation humaine. L'[exemple de maintenance](../examples/MAINTENANCE_EXAMPLE.md) montre la simplicité attendue pour une petite tâche.

## 5. Utiliser des ressources approuvées, quand elles servent

Vous pouvez demander : **« Quelles ressources seraient utiles pour ce projet ? »** L'agent peut suivre [`prompts/resource-discovery.md`](../prompts/resource-discovery.md) : inspecter la stack réelle, repérer les besoins, rechercher et comparer des sources fiables si Internet est disponible, puis proposer une courte sélection. Il ne met à jour `.ai/RESOURCES.md` **qu'après votre validation de références précises**.

Une référence approuvée est consultée lorsque son domaine compte pour une tâche. Elle ne remplace ni vos décisions, ni les règles du projet, ni ses contraintes observées, ni la documentation officielle actuelle. Gardez une liste courte et retirez les références obsolètes avec un accord explicite. Ne copiez pas de livres protégés ou de longs contenus externes dans le dépôt sans disposer des droits nécessaires.

## Situations courantes

### Le projet possède déjà des règles pour les agents

Conservez-les. L'installateur préserve le contenu de `AGENTS.md` hors de son bloc géré et ne modifie pas les autres fichiers d'instructions pour agents. Pendant le bootstrap, demandez à l'agent de relever les conflits importants. Résolvez-les avant de considérer un ensemble de règles comme prioritaire.

### L'installation signale des fichiers différents

Choisissez le mode selon le rôle de ces fichiers dans votre projet. **Update** convient à une installation AI-Assisted antérieure dont vous souhaitez conserver la carte du projet, les commandes de vérification et les ressources approuvées. **Separate** permet de comparer deux méthodes sans en déplacer aucune. **Replace** convient à une réinitialisation volontaire des fichiers correspondants ; examinez ensuite la sauvegarde. Un choix invalide ou une annulation ne modifie rien.

### J'ai installé une copie séparée

Commencez par `.ai/ai-assisted-method/prompts/bootstrap-new-project.md`. La copie installée à part ne devient pas automatiquement prioritaire. Comparez-la aux règles existantes et décidez comment les faire coexister avant de l'appliquer au travail de développement.

### Aucun workflow spécialisé ne correspond à ma tâche

Utilisez [`prompts/start-task.md`](../prompts/start-task.md) et la méthode générale. Un workflow dédié n'existe que si le type de tâche demande des preuves ou des préconditions particulières ; chaque catégorie n'a pas besoin de son propre fichier.

### L'agent demande trop souvent mon accord

Précisez le résultat attendu, les limites et les critères d'acceptation. L'agent peut exécuter sans interruption les étapes claires, bornées, réversibles et vérifiables. Il doit toutefois vous soumettre les choix produit importants et obtenir l'accord requis pour les actions sensibles ou difficiles à annuler selon [`.ai/SECURITY.md`](../.ai/SECURITY.md).

### Un contrôle échoue, ou les tests passent sans me convaincre

Laissez les échecs visibles et cherchez leur cause. Comparez les preuves aux critères d'acceptation et au comportement réel. Des tests réussis sont des éléments de preuve, pas une acceptation finale. Ne désactivez pas un contrôle simplement pour obtenir du vert.

### Je n'ai pas accès à Internet

La méthode et l'installateur peuvent fonctionner depuis un clone local. Pour la découverte de ressources, l'agent doit signaler cette limite et ne jamais inventer de sources. Une référence pourra être proposée plus tard, lorsque sa source pourra être vérifiée.

## Pour continuer

- [`AGENTS.md`](../AGENTS.md) : point d'entrée court pour les agents.
- [`.ai/METHOD.md`](../.ai/METHOD.md) : déroulement et propriété des décisions.
- [`.ai/SECURITY.md`](../.ai/SECURITY.md) : actions sensibles et accords requis.
- [`prompts/`](../prompts/) : amorces réutilisables pour les tâches.
- [`examples/`](../examples/) : exemples illustratifs à plusieurs niveaux de risque.

Commencez par une vraie tâche. Gardez les règles et les contrôles utiles ; utilisez `LEARN` pour améliorer la méthode à partir d'échecs observés plutôt que d'accumuler des procédures.
