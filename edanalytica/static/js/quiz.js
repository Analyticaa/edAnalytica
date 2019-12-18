function go_page(quiz_id, page_num){
    document.location.href = '/s/quiz/'+quiz_id+'/?page='+page_num
}

const paginationBtn = document.querySelector('button[name=pagination-btn]');
const submitBtn = document.querySelector('button[name=submit-btn]');

paginationBtn.addEventListener('click', function() {
    cacheAnswer();
});

function cacheAnswer(){
    var qs = document.querySelectorAll("input[type='radio']:checked")
    var quiz = localStorage.getItem('quiz');
    if(quiz === null){
        quiz = {}
    } else {
        quiz = JSON.parse(quiz);
    }
    qs.forEach(function(q){
        quiz[q.name] = q.value
    });
    quiz = JSON.stringify(quiz);
    localStorage.setItem('quiz', quiz);
}

$(function(){
    var quiz = localStorage.getItem('quiz');
    if(quiz === null){
        quiz = {}
    } else {
        quiz = JSON.parse(quiz); 
    }
    Object.keys(quiz).forEach(function (key){
        // console.log(quiz[key]);
        $('input[name="'+key+'"][value="'+quiz[key]+'"]').prop('checked', true);
    });
});

if(submitBtn != null){
    submitBtn.addEventListener('click', function(){
        cacheAnswer();
        var quiz = localStorage.getItem('quiz');
        if(quiz === null){
            quiz = {}
        } else {
            quiz = JSON.parse(quiz); 
        }
        var answers = [];
        Object.keys(quiz).forEach(function (key){
            answers.push({"question_id": key, "answer": quiz[key]})
        });
        doSubmit(answers);
    });
}

function doSubmit(answers){
    // var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });
    var quizId = $('#quizId').val();
    var data = {};
    data['quiz'] = quizId;
    data['answers'] = answers;
    $.ajax({
        type: 'POST',
        url: "/api/submission/",
        data: JSON.stringify(data),
        contentType: "application/json",
        success: function(resultData) {
            localStorage.setItem('quiz', {});
            document.location.href = '/s/quiz/'+quizId+'/review/';
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert(errorThrown);
        }
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}