import openai

# Set up the OpenAI API key
openai.api_key = "OPENAI_API_KEY"  # Replace with your actual API key


# Function to get a tailored assignment from GPT
def get_assignment(learning_style, chapter_summary):
    # Define the learning style-specific prompts
    prompts = {
        'audio': f"Generate an engaging assignment for students who prefer audio learning that aligns with the {chapter_summary} and their course objectives. The assignment should be feasible for teachers to assign and manageable for students, enhancing their learning experience. Provide a concise description of the assignment in 1-2 sentences, ensuring it encourages active participation and utilizes auditory elements, such as creating a podcast or participating in a group discussion, to help students succeed in their coursework.",
        'kinesthetic': f"Generate an engaging assignment for students who prefer kinesthetic learning that aligns with the {chapter_summary} their course objectives. The assignment should be feasible for teachers to assign and manageable for students, enhancing their learning experience through hands-on activities. Provide a concise description of the assignment in 1-2 sentences, ensuring it encourages physical interaction with the material, such as building a model or conducting a science experiment, to help students succeed in their coursework.",
        'visual': f"Create an engaging assignment for students who prefer visual learning that aligns with the {chapter_summary} their course objectives. The assignment should be easy for teachers to assign and not overwhelming for students, enhancing their understanding through visual elements. Provide a brief description of the assignment in 1-2 sentences, ensuring it encourages the use of diagrams, infographics, or visual presentations to effectively convey key concepts and support student success in their coursework.",
        'reading/writing': f"Develop an engaging assignment for students who prefer reading and writing that aligns with the {chapter_summary} their course objectives. The assignment should be straightforward for teachers to assign and manageable for students, facilitating their understanding through written expression. Provide a concise description of the assignment in 1-2 sentences, ensuring it encourages research, reflection, or essay writing to deepen comprehension and promote success in their coursework."
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
    print("4. Reading/Writing")

    choice = input("Enter 1, 2, or 3: ")

    learning_style = ""
    if choice == "1":
        learning_style = "audio"
    elif choice == "2":
        learning_style = "kinesthetic"
    elif choice == "3":
        learning_style = "visual"
    elif choice == "4":
        learning_style = "reading/writing"
    else:
        print("Invalid choice, defaulting to general assignment.")
        learning_style = "general"  # Default to general if invalid choice

    # For demonstration purposes, let's assume the teacher already uploaded a chapter summary
    chapter_summary = "Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods with the help of chlorophyll."

    # Get tailored assignment from GPT
    assignment = get_assignment(learning_style, chapter_summary)

    # Output assignment
    print(f"\nHi {student_name}, based on your {learning_style} learning style, here is your tailored assignment:")
    print(assignment)


# Run the student interface
if __name__ == '__main__':
    student_interface()
