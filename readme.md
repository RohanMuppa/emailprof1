# Research Opportunity Auto Email

This Python script allows you to send research opportunity inquiry emails to professors. The script supports sending emails with HTML content and attaching PDF files. It uses the SMTP protocol. It reads professor details from a CSV file and sends personalized emails to each professor.


## Prerequisites

- Python 3.6 or above
- pip package manager

## Installation

1. Clone the repository:
`git clone 

2. Install the required modules by running the following command: `pip install -r requirements.txt`

3. Update the CSV file `prof.csv` with the professor information you want to send emails to. Each row should contain the following fields:
- Email
- Last Name
- Area
- Interests
- School
- Department

**Use the folllowing format:**

 `email,lastName,area,interests,school,department`
 `prof1@example.com,LastName1,Area1,Interests1,School1,Department1`
 `prof2@example.com,LastName2,Area2,Interests2,School2,Department2`


## Usage

1. Modify the scripts as needed. You can customize the HTML template and adjust any other settings based on your requirements.
2. Run the script using the following command: `python main.py`

The script will read the CSV file, send emails to the specified professors, and attach PDF files if provided.

## Customization

- HTML Template: Modify the HTML template file in the `templates` folder to match your desired email format. Update the placeholders like `[lastName]`, `[area]`, `[department]`, and `[school]` to the corresponding professor information.
- SMTP Server: Update the SMTP server and port in the `send_emailSSL` and `send_emailTLS` functions according to your email provider's configuration.
- Email Content: Adjust the email subject and body in the `send_emailSSL` and `send_emailTLS` functions as per your requirements.
- PDF Attachment: To attach a PDF file to the emails, provide the file path to the `pdf_file_path` parameter in the `send_emailSSL` and `send_emailTLS` functions.

## Considerations

- This script assumes that the email addresses, last names, areas, interests, schools, and departments are present in the specified columns of the CSV file in the given order.
- The CSV file should be properly formatted without any missing or extra columns.
- Make sure to comply with the email sending policies and guidelines of your email provider.

## License

This project is licensed under the [MIT License](LICENSE).


