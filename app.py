import streamlit as st

# App Title and Description
st.title("📱 Mindful Tech Guide")
st.subheader("Your Digital Wellness & Behavioral Habits Buddy")

st.markdown("---")

# Navigation Tabs matching the Prompt Templates
tab1, tab2, tab3 = st.tabs(["📚 Simple Explanation", "💡 Real-Life Example", "📝 Take the Quiz"])

with tab1:
    st.header("Understanding Screen Addiction & Dopamine Loops")
    st.write("""
    * **The 'Feel-Good' Chemical:** Dopamine is a natural chemical your brain releases whenever you experience something rewarding. It acts like a tiny mental pat on the back that says, 'That felt great, let's do it again!'
    * **How the Loop Hooks Kids:** Mobile apps and games are intentionally designed to trigger this chemical using a strict 4-step loop:
        1. *Trigger:* The phone buzzes, flashes a bright color, or sends a notification.
        2. *Action:* The child automatically taps or swipes the screen.
        3. *Reward:* They see a funny short video, get a 'like,' or win points, which releases a rush of dopamine.
        4. *Craving:* The brain loves that quick feeling, so it immediately demands another hit.
    * **Why it Controls Under-14s:** A child's brain is still growing. The area responsible for willpower and self-control (the prefrontal cortex) isn't fully built yet, making impulse control much harder.
    * **Breaking the Habit:** Digital wellness means breaking this loop by swapping out phone screens for real-world activities (like sports, cooking, or crafts) that give natural rewards.
    """)

with tab2:
    st.header("The Digital Slot Machine: Why Kids Can't Stop Swiping")
    st.info("""
    Imagine a 12-year-old child sitting on the couch scrolling through a short-form video app. Every single time they swipe their thumb down to load a new video, they have no idea what is coming next.
    
    * The first video is a boring dance trend. (No reward)
    * The second video is a random advertisement. (No reward)
    * The third video is a hilarious clip of a puppy doing a trick. (**Big Reward!**)
    
    The child’s brain instantly releases a sudden rush of dopamine. This unpredictability works exactly like a slot machine in a casino. Because the child does not know which swipe will give them the next funny video, their brain enters a state of constant anticipation. It keeps whispering, 'Just one more swipe... the next one might be the best one yet.'
    """)

with tab3:
    st.header("Quiz: Managing Screen Loops & Digital Wellness")
    
    # Form for Quiz Questions
    with st.form("quiz_form"):
        q1 = st.radio(
            "1. What chemical is released in a child’s brain that creates a feeling of pleasure and drives screen addiction?",
            ["Melatonin", "Insulin", "Dopamine", "Adrenaline"]
        )
        
        q2 = st.radio(
            "2. Why do endless scrolling features (like short-form video feeds) keep children hooked for hours?",
            [
                "They provide unpredictable rewards, making the brain constantly swipe to find the next exciting post.",
                "They automatically shut down the phone after 30 minutes.",
                "They require deep mathematical skills to navigate.",
                "They stop working if the user looks away from the screen."
            ]
        )
        
        q3 = st.radio(
            "3. Why are children under the age of 14 physically more vulnerable to digital habit loops than adults?",
            [
                "Children use phones only when they are asleep.",
                "Their prefrontal cortex, which governs impulse control and willpower, is still developing.",
                "Children have a lower number of senses than adults.",
                "Adults do not experience chemical rewards in their brains."
            ]
        )
        
        q4 = st.radio(
            "4. Which of the following is an effective digital wellness habit to break the bedtime screen routine?",
            [
                "Hiding the phone under the mattress while it is turned on.",
                "Setting up a dedicated charging station outside of the bedroom.",
                "Checking notifications every time you wake up in the night.",
                "Upgrading to a bigger tablet screen."
            ]
        )
        
        q5 = st.radio(
            "5. What is the healthiest way to replace the quick dopamine rewards a child gets from a mobile screen?",
            [
                "Spending more hours playing video games on a computer instead.",
                "Engaging in hands-on real-world activities like sports, arts, or interactive board games.",
                "Sitting quietly in a dark room without talking to anyone.",
                "Checking a different app that has fewer bright colours."
            ]
        )
        
        submit_button = st.form_submit_button("Submit Answers")
        
    if submit_button:
        score = 0
        
        # Check Answers precisely based on text matches
        if q1 == "Dopamine": 
            score += 1
        if q2 == "They provide unpredictable rewards, making the brain constantly swipe to find the next exciting post.": 
            score += 1
        if q3 == "Their prefrontal cortex, which governs impulse control and willpower, is still developing.": 
            score += 1
        if q4 == "Setting up a dedicated charging station outside of the bedroom.": 
            score += 1
        if q5 == "Engaging in hands-on real-world activities like sports, arts, or interactive board games.": 
            score += 1
        
        # Display Results & Feedback
        st.subheader(f"Your Score: {score}/5")
        if score == 5:
            st.success("🎉 Perfect score! You completely understand digital wellness frameworks!")
        else:
            st.warning("Good effort! Review the explanations or tabs above to get a perfect score next time.")
            
        # Contextual Evaluation & Feedback Section
        st.markdown("### 🧠 Mindful Buddy Feedback Breakdown:")
        st.write(f"- **Question 1 Evaluation:** {'Correct! Dopamine drives motivation and habits.' if q1 == 'Dopamine' else 'Incorrect. The correct answer is Dopamine.'}")
        st.write(f"- **Question 2 Evaluation:** {'Correct! Variable rewards emulate casino slot-mechanics.' if q2.startswith('They provide unpredictable') else 'Incorrect. Endless scrolling hooks users through variable, unpredictable rewards.'}")
        st.write(f"- **Question 3 Evaluation:** {'Correct! The prefrontal cortex finishes development in adulthood.' if q3.startswith('Their prefrontal cortex') else 'Incorrect. Under-14s have an underdeveloped prefrontal cortex.'}")
        st.write(f"- **Question 4 Evaluation:** {'Correct! Moving chargers out of bedrooms entirely removes temptation.' if q4.startswith('Setting up a dedicated') else 'Incorrect. Bedtime routines are best protected by keeping devices physically out of bedrooms.'}")
        st.write(f"- **Question 5 Evaluation:** {'Correct! Offline achievements offer slower, healthier dopamine tracks.' if q5.startswith('Engaging in hands-on') else 'Incorrect. Active real-world hobbies are the healthiest replacement.'}")
