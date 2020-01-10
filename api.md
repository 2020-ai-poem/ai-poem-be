# ai-poem-be
the back end of ai-poem

### 邮箱验证：
+ api:    url+emailCheck
+ param:  email
+ return: 
          {<br>
          'isOk': true/false,//若为false，则无'number'<br>
	        'errmsg': "未知错误"//默认为未知错误，考虑到该邮箱已注册<br>
	        'number': ''//四位数的str类型验证码
          }
+ <b>注：需要前端进行判断验证码是否正确（后端向注册邮箱发送验证码，并将该验证码返回给前端用于前端判断。）

### 注册：
+ api:		url+signUp
+ param: email,username,password
+return: 
          {<br>
          'isOk': true/false,//若用户名存在则为false<br>
	        'errmsg': "未知错误"<br>
          }
+ <b> 注：该api只判断用户名是否唯一，邮箱在emailCheck时已经判断。
					
### 登录：
+ api:		url+signIn
+ params: email,username(二选一即可),password
+ return: 
          {<br>
          'isOk': true/false,<br>
	        'errmsg': "未知错误"/'密码错误'/'邮箱错误'/'用户名错误'<br>
          }
	 

### 修改信息：
+ api:		url+modifyInfo
+ params: email,userName,password,sex,age,birthDate
+ return: 
          {<br>
          'isOk': true/false,<br>
	        'errmsg': "未知错误"/'请先登录'/'该用户名已存在'<br>
          }
+ <b>注：该接口必须在已登录情况下使用，传参时，只传递用户需修改的属性，不修改则不传该参数。对于email验证可先通过emailCheck接口；对于userName唯一性问题，后端进行了验证，若用户名不唯一，返回‘该用户名已存在’，该情况下，其他传入的参数并未修改。
	
### 注销登录：
+ api:		url+signOut
+ params: 
+ return: 
          {<br>
          'isOk': true/false,<br>
	        'errmsg': "未知错误"<br>
          }
+ <b>注：该接口用于注销登录，删除客户端与服务器间的cookie值。该接口不需要参数，返回值Ture表示之前为登录状态，现在注销成功;False为之前就不是登录，虽然注销失败，但也表明用户现在不在登录状态。

### 查询用户信息：
+ api:		url+getInfo
+ params: 
+ return: 
          {<br>
          'isOk': true/false,<br>
	  'errmsg': "未知错误"/"请先登录"<br>
	  'email': <br>
	  'userName':<br>
	  'age':<br>
	  'birthDate':<br>
	  'sex':<br>
	  'userId':<br>
          }
+ <b>注：当’isOK'为false时，只返回'isok'和'errmsg'