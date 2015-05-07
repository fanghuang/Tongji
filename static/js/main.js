$(function() {

$('#inputSearch').keyup(function(){
    console.log($('#inputSearch').val())  // sanity check
    $.ajax({
        url : "search_title/", // the endpoint
        type : "POST", // http method
        data : { search_text : $('#inputSearch').val() },
        success : function(json) {
            // alert('searched!');
            console.log(json); // log the returned json to the console
            $('#search_results').html(json); // hide the post on success
            console.log("successfully searched");
        },
        dataType: 'html',
        error : function(xhr,errmsg,err) {
            console.log("failed searching")
        }
    })
});

// AJAX for posting
function create_post() {
    console.log("create post is working!") // sanity check
    $.ajax({
        url : "create_post/", // the endpoint
        type : "POST", // http method
        data : { the_post : $('#post-text').val() }, // data sent with the post request

        // handle a successful response
            success : function(json) {
                $('#post-text').val(''); // remove the value from the input
                console.log(json); // log the returned json to the console
                $("#talk").prepend("<li><strong>"+json.text+"</strong> - <em> "+json.author+"</em> - <span> "+json.created+
                    "</span> - <a id='delete-post-"+json.postpk+"'>delete me</a></li>");
       //          $("#talk").prepend("<li id='post-"+json.postpk+"'><strong>"+json.text+"</strong> - <em> "+json.author+"</em> - <span> "+json.created+
    			// "</span> - <a id='delete-post-"+json.postpk+"'>delete me</a></li>");
                console.log("success"); // another sanity check
            },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

$("#accordion").on('click', 'button[id^=update-]', function(event){
    event.preventDefault();
    console.log("update "+$(this).attr('id').split('-')[1]);
    project_id = $(this).attr('id').split('-')[1];
    update_post(project_id);
});

function update_post(project_id){
    console.log("update_post is working")
    $.ajax({
        url : "update_post/", // the endpoint
        type : "POST", // http method
        data : {postpk : project_id,
                postleader : $('#leader-'+project_id).val(),
                postteacher : $('#teacher-'+project_id).val(),
                posttype : $('#type-'+project_id).val(),
                postdes : $('#description-'+project_id).val() }, // data sent with the delete request
        success : function(json) {
            alert('Updated!');
            console.log(json); // log the returned json to the console
          // $('#post-'+project_id).hide(); // hide the post on success
            console.log("post update successful");
        },
        error : function(xhr,errmsg,err) {
            // Show an error
            // $('#results').html("<div class='alert-box alert radius' data-alert>"+
            // "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
            // console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            console.log("BAD BAD BAD")
        }
    });
};

$("#accordion").on('click', 'button[id^=delete-]', function(event){
    event.preventDefault();
    console.log("delete "+$(this).attr('id').split('-')[1]);
    project_id = $(this).attr('id').split('-')[1];
    delete_post(project_id);
});

function delete_post(project_id){
    if (confirm('are you sure you want to remove this post?')==true){
        $.ajax({
            url : "delete_post/", // the endpoint
            type : "DELETE", // http method
            data : { postpk : project_id }, // data sent with the delete request
            success : function(json) {
                // hide the post
              $('#post-'+project_id).hide(); // hide the post on success
              console.log("post deletion successful");
            },

            error : function(json) {
                // Show an error
                // $('#results').html("<div class='alert-box alert radius' data-alert>"+
                // "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
                // console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                console.log("BAD BAD BAD");
                console.log(json);
            }
        });
    } else {
        return false;
    }
};


// nothing
// This function gets cookie with a given name
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
 
/*
The functions below will create a header with csrftoken
*/
 
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
 
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

console.log("last line of main.js")

});