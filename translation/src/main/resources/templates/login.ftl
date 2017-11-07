<#assign base=request.contextPath />
<#import "/spring.ftl" as spring/>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>登录页面</title>
</head>
<script type="text/javascript" src="${base}/static/jquery-2.1.1.min.js"></script>
<script type="text/javascript">
    $(function () {
        $("#formDiv").children(".label").each(function () {
            var v = $(this);
            $.ajax({
                type: 'get',
                url: "/translate",
                data: {s: $(this).text()},
                success: function (ss) {
                    v.html(ss);
                }
            });
        });
    });
</script>
<body>
<h1>i2b2 Login</h1>
<form>
    <div class="formDiv" id="formDiv">
        <@spring.message code='search'></@spring.message>
        <div class="label">Username:</div>
        <div class="input">
            <input type="text" name="uname" id="loginusr" value="demo" size="20" maxlength="50">
        </div>
        <div class="label">Password:</div>
        <div class="input">
            <input type="password" name="pword" id="loginpass" value="demouser" size="20" maxlength="50">
        </div>
        <div class="label">i2b2 Host:</div>
        <div class="input">
            <select name="server" id="logindomain" default="0">
                <option value="0">HarvardDemo</option>
            </select>
        </div>
        <div class="button">
            <input type="button" value="Login">
        </div>
    </div>
</form>
</body>
</html>