from django.test import TestCase
from myapp.models import seats



# Create your tests here.
class ModelUseProfileTest(TestCase):
    """ Test class define the test suite for the UserProfile model."""

    def test_create_user(self):
        """Users can register"""

        # Create an instance of a GET request.
        response = self.client.post({
            'slot_name': "2A",'status': "occupied", })

        use = seats.objects.get(slot_name="2A")

        self.assertEqual(seats.slot_name, "2A")
        #self.assertEqual(user.first_name, "hari")
        self.assertEqual(seats.status, "occupied")
        self.assertEqual(response.status_code, 201)
