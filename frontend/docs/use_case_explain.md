# Provide detail for use-case diagram

## Brief-description

Notification manage time by card. Each card contains list of detail information
relate to a specific task/activity. With this model, the author expects to
leverage the power of card sequence for profiling and visualizing daily actions.

Notification front-end share the same idea with main project, it is designed as
a unique app to hold and control list of task/activity cards and depend on
back-end as a concentration repository to store card ( although itself have
mechanism to store card in local ). This type of model inspired from git model
where git used to store local project and sync with git server as large storage.

## Diagram components

1. **Dashboard**: used to monitor and view list of cards. User can **Add** new
card, **Delete** or **Search** from card list.

2. **Detail**: used to view detail of single card. User can **Modify** detail and
**Save** back to storage.

3. Server: used to connect and interact with back-end. User can **Pull** card
from server to local storage, **push** new or updated card to server and
**Delete** exited card on server.
