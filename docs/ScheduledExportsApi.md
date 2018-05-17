# esp_sdk.ScheduledExportsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_export**](ScheduledExportsApi.md#activate_export) | **PATCH** /api/v2/scheduled_exports/{scheduled_export_id}/activate.json_api | Update a(n) Scheduled Export
[**create**](ScheduledExportsApi.md#create) | **POST** /api/v2/scheduled_exports.json_api | Create a(n) Scheduled Export
[**delete**](ScheduledExportsApi.md#delete) | **DELETE** /api/v2/scheduled_exports/{id}.json_api | Delete a(n) Scheduled Export
[**disable_export**](ScheduledExportsApi.md#disable_export) | **PATCH** /api/v2/scheduled_exports/{scheduled_export_id}/disable.json_api | Update a(n) Scheduled Export
[**show**](ScheduledExportsApi.md#show) | **GET** /api/v2/scheduled_exports/{id}.json_api | Show a single Scheduled Export
[**show_file_details**](ScheduledExportsApi.md#show_file_details) | **GET** /api/v2/reports/scheduled_export/files/{uuid}.json_api | Show a single Scheduled Export Result
[**unsubscribe_export**](ScheduledExportsApi.md#unsubscribe_export) | **PATCH** /api/v2/scheduled_exports/{uuid}/unsubscribe.json_api | Update a(n) Scheduled Export
[**update**](ScheduledExportsApi.md#update) | **PATCH** /api/v2/scheduled_exports/{id}.json_api | Update a(n) Scheduled Export


# **activate_export**
> ScheduledExport activate_export(scheduled_export_id, include=include)

Update a(n) Scheduled Export



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScheduledExportsApi()
scheduled_export_id = 56 # int | The id of the scheduled export to be activated
include = 'include_example' # str | Related objects that can be included in the response:  external_account, creator, user See Including Objects for more information. (optional)

try: 
    # Update a(n) Scheduled Export
    api_response = api_instance.activate_export(scheduled_export_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledExportsApi->activate_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_export_id** | **int**| The id of the scheduled export to be activated | 
 **include** | **str**| Related objects that can be included in the response:  external_account, creator, user See Including Objects for more information. | [optional] 

### Return type

[**ScheduledExport**](ScheduledExport.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> ScheduledExport create(authenticated, external_account_id, hour, time_zone, type, include=include, day=day, filter=filter, recipient=recipient, send_with_attachment=send_with_attachment, user_id=user_id)

Create a(n) Scheduled Export



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScheduledExportsApi()
authenticated = true # bool | Whether or not require authentication before viewing the file. Valid values are true, false
external_account_id = 56 # int | The id of the external account the report will be exported for
hour = 56 # int | Hour of the day to perform the export. Valid values are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23
time_zone = 'time_zone_example' # str | Time zone to use when calculating hour and day
type = 'type_example' # str | Type of export to control frequency. Valid values are weekly, daily, monthly
include = 'include_example' # str | Related objects that can be included in the response:  external_account, creator, user See Including Objects for more information. (optional)
day = 'day_example' # str | Day of the week or day of the month to perform the export.  Allowed Values: Daily: nil - Weekly: sunday, monday, tuesday, wednesday, thursday, friday, or saturday - Monthly: 0 to 31. Valid values are sunday, monday, tuesday, wednesday, thursday, friday, saturday, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31 (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Params used to filter the alerts that will be exported (optional)
recipient = 'recipient_example' # str | Email address the export will be sent to if unauthenticated (optional)
send_with_attachment = true # bool | Whether or not to send the file as an attachment. Valid values are true, false (optional)
user_id = 56 # int | The id of the user the report will be emailed to when authenticated is selected (optional)

try: 
    # Create a(n) Scheduled Export
    api_response = api_instance.create(authenticated, external_account_id, hour, time_zone, type, include=include, day=day, filter=filter, recipient=recipient, send_with_attachment=send_with_attachment, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledExportsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticated** | **bool**| Whether or not require authentication before viewing the file. Valid values are true, false | 
 **external_account_id** | **int**| The id of the external account the report will be exported for | 
 **hour** | **int**| Hour of the day to perform the export. Valid values are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 | 
 **time_zone** | **str**| Time zone to use when calculating hour and day | 
 **type** | **str**| Type of export to control frequency. Valid values are weekly, daily, monthly | 
 **include** | **str**| Related objects that can be included in the response:  external_account, creator, user See Including Objects for more information. | [optional] 
 **day** | **str**| Day of the week or day of the month to perform the export.  Allowed Values: Daily: nil - Weekly: sunday, monday, tuesday, wednesday, thursday, friday, or saturday - Monthly: 0 to 31. Valid values are sunday, monday, tuesday, wednesday, thursday, friday, saturday, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31 | [optional] 
 **filter** | [**dict(str, str)**](str.md)| Params used to filter the alerts that will be exported | [optional] 
 **recipient** | **str**| Email address the export will be sent to if unauthenticated | [optional] 
 **send_with_attachment** | **bool**| Whether or not to send the file as an attachment. Valid values are true, false | [optional] 
 **user_id** | **int**| The id of the user the report will be emailed to when authenticated is selected | [optional] 

### Return type

[**ScheduledExport**](ScheduledExport.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> Meta delete(id)

Delete a(n) Scheduled Export



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScheduledExportsApi()
id = 56 # int | Scheduled Export ID

try: 
    # Delete a(n) Scheduled Export
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledExportsApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Scheduled Export ID | 

### Return type

[**Meta**](Meta.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_export**
> ScheduledExport disable_export(scheduled_export_id, include=include)

Update a(n) Scheduled Export



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScheduledExportsApi()
scheduled_export_id = 56 # int | The id of the scheduled export to be disabled
include = 'include_example' # str | Related objects that can be included in the response:  external_account, creator, user See Including Objects for more information. (optional)

try: 
    # Update a(n) Scheduled Export
    api_response = api_instance.disable_export(scheduled_export_id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledExportsApi->disable_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_export_id** | **int**| The id of the scheduled export to be disabled | 
 **include** | **str**| Related objects that can be included in the response:  external_account, creator, user See Including Objects for more information. | [optional] 

### Return type

[**ScheduledExport**](ScheduledExport.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> ScheduledExport show(id, include=include)

Show a single Scheduled Export



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScheduledExportsApi()
id = 56 # int | Scheduled Export ID
include = 'include_example' # str | Related objects that can be included in the response:  external_account, creator, user See Including Objects for more information. (optional)

try: 
    # Show a single Scheduled Export
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledExportsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Scheduled Export ID | 
 **include** | **str**| Related objects that can be included in the response:  external_account, creator, user See Including Objects for more information. | [optional] 

### Return type

[**ScheduledExport**](ScheduledExport.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_file_details**
> ScheduledExportResult show_file_details(uuid, include=include)

Show a single Scheduled Export Result

The URL provided is temporary and will expire shortly after the request. To download the exported file you will need to follow the URL provided.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScheduledExportsApi()
uuid = 'uuid_example' # str | The uuid to access the result
include = 'include_example' # str | Related objects that can be included in the response:  scheduled_export See Including Objects for more information. (optional)

try: 
    # Show a single Scheduled Export Result
    api_response = api_instance.show_file_details(uuid, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledExportsApi->show_file_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid to access the result | 
 **include** | **str**| Related objects that can be included in the response:  scheduled_export See Including Objects for more information. | [optional] 

### Return type

[**ScheduledExportResult**](ScheduledExportResult.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_export**
> ScheduledExport unsubscribe_export(uuid, include=include)

Update a(n) Scheduled Export



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScheduledExportsApi()
uuid = 'uuid_example' # str | The uuid of the export to unsubscribe
include = 'include_example' # str | Related objects that can be included in the response:  external_account, creator, user See Including Objects for more information. (optional)

try: 
    # Update a(n) Scheduled Export
    api_response = api_instance.unsubscribe_export(uuid, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledExportsApi->unsubscribe_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid of the export to unsubscribe | 
 **include** | **str**| Related objects that can be included in the response:  external_account, creator, user See Including Objects for more information. | [optional] 

### Return type

[**ScheduledExport**](ScheduledExport.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ScheduledExport update(id, include=include, day=day, filter=filter, hour=hour, send_with_attachment=send_with_attachment, time_zone=time_zone)

Update a(n) Scheduled Export



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScheduledExportsApi()
id = 56 # int | Scheduled Export ID
include = 'include_example' # str | Related objects that can be included in the response:  external_account, creator, user See Including Objects for more information. (optional)
day = 'day_example' # str | Day of the week or day of the month to perform the export.  Allowed Values: Daily: nil - Weekly: sunday, monday, tuesday, wednesday, thursday, friday, or saturday - Monthly: 0 to 31. Valid values are sunday, monday, tuesday, wednesday, thursday, friday, saturday, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31 (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Params used to filter the alerts that will be exported (optional)
hour = 56 # int | Hour of the day to perform the export. Valid values are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 (optional)
send_with_attachment = true # bool | Whether or not to send the file as an attachment. Valid values are true, false (optional)
time_zone = 'time_zone_example' # str | Time zone to use when calculating hour and day (optional)

try: 
    # Update a(n) Scheduled Export
    api_response = api_instance.update(id, include=include, day=day, filter=filter, hour=hour, send_with_attachment=send_with_attachment, time_zone=time_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledExportsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Scheduled Export ID | 
 **include** | **str**| Related objects that can be included in the response:  external_account, creator, user See Including Objects for more information. | [optional] 
 **day** | **str**| Day of the week or day of the month to perform the export.  Allowed Values: Daily: nil - Weekly: sunday, monday, tuesday, wednesday, thursday, friday, or saturday - Monthly: 0 to 31. Valid values are sunday, monday, tuesday, wednesday, thursday, friday, saturday, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31 | [optional] 
 **filter** | [**dict(str, str)**](str.md)| Params used to filter the alerts that will be exported | [optional] 
 **hour** | **int**| Hour of the day to perform the export. Valid values are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 | [optional] 
 **send_with_attachment** | **bool**| Whether or not to send the file as an attachment. Valid values are true, false | [optional] 
 **time_zone** | **str**| Time zone to use when calculating hour and day | [optional] 

### Return type

[**ScheduledExport**](ScheduledExport.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

