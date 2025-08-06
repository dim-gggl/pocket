#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse
import sys
from collections.abc import Generator

# Dictionnaire pour mapper les extensions de fichier aux identifiants de langage Markdown
# N'hésitez pas à l'étendre selon vos besoins.
LANG_MAP = {
    '.py': 'python',
    '.js': 'javascript',
    '.ts': 'typescript',
    '.html': 'html',
    '.css': 'css',
    '.scss': 'scss',
    '.json': 'json',
    '.xml': 'xml',
    '.yml': 'yaml',
    '.yaml': 'yaml',
    '.md': 'markdown',
    '.sh': 'bash',
    '.java': 'java',
    '.c': 'c',
    '.cpp': 'cpp',
    '.go': 'go',
    '.rs': 'rust',
    '.php': 'php',
    '.rb': 'ruby',
    '.sql': 'sql',
    '.dockerfile': 'dockerfile',
    'Dockerfile': 'dockerfile',
}

def get_language_identifier(filename: str) -> str:
    """
    Détermine l'identifiant de langage pour un bloc de code Markdown
    à partir de l'extension du nom de fichier.
    """
    # Gère les cas comme 'Dockerfile' qui n'a pas d'extension
    if os.path.basename(filename) in LANG_MAP:
        return LANG_MAP[os.path.basename(filename)]
    
    # Gère les extensions classiques
    _, ext = os.path.splitext(filename)
    return LANG_MAP.get(ext.lower(), 'plaintext')

def generate_tree(root_dir: str, exclude: set[str]) -> Generator[str, None, None]:
    """
    Génère une représentation textuelle de l'arborescence du projet,
    en excluant les fichiers et répertoires spécifiés.
    """
    # On utilise os.walk pour parcourir le répertoire
    for root, dirs, files in os.walk(root_dir, topdown=True):
        # Modification "in-place" pour que os.walk n'explore pas ces répertoires
        dirs[:] = [d for d in dirs if d not in exclude]
        files = [f for f in files if f not in exclude]

        level = root.replace(root_dir, '').count(os.sep)
        indent = '│   ' * (level - 1) + '├── ' if level > 0 else ''
        
        # Affiche le nom du répertoire courant (relatif)
        if level > 0:
            yield f"{indent}{os.path.basename(root)}/"

        # Affiche les fichiers du répertoire courant
        sub_indent = '│   ' * level + '├── '
        for i, f in enumerate(sorted(files)):
            # Utilise un préfixe différent pour le dernier élément
            prefix = '└── ' if i == len(files) - 1 else '├── '
            yield f"{'│   ' * level}{prefix}{f}"

def create_codebase_markdown(project_path: str, output_file: str, exclude_str: str) -> None:
    """
    Fonction principale qui scanne le projet et génère le fichier Markdown.
    """
    # Nettoyage des chemins et des exclusions
    project_path = os.path.abspath(project_path)
    project_name = os.path.basename(project_path)
    exclude_set = set(exclude_str.split(','))

    # Définition du nom de fichier de sortie par défaut si non fourni
    if output_file is None:
        output_file = f"{project_name}-1-file.md"

    print(f"🚀 Démarrage du scan du projet : '{project_name}'")
    print(f"📂 Répertoire source : {project_path}")
    print(f"📋 Fichier de destination : {output_file}")
    print(f"🙈 Éléments exclus : {exclude_set}")

    try:
        with open(output_file, 'w', encoding='utf-8') as md_file:
            # 1. Écrire le titre principal
            md_file.write(f"# {project_name}\n\n")

            # 2. Générer et écrire l'arborescence du projet
            print("🌳 Génération de l'arborescence...")
            md_file.write("```bash\n")
            md_file.write(f"{project_name}/\n")
            for line in generate_tree(project_path, exclude_set):
                md_file.write(f"{line}\n")
            md_file.write("```\n\n")
            print("✅ Arborescence générée.")

            # 3. Parcourir les fichiers et écrire leur contenu
            print("📝 Lecture et écriture du contenu des fichiers...")
            for root, dirs, files in os.walk(project_path, topdown=True):
                # On s'assure de ne pas descendre dans les répertoires exclus
                dirs[:] = [d for d in dirs if d not in exclude_set]
                
                for filename in sorted(files):
                    if filename in exclude_set:
                        continue

                    file_path = os.path.join(root, filename)
                    relative_path = os.path.relpath(file_path, project_path)
                    
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file_content:
                            content = file_content.read()
                            lang = get_language_identifier(filename)
                            
                            md_file.write("---\n\n") # Séparateur horizontal
                            md_file.write(f"**`{relative_path}`**:\n")
                            md_file.write(f"```{lang}\n")
                            md_file.write(content)
                            md_file.write("\n```\n\n")

                    except UnicodeDecodeError:
                        print(f"⚠️  Avertissement : Impossible de lire le fichier '{relative_path}' (probablement un binaire). Il sera ignoré.")
                    except Exception as e:
                        print(f"❌ Erreur lors de la lecture du fichier '{relative_path}': {e}")
            
            print("✅ Contenu des fichiers écrit.")

    except IOError as e:
        print(f"❌ Erreur d'écriture dans le fichier '{output_file}': {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Une erreur inattendue est survenue : {e}", file=sys.stderr)
        sys.exit(1)

    print(f"\n🎉 Succès ! La codebase a été compilée dans le fichier '{output_file}'")

def main():
    """
    Point d'entrée pour la gestion des arguments CLI.
    """
    parser = argparse.ArgumentParser(
        description="Scanne un projet de développement et génère un fichier Markdown unique contenant toute la codebase.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument(
        '-p', '--projet',
        default='.',
        help="Le répertoire racine du projet à scanner.\nPar défaut : le répertoire courant ('.')."
    )
    
    parser.add_argument(
        '-o', '--output',
        default=None,
        help="Le nom du fichier Markdown de destination.\nPar défaut : '<nom_du_projet>-1-file.md'."
    )
    
    default_exclude = "env,.env,venv,.venv,.gitignore,.git,.vscode,.idea,.cursor,lib,bin,site-packages,node_modules,__pycache__,.DS_Store"
    parser.add_argument(
        '-e', '--exclude',
        default=default_exclude,
        help=f"Une chaîne de noms de fichiers et de répertoires à ignorer, séparés par une virgule.\nPar défaut : \"{default_exclude}\"."
    )
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.projet):
        print(f"Erreur : Le chemin du projet '{args.projet}' n'existe pas ou n'est pas un répertoire.", file=sys.stderr)
        sys.exit(1)
        
    create_codebase_markdown(args.projet, args.output, args.exclude)

if __name__ == '__main__':
    main()
