$(document).ready(function(){
	$('#submit').click(function(){
		getInputs()
	});
	function getInputs(){
		var getEmailContent = $('#emailContent').val()
		var getSenderEmail = $('#FromEmailAddress').val()
		var pattern = /^\b[A-Z0-9._%-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b$/i
		var mailContent = ''
		if(!pattern.test(getSenderEmail))
		{
			$('#alert1-div').html('<div id="divAlert" class="alert alert-danger" role="alert"> Please Check your email.. Invalid Email Address </div>')
			return false;
		}else if(getEmailContent == '' || getEmailContent == null){
			$('#alert2-div').html('<div id="divAlert" class="alert alert-danger" role="alert"> Enter Some Text... </div>')
			return false;
		}
		else{
			$('#alert1-div').empty();
			$('#alert2-div').empty();
		}
		$.ajax({
			url: '/sendEmail',
			data: {
				getEmailContent: getEmailContent,
				getSenderEmail: getSenderEmail
			},
			method: 'POST',
			beforeSend: function () {
				$('#waitme').waitMe({
					effect: 'bounce',
					text: 'Please wait...',
					bg: 'rgba(255,255,255,0.7)',
					color: '#435ebe',
					maxSize: '',
					waitTime: -1,
					textPos: 'vertical',
					fontSize: '',
					source: ''
				});
			},
			success: function (data) {
				console.log(data)
				if (data.res == false){
					Swal.fire({
						icon: 'error',
						title: 'Error!',
						showConfirmButton: true
					})
				}
				else{
					Swal.fire({
						icon: 'success',
						title: 'Sent!',
						showConfirmButton: true
					})
				}
			},

		}).done(function(){
			$('#waitme').waitMe('hide');

		})

	}

});