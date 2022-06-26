SHELL=cmd.exe

run:
	go run cmd/footbalTournament/main.go
	
login:
	ssh -i cmd/my-host-key.pem ec2-user@ec2-18-234-207-51.compute-1.amazonaws.com 

build:
	go build cmd/footbalTournament/main.go
	
get_games:
	python scraper/get_games/main.py

get_results:
	python scraper/get_results/main.py

temp_run:
	python scraper/temp.py