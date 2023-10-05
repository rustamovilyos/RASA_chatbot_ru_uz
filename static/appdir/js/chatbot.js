// on input/text enter--------------------------------------------------------------------------------------
$('.usrInput').on('keyup keypress', function (e) {
    const keyCode = e.keyCode || e.which;
    const text = $(".usrInput").val();
    if (keyCode === 13) {
        if (text === "" || $.trim(text) === '') {
            e.preventDefault();
            return false;
        } else {
            $(".usrInput").blur();
            setUserResponse(text);
            send(text);
            e.preventDefault();
            return false;
        }
    }
});


//------------------------------------- Set user response------------------------------------
function setUserResponse(val) {
    const UserResponse = '<div class="clearfix right-messages"><p class="userMsg">' + val + '</p><img class="userAvatar" alt="user" src="./static/appdir/img/userAvatar.jpg"></div>';
    $(UserResponse).appendTo('.chats').show('slow');
    $(".usrInput").val('');
    scrollToBottomOfResults();
    $('.suggestions').remove();
}

//---------------------------------- Scroll to the bottom of the chats-------------------------------
function scrollToBottomOfResults() {
    const terminalResultsDiv = document.getElementById('chats');
    terminalResultsDiv.scrollTop = terminalResultsDiv.scrollHeight;
}

function send(message) {
    console.log("User Message:", message)
    $.ajax({
        // # regions = us, eu, au, ap, sa, jp, in
        // # ngrok http 5005 --region au
        // url: 'https://cd07-195-158-3-102.ngrok-free.app/webhooks/rest/webhook',

        // localhost
        url: 'http://localhost:5005/webhooks/rest/webhook',
        type: 'POST',
        data: JSON.stringify({
            "message": message,
            "sender": "user"
        }),
        success: function (data, textStatus) {
            setBotResponse(data);
            console.log("Rasa Response: ", data, "\n Status:", textStatus)
        },
        error: function (errorMessage) {
            setBotResponse("");
            console.log('Error' + errorMessage);

        }
    });
}

//------------------------------------ Set bot response -------------------------------------
function setBotResponse(val) {
    setTimeout(function () {
        let BotResponse;
        let msg;
        if (val.length < 1) {
            //if there is no response from Rasa
            msg = 'Server not available. Please try again later.';

            BotResponse = '<div class="clearfix"><img class="botAvatar" src="./static/appdir/img/bot.ico" alt="bot">' +
                '<p class="botMsg">' + msg + '</p></div>';
            $(BotResponse).appendTo('.chats').hide().fadeIn(1000);

        } else {
            //if we get response from Rasa
            for (let i = 0; i < val.length; i++) {
                //check if there is text message
                if (val[i].hasOwnProperty("text")) {
                    BotResponse = '<div class="clearfix"><img class="botAvatar" src="./static/appdir/img/bot.ico" alt="bot">' +
                        '<p class="botMsg">' + val[i].text + '</p></div>';
                    $(BotResponse).appendTo('.chats').hide().fadeIn(1000);
                }

                //check if there is image
                if (val[i].hasOwnProperty("image")) {
                    BotResponse = '<div class="singleCard">' +
                        '<img class="imgcard" src="' + val[i].image + '">' +
                        '</div>';
                    $(BotResponse).appendTo('.chats').hide().fadeIn(1000);
                }

                //check if there is  button message
                if (val[i].hasOwnProperty("buttons")) {
                    addSuggestion(val[i].buttons);
                }

            }
            scrollToBottomOfResults();
        }

    }, 500);
}


// ------------------------------------------ Toggle chatbot -----------------------------------------------
$('#profile_div').click(function () {
    $('.profile_div').toggle();
    $('.widget').toggle();
    scrollToBottomOfResults();
});

$('#close').click(function () {
    $('.profile_div').toggle();
    $('.widget').toggle();
});


// ------------------------------------------ Suggestions -----------------------------------------------

function addSuggestion(textToAdd) {
    setTimeout(function () {
        const suggestions = textToAdd;
        const suggLength = textToAdd.length;
        $(' <div class="singleCard"> <div class="suggestions"><div class="menu"></div></div></diV>').appendTo('.chats').hide().fadeIn(1000);
        // Loop through suggestions
        for (i = 0; i < suggLength; i++) {
            $('<div class="menuChips" data-payload=\'' + (suggestions[i].payload) + '\'>' + suggestions[i].title + "</div>").appendTo(".menu");
        }
        scrollToBottomOfResults();
    }, 1000);
}


// on click of suggestions, get the value and send to rasa
$(document).on("click", ".menu .menuChips", function () {
    const text = this.innerText;
    const payload = this.getAttribute('data-payload');
    console.log("button payload: ", this.getAttribute('data-payload'))
    setUserResponse(text);
    send(payload);
    $('.suggestions').remove(); //delete the suggestions
});