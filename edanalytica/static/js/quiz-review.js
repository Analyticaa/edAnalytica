function go_page(quiz_id, page_num){
    document.location.href = '?page='+page_num
}

$(function(){
    $("button[name='view-steps-btn']").on('click',function(){
        var sId = $(this).attr('sId');
        var qIdx = $(this).attr('qIdx');
        // console.log(sId);
        $('.modal-body').load('/s/quiz/steps/?sId='+sId+'&qIdx='+qIdx,function(){
            $('#myModalone').modal({show:true});
            injectIndiaBix();
        });
    });
});

function injectIndiaBix(){
    const modalBody = document.querySelector('.modal-body');
    const images = modalBody.querySelectorAll('img');
    images.forEach(function(img){
        var src = $(img).attr('src');
        $(img).attr('src', 'https://indiabix.com'+src);
    })
}