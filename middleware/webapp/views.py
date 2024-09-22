from django.http import HttpResponse
import json
import requests


def index(request):
    return HttpResponse("Hello, world!")


def recieve_event(request):
    if request.method != "POST":
        return HttpResponse("Hello, world2!")

    data = json.loads(request.body)
    event_type = data.get("event_type")
    if event_type != "appointment":
        return HttpResponse("Hello, world2!")
    
    appointment_id = data.get("data", {}).get("appointment_id")
    if appointment_id is None:
        return HttpResponse("Hello, world2!")
    
    url = "https://api.eka.care/dr/v1/business/appointments/{}".format(appointment_id)
    response = requests.get(url)
    if response.status_code != 200:
        return HttpResponse("Hello, world2!")
    
    appointment_data = response.json()
    url2 = "https://apirni.metropolisindia.com/rest/prshvtexternalapi/v1/HVT"
    data = {
  "patientDetails": {
    "firstName": "BAVITHRA",
    "middleName": "",
    "lastName": "ST",
    "dob": "1992-11-26T00:00:00Z",
    "salutationName": "Ms.",
    "genderName": "Female",
    "age": "31.8",
    "contactNumber": "8754586316",
    "emailId": "bavi2611@gmai.com",
    "externalOrderID": "3168278",
    "pid": "",
    "patientaddress": {
      "addressLine1": "9333 TS GOPAL NAGA TIRUVOTTIYUR",
      "pinCode": "600019"
    },
    "visitdetails": {
      "externalVid": appointment_data["data"]["aid"],
      "visitDate": appointment_data["data"]["visit_start"],
      "samplePickUpDateTime": "2024-08-13T05:26:00.001Z",
      "orgId": 361,
      "orgName": "Hitech-GKS TOWERS",
      "registeredVia": "HVT",
      "locationId": 4102,
      "locationIdName": "TIRUVOTTIYUR PSC",
      "clientCode": "CUS26358",
      "patientType": "Homevisit",
      "doctorID": "0035j000019najjAAA",
      "phleboID": 100612,
      "documentDetails": {
        "document": [
          {
            "documentType": "TRF",
            "documentLink": "https://www.mhlhvt.in/HVT_Images/hvtToRni/1974_202408133168278.PDF",
            "documentExtension": "pdf"
          }
        ]
      },
      "testDetails": {
        "test": [
          {
            "baseMRP": 75,
            "netAmount": 75,
            "discountAmount": 0,
            "discountCode": "doctor referral 10",
            "testCode": "HV75",
            "testType": "GBI"
          },
          {
            "baseMRP": 1150,
            "netAmount": 1035,
            "discountAmount": 115,
            "discountCode": "doctor referral 10",
            "testCode": "V0010",
            "testType": "INV"
          },
          {
            "baseMRP": 320,
            "netAmount": 288,
            "discountAmount": 32,
            "discountCode": "doctor referral 10",
            "testCode": "P0032",
            "testType": "GRP"
          },
          {
            "baseMRP": 2200,
            "netAmount": 1980,
            "discountAmount": 220,
            "discountCode": "doctor referral 10",
            "testCode": "R0007",
            "testType": "GRP"
          },
          {
            "baseMRP": 750,
            "netAmount": 675,
            "discountAmount": 75,
            "discountCode": "doctor referral 10",
            "testCode": "F0018",
            "testType": "INV"
          },
          {
            "baseMRP": 400,
            "netAmount": 360,
            "discountAmount": 40,
            "discountCode": "doctor referral 10",
            "testCode": "I0282",
            "testType": "INV"
          },
          {
            "baseMRP": 550,
            "netAmount": 495,
            "discountAmount": 55,
            "discountCode": "doctor referral 10",
            "testCode": "T0070",
            "testType": "INV"
          },
          {
            "baseMRP": 400,
            "netAmount": 360,
            "discountAmount": 40,
            "discountCode": "doctor referral 10",
            "testCode": "L0012",
            "testType": "INV"
          },
          {
            "baseMRP": 300,
            "netAmount": 270,
            "discountAmount": 30,
            "discountCode": "doctor referral 10",
            "testCode": "R0016",
            "testType": "GRP"
          }
        ]
      },
      "paymentDetails": {
        "grossAmount": 6145,
        "totalDiscountAmount": 607,
        "netAmount": 5538,
        "amountReceived": 5538,
        "billNumber": "",
        "billDate": "",
        "bankAccountNumber": "",
        "transactionDetails": [
          {
            "paymentDate": "2024-08-13T07:31:00.001Z",
            "amount": 5538,
            "transactionID": "240813073052734E010087530",
            "paymentGatewayName": "Ezetap",
            "ezetapReferenceNumber": "8754586316",
            "paymentTypeName": "UPI",
            "cardNo": "",
            "chequeNo": "",
            "chequeDate": "",
            "chequeBank": "",
            "MICRCode": "",
            "cardHolderName": "",
            "authCode": "",
            "userName": "",
            "userMobile": "",
            "messageCode": "",
            "message": ""
          }
        ]
      },
      "CreatedBy": "2403131744051"
    }
  },
  "totalrecords": 0,
  "offset": 0,
  "limit": 0,
  "action": "C"
}
    requests.post(url2)
    return HttpResponse("Hello, world2!")