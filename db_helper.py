#! ./venv/bin/python
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dvzo.settings")
django.setup()

from train_management.tests.helpers import SetupHelper  # noqa

setup_helper = SetupHelper()
setup_helper.create_train_components()

day_planning_1 = setup_helper.get_day_planning()
train_1 = setup_helper.get_train(day_planning_1)
setup_helper.create_train_config(train_1)

train_3 = setup_helper.get_train(day_planning_1)
setup_helper.create_train_config(train_3)

day_planning_2 = setup_helper.get_day_planning(
    date_str="2021-05-22", label="Whatever Planning")
train_2 = setup_helper.get_train(day_planning_2)
setup_helper.create_train_config(train_2)
