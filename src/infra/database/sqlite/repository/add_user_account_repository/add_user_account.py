import random
from src.infra.database.sqlite.views.inventory_pokemon.inventory_pokemon_view import *
from src.infra.database.sqlite.views.pokemon.pokemon_view import *
from src.infra.database.sqlite.views.user.user_view import *
from src.infra.database.sqlite.views.inventory.inventory_view import *
from src.data.protocols.user.add_user_account_repository import AddUserAccountRepository as AddUserAccountRepositoryInterface

class AddUserAccountRepo(AddUserAccountRepositoryInterface):
  
  def add(self, accountUserData):
    insert(accountUserData)
    user_result = getLastUser()
    print('USER_RESULT', user_result)
    insertInventory(user_result[0])
    inventory_result = getLastInventory()
    print('INVENTORY RESULT', inventory_result)
    for i in range(10):
      num = random.randint(1, 150)
      body = { "inventory_id": inventory_result[0], "pokemon_id": num }
      print('body', body)
      insertInventoryPokemon(body)
