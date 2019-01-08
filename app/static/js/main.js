$(function () {

    // 搜索按钮
    var searchBtn = $('.search-btn')
    searchBtn.click(function (e) {
        _hmt.push(['_trackEvent', 'search', 'button']);
        search();

    })

    $(".search-inner").keydown(function (e) {//当按下按键时
        if (e.which == 13) {//.which属性判断按下的是哪个键，回车键的键位序号为13
             _hmt.push(['_trackEvent', 'search', 'enter']);
             search();

        }
    });


})


function search() {
    var value = $('.search-inner').val()
    if (value) {
        var a = $(`<a class='tmp' href="/search?q=${value}"> </a>`)
        $('body').append(a)
        a[0].click()
        $('body').remove('.tmp')
    }
}