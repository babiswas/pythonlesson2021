from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields
from flask_rest_jsonapi import Api, ResourceDetail, ResourceList
from marshmallow_jsonapi.flask import Relationship
from flask_rest_jsonapi import ResourceRelationship


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:36network@localhost/bello"
db=SQLAlchemy(app)

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birth_year = db.Column(db.Integer)
    genre = db.Column(db.String)
    
class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    artist = db.relationship('Artist',backref=db.backref('artworks'))

class ArtistSchema(Schema):
    class Meta:
        type_ = 'artist'
        self_view = 'artist_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'artist_many'

    id = fields.Integer()
    name = fields.Str(required=True)
    birth_year = fields.Integer(load_only=True)
    genre = fields.Str()
    artworks = Relationship(self_view = 'artist_artworks',self_view_kwargs = {'id': '<id>'},related_view = 'artwork_many',many = True,schema = 'ArtworkSchema',type_ = 'artwork')


class ArtworkSchema(Schema):
    class Meta:
        type_ = 'artwork'
        self_view = 'artwork_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'artwork_many'

    id = fields.Integer()
    title = fields.Str(required=True)
    artist_id = fields.Integer(required=True)


class ArtistMany(ResourceList):
    schema = ArtistSchema
    data_layer = {'session': db.session,'model': Artist}

class ArtistOne(ResourceDetail):
    schema = ArtistSchema
    data_layer = {'session': db.session,'model': Artist}


class ArtworkMany(ResourceList):
    schema = ArtworkSchema
    data_layer = {'session': db.session,'model': Artwork}

class ArtworkOne(ResourceDetail):
    schema = ArtworkSchema
    data_layer = {'session': db.session,'model': Artwork}

class ArtistArtwork(ResourceRelationship):
    schema = ArtistSchema
    data_layer = {'session': db.session,'model': Artist}


db.create_all()

api = Api(app)
api.route(ArtistMany, 'artist_many', '/artists')
api.route(ArtistOne, 'artist_one', '/artists/<int:id>')
api.route(ArtworkMany, 'artwork_many', '/artworks')
api.route(ArtworkOne, 'artwork_one', '/artworks/<int:id>')
api.route(ArtistArtwork, 'artist_artworks','/artists/<int:id>/relationships/artworks')


if __name__=="__main__":
  app.run(debug=True)





