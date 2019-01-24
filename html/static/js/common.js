//格式化日期
Date.prototype.Format = function (fmt) {
    if (fmt == 'human') {
        var currentDate = new Date();
        var seconds = (currentDate.getTime() - this.getTime()) / 1000;
        if (seconds < 60) {
            return "刚刚"
        }
        else if (seconds < 60 * 60) {
            return parseInt(seconds / 60) + "分钟前"
        }
        else if (seconds < 60 * 60 * 24) {
            return parseInt(seconds / 60 / 60) + "小时前"
        }
        else if (seconds < 60 * 60 * 24 * 3) {
            return parseInt(seconds / 60 / 60 / 24) + "天前"
        }
        else {
            return this.getFullYear() + '-' + (this.getMonth() + 1) +'-'+ this.getDate()
        }

    }


    var o = {
        "y+": this.getFullYear(),
        "M+": this.getMonth() + 1,                 //月份
        "d+": this.getDate(),                    //日
        "h+": this.getHours(),                   //小时
        "m+": this.getMinutes(),                 //分
        "s+": this.getSeconds(),                 //秒
        "q+": Math.floor((this.getMonth() + 3) / 3), //季度
        "S+": this.getMilliseconds()             //毫秒
    };
    for (var k in o) {
        if (new RegExp("(" + k + ")").test(fmt)) {
            if (k == "y+") {
                fmt = fmt.replace(RegExp.$1, ("" + o[k]).substr(4 - RegExp.$1.length));
            }
            else if (k == "S+") {
                var lens = RegExp.$1.length;
                lens = lens == 1 ? 3 : lens;
                fmt = fmt.replace(RegExp.$1, ("00" + o[k]).substr(("" + o[k]).length - 1, lens));
            }
            else {
                fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
            }
        }
    }
    return fmt;
}

// 加载更多
function loadMore(url, cate, cb) {
    console.log(cate)
    url = url.trim()
    var $scope = {
        currentPage: 1, // 当前页
        pageSize: 10,  // 每页显示数量
        noMore: false,
        loading: false,
        getData: function (page, pageSize, cate) {
            $.ajax({
                url: url,
                data: {
                    page: page,
                    size: pageSize,
                    cate: cate,
                },
                success: function (res) {
                    $scope.loading = false
                    $('.loading.ball-pulse').hide()
                    if (res.data.length < $scope.pageSize) {
                        $scope.noMore = true
                    }
                    cb && cb(res)
                }
            })
        }
    }

    // 监听下拉事件
    $(window).on('scroll', function(){
        console.log(cate)
        var s = $(window).scrollTop(),
            h = $(window).height(),
            documentH = $(document).height();
        if ((s + h + 100) >= documentH && !$scope.noMore) {
            if (!$scope.loading) {
                $scope.loading = true
                $('.loading.ball-pulse').show();

                $scope.getData(++$scope.currentPage, $scope.pageSize, cate);
            }
        }
        if (s > 74) {
            $('.wchannel').addClass('wchannel-fixed')
        } else {
            $('.wchannel').removeClass('wchannel-fixed')
        }
    })

}
