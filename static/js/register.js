
// When DOM loaded
$(function () {
    function bindCaptcha() {
        $("#captcha-btn").click(function(event) {
            // Get email address
            let $this = $(this)

            let email = $("input[name='email']").val();

            if (!email) {
                alert("Please enter your email address first.");
                return;
            }

            // Cancel click event
            $this.off('click');

            // Send AJAX request
            $.ajax('/auth/captcha?email=' + email, {
                method: "GET",
                success: function(result) {
                    if (result["code"] === 200) {
                        alert("Verification code sent successfully")
                    } else {
                        alert(result["message"])
                    }
                },
                fail: function(error) {
                    console.log((error))
                }
            })

            // Counter
            let countdown = 6;

            let timer = setInterval(function () {
                if (countdown <= 0) {
                    $this.text("Get Code");
                    // Remove timer
                    clearInterval(timer)

                    // Bind click event
                    bindCaptcha();
                }
                else{
                    $this.text(countdown + " seconds")
                    countdown--;
                }

            }, 1000)
        })
    }

    bindCaptcha();
})