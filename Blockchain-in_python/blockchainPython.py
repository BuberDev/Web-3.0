## Krok 1 - iimportujemy biblioteki
#generuje stempel czasowy
import datetime
#zawiera algorytm haszujacy
import hashlib

## Krok 2 - Utworz block

# definicja struktury danych dla bloku
class Block:
    # kazdy blok posiada 7 parametrow
    
    #1 numer bloku - w tym momencie inicjalizujemy wartoscia 0
    blockNo = 0
    #2 jakie dane zapisujemy w bloku
    data = None # inicjalizacja wartoscia None
    #3 zmienna wskazujaca na kolejny blok
    next = None
    #4 Wartosc hash dla tego bloku (obsluguje unikalne ID i odpowiada za weryfikacje jego integralnosci)
    # Hash to funkcja, ktora konwertuje dane na liczbe w okreslonym zakresie
    hash = None # inicjalizacja wartoscia None
    #5 Liczba uzyta tylko raz pomga nam obliczyc hash bloku 
    nonce = 0 # Wartosc tymczasowa
    #6 przechowuje ID hashu poprzedniego blok z lancucha blokow  
    previous_hash = 0x0 # wartosc inicjalizacyjna
    #7 stempel czasu
    timestamp = datetime.datetime.now() 

    # inicjalizuje blok wpisujac dane do jego wnetrza 
    def __init__(self, data):
        self.data = data

    def hash(self):
        #SHA-256 to algorytm haszujacy, ktory generuje unikalny 256-bit podpis, ktory jest okreslony tekstem
        h = hashlib.sha256()
        
        #wejsciem dla algorytmu SHA-256 bedzie poloczony string skladajacy sie z 5 atrybutow bloku: the temp, data, previous_hash, timestamp, blokNo
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNo).encode('utf-8') 
        )
        #zwraca 'hexadecimal string'
        return h.hexdigest()

    def __str__(self):
        # wyswietl dane bloku
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n------------------------"

## Krok 3 - Tworzymy Blockchain

#definicja struktury danych dla blockchain sklada sie z blokow polaczonych ze soba w celu stworzenia lancucha. Dlatego cala strukture nazywamy 'blockchian'

class Blockchain:

    #trudnosc kopania blokow
    diff = 20
    #2^32 - jest maksymalna liczba jaka mozemy przechowywac na 32-bitach
    maxNonce = 2**32
    #docelowy hash
    target = 2 ** (256-diff)

    # generuje pierwszy blok w Blockchain po angielsku nazywa sie to 'genesis block' - czyli pierwszy blok w lancuchu
    block = Block("Genesis")
    # ustawienie tego bloku jako pierwszy w lancuchu
    head = block
    
    
    # dodanie blok do lancucha blokow
    def add(self, block):
        # ustawia hash danego bloku jako nowy hash poprzedniego bloku
        block.previous_hash = self.block.hash()
        # ustaw hash naszego nowego bloku jako hash danego bloku +1 
        block.blockNo = self.block.blockNo + 1
        
        #ustawiamy wartosc
        self.block.next = block
        self.block = self.block.next

    # okresla czy mozemy lub nie mozemy dodac dany blok do lancucha blokow
    def mine(self, block):
        # od 0 do 2^32
        for n in range(self.maxNonce):
            # czy wartosc hashu danego bloku jest mniejsza niz nasza docelowa wartosc
            if int(block.hash(), 16) <= self.target:
                #jezeli jest, to dodaj block do lancucha 
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

## Krok 4 - Wyswietl blockchain

#zainicjalizuj blockchain 
blockchain = Blockchain()

#wykop 10 blokow
for n in range(10):
    blockchain.mine(Block("Block " + str(n+1)))

# wyswietl kazdy z 10 blokow w blockchain
while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next
