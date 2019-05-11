$(document).ready(function(){
   $("#input").click(function(){
	    $("#booklist").attr("border", "1 px solid black");
      $.ajax({

                 type: "GET",

                 url: "books.xml",

                 dataType: "xml",

                 success: function(xml) {

                     $(xml).find('book').each(function(){

                        $category = $(this).attr('category');
						
						$title = $(this).find("title").text();
						
						
						var author = [];
						$(this).find('author').each(function(){
								author.push($(this).text());
								
								
						});
						$s = author.join(', ');
						
						
						$year = $(this).find("year").text();
						$price = $(this).find("price").text();
            
						$text = "<tr> <td>" +$title+ "</td><td>" + $s +"</td><td>" +$category+ "</td><td>" + $year +"</td><td>" + $price +"</td></tr>" ;
						$("#heading").after($text);
						
						
						
					 });
				 }
				
	  });
   });
});
        

   



