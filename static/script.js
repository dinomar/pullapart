
//http://www.animeplus.tv/images/site/front/logo.png

function getImagesName(url) {
  let arr = url.split("/");
  result = arr.slice(arr.length - 1);
  return result;
}

$(document).ready(function() {

  //focus on search
  $("#url").focus();

  //Form Submit
  $("#searchForm").submit(function(e) {

    let search = $("#url").val();

    //no user input
    if(!search) {
      e.preventDefault();
      return null;
    }

    //handle search box
    $("#url").removeClass("showSearch");
    $("#url").addClass("hideSearch");
    $("#url").val("");

    let parameters = {
        url: search
    };

    $.getJSON("/info", parameters, function(data) {

      //images
      $("#images").html(""); //clear images ul
      data["images"].forEach(function(img) {
        let alt = getImagesName(img);
        $("#images").append(`<li><img src="${img}" alt="${alt}" class="img-thumbnail imgTemplate"></li>`);
      });

      //links
      let linksString = "";
      data["links"].forEach(function(link) {
        linksString += link + "\n";
      });
      $("#links").val(linksString);

      //css
      let cssString = "";
      data["css"].forEach(function(css) {
        cssString += css + "\n";
      });
      $("#css").val(cssString);

      //scripts
      let scriptsString = "";
      data["scripts"].forEach(function(script) {
        scriptsString += script + "\n";
      });
      $("#scripts").val(scriptsString);

    });

    e.preventDefault();
  });

});