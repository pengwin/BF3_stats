

$(document).ready(function(){
    canvas = document.getElementById("player_info").getContext('2d');
    if (canvas) {
        console.log('canvas is ok');



        var y_pos = 10;
        
        $("#player_name").keypress(function(){
            var player_name_part = $("#player_name").val();
            if  (player_name_part.length > 2)
            {
                $.ajax({
                url: '/ajax/player/search/'+player_name_part+'/',
                dataType: "json",
                success: function(data,textStatus)
                    {
                        canvas.clearRect(0,0,800,600);
                        $.each(data,function(i,val)
                        {
                            canvas.fillText(i+'  rank  '+val.rank,0,y_pos);
                            y_pos += 10;
                            var img = new Image();
                            img.onload = function() {
                                canvas.drawImage(img,0,y_pos);
                            };
                            img.src = val.rank_img;
                        });
                    }
                });
            }
        });


    }
    else
    {
        // canvas is not supported
        console.log('canvas is not supported');
    }
});

