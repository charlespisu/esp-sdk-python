# ScheduledExport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID | [optional] 
**type** | **str** | Type of export to control frequency. Valid values are weekly, daily, monthly | [optional] 
**status** | **str** | Status of the scheduled export. Valid values are active, unsubscribed, disabled | [optional] 
**send_with_attachment** | **bool** | Whether or not to send the file as an attachment. Valid values are true, false | [optional] 
**filter** | **object** | Params used to filter the alerts that will be exported | [optional] 
**authenticated** | **bool** | Whether or not require authentication before viewing the file. Valid values are true, false | [optional] 
**hour** | **int** | Hour of the day to perform the export. Valid values are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 | [optional] 
**day** | **str** | Day of the week or day of the month to perform the export.  Allowed Values: Daily: nil - Weekly: sunday, monday, tuesday, wednesday, thursday, friday, or saturday - Monthly: 0 to 31. Valid values are sunday, monday, tuesday, wednesday, thursday, friday, saturday, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31 | [optional] 
**time_zone** | **str** | Time zone to use when calculating hour and day | [optional] 
**created_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was created | [optional] 
**updated_at** | [**datetime**](DateTime.md) | ISO 8601 timestamp when the resource was updated | [optional] 
**recipient** | **str** | Email address the export will be sent to if unauthenticated | [optional] 
**external_account** | [**ExternalAccount**](ExternalAccount.md) | Associated External Account | [optional] 
**external_account_id** | **int** | Associated External Account ID | [optional] 
**creator** | [**User**](User.md) | Associated Creator | [optional] 
**creator_id** | **int** | Associated Creator ID | [optional] 
**user** | [**User**](User.md) | Associated User | [optional] 
**user_id** | **int** | Associated User ID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


