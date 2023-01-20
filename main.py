from flask import Flask
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()


class ArrayParser(Resource):

  def post(self):
    parser.add_argument("numbers", type=int, action='append')

    args = parser.parse_args()
    numbers = args.get("numbers")

    if isinstance(numbers, type(list)):
      for elem in numbers:
        if not isinstance(elem, type(int)):
          return {
            "Array Elements must be integers"
          }, 400


    even_array = [e for e in numbers if e%2 == 0]
    odd_array = [e for e in numbers if e % 2 != 0]

    resp = {
      "is_success": True,
      "user_id": "ayushi_jain_78",
      "odd": odd_array,
      "even": even_array
    }
    return resp, 201


api.add_resource(ArrayParser, '/bfhl')


if __name__ == "__main__":
  app.run(debug=True)
