function go_page(quiz_id, page_num){
    document.location.href = '/s/quiz/'+quiz_id+'/?page='+page_num
}

const paginationBtn = document.querySelector('button[name=pagination-btn]');
const submitBtn = document.querySelector('button[name=submit-btn]');


paginationBtn.addEventListener('click', function() {
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
});

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
        var quiz = localStorage.getItem('quiz');
        if(quiz === null){
            quiz = {}
        } else {
            quiz = JSON.parse(quiz); 
        }
        var data = [];
        Object.keys(quiz).forEach(function (key){
            data.push({"question_id": key, "answer": quiz[key]})
        });
        console.log(data);
        localStorage.removeItem('quiz', null);
    });
}