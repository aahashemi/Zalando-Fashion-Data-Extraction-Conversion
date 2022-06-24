import web_crawler
import pandas as pd
from selenium.webdriver.common.by import By

# create a csv file with Category and Image_URL being as columns
DATABASE_FILE = "zalando_fashion_data_extraction.csv"
# maximum number of pages for each category
MAX_PAGES = 100

CATEGORIES = ['Jacket', 'Pants', 'Jeans', 'Shorts', 'T-shirt',
              'Pullover', 'Bag', 'Cap', 'Sandal', 'Skirt']

def loadDatabase():
    df = pd.read_csv(DATABASE_FILE)
    return df
def saveDatabase(df):
    df.to_csv(DATABASE_FILE, index=False)

def main_func():
    driver = web_crawler.initiate_driver()
    for category in CATEGORIES:
        for page in range(1,MAX_PAGES):
            try:
                df = loadDatabase()
                website = driver.get(f'https://www.zalando.nl/alle/?q={category}&p={page}')
                web_crawler.scroll_down_the_page(driver, website, 5)
                images = driver.find_elements(By.TAG_NAME, 'img')

                for image in images:
                    try:
                        Image_URL = image.get_attribute('src')
                        df.loc[-1] = [category, Image_URL]
                        df.index = df.index + 1  # shifting index
                    except Exception as e:
                        print(f'EXCEPTION: {e}')
                saveDatabase(df)
                print(f'Completing {round((page / MAX_PAGES) * 100, 2)}% of {category} category')

            except Exception as e:
                print(f'EXCEPTION: {e}')

if __name__ == '__main__':
    main_func()