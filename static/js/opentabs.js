function openPage(evt, pagename) {

$('body').on('click', 'li', function() {
      $('li.active').removeClass('active');
      $(this).addClass('active');
});
$(this).addClass('active');

$('.maincontanet').empty();
$.get(pagename, function (data) {
                    $(".maincontanet").append(data);
                });


}


$(document).ready(function(){
 $('.m1').addClass('active');

})


$(document).ready( function() {
$('.maincontanet').empty();
$.get("home.html", function (data) {
                    $(".maincontanet").append(data);
                });
});



$(document).ready(function() {

getData();
  function getData() {
    $.ajax({
      url: 'data',
      method: 'GET',
      dataType: "json",
      error: function(xhr, status, error) {
        console.log(status, error);
      },
      success: function(json) {
        var tr;
        html='<table class=" tt1 table table-striped"> <thead><tr> <th>Region</th> <th>Country</th> <th>Sla</th> <th>Abends</th> <th>Recovered</th> <th>DWH</th> <th>ORP</th> <th>Genisis</th> <th>Cards</th> <th>Bank</th> </tr></thead> </table>'
        $(".ProgresSummary").append(html);
        $.each(json.records, function(k, v) {
          thead=$("<thead></thead>")
          tb = $("<tbody></tbody>");
          tr=$("<tr></tr>");
          tr.append("<td>" + v.REGION + "</td>");
          tr.append("<td>" + v.COUNTRY+ "</td>");
          tr.append("<td>" + v.SLA + "</td>");
          tr.append("<td>" + v.ABEND+ "</td>");
          tr.append("<td>" + v.RECOVERD+ "</td>");
          tr.append("<td>" + v.DWH+ "</td>");
          tr.append("<td>" + v.ORP+ "</td>");
          tr.append("<td>" + v.GENISIS+ "</td>");
          tr.append("<td>" + v.CARDS+ "</td>");
          tr.append("<td>" + v.BANK+ "</td>");
          tb.append(tr)
          $(".tt1").append(tb);
        });
      }
    });
  }

  $.get("data1", function (data) {
                    $(".ProgresSummary").append(data);
                });


});