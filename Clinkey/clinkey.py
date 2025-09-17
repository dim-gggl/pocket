import random
import string
import argparse

from clinkey_view import ClinkeyView


ALPHABET = [char for char in string.ascii_letters.upper()]
VOWELS = ['A', 'E', 'I', 'O', 'U', 'Y']
CONSONANTS = [char for char in ALPHABET if char not in VOWELS]
FIGURES = [char for char in string.digits]
SPECIALS = [char for char in string.punctuation if char not in ['-', '_']]

SYLLABES = []
for c in CONSONANTS:
    for v in VOWELS:
        SYLLABES.append(c + v)
        
SYLLABES_COMPLEXES = ['TRE', 'TRI', 'TRO', 'TRA', 'TRE', 'TRI', 'TRO', 'TRA', 'DRE', 'DRI', 'DRO', 'DRA',
                    'BRE', 'BRI', 'BRO', 'BRA', 'CRE', 'CRI', 'CRO', 'CRA', 'FRE', 'FRI', 'FRO', 'FRA',
                    'GRE', 'GRI', 'GRO', 'GRA', 'PRE', 'PRI', 'PRO', 'PRA', 'SRE', 'SRI', 'SRO', 'SRA',
                    'VRE', 'VRI', 'VRO', 'VRA', 'ZRE', 'ZRI', 'ZRO', 'ZRA', 'LON', 'LEN', 'LIN', 'LAN',
                    'MON', 'MEN', 'MIN', 'MAN', 'NON', 'NEN', 'NIN', 'NAN', 'PON', 'PEN', 'PIN', 'PAN',
                    'RON', 'REN', 'RIN', 'RAN', 'SON', 'SEN', 'SIN', 'SAN', 'TON', 'TEN', 'TIN', 'TAN',
                    'VON', 'VEN', 'VIN', 'VAN', 'ZON', 'ZEN', 'ZIN', 'ZAN']

