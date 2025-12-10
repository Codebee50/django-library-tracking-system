from django.test import TestCase
from rest_framework.test import APITestCase

from library.models import Loan
from library.tasks import check_overdue_loans

# Create your tests here.


class TestCheckOverdue(APITestCase):
    def setUp(self):
        return super().setUp()
    
    def test_overdue(self):
        check_overdue_loans.delay()
