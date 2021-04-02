# CeneoScraperS11
## Stage 1 - extraction of all components for single opinion
1. extracion of single web page content
2. analysis of single opinion structure
| Component | CSS selector | Variable name | Data type |
| --- | --- | --- | --- |
| Opinion | div.user-post__card  |opinion | _ |
| Opinion  id | ["data-entry-id"] | opinion_id | _ | 
| Author | span.user-post__author-name | author | _ |
| Recommendation | span.user-post__author-recomendation > em | recommendation | _ |
| Stars rating | span.user-post__score_count | stars | _ |
| Content | div.user-post__text | content | _ |
| Advantages | 	div.review-feature__col:has(> div[class$="positives"]) > div.review-feature__item | pros | _ |
| Disadvantages | div.review-feature__col:has(> div[class$="negatives"]) > div.review-feature__item | cons | _ |
| Verification | div.review-pz | verified | _ |
| Post date | span.user-post__published > time:nth-child(1)["datetime"] | post_date | _ | 
| Purchase date | span.user-post__published > time:nth-child(2)["datetime"] | purchase_date | _ |
| Usefulness count | span[id^="votes-yes] | usefulness | _ |
| Uselessness count | span[id^="votes-no] | uselessness | _ |

3. extracion of single opinion components
4. transformation of extracted data to given data types