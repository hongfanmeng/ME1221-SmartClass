# ME1221-Smart Class
这是工程学导论的项目后端

## API list
### votes/
#### GET Response

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

#### POST

##### Request

新增一个投票，需要 title（投票标题），choicesCount（选项数量）

```json
{
    "title" : "1 + 1 = ?",
    "choicesCount" : 4
}
```

##### Response

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

### votes/\<int:id>/

#### GET Reponse

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

#### POST

##### Request

对所请求的id的order 项投一票

```json
{
    "order" : 1
}
```

##### Response

注意∶choices 里面的 order : 1 该选项的 voteCount 改变了

```json
{
    "id": 2,
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

### feedbacks/

#### GET Response

获得所有的课堂反馈，feedbackType为反馈类型，有faster(讲快一点)，slower(讲慢一点)，待加；created为反馈提交时间，可用于只显示最近反馈

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

####  POST

##### Request

提交一个反馈，需要参数有feedbackType(反馈类型)

```json
{
    "feedbackType":"faster"
}
```

##### Response

返回提交返回的类型的提交时间

```json
{
    "feedbackType": "faster",
    "created": "2021-04-30T10:28:40.476611Z"
}
```



