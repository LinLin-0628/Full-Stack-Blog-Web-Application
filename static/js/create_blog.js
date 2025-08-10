window.onload = function() {

    const { createEditor, createToolbar } = window.wangEditor

    const editorConfig = {
        placeholder: 'Type here...',
        onChange(editor) {
            const html = editor.getHtml()
            console.log('editor content', html)
            // You can sync HTML to <textarea>
        }
    }

    const editor = createEditor({
        selector: '#editor-container',
        html: '<p><br></p>',
        config: editorConfig,
        mode: 'default', // or 'simple'
    })

    const toolbarConfig = {}

    const toolbar = createToolbar({
        editor,
        selector: '#toolbar-container',
        config: toolbarConfig,
        mode: 'default', // or 'simple'
    })



    $("#submit-btn").click(function (event) {

        event.preventDefault()

        let title = $("input[name='title']").val()
        let category = $("#form-category").val()
        let content = editor.getHtml()
        let csrfmiddlewaretoken = $("input[name='csrfmiddlewaretoken']").val()

        $.ajax('/create', {
            method:"POST",
            data: {
                title,
                content,
                category,
                csrfmiddlewaretoken
            },
            success: function(result) {
                if (result["code"] == 200) {
                    let blog_id = result["data"]["blog_id"]
                    window.location = "/blog/" + blog_id
                }
                else {
                    alert(result["message"])
                }
            }
        })



    })

}