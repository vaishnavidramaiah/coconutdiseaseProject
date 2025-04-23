$(document).ready(function () {
    $('.image-section').hide();
    $('.loader').hide();
    $('#result').hide();

    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
                $('#imagePreview').hide();
                $('#imagePreview').fadeIn(650);
            };
            reader.readAsDataURL(input.files[0]);
        }
    }

    $("#imageUpload").change(function () {
        $('.image-section').show();
        $('#btn-predict').show();
        $('#result').text('');
        $('#result').hide();
        readURL(this);
    });

    $('#btn-predict').click(function (e) {
        e.preventDefault(); // Prevent default form submission

        var form_data = new FormData($('#upload-file')[0]);

        // Show loading animation
        $(this).hide();
        $('.loader').show();

        // Make prediction via AJAX
        $.ajax({
            type: 'POST',
            url: '/predict',  // Updated endpoint for prediction
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (response) {
                if (response.redirect_url) {
                    window.location.href = response.redirect_url; // Redirect to base.html with prediction
                }
            },
            error: function (xhr) {
                $('.loader').hide();
                $('#result').fadeIn(600);
                $('#result').html('<span style="color: red;">Error: ' + xhr.responseText + '</span>');
            }
        });
    });

});
