var medals_5ths = [];
var medals_5ths_cursor = 0;

var ribbons_5ths = [];
var ribbons_5ths_cursor = 0;

function get_medals_list()
{
	var list = [];
	$(".medals_list").each(function (){ list.push($(this)); });	
	return list;
}

function get_ribbons_list()
{
    var list = [];
	$(".ribbons_list").each(function (){ list.push($(this)); });	
	return list;
}

function show_list(pos,list)
{
        for (var i = 0; i < list.length; i++) {
            if (i == pos){
                    list[i].show();
            }
            else {
                  list[i].hide();
            }
        }        
}

function set_medals_cursor()
{
    if (medals_5ths_cursor == 0)
        {
            $("#prev_medals").css({ opacity: 0.1 });
        }
        else
        {
            $("#prev_medals").css({ opacity: 1.0 });
        }
        if (medals_5ths_cursor == (medals_5ths.length-1))
        {
           $("#next_medals").css({ opacity: 0.1 });
        }
        else
        {
            $("#next_medals").css({ opacity: 1.0 });
        }
}

function set_ribbons_cursor()
{
    if (ribbons_5ths_cursor == 0)
        {
            $("#prev_ribbons").css({ opacity: 0.1 });
        }
        else
        {
            $("#prev_ribbons").css({ opacity: 1.0 });
        }
        if (ribbons_5ths_cursor == (ribbons_5ths_cursor.length-1))
        {
           $("#next_ribbons").css({ opacity: 0.1 });
        }
        else
        {
            $("#next_ribbons").css({ opacity: 1.0 });
        }
}

function next_medals_list_click()
{
	if (medals_5ths_cursor < (medals_5ths.length-1))
	{
		medals_5ths_cursor++;
		show_list(medals_5ths_cursor,medals_5ths);
    set_medals_cursor();
	}
}

function prev_medals_list_click()
{
	if (medals_5ths_cursor > 0)
	{
		medals_5ths_cursor--;
		show_list(medals_5ths_cursor,medals_5ths);
        set_medals_cursor();
	}
}

function next_ribbons_list_click()
{
	if (ribbons_5ths_cursor < (ribbons_5ths.length-1))
	{
		ribbons_5ths_cursor++;
		show_list(ribbons_5ths_cursor,ribbons_5ths);
        	set_ribbons_cursor();
	}
}

function prev_ribbons_list_click()
{
	if (ribbons_5ths_cursor > 0)
	{
		ribbons_5ths_cursor--;
		show_list(ribbons_5ths_cursor,ribbons_5ths);
        	set_ribbons_cursor();
	}
}

$(document).ready(function(){
	medals_5ths = get_medals_list();
	show_list(medals_5ths_cursor,medals_5ths);
	set_medals_cursor();
	$("#prev_medals").click( prev_medals_list_click);
	$("#next_medals").click( next_medals_list_click);

	ribbons_5ths = get_ribbons_list();
	show_list(ribbons_5ths_cursor,ribbons_5ths);
	set_ribbons_cursor();    
	$("#prev_ribbons").click( prev_ribbons_list_click);
	$("#next_ribbons").click( next_ribbons_list_click);
});	
