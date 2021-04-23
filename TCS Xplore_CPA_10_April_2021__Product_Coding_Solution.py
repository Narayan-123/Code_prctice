class Product:
    def __init__(self, productName, productType, productPrice, quantityOnHand, reorderedQuantity):
        self.productName = productName  # string
        self.productType = productType  # string
        self.productPrice = productPrice  # Number
        self.quantityOnHand = quantityOnHand  # Number
        self.reorderedQuantity = reorderedQuantity  # Number


def findAvailableStock(list_of_Product, Product_Name):
    count = 0
    for y in Product_Name:
        for x in list_of_Product:
            if y.lower() == x.productName.lower():
                count += 1
                print(y, x.quantityOnHand)
    if count == 0:
        print('Product Not Found')


def updateStockByProductType(list_of_Product2, quantity_to_be_added, Product_Type):
    count = 0
    for x in list_of_Product2:
        if x.productType.lower() == Product_Type.lower():
            count += 1
            if x.quantityOnHand <= reorderedQuantity:
                x.quantityOnHand += quantity_to_be_added
    if count == 0:
        print('Product Not Found')
    else:
        for i in list_of_Product2:
            print(i.productName, i.quantityOnHand)


if __name__ == '__main__':
    list_for_class = []
    for i in range(5):
        productName = input('productName: ')
        productType = input('productType: ')
        productPrice = eval(input('productPrice: '))
        quantityOnHand = eval(input('quantityOnHand: '))
        reorderedQuantity = eval(input('reorderedQuantity: '))
        list_for_class.append(Product(productName, productType, productPrice, quantityOnHand, reorderedQuantity))

    list3 = []
    for i in range(int(input('no of Product_Name: '))):
        list3.append(input('Product_Name: '))

    q = int(input('quantity_to_be_added: '))
    t = input('Product_Type: ')

    findAvailableStock(list_for_class, list3)
    updateStockByProductType(list_for_class, q, t)


