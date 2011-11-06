<center>
	<img src="http://localhost:8000/static/images/bf3/rankslarge/r{{ rank }}.png">
	<h1>{{ name }} </h1>
	<h3>Last update {{ last_update }} <a href="update/">Update</a></h3>
	<div id="list">	
	<img id="prev_medals" class="prev_list" src="http://localhost:8000/static/images/prev.png">
{% for medals in medals_5th %}
	<ol class="medals_list">
		{% for medal in medals %}
			<li>
				<div class="progress_bar">
					<div class="bar_wrap">
			    		<div class="bar" style="width:{{ medal.percent }}%"></div>
					</div>
					<div class="captions">
			    		<div class="left">{{ medal.progress }} / {{ medal.needed }}</div>
			    		<div class="right">{{ medal.percent }}%</div>
					</div>
				</div>
				<br>
				<img src="http://localhost:8000/static/images/bf3/awards_m/{{ medal.id }}.png">
				<br>
				{{ medal.name }}
                {%if medal.count != 0 %}
                    x {{ medal.count }}
                {% endif %}
                <br>
				{{ medal.description }}		
			</li>	
		{% endfor %}				
	</ol>
{% endfor %}
<img id="next_medals" class="next_list" src="http://localhost:8000/static/images/next.png">
</div>

<div id="list">	
	<img id="prev_ribbons" class="prev_list" src="http://localhost:8000/static/images/prev.png">
{% for ribbons in ribbons_5th %}
	<ol class="ribbons_list">
		{% for ribbon in ribbons %}
			<li>
				<br>
				<img src="http://localhost:8000/static/images/bf3/awards_m/{{ ribbon.id }}.png">
				<br>
				{{ ribbon.name }}
                {%if ribbon.count != 0 %}
                    x {{ ribbon.count }}
                {% endif %}
                <br>
				{{ ribbon.description }}		
			</li>	
		{% endfor %}				
	</ol>
{% endfor %}
<img id="next_ribbons" class="next_list" src="http://localhost:8000/static/images/next.png">
</div>
</center>

