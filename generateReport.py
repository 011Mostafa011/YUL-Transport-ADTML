import requests
import pandas as pd
from io import StringIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

# URL of the CSV file
print('working...')
url = 'https://yul-transport.admtl.com/admapi/report'
headers= {
"Accept":"application/json, text/plain, */*",
"Accept-Encoding":"gzip, deflate, br, zstd",
"Accept-Language":"en-US,en;q=0.9",
"Authorization":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI1MTU3ODYiLCJhdWRpZW5jZSI6InVua25vd24iLCJjcmVhdGVkIjoxNzIwMjExNTMyNDMxLCJzZXNzaW9uSWQiOiJjZGU0ZWEyZi1iYTIyLTQzZjUtOTZkYy03MzFiMTFkMThkZGEiLCJzb3VyY2UiOiJXRUIiLCJleHAiOjE3MjAyMTUxMzJ9.SmtoMOuLLxGy_B-nzdVzdNyF_6krluzuO7Blwtn9-ibEXhX8nUlAnZN1V6xbJnBasT9PU0ELOEfqKrNucnCzmQ",
"Connection":"keep-alive",
"Content-Length":"1766",
"Content-Type":"application/json",
"Cookie":"ai_user=WpXwEsrqaezVK1X0/8LJ2B|2024-07-04T22:13:11.028Z; __Host-next-auth.csrf-token=047d0aae368640cb1b0dec81742fd234a42139c942a3d03da31c0e5de87dd555%7C32bc00a3b52a4ea3e162634e44c9f746d12326db9502559e4acc3035b11f9506; ai_session=D/SZ5zQhHwIPkyBS5JrxMz|1720211508815|1720211524055; __Secure-next-auth.callback-url=https%3A%2F%2Fyul-transport.admtl.com%2Fuser%2Flogin%3FcallbackUrl%3Dhttps%253A%252F%252Fyul-transport.admtl.com%252Fen%252Fprovider%252F1115%26error%3DSessionRequired; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..J5JJkAm-f3Z4jVr3.98Hk5g5s6EaO8agR1J9JRtgWJrmrv-CpePX4CDloPCZlgbaOrejksJ4v9Yv9YjbaVIs9TNjrmSgfc_4J5Zw0fzmFcCavira3V_qBjpleGGgNN071fE7pcKwP_T8SFVFrT3JJGSibMlp9pCBXmoZA6H6Dk-OGYO0DeoXB1-PIZoQuR7K7_EhfqjpxViDrwE9deN8Ha6Ew7JMqOjUNf_7imCWv9EqENebIPCYD6M2Rs8aGRdI-po3K8GITAD4Yfwq7w0LeP-WoZoHn82Ne_uxe230JxxkpW-6EdEFVh6lqD6NBmywLB4s8-qv8yGMAmEunEyJWwgjctJ4qSiEnMaoAexpFNR0oEKdCu-639nzK4vOsyvRypGV56Ayclr5jo34xL5493enhZ6A7pj4ZsAM-7SN2lbyhVuQ5ZQIMKjOnNrC19W9XObOobn6N2OEgV6FmDrkjLupGoxe2yHp5c6GOe08TY_JY1bI5FD4GCY4QPiEEHVlWgy6h19b8-JUaeSBaD3sT48CkgMkmrYQzokOqDs0-DOuRc71Xi7dSNTZDIMUDRXiEkfAtxrIF5ixpJZczeeyN2zy644I6RAlWBkHZZzYLrJxtXjeyRd0mu9mvT69OPx_fLeVsgapCb0fVQJk03u46H7iLePHe6WfclvjVrpH8HkKzuSEt1vEEXH023tWgaH7YM-Hx08ECoePmT8A0ZuD2qy4jHS8785Nj_CUcakywUXpHGUYoyo7K9sbbKrICPdE.JX6jazqw11NRfNO0MEmWDQ",
"Host":"yul-transport.admtl.com",
"Origin":"https://yul-transport.admtl.com",
"Referer":"https://yul-transport.admtl.com/en/provider/1115",
"Request-Id":"|a9a1a71d63814f7783957cd122250a5d.802101db2ad24abf",
"Sec-Fetch-Dest":"empty",
"Sec-Fetch-Mode":"cors",
"Sec-Fetch-Site":"same-origin",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
"sec-ch-ua":'"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
"sec-ch-ua-mobile":'?0',
"sec-ch-ua-platform":"Windows",
"traceparent":"00-a9a1a71d63814f7783957cd122250a5d-802101db2ad24abf-01",

}

