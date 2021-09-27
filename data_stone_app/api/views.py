from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter

from .utils.utils_decorators import return_api_errors_currency_params


class ConvertCoin(APIView):

    currency_rates = CurrencyRates()
    btc_converter = BtcConverter()

    @return_api_errors_currency_params
    def get(self, request, format=None):

        values = {key: value[0] for key, value in request.query_params.lists()}
        values["from_cur"] = values.pop("from")  # from é uma palavra reservada

        if "BTC" in values.values():
            currency_return = self.convert_to_cripto(**values)
        else:
            currency_return = self.convert_to_currency(**values)

        response = {"status": "success", "msg": currency_return}

        return Response(response, status=status.HTTP_200_OK)

    def convert_to_cripto(self, amount, from_cur, to):

        if to == "BTC":
            return self.btc_converter.convert_to_btc(float(amount), from_cur)
        return round(
            self.btc_converter.convert_btc_to_cur(float(amount), to), 2
        )

    def convert_to_currency(self, amount, from_cur, to):
        return round(
            self.currency_rates.convert(from_cur, to, float(amount)), 2
        )
