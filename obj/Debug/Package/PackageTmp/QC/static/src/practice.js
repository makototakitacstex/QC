$(function () {
    $('ul.list-group li').on('click', function () {
        if (!$(this).parent().hasClass('choiced')) {
            var $this = $(this);
            $this.siblings('.check').removeClass('check');
            $this.addClass('check');
            $this.parent().parent().next('decide').addClass('valid');
        }
    });
    $('.decide').on('click', function () {
        if ($(this).hasClass('valid')) {
            var $this = $(this);
            var answer = $this.prev().find('.check').data('answer');
/*
            var correct = $this.data('correct');
            var anstxt = "あなたの答え：" + answer;
            var corrtxt = "正解：" + correct;
            if (answer == correct) {
                var result = "正解";
            } else {
                var result = "不正解";
            }
            var restxt = '<h4>' + result + '</h4><p><span>' + anstxt + '</span> / <b class="txtxl">' + corrtxt + '</b></p>';
            $this.next().attr('data-result', result).children('.answer').html(restxt);
            $this.prev().find('li:nth-of-type(' + correct + ')').addClass('correct');
            $this.slideToggle(400).next('.descbox').slideToggle(400);
            $this.prev().children('.quelist.choice').removeClass('choice').addClass('choiced');
*/
            $this.prev().find('komarigoto_code').val(answer)

        }
    });

});