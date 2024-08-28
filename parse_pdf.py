import pdfplumber
import re



# Function to parse questions and answers
def parse_questions_answers(pdf_path):
    questions_dict = {}
    
    # Define regex patterns for questions and answers
    question_pattern = re.compile(r'^\d+\s+(.*?)(?=(?:\n[A-E]\s|\n\d+\s))', re.DOTALL | re.MULTILINE)
    answer_pattern = re.compile(r'([A-E])\.\s*(.*?)\n')
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            
            # Find all questions in the page text
            questions = question_pattern.findall(text)
            
            for question in questions:
                # Extract question text
                question_text = question[0].strip()
                
                # Extract all answers for this question
                answers = answer_pattern.findall(question[0])
                answers_dict = {letter: answer.strip() for letter, answer in answers}
                
                # Add to dictionary
                questions_dict[question_text] = answers_dict
                
    return questions_dict

# Path to the PDF file
pdf_path = 'IMAT-2012-past-paper.pdf'

# Parse the questions and answers
parsed_questions = parse_questions_answers(pdf_path)

# Print the parsed questions and answers to verify
for question, answers in parsed_questions.items():
    print(f"Question: {question}")
    for letter, answer in answers.items():
        print(f"  {letter}: {answer}")
    print("\n" + "-"*50 + "\n")