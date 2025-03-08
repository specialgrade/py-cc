# Implementation of print() and input() function
# Dela Cruz, Alyssa Marie D.

# Employment Application Form

# Print the heading and sub-heading
print('===== EMPLOYMENT APPLICATION FORM =====')
print('\nApplicant\'s Personal Information >>>')

# Take inputs from the user
name = str(input('Enter your full name: '))
gen = str(input('Enter your gender (Male/Female/Other): '))
age = int(input('Enter your age: '))
contact = str(input('Enter your contact number: '))
email = str(input('Enter your email: '))
pos = str(input('Enter the position you\'re applying for: '))

# Print application status confirmation
print('\n*Application Successfully Submitted!')

# Display the application summary
print('\n===== APPLICATION SUMMARY =====\n')
print('Name:', name, '\nGender:', gen, '\nAge: ', age,
      '\nContact Number: ', contact, '\nEmail: ', email,
      '\nPosition Applied For: ', pos, '\n\n===============================')
