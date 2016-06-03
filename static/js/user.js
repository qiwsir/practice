//register users and others about manage users
$(document).ready(function(){
    $("#username").focus();
});

$(document).ready(function(){

    $("#register").click(function(){
        var username = $("#username").val();
        var password = $("#password").val();
        var c_password = $("#c_password").val();
        var email = $("#email").val();
        //略去了用正则表达式校验长度和符号规则
        if (password == c_password){
            var post_data = {"username":username, "password":password, "email":email};
            var post_url = "";
            ajaxPostData(post_data, post_url);
        } else {
            layer.msg("两次所输入的密码不一样");
        }
        
    });
});

function ajaxPostData(post_data, post_url){
    $.ajax({
        type: 'post',
        url: post_url,
        data: post_data,
        dataType: "json",
        success: function(e){
            if(e == "1"){
                layer.msg("注册成功");
            } else if (e == "0") {
                layer.msg("用户名已经存在，请更换");
            } else{
                layer.msg("注册失败");
            }
        },
    });
}


