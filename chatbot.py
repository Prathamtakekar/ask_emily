# chatbot.py
def chatbot_query(user_input):
    user_input = user_input.lower()
    if "campground" in user_input:
        return "You can find campgrounds in your area by checking the 'Campgrounds' section."
    elif "bridge height" in user_input:
        return "Our database includes bridge heights for major routes."
    elif "technician" in user_input:
        return "We have a list of technicians available based on your location and needs."
    else:
        return "I'm here to help with trip planning, route information, and more!"
