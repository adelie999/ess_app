$('.custom-file-input').on('change', handleFileSelect);
function handleFileSelect(evt) {
    $('#preview').remove();
    $(this).parents('.input-group').after('<div id="preview"></div>');
    var files = evt.target.files;

    for (var i = 0, f; f = files[i]; i++) {

        var reader = new FileReader();

        reader.onload = (function (theFile) {
            return function (e) {
                if (theFile.type.match('image.*')) {
                    var $html = [
                        '<div class="d-inline-block mr-1 mt-1"><img class="img-thumbnail" src="', e
                        .target.result, '" title="', escape(theFile.name),
                        '" style="height:100px;" /><div class="small text-muted text-center">',
                        escape(theFile.name), '</div></div>'
                    ].join('');
                } else {
                    var $html = ['<div class="d-inline-block mr-1"><span class="small">', escape(theFile
                        .name), '</span></div>'].join('');
                }

                $('#preview').append($html);
            };
        })(f);

        reader.readAsDataURL(f);
        
    }

    $(this).next('.custom-file-label').html(+files.length + '個のファイルを選択しました');
};

$('.reset').click(function () {
    $(this).parent().prev().children('.custom-file-label').html('ファイル選択...');
    $('.custom-file-input').val('');
    $('#preview').remove('');
});

$('#register').click(function() {
    console.log('test')
    var fm = document.getElementById("register_form");

    fm.method = "post";
    fm.target = "_self";
    fm.action = "form/register";
    fm.submit();
});