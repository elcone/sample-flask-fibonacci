from flask import Flask
from flask_restful import Api, Resource

from fibonacci import fibonacci
from models import db, NumberRequested
from schemas import NumberRequestedSchema


app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

api = Api(app)

db.app = app
db.init_app(app)


class Fibonacci(Resource):
    def post(self, number: int):
        result = fibonacci(number)
        number_requested = NumberRequested(
            number_requested=number,
            result=result)
        db.session.add(number_requested)
        db.session.commit()

        return result


class FibonacciList(Resource):
    def get(self):
        numbers = NumberRequested.query.all()
        number_schema = NumberRequestedSchema(many=True)
        dump = number_schema.dump(numbers)

        return dump


api.add_resource(Fibonacci, '/fibonacci/<int:number>')
api.add_resource(FibonacciList, '/fibonacci')


if __name__ == '__main__':
    app.run(debug=True)
