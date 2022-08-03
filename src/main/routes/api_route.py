import json
from flask import Blueprint, jsonify, request

# User Factory Import
from src.main.factory.user.list_user_account_factory import ListUserAccountFactory
from src.main.factory.user.list_user_inventory_factory import ListUserInventoryFactory
from src.main.factory.user.add_user_account_factory import AddUserAccountFactory
from src.main.factory.user.authenticate_user_factory import AuthenticateUserFactory

# Trade Factory Import
from src.main.factory.trade.add_trade_solicitations_factory import AddTradeSolicitationsFactory
from src.main.factory.trade.list_trade_solicitations_factory import ListTradeSolicitationsFactory
from src.main.factory.trade.refuse_exchange_factory import RefuseExchangeFactory
from src.main.factory.trade.trade_pokemon_factory import TradePokemonFactory

api_routes_bp = Blueprint("api_routes", __name__)

@api_routes_bp.route("/api/user", methods=["GET"])
def getAllUsers():
  result = ListUserAccountFactory.makeListUserAccountFactory(request.json["params"])
  return jsonify(result)

@api_routes_bp.route("/api/user/inventory", methods=["GET"])
def getUserInventory():
  result = ListUserInventoryFactory.makeListUserInventoryFactory(request.json["params"])
  return jsonify(result)

@api_routes_bp.route("/api/user", methods=["POST"])
def createUser(self):
  result = AddUserAccountFactory.makeUserAccountFactory(request.json["params"])
  return jsonify(result)

@api_routes_bp.route("/api/user/authenticate", methods=["GET"])
def getUser(self):
  result = AuthenticateUserFactory.makeAuthenticateUserFactory(request.json["params"])
  return jsonify(result)

# Trade Routes
@api_routes_bp.route("/api/trade", methods=["GET"])
def getTradeSolicitation(self):
  result = ListTradeSolicitationsFactory.makeListTradeSolicitationsFactory(request.json["params"])
  return jsonify(result)

@api_routes_bp.route("/api/trade", methods=["POST"])
def createTradeSolicitation(self):
  result = AddTradeSolicitationsFactory.makeAddTradeSolicitationsFactory(request.json["params"])
  return jsonify(result)

@api_routes_bp.route("/api/trade/refuse", methods=["PUT"])
def refuseTradeSolicitation(self):
  result = RefuseExchangeFactory.makeRefuseExchangeFactory(request.json["params"])
  return jsonify(result)

@api_routes_bp.route("/api/trade/refuse", methods=["PUT"])
def tradePokemon(self):
  result = TradePokemonFactory.makeTradePokemonFactory(request.json["params"])
  return jsonify(result)