#this test based on 'Market_Basket_Optimisation.csv' dataset for eclat.

import unittest 
import calc

class Testeclat(unittest.testcase):
	def test_Eclat_func(self)
	key1=[('shrimp', 'almonds'), 0.00013333333333333334]
	message1="FALSE, key isn't in eclat"
	self.assertIn(key1 , eclat , message1)
	
	key2=('french fries', 'burger sauce'), 0.00013333333333333334]
	self.assertIn(key2 , eclat , message1)
	
	key3=[('sparkling water', 'butter'), 0.00013333333333301743]
	self.assertIn(key3 , eclat , message1)
	
	key4=[('red wine', 'bramble'), 0.0001333155579256099]
	self.assertIn(key4 , eclat , message1)
	
	key5=[('escalope', 'french wine'), 0.00013333333333333334]
	self.assertIn(key5 , eclat , message1)
	
	
	def test_fpg_func(self)
	first=Ui_MainWindow.rules['lift']
	second=Ui_MainWindo.rules['confidence']
	message1="incorrect number"
	self.assertGreaterEqual(first , 1.4 , message1)
	self.assertGreaterEqual(second , 0.3 , message1)
	
	key1=[frozenset({'ALARM CLOCK BAKELIKE GREEN'}) , frozenset({'ALARM CLOCK BAKELIKE PINK'}) , 0.040088358013581 , 0.0320297799230958 , 0.0170989118874253 ,
	0.426530612244898 ,	13.3166888211223 , 0.0158148906027721 , 1.68791960084585 ]

	message1="false"
	self.assertIn(key1 , Ui_MainWindo.rules , message1)
	