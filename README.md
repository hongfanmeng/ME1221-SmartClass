# ME1221-Smart Class

这是工程学导论的项目后端

# API list

## 说明

若进行无权限操作，会返回

```json
{
    "detail": "You do not have permission to perform this action."
}
```

若在要使用token的API中没有提交token ，则会返回

```json
{
    "detail": "Authentication credentials were not provided."
}
```

若提交的token错误，返回

```json
{
    "detail": "Invalid token."
}
```

## api-token-auth/

### POST（公开功能）

**Request**

发送用户名及密码请求

```json
{
    username:"student01",
    password:"student01"
}
```

**Response**

返回token 及所属用户组

```json
{
    "token": "537410732a4317fb58f93bea97516e9e6c7a2fd4",
    "groups": [
        "student"
    ]
}
```

**以下所有老师或学生API 需要在header 中加入**

```
Authorization: Token 537410732a4317fb58f93bea97516e9e6c7a2fd4
```

## votes/

### GET（公开功能）

查询所有目前投票的简略情况，choicesCount为选项数量，title为投票标题，id 为投票对应编号

```json
[
    {
        "id": 1,
        "title": "1 + 1 = ?",
        "choicesCount": 4
    },
    {
        "id": 2,
        "title": "3 + 1 = ?",
        "choicesCount": 2
    },
]
```

### POST（老师功能）

**Request**

新增一个投票，需要 title（投票标题），choicesCount（选项数量）

```json
{
    "title" : "1 + 1 = ?",
    "choicesCount" : 4
}
```

**Response**

返回新增的投票的详细资料，order 为选项顺序，voteCount为投该选项人数

```json
{
    "id": 2,
    "title": "3 + 1 = ?",
    "choicesCount": 2,
    "choices": [
        {
            "order": 1,
            "voteCount": 0
        },
        {
            "order": 2,
            "voteCount": 0
        }
    ]
}
```

此操作只有老师帐号有权限进行，若非老师帐户进行此操作，则返回



## votes/\<int:id>/

### GET（公开功能）

**Reponse**

查看对应 id 项的详细情况

```json
{
    "id": 2,
    "title": "3 + 1 = ?",
    "choicesCount": 2,
    "choices": [
        {
            "order": 1,
            "voteCount": 0
        },
        {
            "order": 2,
            "voteCount": 0
        }
    ]
}
```

### PUT（学生功能）

**Request**

对所请求的id的order 项投一票

```json
{
    "order" : 1
}
```

**Response**

注意∶choices 里面的 order : 1 该选项的 voteCount 改变了

```json
{
    "id": 1,
    "title": "3 + 1 = ?",
    "choicesCount": 2,
    "choices": [
        {
            "order": 1,
            "voteCount": 1 
        },
        {
            "order": 2,
            "voteCount": 0
        }
    ]
}
```

## vote/\<int:id>/status

### GET（学生功能）

**Response**

返回是否已经对id对应的问题进行投票

```json
{
    "hasVote": true
}
```

## feedbacks/

### GET（公开功能）

**Response**

获得所有的课堂反馈，feedbackType为反馈类型，有faster(讲快一点)，slower(讲慢一点)，notUnderstand(听不懂)，notClear(没听清)；created为反馈提交时间，可用于只显示最近反馈

```json
[
    {
        "feedbackType": "faster",
        "created": "2021-04-30T10:28:40.476611Z"
    },
    {
        "feedbackType": "slower",
        "created": "2021-04-30T10:29:59.852745Z"
    }
]
```

###  POST（学生功能）

**Request**

提交一个反馈，需要参数有feedbackType(反馈类型)

```json
{
    "feedbackType":"faster"
}
```

**Response**

返回提交返回的类型的提交时间

```json
{
    "feedbackType": "faster",
    "created": "2021-04-30T10:28:40.476611Z"
}
```

每次提交反馈后需要一分钟后才能提交下次反馈，若在一分钟内再次提交反馈，则返回

```json
{
    "detail": "Request was throttled. Expected available in 59 seconds."
}
```



## attendances/

### POST（老师功能）

**Request**

创建一个新签到，标题为title

```json
{
    "title": "Attendance 01"
}
```

**Response**

返回签到id，标题，创建时间。

```json
{
    "id": 1,
    "title": "Attendance 01",
    "created": "2021-05-18T08:42:20.960497Z"
}
```

### GET（公开功能）

返回所有签到

```json
[
    {
    	"id": 1,
    	"title": "Attendance 01",
    	"created": "2021-05-18T08:42:20.960497Z"
	}, 
    {
    	"id": 2,
    	"title": "Attendance 02",
    	"created": "2021-05-18T08:53:20.960497Z"
	},
]
```

## attendances/\<int:id>/

### PUT（学生功能）

**Reponse**

进行签到

```json
{
    "success": true
}
```

### GET（老师功能）

获取签到的详细内容，attendanceCount 为签到人数，users为签到用户的用户名

```json
{
    "id": 1,
    "title": "Attendance 01",
    "created": "2021-05-18T08:42:20.960497Z",
    "attendanceCount": 1,
    "users": [
        "student01"
    ]
}
```



## attendances/\<int:id>/status

### GET（学生功能）

查询是否已签到

```json
{
    "hasChecked" : true
}
```

