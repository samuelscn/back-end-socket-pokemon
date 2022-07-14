from urllib import response
from src.main.middlewares.grpc_middlewares.protos.trade.list_trade_solicitations_proto import list_trade_solicitations_pb2
from src.main.middlewares.grpc_middlewares.protos.trade.list_trade_solicitations_proto import list_trade_solicitations_pb2_grpc
from src.main.factory.trade.list_trade_solicitations_factory import ListTradeSolicitationsFactory

class ListTradeSolicitationsService(list_trade_solicitations_pb2_grpc.ListTradeSolicitationsServicer):
    def makeListTradeSolicitationsFactory(self, request, context):
        new_request = { 
            "id": request.id,
        }
        result = ListTradeSolicitationsFactory.makeListTradeSolicitationsFactory(new_request)
        if (result['statusCode'] == 400):
            response = list_trade_solicitations_pb2.Response(statusCode = result['statusCode'], message = result['body']['message'])
        response = list_trade_solicitations_pb2.Response(
            statusCode = result['statusCode'],
            received_user_id = result['received_user_id'],
            sender_user_id = result['sender_user_id'],
            want_pokemon_id = result['want_pokemon_id'],
            give_pokemon_id = result['give_pokemon_id'],
            status = result['status'],
            want_pokemon_name = result['want_pokemon_name'],
            want_pokemon_image = result['want_pokemon_image'],
            give_pokemon_name = result['give_pokemon_name'],
            give_pokemon_image = result['give_pokemon_image'],
            received_user_name = result['received_user_name'],
            sender_user_name = result['sender_user_name'],
        )
        return response
