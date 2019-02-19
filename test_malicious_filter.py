import unittest,string,random,malicious_filter,time,calendar

"""
__author__ = "Amarjit Singh Dhillon"
__copyright__ = "Copyright (C) 2019 Amarjit Singh Dhillon"
__license__ = "GPL GNU"
__version__ = "1.0"
__email__ = 'amarjitdhillon@cmail.carleton.ca'
__status__ = 'Development'
 
Description: This code tests the malicious_filter.py file by generating the 10000 random logs in JSON format
             These values are passed to json_validator function of malicious_filter.py file which will return true if the values are valid
"""
class UnitTest(unittest.TestCase):

    def setUp(self):
        #   --------- Generating valid values ----------
        ts  = calendar.timegm(time.gmtime())                                                                        # generate value of ts

        sha = ''.join(random.choice(('abcdef') + string.digits) for i in range(64))                                 # generate value of sha

        pt  = random.randint(1,100)                                                                                 # generate value of pt

        si_uu_bg = ''.join(random.choice(('abcdef') + string.digits) for i in range(8)) + '-' \
                    + ''.join(random.choice(('abcdef') + string.digits) for i in range(4)) + '-' \
                    + ''.join(random.choice('12345') for i in range(1)) + ''.join(
                    random.choice(('abcdef') + string.digits) for i in range(3)) + '-' \
                    + ''.join(random.choice('89ab') for i in range(1)) + ''.join(
                    random.choice(string.ascii_lowercase + string.digits) for i in range(3)) + '-' \
                    + ''.join(random.choice(('abcdef') + string.digits) for i in range(12))                         # generate value of si, uu and bg

        nm  = ''.join(random.choice(string.ascii_letters) for i in range(10)) + '- ' + '.' + \
                ''.join(random.choice(('43') + string.ascii_lowercase) for i in range(4))                           # generate value of nm

        ph  = ''.join(random.choice(string.ascii_letters) for i in range(10)) + '- /' + '.'+\
             ''.join(random.choice(('43') + string.ascii_lowercase) for i in range(4))                              # generate value of ph

        dp  = random.randint(1,3)                                                                                   # generate value of dp

        valid_log_entry = {'ts': ts,'pt': pt,'si': si_uu_bg,'uu': si_uu_bg,'bg': si_uu_bg,'sha': sha,'nm': nm,'ph': ph,'dp': dp}

        self.valid_log = valid_log_entry


        #   --------- Generating invalid logs ----------
        in_ts = random.randint(19, 199)                                                                             # generate value of ts

        in_sha = ''.join(random.choice(('qwertyuiopasddg') + string.digits) for i in range(62))                     # generate value of sha

        in_pt = random.randint(100, 200)                                                                            # generate value of pt

        in_si_uu_bg = ''.join(random.choice(('qwertyuiopasddg') + string.digits) for i in range(8)) + '-' \
                        + ''.join(random.choice(('qwertyuiopasddg') + string.digits) for i in range(4)) + '-' \
                        + ''.join(random.choice('1234234234245') for i in range(21)) + \
                        ''.join(random.choice(('qwertyuiopasddg') + string.digits) for i in range(31)) + '-' \
                        + ''.join(random.choice('qwertyuiopasddg') for i in range(17)) +\
                        ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(3)) + '-' \
                        + ''.join(random.choice(('qwertyuiopasddg') + string.digits) for i in range(12))            # generate value of si, uu and bg

        in_nm = ''.join(random.choice(string.ascii_letters) for i in range(140)) + '- ' + '.' + \
                ''.join(random.choice(('qwertyuiopasddg') + string.ascii_lowercase) for i in range(42))             # generate value of nm

        in_ph = ''.join(random.choice(string.ascii_letters) for i in range(50)) + '- /' + '.' + \
                ''.join(random.choice(('qwertyuiopasddg') + string.ascii_lowercase) for i in range(46))             # generate value of ph

        in_dp = random.randint(1, 3)                                                                                # generate value of dp

        invalid_log_entry = {'ts': in_ts, 'pt': in_pt, 'si': in_si_uu_bg, 'uu': in_si_uu_bg, 'bg': in_si_uu_bg, 'sha': in_sha, 'nm': in_nm,'ph': in_ph, 'dp': in_dp}

        self.invalid_log = invalid_log_entry

    def test_json_validator(self):
        for i in range(10000):
            self.assertTrue(malicious_filter.json_validator(self.valid_log))                                        # testing the correct values

    def test_json_invalidator(self):
        for i in range(10000):
            self.assertFalse(malicious_filter.json_validator(self.invalid_log))                                     # testing the in-correct values


if __name__ == "__main__":
    unittest.main()

