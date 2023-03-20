# improved-computing-machine

## Links

* `/` - to obtain login token
* `login/refresh/` - to refresh login token
* `register/` - to Register user and creates wallet for each user
* `/update-wid` - [GET] to update wallet value based on wid
* `/update-uid` - [GET] to update wallet value based on uid
* `/get-uid` - [POST] To get wallet values based on uid
* `/get-uid/?uid=[uid]` - [GET] To get wallet values based on uid RETURNS the queryset
* `/get-wid` - [POST] To get wallet values based on wid
* `/get-wid/?wid=[wid]` - [GET] To get wallet values based on wid RETURNS the queryset
* `/get-name` - [POST] To get first_name & last_name of the user values based on uid
* `/get-name/?uid=[uid]` - [POST] To get first_name & last_name of the user values based on uid {'first_name', 'last_name'}

## Station endpoints

* `charge/` - Lists the existing stations and there status
* `charge/lock` - Locks the cid with user input and updates the status but stays on the page loading till the lock is unlocked(1 minute) but the server can be access from different instances meanwhile input{'uid', 'cid'}
* `charge/get-stat/?cid=[cid]` - [GET] gives the status of the charging station using the cid.
* `charge/create-stat` - [POST] used to create new instance of station which return the cid, and the created_at instance.