import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('serverlessSiddhesh_addStudent_practise')

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        #"input": event
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response

def RxInput(event,context):
    print(event)
    fname = input("Please enter your name ")
    lname = input("Please enter your last name ")
    mnumber = input("Please Enter your Mobile number ")

    student_data = {
        'student_Name': fname,
        'last_Name': lname,
        'Mobile': mnumber
    }
    table.Put_item(Item=student_data)

    return ("Success")

