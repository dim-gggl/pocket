# Générateur de Mots de Passe Prononçables

## Description

Cette classe Python `PasswordGenerator` génère des mots de passe sécurisés qui sont **prononçables** et basés sur des syllabes françaises. Contrairement aux mots de passe aléatoires traditionnels, ces mots de passe sont plus faciles à mémoriser tout en restant sécurisés.

## Caractéristiques

- ✅ **Prononçables** : Basés sur des syllabes françaises réelles
- ✅ **Sécurisés** : Combinaison de lettres, chiffres et caractères spéciaux
- ✅ **Structurés** : Patterns cohérents et prévisibles
- ✅ **Variés** : Longueurs et séparateurs variables

## Installation

Aucune installation requise ! La classe utilise uniquement les modules Python standard (`random` et `string`).

```bash
# Téléchargez les fichiers
password_generator.py
test_password_generator.py
README.md
```

## Utilisation

### Import et création d'instance

```python
from password_generator import PasswordGenerator

# Créer une instance
generator = PasswordGenerator()
```

### Méthodes disponibles

#### 1. `super_strong()`
Génère un mot de passe avec lettres, chiffres et caractères spéciaux.

**Pattern :** `MOT-CARACTERES-CHIFFRES-MOT-CARACTERES-CHIFFRES-MOT`

**Exemple :** `GALIponti-342-^*-Soudu-810-/!_ù-XAHdertropil-007`

```python
password = generator.super_strong()
print(password)  # Ex: XIFALE_èç\_787-SOZR|é+]|247|NUJONINNUN_317
```

#### 2. `strong()`
Génère un mot de passe avec lettres et chiffres.

**Pattern :** `MOT-CHIFFRES-MOT-CHIFFRES-MOT-CHIFFRES`

**Exemple :** `FRAX-371120-trijacred-551-CloupDEONTREINE-93`

```python
password = generator.strong()
print(password)  # Ex: HILINZ-024815.NASOTRENINGRITR_907-PEBRECRIVR_82
```

#### 3. `normal()`
Génère un mot de passe avec seulement des lettres.

**Pattern :** `MOT-SEPARATEUR-MOT-SEPARATEUR-MOT-SEPARATEUR-MOT`

**Exemple :** `RATIBULAX-CHAW-luc-feodrip-VARTEK`

```python
password = generator.normal()
print(password)  # Ex: MEDOTREVEN_KOH_PECAF|BORETINN
```

## Méthodes privées

La classe utilise plusieurs méthodes privées pour générer les composants :

- `_generer_syllabe_simple()` : Syllabes de 2 lettres (consonne + voyelle)
- `_generer_syllabe_complexe()` : Syllabes de 3 lettres
- `_generer_mot_prononcable()` : Mots complets basés sur des syllabes
- `_generer_bloc_chiffres()` : Blocs de chiffres
- `_generer_bloc_caracteres_speciaux()` : Blocs de caractères spéciaux
- `_generer_separateur()` : Séparateurs entre les blocs

## Exemple complet

```python
from password_generator import PasswordGenerator

# Créer le générateur
generator = PasswordGenerator()

# Générer différents types de mots de passe
print("Super Strong:", generator.super_strong())
print("Strong:", generator.strong())
print("Normal:", generator.normal())
```

## Test et démonstration

Pour voir des exemples de mots de passe générés :

```bash
# Test simple
python password_generator.py

# Test complet avec démonstration
python test_password_generator.py
```

## Syllabes utilisées

La classe utilise des syllabes françaises courantes :

- **Syllabes simples** : BA, BE, BI, BO, BU, CA, CE, CI, CO, CU, etc.
- **Syllabes complexes** : TRE, TRI, TRO, TRA, DRE, DRI, DRO, DRA, etc.
- **Caractères spéciaux** : !, @, #, $, %, ^, &, *, (, ), -, _, +, =, etc.
- **Séparateurs** : -, _, ., |

## Sécurité

- Les mots de passe sont générés de manière aléatoire
- Chaque appel produit un résultat différent
- Les patterns respectent les bonnes pratiques de sécurité
- Les longueurs sont variables pour éviter les attaques par dictionnaire

## Avantages

1. **Mémorisation facile** : Les syllabes françaises sont plus faciles à retenir
2. **Sécurité maintenue** : Complexité suffisante pour résister aux attaques
3. **Flexibilité** : Trois niveaux de sécurité différents
4. **Prononçabilité** : Possibilité de "lire" le mot de passe à haute voix

## Licence

Ce code est fourni à des fins éducatives et d'utilisation personnelle. 