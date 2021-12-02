"""
This is the people module and supports all the REST actions for the
people data
"""

from flask import make_response, abort
from config import db
from models import (Person, PersonSchema)



def read_one(Barcode_ID):
    """
    This function responds to a request for /api/asaren/{person_id}
    with one matching person from people
    :param person_id:   Id of person to find
    :return:            person matching id
    """
    # Get the person requested
    person = Person.query.filter(Person.Barcode == Barcode_ID).one_or_none()
    print(person)
    # Did we find a person?
    if person is not None:
        # Serialize the data for the response
        person_schema = PersonSchema()
        data = person_schema.dump(person)
        return data

    # Otherwise, nope, didn't find that person
    else:
        abort(
            404,
            "Person not found for Id: {Barcode_ID}".format(Barcode_ID=Barcode_ID),
        )


