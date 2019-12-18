function go_page(quiz_id, page_num){
    document.location.href = '/s/quiz/'+quiz_id+'/review/?page='+page_num
}

$(function(){
    $("button[name='view-steps-btn']").on('click',function(){
        var sId = $(this).attr('sId');
        var qIdx = $(this).attr('qIdx');
        // console.log(sId);
        $('.modal-body').load('/s/quiz/steps/?sId='+sId+'&qIdx='+qIdx,function(){
            $('#myModalone').modal({show:true});
        });
    });
});
