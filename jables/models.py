from django.db.models import Model
from django.db.models.fields import CharField, DateTimeField
import nanoid


def generate():
    """ Given these parameters, ~448 thousand years needed, 
        in order to have a 1% probability of at least one collision.
        (from: https://zelark.github.io/nano-id-cc/)
    """
    return nanoid.generate(alphabet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
                            size=15)


class JBModel(Model):
    """ This is a basic model from which all the project's model should inherit. It is defined as "abstract".
            https://docs.djangoproject.com/en/3.1/topics/db/models/#abstract-base-classes
        It defines a couple of basic fields every model should have:
        - an ID as CharField/NanoID: this avoids that content could be "discovered" if using auto increment integers.
            https://github.com/puyuan/py-nanoid
        - created_at: a datetime field with "auto_now_add", so we track when the model was created.
        - updated_at: a datetime field with "auto_now", so we track when the model was last updated.
    """
    id = CharField(max_length=21, primary_key=True, default=generate, editable=False)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True
