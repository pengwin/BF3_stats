$(document).ready(function(){
	$("#find_player").click(function(){
		var player_name = $("#player_name").val();
		
		if (player_name != "")
		{
			 window.location.href += player_name+"/";																																	}
		else
		{
			//show_result('Please enter player name');
		}
	});
});		

																																														