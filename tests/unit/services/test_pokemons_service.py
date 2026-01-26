from app.services.pokemon_services import list_pokemons
from unittest.mock import patch

def test_list_pokemons():
    with patch (
        "app.repositories.pokemon_repo.obtain_pokemons"
    ) as mock_repo:
        mock_repo.return_value=[]
        resultado=list_pokemons()
        assert resultado==[]