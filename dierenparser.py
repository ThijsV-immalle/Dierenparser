from dataclasses import dataclass

@dataclass
class Dier:

   
        naam: ""
        soort: ""
        aantalPoten: 0
        kleur: ""
        geluid: ""

     


def parse_line(line):
    naam, soort, aantalpoten, kleur, geluid = line.split(' - ')
    d = Dier()
    d.naam = naam
    d.soort = soort
    d.aantalpoten = int(aantalpoten)
    d.kleur = kleur
    d.geluid = geluid
    print(f'Parsed: [{naam}] [{soort}] [{aan²talpoten}] [{kleur}] [{geluid}]')
    return d

def parse_text(str):
    dieren = []
    for line in str.splitlines():
        d = parse_line(line)
        dieren.append(d)
    return dieren


if __name__ == '__main__':
    dieren = []                                                     
    with open('dieren.txt', 'r') as f:
        dieren = parse_text(f.read())
    
    for dier in dieren:
        dier.print()

if __name__ == '__main__':
    import doctest
    doctest.testfile("parse_line.txt")

