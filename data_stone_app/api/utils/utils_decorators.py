from django.db.utils import OperationalError
from rest_framework.response import Response
from rest_framework import status

from api.utils.utils_exceptions import ParamsMissing, SameParams

get_params = set(["from", "to", "amount"])
currency = set(["USD", "BRL", "BTC", "EUR"])


def compare_from_and_to(from_cur, to):
    return bool(from_cur != to)


def return_api_errors_currency_params(func):
    def inner(*args, **kwargs):
        try:
            dict_params = {
                key: value[0] for key, value in args[1].query_params.lists()
            }
            params = set(dict_params.keys())
            params_faltando = get_params.difference(params)

            if params_faltando:
                raise ParamsMissing(list(params_faltando))

            if not compare_from_and_to(dict_params["from"], dict_params["to"]):
                raise SameParams()

            return func(*args, **kwargs)

        except ParamsMissing as error:
            error.args[0].sort()
            err = error.args[0]

            params_faltando_string = ", ".join(param for param in err)

            content = {
                "status": "error",
                "msg": f"Os seguintes parâmetros estão faltando: {params_faltando_string}",
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        except SameParams:
            content = {
                "status": "error",
                "msg": "Não é possível transmitir para a mesma moeda",
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

    return inner
