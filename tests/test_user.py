import pytest
from app import create_app, db
from user.user import User


@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

def test_add_user_and_select_pj(app):
    with app.app_context():
        user = User(username='Lucas', password='RayoDeSol')
        user.add_user('Lucas', 'RayoDeSol')
        response = User.query.filter_by(username='Lucas').first()
        assert response is not None
        assert response.username == 'Lucas'
        assert response.password == 'RayoDeSol'
        user = User.query.filter_by(username='Lucas').first()
        assert user is not None
        user.select_character(2)
        selected_user = User.query.filter_by(username='Lucas').first()
        assert selected_user is not None
        assert int(selected_user.character) == 2

def test_get_user_id(app):
    with app.app_context():
        user = User()
        user.add_user('Lucas', 'RayoDeSol')
        user_one = User.query.filter_by(username='Lucas').first()
        assert user_one.get_id() == 1
        user = User()
        user.add_user('Maik', 'Casita')
        user_two = User.query.filter_by(username='Maik').first()
        assert user_two.get_id() == 2