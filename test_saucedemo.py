import time

from page_objsauce.saucedemo import Saucedemo
from utilities.basesauce import BaseSauce


class Testsausedemo(BaseSauce):
    def test_saucedemo(self):
        self.Login()
        time.sleep(2)
        sau=Saucedemo(self.driver)
        sau.sauce()
<<<<<<< HEAD
#another sample file by sdet2
=======
#new change
>>>>>>> 24e284b083aaa78195ad833c8a597ac8d09c2777
#sampleline