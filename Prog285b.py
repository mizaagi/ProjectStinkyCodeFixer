from CL285b import SalesPerson

def main():
    try:
        print("Number\tCode\tSales\tCommission")
        with open("Langdat/prog285b.dat", 'r') as f:
            for line in f:
                ldata = line.split(" ")
                id = int(ldata[0])
                code = int(ldata[1])
                sales = float(ldata[2])

                seller = SalesPerson(id, code, sales)
                seller.setComm()
                print(seller)


    except Exception as e:
        print("Error:", e)
    pass

if __name__ == "__main__":
    main()