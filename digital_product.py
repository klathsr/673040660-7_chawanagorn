# Your code here
from abc import ABC, abstractmethod

class DigitalProduct(ABC):
  product_counter = 0

  def __init__(self, title, price):
    self.title = title
    self.price = price
    DigitalProduct.product_counter += 1
    self.product_ID = 1000 + DigitalProduct.product_counter

  @abstractmethod
  def calc_download_size(self):
    pass

  @abstractmethod
  def calc_delivery_time(self):
    pass

  # concrete method
  def gen_download_link(self):
    return f"https://domain.com/download/{self.product_id}"


class EBook(DigitalProduct):
  def __init__(self, num=0, format="PDF"):
    self.page_num = num
    self.format = format

  # implement abstract classes
  def calc_download_size(self):
    return self.page_num * 0.1

  # 1 minute + (1 minute per 100 pages)
  def calc_delivery_time(self):
    return 1 + (self.page_num / 100)

class VideoGame(DigitalProduct):
  def __init__(self, genre="RPG", size=1):
    self.genre = genre
    self.required_storage = size # MB

  # implement abstract classes
  def calc_download_size(self):
    return self.required_storage

  # 5 minutes + (2 minutes per GB of storage)
  def calc_delivery_time(self):
    return 5 + (self.required_storage / 1000) * 2

class DigitalProduct(ABC):
    product_counter = 0

    def __init__(self, title, price):
        self.title = title
        self.price = price
        DigitalProduct.product_counter += 1
        self.product_ID = 1000 + DigitalProduct.product_counter

    @abstractmethod
    def calc_download_size(self):
        pass

    @abstractmethod
    def calc_delivery_time(self):
        pass

    def gen_download_link(self):
        return f"https://domain.com/download/{self.product_ID}"



class EBook(DigitalProduct):
    def __init__(self, title, price, num=0, format="PDF"):
        super().__init__(title, price)
        self.page_num = num
        self.format = format

    def calc_download_size(self):
        return self.page_num * 0.1  # MB

    def calc_delivery_time(self):
        return 1 + (self.page_num / 100)  # minutes



class VideoGame(DigitalProduct):
    def __init__(self, title, price, genre="RPG", size=1):
        super().__init__(title, price)
        self.genre = genre
        self.required_storage = size  # MB

    def calc_download_size(self):
        return self.required_storage

    def calc_delivery_time(self):
        return 5 + (self.required_storage / 1000) * 2  # minutes


# Test Code

# create EBook object
ebook = EBook(title="Python Basics", price=9.99, num=300, format="PDF")

# test methods on it
print("EBook ID:", ebook.product_ID)
print("EBook download size (MB):", ebook.calc_download_size())
print("EBook delivery time (minutes):", ebook.calc_delivery_time())
print("EBook download link:", ebook.gen_download_link())

print()

# create VDO game object
video_game = VideoGame(title="Dragon Quest", price=59.99, genre="RPG", size=5000)

# test methods on it
print("Video Game ID:", video_game.product_ID)
print("Video Game download size (MB):", video_game.calc_download_size())
print("Video Game delivery time (minutes):", video_game.calc_delivery_time())
print("Video Game download link:", video_game.gen_download_link())
