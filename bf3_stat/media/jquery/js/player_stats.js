var medals;

var ribbons = [];
var ribbons_cursor = 0;

$(document).ready(function(){

    medals = new ItemsList("medals_list");
    medals.set_up_list();

    ribbons = new ItemsList("ribbons_list");
    ribbons.set_up_list();

    $("#medals_prev").click(function(){ medals.move_left(); });
    $("#medals_next").click(function(){ medals.move_right(); });

     $("#ribbons_prev").click(function(){ ribbons.move_left(); });
     $("#ribbons_next").click(function(){ ribbons.move_right(); });
});

