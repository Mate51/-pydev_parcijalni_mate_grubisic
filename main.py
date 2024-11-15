import json

#TODO: dodati type hinting na sve funkcije

OFFERS_FILE = "offers.json"
PRODUCTS_FILE = "products.json"
CUSTOMERS_FILE = "customers.json"


def load_data(filename):
    """Load data from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error decoding {filename}. Check file format.")
        return []


def save_data(filename, data):
    """Save data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# TODO: Implementirajte funkciju za kreiranje nove ponude.
def create_new_offer(offers, products, customers: dict) -> dict:
    """
    Prompt user to create a new offer by selecting a customer, entering date,
    choosing products, and calculating totals.
    """
    # Omogućite unos kupca
    # Izračunajte sub_total, tax i total
    # Dodajte novu ponudu u listu offers
    redni_broj_ponude = []
    for ponuda in offers:
        for id, redni_broj in ponuda.items():
            if id == "offer_number":
                redni_broj_ponude.append(redni_broj)
    redni_broj_ponude.sort()
    redni_broj_nove_ponude = redni_broj_ponude[-1] + 1

    print("Kupci:")
    for kupac in customers:
        print(f"{kupac['name']}")
    ime_kupca_nova_ponuda = input(f"\nUpišite ime kupca: ")

    datum_ponude = input("Unesite datum ponude (yyyy-dd-mm): ")

    ukupni_porez = 0
    ukupna_cijena = 0
    ukupna_cijena_s_porezom = 0
    nova_ponuda_proizvodi = []


    while True:
        for proizvod in products:
            print(f"\nRedni broj proizvoda: {proizvod['id']}")
            print(f"Ime proizvoda: {proizvod['name']}")
            print(f"Opis proizvoda: {proizvod['description']}")
            print(f"Cijena: {proizvod['price']}\n")
        odabir_proizvoda = input("Unesite redni broj proizvoda: ")
        kolicina_proizvoda = input("Unesite kolicinu proizvoda: ")
        for proizvod in products:
            if proizvod['id'] == int(odabir_proizvoda):
                cijena_proizvoda = proizvod['price'] * float(kolicina_proizvoda)
                ukupna_cijena += cijena_proizvoda
                
                cijena_s_porezom = cijena_proizvoda * 1.1
                ukupna_cijena_s_porezom += cijena_s_porezom
                
                porez = cijena_proizvoda * 0.1
                ukupni_porez += porez

                pod_ponuda = { 
                    "product_id": int(proizvod['id']),
                    "product_name": str(proizvod['name']),
                    "description": str(proizvod['description']),
                    "price": float(proizvod['price']),
                    "quantity": int(kolicina_proizvoda),
                    "item_total": float(cijena_proizvoda)
                     }
                nova_ponuda_proizvodi.append(pod_ponuda)
        nastavak_unosa_proizvoda = input("Želite li nastaviti unos proizvoda: ")
        if nastavak_unosa_proizvoda == "ne":
            break
    
    nova_ponuda = {
        "offer_number": int(redni_broj_nove_ponude),
        "customer": str(ime_kupca_nova_ponuda),
        "date": str(datum_ponude),
        "items": nova_ponuda_proizvodi,
        "sub_total": float(ukupna_cijena),
        "tax": float(ukupni_porez),
        "total": float(ukupna_cijena_s_porezom)
        }
    offers.append(nova_ponuda)
    
    #pass


# TODO: Implementirajte funkciju za upravljanje proizvodima.
def manage_products(products: dict) -> dict:
    """
    Allows the user to add a new product or modify an existing product.
    """
    # Omogućite korisniku izbor između dodavanja ili izmjene proizvoda
    # Za dodavanje: unesite podatke o proizvodu i dodajte ga u listu products
    # Za izmjenu: selektirajte proizvod i ažurirajte podatke

    while True:
        print("1. Dodavanje proizvoda")
        print("2. Izmjena proizvoda")
        izbor_postupka = str(input("Odabrana opcija: "))

        if izbor_postupka == "1":
            lista_rednih_brojeva = []

            for proizvod in products:
                for id, redni_broj in proizvod.items():
                    if id == "id":
                        lista_rednih_brojeva.append(redni_broj)
            lista_rednih_brojeva.sort()

            redni_broj_novog_proizvoda = lista_rednih_brojeva[-1] + 1

            naziv_proizvoda = input("Unesite naziv proizvoda: ")
            opis_proizvoda = input("Unesite opis proizvoda: ")
            cijena_proizvoda = input("Unesite cijenu proizvoda: ")

            novi_proizvod = {
                "id": int(redni_broj_novog_proizvoda),
                "name": str(naziv_proizvoda),
                "description": str(opis_proizvoda),
                "price": float(cijena_proizvoda)
            }

            products.append(novi_proizvod)

        elif izbor_postupka == "2":
            print("1. Pregled proizvoda: ")
            print("2. Izmjena proizvoda: ")
            popis_ili_izbor = str(input("Odabrana opcija: "))
            
            if popis_ili_izbor == "1":
                for proizvod in products:
                    print(f"\nRedni broj proizvoda: {proizvod['id']}")
                    print(f"Ime proizvoda: {proizvod['name']}")
                    print(f"Opis proizvoda: {proizvod['description']}")
                    print(f"Cijena: {proizvod['price']}\n")

            elif popis_ili_izbor == "2":
                redni_broj_proizvoda = input("Unesite redni broj proizvoda koji želite izmijeniti: ")
                novo_ime = input("Unesite novo ime proizvoda (kliknite Enter ako ne želite mijenjati): ")
                novi_opis_proizvoda = input("Unesite novi opis proizvoda (kliknite Enter ako ne želite mijenjati): ")
                nova_cijena_proizvoda = input("Unesite novu cijenu proizvoda (kliknite Entar ako ne želite mijenjati): ")

                for proizvod in products:
                    if proizvod['id'] == int(redni_broj_proizvoda):
                        if novo_ime != "":
                            proizvod['name'] = str(novo_ime)
                        if novi_opis_proizvoda != "":
                            proizvod['description'] = str(novi_opis_proizvoda)
                        if nova_cijena_proizvoda != "":
                            proizvod['price'] = float(nova_cijena_proizvoda)
        nastavak_rada_s_proizvodima = input("Želite li nastaviti rad s proizvodima: ")
        if nastavak_rada_s_proizvodima == "ne":
            break

    #pass


