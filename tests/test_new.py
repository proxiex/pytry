import unittest

class Testing(unittest.TestCase):
  def setUp(self):
    print ("some stuff here o")

  def test_for_some_thihg(self):
    print( "this works o")

  def tearDown(self):
    print ("we wrap thing up there.")

if __name__ == "__main__":
    unittest.main()