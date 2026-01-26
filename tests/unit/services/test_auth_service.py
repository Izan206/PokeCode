from app.services.auth_services import authenticate
from unittest.mock import patch

# def test_authenticate():
#     with patch(
#         "app.repositories.trainer_repo.get_trainer_by_name"
#     ) as mock_repo:
#         mock_repo.return_value=[]
#         resultado=authenticate("axel", "1234")
#         assert resultado==