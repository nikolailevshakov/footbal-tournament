SHELL=cmd.exe

run:
	python cmd/footbalTournament/main.py
	
login:
	ssh -i cmd/my-host-key.pem ec2-user@ec2-18-234-207-51.compute-1.amazonaws.com 
	
get_games:
	python scraper/get_games/main.py

get_results:
	python scraper/get_results/main.py

temp_run:
	python scraper/temp.py