#!/usr/bin/python3
""" Test Base Model"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Test Class"""

    def test_1(self):
        """Test"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_2(self):
        """Test"""
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_3(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_4(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_5(self):
        """Test"""
        case1 = BaseModel()
        case2 = BaseModel()
        self.assertNotEqual(case1.id, case2.id)

    def test_6(self):
        """Test"""
        case1 = BaseModel()
        sleep(0.05)
        case2 = BaseModel()
        self.assertLess(case1.created_at, case2.created_at)

    def test_7(self):
        """Test"""
        case1 = BaseModel()
        sleep(0.05)
        case2 = BaseModel()
        self.assertLess(case1.updated_at, case2.updated_at)

    def test_8(self):
        """Test"""
        cal = datetime.today()
        cal_repr = repr(cal)
        basemod = BaseModel()
        basemod.id = "123456"
        basemod.created_at = basemod.updated_at = cal
        str_base = basemod.__str__()
        self.assertIn("[BaseModel] (123456)", str_base)
        self.assertIn("'id': '123456'", str_base)
        self.assertIn("'created_at': " + cal_repr, str_base)
        self.assertIn("'updated_at': " + cal_repr, str_base)

    def test_9(self):
        basemod = BaseModel(None)
        self.assertNotIn(None, basemod.__dict__.values())

    def test_10(self):
        """Test"""
        cal = datetime.today()
        cal_iso = cal.isoformat()
        basemod = BaseModel(id="345", created_at=cal_iso, updated_at=cal_iso)
        self.assertEqual(basemod.id, "345")
        self.assertEqual(basemod.created_at, cal)
        self.assertEqual(basemod.updated_at, cal)

    def test_11(self):
        """Test"""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_12(self):
        """Test"""
        cal = datetime.today()
        c_iso = cal.isoformat()
        basemod = BaseModel("12", id="345", created_at=c_iso, updated_at=c_iso)
        self.assertEqual(basemod.id, "345")
        self.assertEqual(basemod.created_at, cal)
        self.assertEqual(basemod.updated_at, cal)


class TestBaseModel_save(unittest.TestCase):
    """Test"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_13(self):
        """Test"""
        basemod = BaseModel()
        sleep(0.05)
        first_updated_at = basemod.updated_at
        basemod.save()
        self.assertLess(first_updated_at, basemod.updated_at)

    def test_14(self):
        """Test"""
        basemod = BaseModel()
        sleep(0.05)
        first_updated_at = basemod.updated_at
        basemod.save()
        second_updated_at = basemod.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        basemod.save()
        self.assertLess(second_updated_at, basemod.updated_at)

    def test_15(self):
        """Test"""
        basemod = BaseModel()
        with self.assertRaises(TypeError):
            basemod.save(None)

    def test_16(self):
        """Test"""
        basemod = BaseModel()
        basemod.save()
        basemodid = "BaseModel." + basemod.id
        with open("file.json", "r") as f:
            self.assertIn(basemodid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Test"""

    def test_17(self):
        """Test"""
        basemod = BaseModel()
        self.assertTrue(dict, type(basemod.to_dict()))

    def test_18(self):
        """Test"""
        basemod = BaseModel()
        self.assertIn("id", basemod.to_dict())
        self.assertIn("created_at", basemod.to_dict())
        self.assertIn("updated_at", basemod.to_dict())
        self.assertIn("__class__", basemod.to_dict())

    def test_19(self):
        """Test"""
        basemod = BaseModel()
        basemod.name = "Holberton"
        basemod.my_number = 98
        self.assertIn("name", basemod.to_dict())
        self.assertIn("my_number", basemod.to_dict())

    def test_20(self):
        """Test"""
        basemod = BaseModel()
        basemod_dict = basemod.to_dict()
        self.assertEqual(str, type(basemod_dict["created_at"]))
        self.assertEqual(str, type(basemod_dict["updated_at"]))

    def test_21(self):
        """Test"""
        cal = datetime.today()
        basemod = BaseModel()
        basemod.id = "123456"
        basemod.created_at = basemod.updated_at = cal
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': cal.isoformat(),
            'updated_at': cal.isoformat()
        }
        self.assertDictEqual(basemod.to_dict(), tdict)

    def test_22(self):
        """Test"""
        basemod = BaseModel()
        self.assertNotEqual(basemod.to_dict(), basemod.__dict__)

    def test_23(self):
        """Test"""
        basemod = BaseModel()
        with self.assertRaises(TypeError):
            basemod.to_dict(None)


if __name__ == "__main__":
    unittest.main()
