from finder import *
import argparse

parser = argparse.ArgumentParser(description='Find reviews from Tokopedia product')

parser.add_argument('productURL', type=str, help='URL of the product, ex: "tokopedia.com/shopname/productname"')
parser.add_argument('text', type=str, help='text to find, support regex')
parser.add_argument('--save-to', type=str, help='save the found reviews to desired file name, optional. Example: "output.txt"')

args = parser.parse_args()

def main():
    productID = getProductID(args.productURL)
    reviewSummary = getAllReviews(productID)
    findReviews(args.text, reviewSummary, fileName=args.save_to)

if __name__ == "__main__":
    main()