# TODO: Implementirajte funkciju za upravljanje kupcima.
def manage_customers(customers: dict) -> dict:
    """
    Allows the user to add a new customer or view all customers.
    """
    # Za dodavanje: omogući unos imena kupca, emaila i unos VAT ID-a
    # Za pregled: prikaži listu svih kupaca

    while True:
        print("1. Dodavanje kupca")
        print("2. Pregled kupaca")
        izbor_kupaca = str(input("Odabrana opcija: "))

        if izbor_kupaca == "1":
            ime_kupca = input("Unesite ime kupca: ")
            mail_kupca = input("Unesite e-mail kupca: ")
            oib_kupca = input("Unesite porezni broj kupca: ")
            novi_kupac = {
                "name": str(ime_kupca),
                "email": str(mail_kupca),
                "vat_id": str(oib_kupca)
            }
            customers.append(novi_kupac)
        
        elif izbor_kupaca == "2":
            for kupac in customers:
                print(f"\nIme kupca: {kupac['name']}")
                print(f"E-mail kupca: {kupac['email']}")
                print(f"OIB kupca: {kupac['vat_id']}\n")

        nastavak_rada_s_kupcima = input("Želite li nastaviti rad s kupcima: ")
        if nastavak_rada_s_kupcima == "ne":
            break
    #pass


# TODO: Implementirajte funkciju za prikaz ponuda.
def display_offers(offers: dict) -> str:
    """
    Display all offers, offers for a selected month, or a single offer by ID.
    """
    # Omogućite izbor pregleda: sve ponude, po mjesecu ili pojedinačna ponuda
    # Prikaz relevantnih ponuda na temelju izbora

    while True:
        print("1. Prikaži sve ponude")
        print("2. Prikaži ponude po mjesecima")
        print("3. Prikaži pojedinačnu ponudu")
        izbor_pregleda = str(input("Odabrana opcija: "))

        if izbor_pregleda == "1":
            for ponuda in offers:
                print_offer(ponuda)

        elif izbor_pregleda == "2":
            zeljeni_mjesec_ponude = str(input("Unesite željeni mjesec pregleda (mm): "))
            print(f"\nPonude u {zeljeni_mjesec_ponude}. mjesecu: \n")
            for ponuda in offers:
                mjesec_ponude = ((ponuda['date']).split("-"))[2]
                if zeljeni_mjesec_ponude == mjesec_ponude:
                    print_offer(ponuda)

        elif izbor_pregleda == "3":
            zeljeni_broj_pojedinacne_ponude = int(input("Unesite broj ponude: "))
            print(f"\nPonuda broj {zeljeni_broj_pojedinacne_ponude}:\n")
            for ponuda in offers:
                broj_pojedinacne_ponude = int(ponuda['offer_number'])
                if zeljeni_broj_pojedinacne_ponude == broj_pojedinacne_ponude:
                    print_offer(ponuda)
        nastavak_rada_s_ponudama = input("Želite li nastaviti raditi s ponudama: ")
        if nastavak_rada_s_ponudama == "ne":
            break

    #pass


# Pomoćna funkcija za prikaz jedne ponude
def print_offer(offer):
    """Display details of a single offer."""
    print(f"Ponuda br: {offer['offer_number']}, Kupac: {offer['customer']}, Datum ponude: {offer['date']}") # print(f"Kupac: {offer['customer']['name']}... ['name'] ne postoji u json datoteci offers
    print("Stavke:")
    for item in offer["items"]:
        print(f"  - {item['product_name']} (ID: {item['product_id']}): {item['description']}")
        print(f"    Kolicina: {item['quantity']}, Cijena: ${item['price']}, Ukupno: ${item['item_total']}")
    print(f"Ukupno: ${offer['sub_total']}, Porez: ${offer['tax']}, Ukupno za platiti: ${offer['total']}")


def main():
    # Učitavanje podataka iz JSON datoteka
    offers = load_data(OFFERS_FILE)
    products = load_data(PRODUCTS_FILE)
    customers = load_data(CUSTOMERS_FILE)

    while True:
        print("\nOffers Calculator izbornik:")
        print("1. Kreiraj novu ponudu")
        print("2. Upravljanje proizvodima")
        print("3. Upravljanje korisnicima")
        print("4. Prikaz ponuda")
        print("5. Izlaz")
        choice = input("Odabrana opcija: ")

        if choice == "1":
            create_new_offer(offers, products, customers)
        elif choice == "2":
            manage_products(products)
        elif choice == "3":
            manage_customers(customers)
        elif choice == "4":
            display_offers(offers)
        elif choice == "5":
            # Pohrana podataka prilikom izlaza
            save_data(OFFERS_FILE, offers)
            save_data(PRODUCTS_FILE, products)
            save_data(CUSTOMERS_FILE, customers)
            break
        else:
            print("Krivi izbor. Pokusajte ponovno.")


if __name__ == "__main__":
    main()
