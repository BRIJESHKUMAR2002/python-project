# try:
#     print(
#         "---------------------------------------------UNDER THE EXCEPT PART--------------------------------------------")
#     print(
#         "---------------------------------------------UNDER THE EXCEPT PART--------------------------------------------")
#     response = client.chat.completions.create(
#         model="gpt-4-0125-preview",
#         messages=[
#             {"role": "system",
#              "content": '''You are a helpful intelligent assistant,Please generate a comprehensive and detailed summary of the provided case study.
#              Your response should exceed 1500 words, and meticulously cover all aspects of the case without omitting any significant information, especially quantitative data like the financial judgment.
#              Ensure your summary includes the following details clearly structured and elaborated upon:
#
#             - Case Title: Reflect the title of the case as 'Case Title'.
#             - Year: Indicate the year of the case as 'Case Year'.
#             - Location: Mention the location where the case was held as 'Location'.
#             - Case Number: Include the specific case number as 'Case Number'.
#             - Judge Name: State the name of the judge involved as 'Judge Name'.
#             - Decision: Describe the decision that was reached in 'Decision'.
#             - Contracts: Detail any contracts discussed in the case under 'Contracts'.
#             - Legal Significance: Analyze the legal significance of the case under 'Legal Significance'.
#             - Financial Judgment: Report the financial judgment awarded in the case under 'financial judgment'.
#             - Key Takeaways: Highlight the key takeaways from the case under 'key takeaways'.

#              - Provide the information extracted from User Data in a string format.'''},
#             {"role": "user", "content": case_value}
#         ],
#         temperature=1,
#         # max_tokens=4000,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     case_data = response.choices[0].message.content
#     print(
#         "==================================================================================================")
#     print(case_data)
#     print("==================================================================================================")
#     prompt_text = f""""You are a content writing expert tasked with producing detailed reports based on the case data provided below.
#             Please adhere strictly to the instructions and use the user data as a reference to generate a comprehensive report.
#
#             Create a report for {case_name}:
#             Title of the report should be the name of the CASE.
#
#
#             **Instructions**:
#             - User Prompt: Follow the User Prompt guidelines closely to generate your response.
#             - User Data: Utilize the data provided below as a reference for your response.
#
#             ##User Prompt:
#             {user_prompt}
#
#             ##User Data:
#             {case_data}
#
#             Requirements:
#             - Do not omit any quantitative data, such as financial judgments.
#             - Provide the information extracted from User Data in a dictionary format with the specified keys and values.
#
#             **Expected Output Format**:
#             Case_data = {{
#                 "Case": 'Case Title',
#                 "year": 'Case Year',
#                 "location": 'Location if available, otherwise "Not given"',
#                 "Case No": 'Case Number if available, otherwise "Not given"',
#                 "Judge Name": 'Judge Name if available, otherwise "Not given"',
#                 "summary": 'Create a summary for the case.',
#                 "Decision": 'Decision if available, otherwise "Not given"',
#                 "Contracts": 'Information on contracts involved, otherwise "Not given"',
#                 "Legal Significance": 'Legal significance of the case, otherwise "Not given"',
#                 "Financial Judgment": 'Financial judgment amount, otherwise "Not given"',
#                 "key takeaways": 'Key takeaways from the case, otherwise "Not given"',
#             }}
#
#             ##If something is missing, replace the value with 'Not given'.
#             ##Remember, do not add extra spaces between words or lines."""
#
#     response = gpt_4_response(prompt_text)
# except:
#     prompt_text = f""""You are a content writing expert tasked with producing detailed reports based on the case data provided below.
#     Please adhere strictly to the instructions and use the user data as a reference to generate a comprehensive report.
#
#     Create a report for {case_name}:
#     Title of the report should be the name of the CASE.
#
#
#     **Instructions**:
#     - User Prompt: Follow the User Prompt guidelines closely to generate your response.
#     - User Data: Utilize the data provided below as a reference for your response.
#
#     ##User Prompt:
#     {user_prompt}
#
#     ##User Data:
#     {case_data}
#
#     Requirements:
#     - Do not omit any quantitative data, such as financial judgments.
#     - Provide the information extracted from User Data in a dictionary format with the specified keys and values.
#
#     **Expected Output Format**:
#     Case_data = {{
#         "Case": 'Case Title',
#         "year": 'Case Year',
#         "location": 'Location if available, otherwise "Not given"',
#         "Case No": 'Case Number if available, otherwise "Not given"',
#         "Judge Name": 'Judge Name if available, otherwise "Not given"',
#         "summary": 'Create a summary for the case.',
#         "Decision": 'Decision if available, otherwise "Not given"',
#         "Contracts": 'Information on contracts involved, otherwise "Not given"',
#         "Legal Significance": 'Legal significance of the case, otherwise "Not given"',
#         "Financial Judgment": 'Financial judgment amount, otherwise "Not given"',
#         "key takeaways": 'Key takeaways from the case, otherwise "Not given"',
#     }}
#
#     ##If something is missing, replace the value with 'Not given'.
#     ##Remember, do not add extra spaces between words or lines."""
#
#     response = gpt_4_response(prompt_text)
import re

response = '<a href="https://scholar.google.com/scholar_case?case=1234567890">16-474-RGA</a>'

# Regular expression pattern to extract URL and case number text
pattern = r'<a\s+href=["\'](.*?)["\']>(.*?)<\/a>'

# Match the pattern in the response
match = re.search(pattern, response)

if match:
    # Extract URL and case number text from the matched groups
    url = match.group(1)
    case_no_text = match.group(2)

    print("URL:", url)
    print("Case Number Text:", case_no_text)
else:
    print("No match found.")
