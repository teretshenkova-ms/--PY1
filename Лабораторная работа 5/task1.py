# TODO решить с помощью list comprehension и распечатать его
import pprint as pp
dict_ = [{"bin": bin(i), "dec": i, "oct": oct(i), "hex": hex(i)} for i in range(16)]
pp.pprint(dict_)
