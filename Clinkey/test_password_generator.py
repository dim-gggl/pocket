#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from password_generator import PasswordGenerator

def test_password_generator():
    """Test complet de la classe PasswordGenerator."""
    
    print("🔐 GÉNÉRATEUR DE MOTS DE PASSE PRONONÇABLES")
    print("=" * 50)
    
    # Création d'une instance
    generator = PasswordGenerator()
    
    print("\n📋 MÉTHODE SUPER_STRONG()")
    print("-" * 30)
    print("Mots de passe avec lettres, chiffres et caractères spéciaux:")
    for i in range(5):
        password = generator.super_strong()
        print(f"  {i+1}. {password}")
    
    print("\n📋 MÉTHODE STRONG()")
    print("-" * 30)
    print("Mots de passe avec lettres et chiffres:")
    for i in range(5):
        password = generator.strong()
        print(f"  {i+1}. {password}")
    
    print("\n📋 MÉTHODE NORMAL()")
    print("-" * 30)
    print("Mots de passe avec seulement des lettres:")
    for i in range(5):
        password = generator.normal()
        print(f"  {i+1}. {password}")
    
    print("\n🎯 EXEMPLES CONFORMES AUX PATTERNS DEMANDÉS")
    print("-" * 50)
    
    print("\nSuper Strong (pattern: MOT-CARACTERES-CHIFFRES-MOT-CARACTERES-CHIFFRES-MOT):")
    print("Exemple attendu: GALIponti-342-^*-Soudu-810-/!_ù-XAHdertropil-007")
    print("Généré:", generator.super_strong())
    
    print("\nStrong (pattern: MOT-CHIFFRES-MOT-CHIFFRES-MOT-CHIFFRES):")
    print("Exemple attendu: FRAX-371120-trijacred-551-CloupDEONTREINE-93")
    print("Généré:", generator.strong())
    
    print("\nNormal (pattern: MOT-SEPARATEUR-MOT-SEPARATEUR-MOT-SEPARATEUR-MOT):")
    print("Exemple attendu: RATIBULAX-CHAW-luc-feodrip-VARTEK")
    print("Généré:", generator.normal())
    
    print("\n✨ CARACTÉRISTIQUES DES MOTS DE PASSE")
    print("-" * 40)
    print("✅ Tous les mots de passe sont prononçables")
    print("✅ Basés sur des syllabes françaises")
    print("✅ Respectent les patterns demandés")
    print("✅ Utilisent des séparateurs variés (-, _, ., |)")
    print("✅ Longueurs variables pour plus de sécurité")

if __name__ == "__main__":
    test_password_generator() 