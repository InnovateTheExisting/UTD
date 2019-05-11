$(document).ready(function(){
	$("#country").change(function() {
		var data = {
			country : $("#country").val()
		};
		$.ajax({
			type:"POST",
			url : "update.php",
			data : data,
			dataType : 'json',
			success : function(response) {
				$("#state option").remove();
				$("#city option").remove();
				var len = response.length;
				var none = "<option value='0'>Select</option>";
				$("#state").append(none);
				$("#city").append(none);
				for(var i=0; i<len; i++){
					var option = "<option value="+ response[i].id +">" + response[i].name + "</option>";
					$("#state").append(option);
				}
			},
			error: function() {
				alert('Error occured');
			}
		});
	});

	$("#state").change(function() {
		if($("#state").val()!=0){
			var data = {
				state : $("#state").val()
			};
			$.ajax({
				type:"POST",
				url : "update.php",
				data : data,
				dataType : 'json',
				success : function(response) {
					$("#city option").remove();
					var len = response.length;
					var none = "<option value='0'>Select</option>";
					$("#city").append(none);
					for(var i=0; i<len; i++){
						var option = "<option value="+ response[i].id +">" + response[i].name + "</option>";
						$("#city").append(option);
					}
				},
				error: function() {
					alert('Error occured');
				}
			});
		}
		else{
			$("#city option").remove();
			var none = "<option value='0'>Select</option>";
			$("#city").append(none);
		}
	});
});