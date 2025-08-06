import random
import string

from clinkey_view import ClinkeyView


class Clinkey(ClinkeyView):
    """
    Generate pronounceable passwords based on French syllables.
    """
    
    def __init__(self) -> None:
        """
        Initialize the generator with the French syllables.
        """
        # Common French syllables
        self._consonnes = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
        self._voyelles = ['A', 'E', 'I', 'O', 'U', 'Y']
        self._syllabes_simples = ['BA', 'BE', 'BI', 'BO', 'BU', 'CA', 'CE', 'CI', 'CO', 'CU', 'DA', 'DE', 'DI', 'DO', 'DU',
                                 'FA', 'FE', 'FI', 'FO', 'FU', 'GA', 'GE', 'GI', 'GO', 'GU', 'HA', 'HE', 'HI', 'HO', 'HU',
                                 'JA', 'JE', 'JI', 'JO', 'JU', 'KA', 'KE', 'KI', 'KO', 'KU', 'LA', 'LE', 'LI', 'LO', 'LU',
                                 'MA', 'ME', 'MI', 'MO', 'MU', 'NA', 'NE', 'NI', 'NO', 'NU', 'PA', 'PE', 'PI', 'PO', 'PU',
                                 'RA', 'RE', 'RI', 'RO', 'RU', 'SA', 'SE', 'SI', 'SO', 'SU', 'TA', 'TE', 'TI', 'TO', 'TU',
                                 'VA', 'VE', 'VI', 'VO', 'VU', 'WA', 'WE', 'WI', 'WO', 'WU', 'XA', 'XE', 'XI', 'XO', 'XU',
                                 'ZA', 'ZE', 'ZI', 'ZO', 'ZU']
        
        # More complex syllables
        self._syllabes_complexes = ['TRE', 'TRI', 'TRO', 'TRA', 'TRE', 'TRI', 'TRO', 'TRA', 'DRE', 'DRI', 'DRO', 'DRA',
                                   'BRE', 'BRI', 'BRO', 'BRA', 'CRE', 'CRI', 'CRO', 'CRA', 'FRE', 'FRI', 'FRO', 'FRA',
                                   'GRE', 'GRI', 'GRO', 'GRA', 'PRE', 'PRI', 'PRO', 'PRA', 'SRE', 'SRI', 'SRO', 'SRA',
                                   'VRE', 'VRI', 'VRO', 'VRA', 'ZRE', 'ZRI', 'ZRO', 'ZRA', 'LON', 'LEN', 'LIN', 'LAN',
                                   'MON', 'MEN', 'MIN', 'MAN', 'NON', 'NEN', 'NIN', 'NAN', 'PON', 'PEN', 'PIN', 'PAN',
                                   'RON', 'REN', 'RIN', 'RAN', 'SON', 'SEN', 'SIN', 'SAN', 'TON', 'TEN', 'TIN', 'TAN',
                                   'VON', 'VEN', 'VIN', 'VAN', 'ZON', 'ZEN', 'ZIN', 'ZAN']
        
        # Special characters for super_strong
        self._caracteres_speciaux = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '~', '`', 'ù', 'à', 'é', 'è', 'ç']
        
        # Numbers
        self._chiffres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
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
        return random.choice(['-', '——', '——', ' • '])
    
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
        
        return result
    
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
        
        return result
    
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
        
        return result


# Example of usage
if __name__ == "__main__":
    clinkey = Clinkey()
    clinkey.display_greeting()
    nombre = clinkey._get_user_input(
        "How many passwords do you want to generate ?"
    ).strip()
    nombre = int(nombre) if nombre.isdigit() else 3
    clinkey.header()
    
    print("=== Examples of generated passwords ===")
    print("\nSuper Strong:")
    for i in range(nombre):
        print(f"  {clinkey.super_strong()}")
    
    print("\nStrong:")
    for i in range(nombre):
        print(f"  {clinkey.strong()}")
    
    print("\nNormal:")
    for i in range(nombre):
        print(f"  {clinkey.normal()}") 