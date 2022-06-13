package main

import (
	"fmt"
	"net/http"

	"golang.org/x/net/html"
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
	doc, err := html.Parse(resp.Body)
	if err != nil {
		fmt.Println(err)
	}
	var f func(*html.Node)
	f = func(n *html.Node) {
		if n.Type == html.ElementNode && n.Data == "a" {
			for _, a := range n.Attr {
				if a.Key == "href" {
					fmt.Println(a.Val)
					break
				}
			}
		}
	}
	f(doc)
}