payload = {"provider":{"providerId":1115,"version":0,"legalName":"Abdul Nasser El-Boustani","dome":"6249","numeroADM":6249,"status":"ACTIVE","vehicleCategory":"TAXI","attestationSAAQ":"AA86E5","person":{"id":3068,"version":0,"firstName":"Abdul","lastName":"El-Boustani","middleName":"Nasser","language":"ENGLISH","fullName":"Abdul Nasser El-Boustani","driverInformation":'null',"address":'null',"phones":'null'},"address":{"city":"Montreal","line01":"474 boul. Decarie","line02":'null',"zipCode":"H4L 3K9"},"phones":{"phone":"514-980-3232","cell":"514-980-3232"},"owner":{"userId":1371,"version":2603,"username":"abdulnasserboustani@gmail.com","person":{"id":1995,"version":3,"firstName":"Abdulnasser","lastName":"El-Boustani","middleName":'null',"language":"ENGLISH","fullName":"Abdulnasser El-Boustani","driverInformation":{"workPermit":"515786","providers":[{"providerId":1115,"version":0,"legalName":"Abdul Nasser El-Boustani","dome":"6249","numeroADM":6249,"status":"ACTIVE","vehicleCategory":"TAXI"}],"provider":'null',"currentProvider":False},"address":{"addressId":2010,"version":2,"city":"Montreal","line01":"103-3505 Boul Edouard-Montpetit","line02":'null',"zipCode":"H3T 1K6"},"phones":{"phone":"438-929-6019","cell":"438-929-6019"}},"temporaryUsername":'null',"newPassword":'null',"confirmPassword":'null',"status":"ACTIVE","authorities":["ROLE_ADMIN_PROVIDER","ROLE_DRIVER"],"lastLoginTime":"2024-07-04T14:13:23","action":{"edit":True,"delete":False,"changePassword":True,"resetPassword":False,"changeUsername":True,"changeProviders":False},"providers":[{"providerId":1115,"version":0,"legalName":"Abdul Nasser El-Boustani","dome":"6249","numeroADM":6249,"status":"ACTIVE","vehicleCategory":"TAXI"}]}},"fromDate":"2022-01-02","toDate":"2023-01-02","reportType":"TRANSPORT_TRANSACTION"}

