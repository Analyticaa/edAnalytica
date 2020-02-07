// function go_page(quiz_id, page_num){
//     cacheAnswer();
//     // document.location.href = '?page='+page_num
//     doSubmit(page_num);
// }

function go_page(quiz_id, page_num){
    cacheAnswer();

    $.ajax({
        type: 'GET',
        url: '?page='+page_num,
        success: function(resultData) {
            $('#quiz-body').html(resultData);
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert(errorThrown);
        }
    });
}

// const paginationBtn = document.querySelector('button[name=pagination-btn]');
const submitBtn = document.querySelector('button[name=submit-btn]');

// paginationBtn.addEventListener('click', function() {
//     cacheAnswer();
// });

String.prototype.lpad = function(padString,  length){
    var str = this;
    while(str.length < length){
        str = padString + str;
    }
    return str;
}

function getTimeString(msec){
    var secs = parseInt(msec/1000);
    var hours = String(parseInt(secs/3600));
    var mins = String(parseInt((secs%3600)/60));
    var seconds = String(parseInt(secs%3600%60));
    hours = hours.lpad('0', 2);
    mins = mins.lpad('0', 2);
    seconds = seconds.lpad('0', 2);
    return hours+":"+mins+":"+seconds;
}

var timer = setInterval(myTimer ,1000);
function myTimer() {
    var startedAt = document.getElementById("started-at").value;
    var s = new Date(startedAt)
    var d = new Date();
    var diff = s - d;
    diff -= 1000;
    // console.log(diff);
    document.getElementById("timer").innerHTML = getTimeString(diff);
}

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

function quizSubmit(){
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
}

function doSubmit(answers){
    // var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });
    var submissionUUID = $('#submission-uuid').val();
    var data = {};
    data['submission_uuid'] = submissionUUID;
    data['answers'] = answers;
    $.ajax({
        type: 'POST',
        url: "/api/submission/",
        data: JSON.stringify(data),
        contentType: "application/json",
        success: function(resultData) {
            localStorage.setItem('quiz', {});
            document.location.href = '/s/quiz/'+submissionUUID+'/review/';
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