class Clinkey(ClinkeyView):
    """
    Generate pronounceable passwords based on French syllables.
    """
    
    def __init__(self) -> None:
        """
        Initialize the generator with the French syllables.
        """
        # Common French syllables
        self._consonnes = CONSONANTS
        self._voyelles = VOWELS
        self._syllabes_simples = SYLLABES
        
        # More complex syllables
        self._syllabes_complexes = SYLLABES_COMPLEXES
        
        # Special characters for super_strong
        self._caracteres_speciaux = SPECIALS
        
        # Numbers
        self._chiffres = FIGURES
    
    def _generate_simple_syllable(self) -> str:
        """
        Generate a simple syllable of 2 letters (consonant + vowel).
        """
        return random.choice(self._syllabes_simples)
    
    def _generate_complex_syllable(self) -> str:
        """
        Generate a complex syllable of 3 letters.
        """
        return random.choice(self._syllabes_complexes)
    
    def _generate_pronounceable_word(self, min_length: int = 4, max_length: int = 8) -> str:
        """
        Generate a pronounceable word of variable length.
        """
        mot = ""
        longueur = random.randint(min_length, max_length)
        
        # Start with a simple syllable
        mot += self._generate_simple_syllable()
        
        # Add additional syllables
        while len(mot) < longueur:
            if random.choice([True, False]):
                mot += self._generate_simple_syllable()
            else:
                mot += self._generate_complex_syllable()
        
        # Truncate if necessary
        return mot[:longueur]
    
    def _generate_number_block(self, longueur: int = 3) -> str:
        """
        Generate a block of numbers.
        """
        return ''.join(random.choices(self._chiffres, k=longueur))
    
    def _generate_special_characters_block(self, longueur: int = 3) -> str:
        """
        Generate a block of special characters.
        """
        return ''.join(random.choices(self._caracteres_speciaux, k=longueur))
    
    def _generate_separator(self) -> str:
        """
        Generate a separator between blocks.
        """
        return random.choice(['-', '_'])
    
    def super_strong(self) -> str:
        """
        Generate a super strong password with letters, numbers and special characters.
        Pattern: MOT-CARACTERES-CHIFFRES-MOT-CARACTERES-CHIFFRES-MOT
        """
        words = []
        rint = random.randint
        for _ in range(3):
            words.append(self._generate_pronounceable_word(rint(4, 6), rint(8, 12)))

        figures = []
        for _ in range(3):
            figures.append(self._generate_number_block(rint(3, 6)))

        specials = []
        for _ in range(2):  # Retour à 2 car on n'a besoin que de 2 blocs de caractères spéciaux
            specials.append(self._generate_special_characters_block(rint(3, 6)))
        
        seps = []
        for _ in range(6):
            seps.append(self._generate_separator())

        result = ""
        # Première itération : MOT-CARACTERES-CHIFFRES
        result += words.pop() + seps.pop() + specials.pop() + seps.pop() + figures.pop() + seps.pop()
        # Deuxième itération : MOT-CARACTERES-CHIFFRES  
        result += words.pop() + seps.pop() + specials.pop() + seps.pop() + figures.pop() + seps.pop()
        # Troisième itération : MOT (le dernier mot)
        result += words.pop()
        
        return result.strip()
    
    def strong(self) -> str:
        """
        Generate a strong password with letters and numbers.
        Pattern: MOT-CHIFFRES-MOT-CHIFFRES-MOT-CHIFFRES
        """
        words = []
        rint = random.randint
        for _ in range(3):
            words.append(self._generate_pronounceable_word(rint(4, 6), rint(8, 12)))

        figures = []
        for _ in range(3):
            figures.append(self._generate_number_block(rint(3, 6)))
        
        seps = []
        for _ in range(6):
            seps.append(self._generate_separator())
        
        result = ""
        for _ in range(3):
            result += words.pop(0) + seps.pop(0) + figures.pop(0) + seps.pop(0)
        
        return result.strip()
    
    def normal(self) -> str:
        """
        Generate a normal password with only letters.
        Pattern: MOT-SEPARATEUR-MOT-SEPARATEUR-MOT-SEPARATEUR-MOT
        """
        words = []
        rint = random.randint
        for _ in range(3):
            words.append(self._generate_pronounceable_word(rint(4, 6), rint(8, 12)))

        seps = []
        for _ in range(6):
            seps.append(self._generate_separator())
        
        result = ""
        for _ in range(3):
            result += words.pop(0) + seps.pop(0)
        
        return result.strip()
    
    def generate_password(self, method):
        result = ""
        while len(result) < 128:
            result += method()
        return result

def parse_args():
    parser = argparse.ArgumentParser(description="Generate pronounceable passwords based on French syllables.")
    parser.add_argument("-n", "--number", type=int, default=1, help="Number of passwords to generate")
    parser.add_argument("-l", "--length", type=int, default=32, help="Length of the passwords")
    parser.add_argument("-t", "--type", type=str, default="strong", help="Type of the passwords")
    parser.add_argument("-o", "--output", type=str, default="", help="Output file")
    parser.add_argument("--lower", action="store_true", help="Lowercase the passwords")
    parser.add_argument("--no-separator", "--no-sep", action="store_true", help="No separator between blocks")
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    clinkey = Clinkey()
    number = int(args.number)
    length = int(args.length)
    type = args.type
    output = args.output
    lower = args.lower
    no_separator = args.no_separator
    action = {
        "super_strong": clinkey.super_strong,
        "strong": clinkey.strong,
        "normal": clinkey.normal
    }
    passwords = []
    for _ in range(number):
        passwords.append(clinkey.generate_password(action[type])[0:length])
    if lower:
        passwords = [password.lower() for password in passwords]
    if no_separator:
        passwords = [password.replace("-", "").replace("_", "") for password in passwords]
    
    if output:
        with open(output, "w") as file:
            for password in passwords:
                file.write(password.rstrip("_").rstrip("-").lstrip("_").lstrip("-") + "\n")
        print(f"Passwords saved to {output}")
    else:
        for password in passwords:
            print(password)


if __name__ == "__main__":
    main()