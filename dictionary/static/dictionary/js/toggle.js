/**
 * Created by MBK on 14/01/16.
 */
$(document).ready(function(){
	$(".toggle").click(function(){
		$(this).parent().next(".examples").slideToggle("fast");
		if ($(this).text() == 'Toggle fewer examples') {
            $(this).text('Toggle more examples');
            $(this).css("background-color","#9b9b9b");
        } else {
            $(this).text('Toggle fewer examples');
            $(this).css("background-color","lightgray");
        }
		return false;
	});
});