cookies={
    '__Host-next-auth.csrf-token':'047d0aae368640cb1b0dec81742fd234a42139c942a3d03da31c0e5de87dd555',
    '__Secure-next-auth.callback-url':'https%3A%2F%2Fyul-transport.admtl.com%2Fuser%2Flogin%3FcallbackUrl%3Dhttps%253A%252F%252Fyul-transport.admtl.com%252Fen%252Fprovider%252F1115%26error%3DSessionRequired',
    '__Secure-next-auth.session-token': 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..uNthSaOYAKShMQ8_.5VmtjaQImI-VEjhgPii-Uw6zg8CpOZg7IhTW2gJEzZYYSqD9OyoBiWnkc1vt_d-GI-B961hbkpuRV90EiHhpSl34dWEM0ByAErRFUAUMYvRnZPV11n_HSQAdJYj91Be4nqjILeiiycZ3YFVAaV1FO52A_0ZVVO-1rhr_merxtiegq-3VeJgnA0vqFS__fY0Ro2A2lGiVhkMR1dNNE33LUFiz0wMBgwZuxy4k6GH-jDoG5KSO9DQSxvtVO9xRPPspD1wQ9XSJcvMItsSwQ1jKJcZuMrvCO7c5VWDCoSf6PF23MdviboZLi6bASLmoik6JFK7myRa63kkB_iO9JSvJ1qAMCpu0wNw1MKB8UOWfMewsJDqSqq03Ow8182_cq49QyHFomnp1FdRzoqa6GrXgyknWTn-vmVZCW28WjSZ7sXva8KsaQQTSJGEGOCAIONtnlCBnB5SgH0MvzUWCVMaRw7lJ4q_irFOZbPL0f40I9HVumSfFiGJAiqp5zJvY0mtsAfH-BLS30Mh9LBhPAqwMRLLJYvM_un9bTDPyboKUk94y1kCG4Yc-fglHl0fzuJF0SwvA87RYbVn-eIMhfPIGNfmH4Nt95ooChTgRFfDAEdHATSt7sv2nnRHfMcLvRO0Ixlptk35bMlpl8OapKVg63Y4txahaHsBefHdvcD4lWhg3mRK-mww2TjZDW6kO5SL6pNQMe1HsmlySL9V4JBGTSsXbPdG6xPZGsLlVh_aLNeuTLk8.luHiGk7weYxlH6m-jhsVyQ',
    'ai_session': '9kxU25QUD3cAk9zMtoiBe7|1720138171708|1720138522107',
    'ai_user':'WpXwEsrqaezVK1X0/8LJ2B|2024-07-04T22:13:11.028Z'	
}
print('sending request')
# Fetch the CSV file from the server then calculate Total of stub payload
def getTotal():
    response = requests.post(url,json=payload,headers=headers)
    print('request sent')

    # Check if the request was successful
    if response.status_code == 200:
        # Read the CSV content
        print('Accecpted')
        print(response)
        csv_content = response.content.decode('utf-8')

        # Use StringIO to load the CSV content into a pandas DataFrame
        data = pd.read_csv(StringIO(csv_content))

        # Check if the DataFrame has at least 6 rows
        if len(data) >= 6:
            # Get the 6th row (index 5 since Python is 0-indexed)
            
            data['Amount'] = data['Amount'].str.replace(',', '.').astype(float)

            # Calculate the sum of the numbers in the 6th row
            total = data['Amount'].sum()
            total = total * -1
            
            # Calculate the sum of the numbers in the 6th row

            print(f"The sum of the numbers in the 6th row is: {total}")
            return total
        else:
            print("The CSV file does not have at least 6 rows.")
            return ValueError
    else:
        print(f"Failed to fetch the CSV file. Status code: {response.status_code}")


def generateReport():
    print(payload["fromDate"])
    print(payload["toDate"])
    print(payload["provider"]["legalName"])
    # Sample data and calculations
    start_date = payload["fromDate"]
    end_date = payload["toDate"]
    authorized_driver = payload["provider"]["legalName"] 
    total_amount = getTotal() # Example total amount from your calculations
    company_logo_path = "YUL-Transport-ADTML\logo-yul.webp"  # Path to the company logo

    print(total_amount)
    # Create a PDF document
    pdf_file_path = "./output.pdf"
    c = canvas.Canvas(pdf_file_path, pagesize=letter)
    width, height = letter

    # Add company logo
    c.drawImage(company_logo_path, width - 150, height - 100, width=100, height=100)

    # Add document title and header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(30, height - 50, "YUL-Transport-ADTML")
    c.setFont("Helvetica", 12)
    c.drawString(30, height - 70, f"Expense Report for Authorized Driver: {authorized_driver}")
    c.drawString(30, height - 90, f"Period: {start_date} to {end_date}")

    # Add the calculated total amount
    c.setFont("Helvetica-Bold", 14)
    c.drawString(30, height - 130, "Total Amount Calculation")
    c.setFont("Helvetica", 12)
    c.drawString(30, height - 150, f"Total amount paid between the dates {start_date} and {end_date} for authorized driver")
    c.drawString(30,height -170 ,f"{authorized_driver} is {total_amount:.2f}")

    # Save the PDF
    c.save()

    print(f"PDF document created: {pdf_file_path}")

generateReport()