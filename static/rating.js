var ratings_lists = document.getElementsByClassName("review mainheaderrating")

for (let i = 0, ratings_len = ratings_lists.length; i < ratings_len; i++) {
    let ratingValueString = ratings_lists[i].querySelector("p").innerHTML;
    let ratingValue = parseInt(ratingValueString, 10);
    let stars = ratings_lists[i].getElementsByClassName("starcontainer")[0].children;
    for (let j = 0, len = ratingValue; j < len; j++) {
        let star = stars.item(j)
        star.classList.add("checked")
    }
}

console.log(ratings_lists)