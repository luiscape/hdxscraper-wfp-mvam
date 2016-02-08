#
#  Makefile Instructions:
#  ----------------------
#
#  - setup:    installs all dependencies in a
#              Python virtual environment.
#  - run:      runs collector.
#  - tet:      runs tests.
#  - register: updates datasets on HDX with
#              resulting data.
#

setup:
	bash bin/setup.sh;

run:
	bash bin/run.sh;

test:
	bash bin/test.sh;

register:
	bash bin/register.sh;
