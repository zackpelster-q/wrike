# Wrike

## Thanks!
Thank you to Pretzel for the great tutorial on creating a Python JSON REST API wrapper library, I would not have gotten very far without it!
Go to [Python JSON REST API wrapper library: a How-To in 15 simple steps](https://www.pretzellogix.net/2021/12/08/how-to-write-a-python3-sdk-library-module-for-a-json-rest-api/) to see Pretzel's tutorial and create your own wrapper library.

## Implementation Status
| Other                     | Links                                                         | Added | Tested | Examples | Complete |
|---------------------------|---------------------------------------------------------------|-------|--------|----------|----------|
| Permnent Access Token     | https://developers.wrike.com/oauth-20-authorization/          | [x]   | [x]    | [x]      | [ ]      |
| OAuth 2.0 Authorization   | https://developers.wrike.com/oauth-20-authorization/          | [ ]   | [ ]    | [ ]      | [ ]      |
| Webhooks                  | https://developers.wrike.com/webhooks/                        | [ ]   | [ ]    | [ ]      | [ ]      |

### Method Implementation Status
| Methods                   | Links                                                         | GET | POST | PUT | DELETE | Tested | Complete |
|---------------------------|---------------------------------------------------------------|-----|------|-----|--------|--------|----------|
| Contacts                  | https://developers.wrike.com/api/v4/contacts/                 | [x] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Users                     | https://developers.wrike.com/api/v4/users/                    | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Groups                    | https://developers.wrike.com/api/v4/groups/                   | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Invitations               | https://developers.wrike.com/api/v4/invitations/              | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Account                   | https://developers.wrike.com/api/v4/account/                  | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Workflows                 | https://developers.wrike.com/api/v4/workflows/                | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Custom Fields             | https://developers.wrike.com/api/v4/custom-fields/            | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Folders & Projects        | https://developers.wrike.com/api/v4/folders-projects/         | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Tasks                     | https://developers.wrike.com/api/v4/tasks/                    | [x] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Comments                  | https://developers.wrike.com/api/v4/comments/                 | [x] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Dependencies              | https://developers.wrike.com/api/v4/dependencies/             | [x] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Timelogs                  | https://developers.wrike.com/api/v4/timelogs/                 | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Timelog categories        | https://developers.wrike.com/api/v4/timelog-categories/       | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Attachments               | https://developers.wrike.com/api/v4/attachments/              | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Version                   | https://developers.wrike.com/api/v4/version/                  | [x] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| IDs                       | https://developers.wrike.com/api/v4/ids/                      | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Colors                    | https://developers.wrike.com/api/v4/colors/                   | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Spaces                    | https://developers.wrike.com/api/v4/spaces/                   | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Data Export               | https://developers.wrike.com/api/v4/data-export/              | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Audit Log                 | https://developers.wrike.com/api/v4/audit-log/                | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Access Roles              | https://developers.wrike.com/api/v4/access-roles/             | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Async job                 | https://developers.wrike.com/api/v4/async-job/                | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Approvals                 | https://developers.wrike.com/api/v4/approvals/                | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Work Schedules            | https://developers.wrike.com/api/v4/work-schedules/           | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Copy Work Schedule        | https://developers.wrike.com/api/v4/copy-work-schedule/       | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Work Schedule exceptions  | https://developers.wrike.com/api/v4/work-schedule-exceptions/ | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| User Schedule exceptions  | https://developers.wrike.com/api/v4/user-schedule-exceptions/ | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Bookings                  | https://developers.wrike.com/api/v4/bookings/                 | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Job Roles                 | https://developers.wrike.com/api/v4/job-roles/                | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Placeholders              | https://developers.wrike.com/api/v4/placeholders/             | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Folder Blueprints         | https://developers.wrike.com/api/v4/folder-blueprints/        | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Task Blueprints           | https://developers.wrike.com/api/v4/task-blueprints/          | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| EDiscovery                | https://developers.wrike.com/api/v4/ediscovery/               | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Hourly rates provision    | https://developers.wrike.com/api/v4/hourly-rates-provision/   | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Hourly rates              | https://developers.wrike.com/api/v4/hourly-rates/             | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| Custom Item Types         | https://developers.wrike.com/api/v4/custom-item-types/        | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |
| User Types                | https://developers.wrike.com/api/v4/user-types/               | [ ] | [ ]  | [ ] | [ ]    | [ ]    | [ ]      |