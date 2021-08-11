Jean-Baptiste, aka Jables
---

This package contains a single useful base model I was copying over and over onto every new project. It was time to package it up and reuse it.

This is a basic model from which all the project's model should inherit. It is defined as "[abstract](https://docs.djangoproject.com/en/3.1/topics/db/models/#abstract-base-classes)".
    
It defines a couple of basic fields every model should have:
- an ID as CharField/[NanoID](https://github.com/puyuan/py-nanoid): this avoids that content could be "discovered" if using auto increment and instead is a better UUID
    
- created_at: a datetime field with "auto_now_add", so we track when the model was created.
- updated_at: a datetime field with "auto_now", so we track when the model was last updated.

The name comes from Django Reinhart father, Jean-Baptiste (or Jables, for short).

### How to use it
1. Install the package `django-jables` as any other requirement to your project.

2. When creating models, inherit from `JBModel`:
```py
from jables.models import JBModel

class MyModel(JBModel):
    ...
```
