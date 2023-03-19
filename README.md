# improved-computing-machine

## Links

* `/` - to obtain login token
* `login/refresh/` - to refresh login token
* `register/` - to Register user and creates wallet for each user
* `/update-wid` - to update wallet value based on wid
* `/update-uid` - to update wallet value based on uid
* `/get-uid` - To get wallet values based on uid
* `/get-wid` - To get wallet values based on wid
* `/get-name` - To get first_name & last_name of the user values based on uid

## Station endpoints

* `charge/` - Lists the existing stations and there status
* `charge/lock` - Locks the cid with user input and updates the status but stays on the page loading till the lock is unlocked(1 minute) but the server can be access from different instances meanwhile
* `charge/get-stat?cid=[cid]` - [GET] gives the status of the charging station using the cid.
* `charge/create-stat` - [POST] used to create new instance of station which return the cid, and the created_at instance.
