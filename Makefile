# code templates
gen_temp:
	# generate code from models
	# ex: make gen_temp app=pixbum.userapp
	python manage.py generator app $(app)
gen_temp_all:
	for app in pixbum.userapp; do \
		python manage.py generator app $$app ; \
	done

# docker compose in development
build_dev:
	docker-compose -f local.yml up --build
dev:
	docker-compose -f local.yml down
	docker-compose -f local.yml up
test:
	docker-compose -f local.yml run web pytest

redeploy-staging:
	bash redeploy.sh