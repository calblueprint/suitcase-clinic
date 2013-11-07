function sortNewestFirst(a, b) {
  var date1 = a.children[4].textContent;
  date1 = date1.split('/');
  date1 = new Date(date1[2], date1[0], date1[1] - 1);
  var date2 = b.children[4].textContent;
  date2 = date2.split('/');
  date2 = new Date(date2[2], date2[0], date2[1] - 1);
  return date1 < date2 ? 1 : -1;
}

function sortOldestFirst(a, b) {
  var date1 = a.children[4].textContent;
  date1 = date1.split('/');
  date1 = new Date(date1[2], date1[0], date1[1] - 1);
  var date2 = b.children[4].textContent;
  date2 = date2.split('/');
  date2 = new Date(date2[2], date2[0], date2[1] - 1);
  return date1 > date2 ? 1 : -1;
}

function sortLowestReviewFirst(a, b) {
  rating1 = a.children[2].className;
  rating2 = b.children[2].className;
  return rating1 > rating2 ? 1 : -1;
}

function sortHighestReviewFirst(a, b) {
  rating1 = a.children[2].className;
  rating2 = b.children[2].className;
  return rating1 < rating2 ? 1 : -1;
}

// function sortOldestFirst(a, b) {
//   var date1 = $(a).find(".review_date").textContent;
//   date1 = date1.split('/');
//   date1 = new Date(date1[2], date1[1] - 1, date1[0]);
//   var date2 = $(b).find(".review_date").textContent;
//   date2 = date2.split('/');
//   date2 = new Date(date2[2], date2[1] - 1, date2[0]);
//   return date1 > date2 ? 1 : -1;
// }

$(document).ready(function () {

  var desc = false;
  document.getElementById("sort_dropdown").onchange = function () {
    var waitTime = 400;
    $('ul#reviews > li').fadeOut(waitTime);
    setTimeout(function() {
      if (document.getElementById("sort_dropdown").value == "newest") {
        $('ul#reviews > li').sort(sortNewestFirst).appendTo('ul#reviews');
      } else if (document.getElementById("sort_dropdown").value == "oldest") {
        $('ul#reviews > li').sort(sortOldestFirst).appendTo('ul#reviews');
      } else if (document.getElementById("sort_dropdown").value == "lowestReview") {
        $('ul#reviews > li').sort(sortLowestReviewFirst).appendTo('ul#reviews');
      } else if (document.getElementById("sort_dropdown").value == "highestReview") {
      $('ul#reviews > li').sort(sortHighestReviewFirst).appendTo('ul#reviews');
      }

    }, waitTime)
    
    $('ul#reviews > li').fadeIn(waitTime);
    return false;
  };

  //Sorts descending based on value of date as default.
  $('li.review').sort(sortNewestFirst).appendTo('ul#reviews');
});