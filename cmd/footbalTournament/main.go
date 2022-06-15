package main

import (
	"fmt"
	"net/http"

	"github.com/PuerkitoBio/goquery"
)

// + results
// + standings
// + fixtures

const (
	urlMain   = "https://www.flashscore.com"
	urlEPL    = "england/premier-league/"
	urlL1     = "france/ligue-1/"
	urlBUNDES = "germany/bundesliga/"
	urlSA     = "italy/serie-a/"
	urlRPL    = "russia/premier-league/"
)

var (
	EPLTeams    = []string{"Manchester City", "Liverpool", "Chelsea", "Arsenal", "Manchester United", "Tottenham"}
	L1Teams     = []string{"Paris SG", "Monaco"}
	BUNDESTeams = []string{"RB Leipzig", "Dortmund", "Bayern Munich"}
	SATeams     = []string{"AC Milan", "Inter", "Napoli", "Atalanta", "AS Roma"}
	RPLTeams    = []string{"CSKA Moscow", "Spartak Moscow", "Krasnodar", "Lokomotiv Moscow", "Zenit"}
)

func main() {
	resp, err := http.Get(urlMain)
	if err != nil {
		fmt.Println(err)
	}
	defer resp.Body.Close()
	//	body, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Println(err)
	}

	doc, err := goquery.NewDocumentFromReader(resp.Body)
	if err != nil {
		fmt.Println(err)
	}

	// Find the review items
	s := doc.Find(".container__fsbody").Text()
	fmt.Println(s)
}
