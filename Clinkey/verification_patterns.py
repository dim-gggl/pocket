#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from password_generator import PasswordGenerator
import re

def verifier_patterns():
    """Vérifie que les patterns générés correspondent aux exemples demandés."""
    
    print("🔍 VÉRIFICATION DES PATTERNS")
    print("=" * 40)
    
    generator = PasswordGenerator()
    
    # Test super_strong
    print("\n📋 VÉRIFICATION SUPER_STRONG()")
    print("-" * 30)
    print("Pattern attendu: MOT-CARACTERES-CHIFFRES-MOT-CARACTERES-CHIFFRES-MOT")
    print("Exemple attendu: GALIponti-342-^*-Soudu-810-/!_ù-XAHdertropil-007")
    
    for i in range(3):
        password = generator.super_strong()
        print(f"\nGénéré {i+1}: {password}")
        
        # Vérifier la structure
        parts = re.split(r'[-_.|]', password)
        print(f"  Parties: {parts}")
        print(f"  Nombre de parties: {len(parts)}")
        
        # Vérifier qu'il y a des caractères spéciaux
        special_chars = re.findall(r'[!@#$%^&*()_+\-=\[\]{}|\\:;"\'<>?,./~`ùàéèç]', password)
        print(f"  Caractères spéciaux trouvés: {special_chars}")
        
        # Vérifier qu'il y a des chiffres
        numbers = re.findall(r'\d+', password)
        print(f"  Blocs de chiffres: {numbers}")
    
    # Test strong
    print("\n📋 VÉRIFICATION STRONG()")
    print("-" * 30)
    print("Pattern attendu: MOT-CHIFFRES-MOT-CHIFFRES-MOT-CHIFFRES")
    print("Exemple attendu: FRAX-371120-trijacred-551-CloupDEONTREINE-93")
    
    for i in range(3):
        password = generator.strong()
        print(f"\nGénéré {i+1}: {password}")
        
        # Vérifier la structure
        parts = re.split(r'[-_.|]', password)
        print(f"  Parties: {parts}")
        print(f"  Nombre de parties: {len(parts)}")
        
        # Vérifier qu'il n'y a que des lettres et des chiffres
        letters_only = all(re.match(r'^[A-Za-z]+$', part) or re.match(r'^\d+$', part) for part in parts if part)
        print(f"  Uniquement lettres et chiffres: {letters_only}")
        
        # Vérifier qu'il y a des chiffres
        numbers = re.findall(r'\d+', password)
        print(f"  Blocs de chiffres: {numbers}")
    
    # Test normal
    print("\n📋 VÉRIFICATION NORMAL()")
    print("-" * 30)
    print("Pattern attendu: MOT-SEPARATEUR-MOT-SEPARATEUR-MOT-SEPARATEUR-MOT")
    print("Exemple attendu: RATIBULAX-CHAW-luc-feodrip-VARTEK")
    
    for i in range(3):
        password = generator.normal()
        print(f"\nGénéré {i+1}: {password}")
        
        # Vérifier la structure
        parts = re.split(r'[-_.|]', password)
        print(f"  Parties: {parts}")
        print(f"  Nombre de parties: {len(parts)}")
        
        # Vérifier qu'il n'y a que des lettres
        letters_only = all(re.match(r'^[A-Za-z]+$', part) for part in parts if part)
        print(f"  Uniquement des lettres: {letters_only}")
        
        # Vérifier les séparateurs
        separators = re.findall(r'[-_.|]', password)
        print(f"  Séparateurs utilisés: {separators}")
    
    print("\n✅ VÉRIFICATION TERMINÉE")
    print("=" * 40)

if __name__ == "__main__":
    verifier_patterns() 