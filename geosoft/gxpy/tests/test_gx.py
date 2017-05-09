﻿import unittest
import os
import time

import geosoft
import geosoft.gxpy.gx as gx

from geosoft.gxpy.tests import GXPYTest


class Test(GXPYTest):
    @classmethod
    def setUpClass(cls):
        pass

    def test_gxpy(self):
        with gx.GXpy(log=print) as gxc:
            self.assertTrue(gxc.gid.find('@') > 0)
            self.assertEqual(gxc.main_wind_id,0)
            self.assertEqual(gxc.active_wind_id, 0)
            self.assertEqual(gx.__version__, geosoft.__version__)
            gxc._close()

    def test_env(self):
        with gx.GXpy(log=print) as gxc:
            self.assertFalse(gxc.gid is None)
            self.assertFalse(gxc.current_date is None)
            self.assertFalse(gxc.current_utc_date is None)
            self.assertFalse(gxc.current_time is None)
            self.assertFalse(gxc.current_utc_time is None)
            self.assertFalse(gxc.license_class is None)
            self.assertFalse(gxc.folder_workspace is None)
            self.assertFalse(gxc.folder_temp is None)
            self.assertFalse(gxc.folder_user is None)
            gxc._close()

    def test_entitlements(self):
        with gx.GXpy(log=print) as gxc:
            ent = gxc.entitlements()
            self.assertTrue(ent.get('1000'), 'Oasis montaj™ Base')
            gxc._close()

    def test_temp(self):
        with gx.GXpy(log=print) as gxc:
            tf = gxc.temp_folder()
            self.assertTrue(os.path.isdir(tf))

            tf = gxc.temp_file()
            self.assertFalse(os.path.exists(tf))

            tf = gxc.temp_file(ext=".dummy")
            self.assertFalse(os.path.exists(tf))
            self.assertEqual(tf[-6:], ".dummy")
            try:
                with open(tf, 'x'):
                    pass
            except:
                self.assertTrue(False)

            #gxc.keep_temp_folder(True)
            gxc._close()

    def test_elapsed_time(self):
        with gx.GXpy() as gxc:
            self.assertTrue(gxc.elapsed_seconds("startup") > 0.0)
            time.sleep(0.25)
            self.assertTrue(gxc.elapsed_seconds("0.25 seconds later") > 0.25)
            gxc._close()


###############################################################################################

if __name__ == '__main__':

    unittest.main()
