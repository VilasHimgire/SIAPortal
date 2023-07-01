$(document).ready(function() {
	$.ajax({
		url: '/api/questions/',
		type: 'GET',
		success: function(response) {
			var questions = response.data;
			for (var i = 0; i < questions.length; i++) {
				var q = questions[i];
				var questionDiv = $('<div class="form-group"></div>');
				var questionLabel = $('<label class="form-label"></label>').text(q.question);
				var optionsDiv = $('<div class="form-check"></div>');
				for (var j = 0; j < q.options.length; j++) {
					var option = q.options[j];
					var optionInput = $('<input class="form-check-input" type="radio" name="question-' + i + '" value="' + option + '">');
					var optionLabel = $('<label class="form-check-label"></label>').text(option);
					optionsDiv.append(optionInput);
					optionsDiv.append(optionLabel);
				}
				questionDiv.append(questionLabel);
				questionDiv.append(optionsDiv);
				$('#questions').append(questionDiv);
			}
		},
		error: function(response) {
			alert('Error fetching questions');
		}
	});
});
