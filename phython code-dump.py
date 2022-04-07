from cs103 import *
import matplotlib.pyplot as plt
from typing import NamedTuple, List, Optional
import csv

##################
# Data Definitions

Pokemon = NamedTuple("Pokemon", [("pokedex_number", int),
                                 ("name", str),
                                 ("attack", int),
                                ("defense", int),
                                ("type1", str),
                                ("type2", str)])

#Interp. a pokemon with its pokedex number, name, attack, defense, types 1 and 2.

PIKATCHU = Pokemon(25, "Pikatchu", 55, 40, "electric", "")
GARDEVOIR = Pokemon(282, "Gardevoir", 85, 65, "psychic", "fairy")

#Template based on Compound 

def fn_for_Pokemon(p: Pokemon) -> ...:
    return ...(p.pokedex_number,
               p.name,
               p.attack,
               p.defense,
               p.type1,
               p.type2)

                    
# List[Pokemon]
# interp. a list of Consumed

LOP0 = []
LOP1 = [PIKATCHU, GARDEVOIR]

@typecheck
def fn_for_lop(lop: List[Pokemon]) -> ...:
    acc = ...
    for l in lop:
        if ...:
            return acc


Sapphire = int #range [1-300]
# Interp. The Pokedex number of a Pokemon in the game Alpha Sapphire

S1 = 25
S2 = 27

@typecheck
def fn_for_sapphire (s: Sapphire) -> ...:
    return ...(s) #template based on Atomic non-distinct 

#List[Sapphire]
#interp. A list of Sapphire

LOS0 = []
LOS1 = [25, 27]

@typecheck
def fn_for_los(los: List[Sapphire]) -> ...:
    return ...(los)

AverageRatio = float 
#Interp. The Average Ratio of a Pokemon type 

AR_Bug = 14.791007869495925
AR_Ground = 10.757096632360673

LOAR0 = []
LOAR1 = [AR_Bug, AR_Ground]

@typecheck
def fn_for_average_ratio (ar: AverageRatio) -> ...:
    return ...(ar) #template based on Atomic non-distinct 

#List[AverageRatio]
#interp. A list of AverageRatio

LOARR0 = []
LOARR1 = [AR_Bug, AR_Ground]

@typecheck
def fn_for_loarr(loarr: List[AverageRatio]) -> ...:
    return ...(loarr)

Type = str
#Interp. 

LOT0 = []
LOTT1 = ["bug", "fairy"]
LOTT_ALL = ['bug','dark','dragon','electric','fairy','fighting','fire','flying','ghost','grass','ground','ice','normal','poison','psychic','rock','steel','water']



###########
# Functions

@typecheck
def read(filename: str) -> List[Pokemon]:
    """    
    reads information from the specified file and returns of the list of Pokemons in the National Pokedex 
    """
    # return []  #stub
    # Template from HtDAP
    # loc contains the result so far
    lop = [] # type: List[Consumed]

    with open(filename) as csvfile:
        
        reader = csv.reader(csvfile)
        next(reader) # skip header line

        for row in reader:
            p = Pokemon(parse_int(row[32]), row[30], parse_int(row[19]), parse_int(row[25]), row[36], row[37])
            lop.append(p)
    
    return lop

@typecheck
def read_sapphire(filename: str) -> List[Sapphire]:
    """    
    reads information from the specified file and returns a list of Pokemons in the Alpha Sapphire 
    """
    # return []  #stub
    # Template from HtDAPf
    # loc contains the result so far
    los = [] # type: List[Sapphire]

    with open(filename) as csvfile:
        
        reader = csv.reader(csvfile)

        for row in reader:
            s = Sapphire(parse_int(row[0]))
            los.append(s)
            
    return los

#Following functions plot the bar graph 


@typecheck
def produce_num_sequence(values: List[float], initial: float, gap: float) -> List[float]:
    """
    Produce a list of numbers like [initial, initial + gap, initial + 2*gap, ...] of the same
    length as values, e.g., to give alignment coordinates for a plot. The number
    of numbers in the list is equal to len(values). The first value is initial. The gap between values
    is gap.
    
    E.g., [5,15,25,35,45,55,65,75] for 8 values, initial == 5, and gap == 10.
    """
    #return []  #stub
    # Template from List[float] with two additional parameters
    
    # nums is the numbers for the values seen so far
    nums = []  # type: List[int]
    
    # next_num is the next number to use
    next_num = initial
    
    for val in values:
        nums.append(next_num)
        next_num = next_num + gap
    
    return nums


    
#Following functions are for attack/defense ratio calculation

@typecheck
def all_ratio(lot: List[Type]) -> List[AverageRatio]:
    """
    Returns a list of all average ratios
    """
    #Return LOAR0 #stub
    #Template based on List[Type]
    
    acc = []
    for t in lot:
        acc.append(avg_ratio_typed(filtered(read("pokemon.csv"), read_sapphire("sapphire.csv")), t))
    return acc

@typecheck
def avg_ratio_typed(lop: List[Pokemon], t: str) -> AverageRatio:
    """
    Returns an average attack/defense ratio for the given type, t 
    """
    #Return 10.0 #stub
    #Template based on Compounds 
    
    return sum_ratio_typed(lop,t)/num_of_pokemons_per_type(lop,t)

