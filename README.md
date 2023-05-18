# REPLIQ-Django-Coding-Assessment-
In this project i implemented the key components required to track corporate assets and i created a project name "DjangoApp" and app name "Asset" 

# Structure of this project
## Model
Firstly, i wrote code for the model.i created 5 models named "Employee", "Company", "Device", "Asset" and "DelegatedDevice".
The Company model has a many-to-many relationship with the Employee model using the employees field.
The Asset model represents the delegation of devices to employees. It has fields such as company, employee, checked_in_at, and checked_out_at to track which company delegated the device, which employee it was delegated to, and the timestamps for checking in and checking out.An asset can be associated with one or more devices.An employee can be assigned to one or more assets.

## Serializer
Secondly, i created serializers.py file to convert Django model instances to and from JSON.

## View
i wrote the business logic here for this project so that i can interact with the models what i had defined. I import generic views from the rest framework so that i can smoothly handle the CRUD operation. 

## Admin
i customized the admin to get a better data visibility, filtering and searching and to enhance the user experience.

