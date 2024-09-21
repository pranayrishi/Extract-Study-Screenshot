import openai

# Set up the OpenAI API key
openai.api_key = "OPENAI_API_KEY"  # Replace with your actual API key

# Function to get a tailored assignment from GPT
def get_assignment(learning_style, chapter_summary):
    # Define the learning style-specific prompts
    prompts = {
        'audio': f"Create an assignment based on this chapter for an auditory learner: {chapter_summary}. Focus on listening activities and instructions.",
        'kinesthetic': f"Create an assignment based on this chapter for a kinesthetic learner: {chapter_summary}. Focus on hands-on tasks and physical interaction.",
        'visual': f"Create an assignment based on this chapter for a visual learner: {chapter_summary}. Focus on diagrams, images, and visual elements."
    }

    # Get the tailored assignment from GPT based on the learning style
    prompt = prompts.get(learning_style, "Create a general assignment based on this chapter.")
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Updated to use model
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    
    return response['choices'][0]['message']['content'].strip()  # Access the content properly

# Student input
def student_interface():
    print("Welcome to the AI Learning Assignment Program")
    
    # Ask for student name
    student_name = input("Enter your name: ")
    
    # Ask for learning preference
    print("Choose your preferred learning style:")
    print("1. Audio")
    print("2. Kinesthetic")
    print("3. Visual")
    
    choice = input("Enter 1, 2, or 3: ")
    
    learning_style = ""
    if choice == "1":
        learning_style = "audio"
    elif choice == "2":
        learning_style = "kinesthetic"
    elif choice == "3":
        learning_style = "visual"
    else:
        print("Invalid choice, defaulting to general assignment.")
        learning_style = "general"  # Default to general if invalid choice
    
    # Read chapter summary from the extracted text file
    try:
        with open('extracted_text.txt', 'r') as file:
            chapter_summary = file.read()
    except FileNotFoundError:
        print("Error: 'extracted_text.txt' file not found. Please run the text extractor first.")
        return

    # Get tailored assignment from GPT
    assignment = get_assignment(learning_style, chapter_summary)

    # Output assignment
    print(f"\nHi {student_name}, based on your {learning_style} learning style, here is your tailored assignment:")
    print(assignment)

# Run the student interface
if __name__ == '__main__':
    student_interface()