@typecheck
def sum_ratio_typed(lop: List[Pokemon], t: str) -> float:
    """
    Returns a list of attack/defense ratios filtered for the given type, t
    """
    #Return 10.0 #stub
    #Template based on List[Pokemon], with an additional parameter
    
    acc = []
    for p in lop:
        if filter_type(lop,t):
            acc.append(ratio(p))
    return sum(acc)
        
@typecheck
def ratio(p: Pokemon) -> float:
    """
    Calculates the attack/defense ratio of a given Pokemon
    """
    #Return 10.0 #stub
    #Template based on Pokemon
    
    return p.attack/p.defense

@typecheck
def num_of_pokemons_per_type(lop: List[Pokemon], t: str) -> int:
    """
    Returns the number of Pokemons within a given type 
    """
    #return 2 #stub
    #Template based on List[Pokemon]
    
    return len(filter_type(lop, t))


#Following functions create a list of all Pokemon Types (for graphing/x-axis)

@typecheck
def type_list(lot: List[Type]) -> List[Type]:
    """
    Returns a list of Pokemon types, repeated once 
    """
    #return LOT0 #stub
    #Template based on List[Type]
    acc = [] #type: List[Type]
    
    for t in lot:
        if t not in acc and t is not None and t != "":
            acc.append(t)
    return sorted(acc)

@typecheck
def all_types(lop: List[Pokemon]) -> List[Type]:
    """
    Returns a list of types of all Pokemons
    """
    #return LOC0 #stub
    #Template based on List[Pokemon], with an additional parameter t
    acc = [] #type: List[Type]
    for p in lop:
            acc.append(p.type1) 
            acc.append(p.type2)
    return acc

#Following functions filter for Pokemon Type 

@typecheck
def filter_type(lop: List[Pokemon], t: str) -> List[Pokemon]:
    """
    Returns a list of Pokemons that have the type, t
    """
    #return LOC0 #stub
    #Template based on List[Pokemon], with an additional parameter t
    
    acc = [] #type: List[Pokemon]
    for p in lop:
        if in_type(p, t, t):
            acc.append(p)
    return acc

@typecheck
def in_type(p:Pokemon, t1: str, t2: str) -> bool:
    """
    Returns True if Pokemon t1 is type 1 or type 2 
    """
    #return True #stub
    #template based on Pokemon with two additional parameters (t1, t2)
    
    return p.type1 == t1 or p.type2 == t2

#Following functions are for filtering the Pokemon dataset for Sapphire Pokedex 

@typecheck 
def filtered(lop: List[Pokemon], los: List[Sapphire]) -> List[Pokemon]: 
    """
    Filters the Pokemon list for the ones included in the Sapphire list 
    """
    #return LO1 #stub
    #Template based on List[Pokemon]
    acc = []
    for p in lop:
        for s in los:
            if id_check(p, s):
                acc.append(p)
    return acc
            
@typecheck
def id_check(n1: Pokemon, n2: int) -> bool:
    """
    Returns True if n1 is equal to n2 
    """
    #Return True #stub
    #Template based on Atomic distinct 
    return n1.pokedex_number == n2

#Begin testing
start_testing()

# Examples and tests for read
expect(read("pokemon_test1.csv"),[Pokemon(pokedex_number=1, name='Bulbasaur', attack=49, defense=49, type1='grass', type2='poison'),
 Pokemon(pokedex_number=2, name='Ivysaur', attack=62, defense=63, type1='grass', type2='poison')])
expect(read("pokemon_test2.csv"),[Pokemon(pokedex_number=25, name='Pikachu', attack=55, defense=40, type1='electric', type2=''),
 Pokemon(pokedex_number=26, name='Raichu', attack=85, defense=50, type1='electric', type2='electric')])

# Examples and tests for read_sapphire
expect(read_sapphire("sapphire_test1.csv"), [252, 253, 254])
expect(read_sapphire("sapphire_test2.csv"),[274, 275, 276, 277])

# Examples and tests for avg_ratio_typed
#expect(..., ...)

# Examples and tests for sum_ratio_typed
#expect(..., ...)

# Examples and tests for ratio
#expect(..., ...)

# Examples and tests for num_of_pokemons_per_type
#expect(..., ...)

# Examples and tests for filter_type
#expect(..., ...)

# Examples and tests for in_type
#expect(..., ...)

# Examples and tests for filtered
#expect(..., ...)

# Examples and tests for id_check
#expect(..., ...)

# show testing summary
summary()

avg_ratio_typed(filtered(read("pokemon.csv"), read_sapphire("sapphire.csv")), "fairy")
type_list(all_types(filtered(read("pokemon.csv"), read_sapphire("sapphire.csv"))))
all_ratio(type_list(all_types(filtered(read("pokemon.csv"), read_sapphire("sapphire.csv")))))
display_bar_chart(all_ratio(type_list(all_types(filtered(read("pokemon.csv"), read_sapphire("sapphire.csv"))))))
