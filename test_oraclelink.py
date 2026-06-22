# test_oraclelink.py
"""
Tests for OracleLink module.
"""

import unittest
from oraclelink import OracleLink

class TestOracleLink(unittest.TestCase):
    """Test cases for OracleLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OracleLink()
        self.assertIsInstance(instance, OracleLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OracleLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
