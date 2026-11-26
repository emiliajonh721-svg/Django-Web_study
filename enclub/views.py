from django. http import HttpResponse
from django. shortcuts import render

# def homepage(request):
#     return HttpResponse("hello django!")

def Home(request):
    return render(request, 'Homepage.html')
def Allcourse(request):
    CoursesData=[
        # {
        #     'name': 'Grammar courses',
        #     'description': 'Master verb tenses and sentence structures easily without getting bogged down in complex rules.',
        #     'image': 'images/Grammar_course.jpg',
        #     'visit':9,
        #     'urls_name':''
        # },
        # {
        #     'name': 'Vocabulary courses',
        #     'description': 'Build real-world fluency and confident pronunciation through guided conversations and practical daily scenarios.',
        #     'image': 'images/Vocabulary_course.webp',
        #     'visit':40,
        #     'urls_name':''      
        # },
        # {
        #     'name': 'Speakinng courses',
        #     'description': 'Expand your everyday word bank with essential phrases and natural expressions for clear communication.',
        #     'image': 'images/Speaking_course.jpg',
        #     'visit':278,
        #     'urls_name':''     
        # },
        {
            'name': 'Beginer courses',
            'description': 'Build a strong foundation in everyday vocabulary and basic speaking skills from day one.',
            'image': 'images/English-for-Beginners.jpg',
            'visit':217,
            'urls_name':'Beginers'
        },
        {
            'name': 'Intermidiate courses',
            'description': 'Bridge the gap between basic phrases and natural conversation with practical grammar and fluency practice.',
            'image': 'images/English-for-intermidiate.png',
            'visit':104,
            'urls_name':'Intermediate'     
        },
        {
            'name': 'Advance courses',
            'description': 'Refine your fluency, master complex nuances, and speak English with the confidence of a native speaker.',
            'image': 'images/English-for-advance.jpg',
            'visit':18,
            'urls_name':'Advance'    
        },
        {
            'name': 'IELS courses',
            'description': 'Boost your band score with targeted exam strategies and real-world practice across all four test modules.',
            'image': 'images/English-for-IELS-1.png',
            'visit':50,
            'urls_name':'IELS'
        },
        {
            'name': 'Electronic Books',
            'description': ' Learn at your own pace anytime, anywhere with interactive lessons and clear, practical examples.',
            'image': 'images/Ego-book.jpg',
            'visit':139,
            'urls_name':'ElectronicBooks'     
        },
        {
            'name': 'English for Politicians courses',
            'description': 'Deliver persuasive speeches, handle tough interviews, and navigate diplomatic discussions with authority.',
            'image': 'images/English-for-Politician.jpg',
            'visit':23,
            'urls_name':'EnglishPolotics'  
        },
        {
            'name': 'English for Tour Guides courses',
            'description': 'Master verb tenses and sentence structures easily without getting bogged down in complex rules.',
            'image': 'images/English-for-tour.jpg',
            'visit':29,
            'urls_name':'TourGuides'
        },
        {
            'name': 'English for Tech courses',
            'description': 'Master essential industry terminology to collaborate effectively with global engineering and product teams.',
            'image': 'images/English-for-tech.webp',
            'visit':9,
            'urls_name':'EnglishTech'     
        },
        {
            'name': 'Englsih for Business courses',
            'description': 'Lead meetings, negotiate deals, and write professional emails with clarity and confidence.',
            'image': 'images/English-for-business.jpg',
            'visit':39,
            'urls_name':'EnglishBussiness'
                   
        }   
        
        
    ]
    context={'CoursesData': CoursesData}
    return render(request, 'Allcourse.html',context)

def ElectronicBookspage(request):
    books=[
        {
            'name':'20 Cyber terms',
            'description': 'Nov-17-2026',
            'image': 'booksimage/20-cyber-terms.png',
            'visit':39,
            'pdfs':'pdfs/20-cyber-terms.pdf'
        },
        {
            'name':'Mobile Application',
            'description': 'Nov-17-2026',
            'image': 'booksimage/Mobile-app.png',
            'visit':89,
            'pdfs':'pdfs/Mobile Application Security Verification Standard.pdf'
        },
        {
            'name':'1800 Vocabulary',
            'description': 'Nov-17-2026',
            'image': 'booksimage/1800-vocabulary.png',
            'visit':19,
            'pdfs':'pdfs/1800-Synonyms.pdf'
        },
        {
            'name':'Common mistake in English',
            'description': 'Nov-17-2026',
            'image': 'booksimage/Common-mistake.png',
            'visit':81,
            'pdfs':'pdfs/Common_Mistakes_in_English.pdf'
        },
{
            'name':'Ego is the enemy',
            'description': 'Nov-17-2026',
            'image': 'booksimage/ego-enemy.png',
            'visit':13,
            'pdfs':'pdfs/ego-is the enemy.pdf'
        },
        {
            'name':'Window Event log',
            'description': 'Nov-17-2026',
            'image': 'booksimage/window-Event.png',
            'visit':46,
            'pdfs':'pdfs/Windows_Event_Log_Analysis__1606817397.pdf'
        },
        {
            'name':'How to speak fluent',
            'description': 'Nov-17-2026',
            'image': 'booksimage/speak-fluent.png',
            'visit':98,
            'pdfs':'pdfs/How to Speak English Fluently.pdf'
        },
        {
            'name':'Wireshark',
            'description': 'Nov-17-2026',
            'image': 'booksimage/whireshark.png',
            'visit':54,
            'pdfs':'pdfs/Wireshark_4_Red_Teamers_1741001457.pdf'
        },
{
            'name':'Network Security',
            'description': 'Nov-17-2026',
            'image': 'booksimage/Network-security.png',
            'visit':38,
            'pdfs':'pdfs/NetworkSecurityCheckList.pdf'
        },
        {
            'name':'Malware hunting',
            'description': 'Nov-17-2026',
            'image': 'booksimage/malware-hunting.png',
            'visit':76,
            'pdfs':'pdfs/Hunting_Malware_Using_Memory_Forensics_1729781445.pdf'
        },
        {
            'name':'Email Security',
            'description': 'Nov-17-2026',
            'image': 'booksimage/Email-awareness.png',
            'visit':12,
            'pdfs':'pdfs/Email_Security_1730010177.pdf'
        },
        {
            'name':'Artifictial Intellegence',
            'description': 'Nov-17-2026',
            'image': 'booksimage/ai.png',
            'visit':20,
            'pdfs':'pdfs/Artificial Intelligence and Democracy - UNESCO (2024).pdf'
        },
{
            'name':'50 sample eassay',
            'description': 'Nov-17-2026',
            'image': 'booksimage/50essay.png',
            'visit':98,
            'pdfs':'pdfs/50 Sample Essays book - Cam-Edu.pdf'
        },
        {
            'name':'Cyber threat',
            'description': 'Nov-17-2026',
            'image': 'booksimage/cyber-threat.png',
            'visit':86,
            'pdfs':'pdfs/Cyber_Threat_Intelligence_1607689310.pdf'
        },
        {
            'name':'50 powerfull vocabulary',
            'description': 'Nov-17-2026',
            'image': 'booksimage/50powerfull.png',
            'visit':11,
            'pdfs':'pdfs/50_Vocabulary_Mini_Book_Khmer_CamEdu.pdf'
        },
        {
            'name':'Specail voculary',
            'description': 'Nov-17-2026',
            'image': 'booksimage/Specialwords.png',
            'visit':72,
            'pdfs':'pdfs/Assessment-of-Vocabulary.pdf'
        },
{
            'name':'Dark web',
            'description': 'Nov-17-2026',
            'image': 'booksimage/Darkweb.png',
            'visit':100,
            'pdfs':'pdfs/Dark Web the Other Side.pdf'
        },
        {
            'name':'Open Ai',
            'description': 'Nov-17-2026',
            'image': 'booksimage/openAi.png',
            'visit':209,
            'pdfs':'pdfs/Open_AI_Agents_Guide_1757373756.pdf'
        },
        {
            'name':'Man middle attack',
            'description': 'Nov-17-2026',
            'image': 'booksimage/MMA.png',
            'visit':11,
            'pdfs':'pdfs/Man_in_the_Middle_Attack_1607661253.pdf'
        },
        {
            'name':'English conversation',
            'description': 'Nov-17-2026',
            'image': 'booksimage/30conversation.png',
            'visit':20,
            'pdfs':'pdfs/English Conversation.pdf'
        },
{
            'name':'Idoim',
            'description': 'Nov-17-2026',
            'image': 'booksimage/180idiom.png',
            'visit':31,
            'pdfs':'pdfs/180 Essential English Idioms.pdf'
        },
        {
            'name':'Blockchain',
            'description': 'Nov-17-2026',
            'image': 'booksimage/Blockchain.png',
            'visit':54,
            'pdfs':'pdfs/Blockchain_Integration_and_Its_Impact_on_Renewable_Energy_1741522358.pdf'
        },
        {
            'name':'DevOps',
            'description': 'Nov-17-2026',
            'image': 'booksimage/Devop.png',
            'visit':61,
            'pdfs':'pdfs/DevSecOps_Fundamentals_Guidebook_1677510698.pdf'
        },
        {
            'name':'Linux',
            'description': 'Nov-17-2026',
            'image': 'booksimage/LinuxJourney.png',
            'visit':87,
            'pdfs':'pdfs/The_Linux_Process_Journey_Version_1_0_beta_Feb2023_1676714822.pdf'
        },
{
            'name':'English conversation premium',
            'description': 'Nov-17-2026',
            'image': 'booksimage/Conversation-Premuim.png',
            'visit':18,
            'pdfs':'pdfs/English-Conversation-Premium_Teachong (1).pdf'
        },
        {
            'name':'Microsoft Security',
            'description': 'Nov-17-2026',
            'image': 'booksimage/Microsoft-security.png',
            'visit':28,
            'pdfs':'pdfs/Microsoft_AI_Security_1741571491.pdf'
        },
        {
            'name':'Bug bounty',
            'description': 'Nov-17-2026',
            'image': 'booksimage/Bug.png',
            'visit':33,
            'pdfs':'pdfs/Bug_Bounty_Playbook_1746861014.pdf'
        },
        {
            'name':'Grammar exercise',
            'description': 'Nov-17-2026',
            'image': 'booksimage/Exercise500.png',
            'visit':28,
            'pdfs':'pdfs/500+ Grammar exercises for teachers.pdf'
        },

    ]
    context={'books':books}
    return render(request, 'ElectronicBooks.html',context)



def Beginers(request):

    videos = [
        {
            'title': 'Introduction',
            'url': 'video/Beginner English Introduction.mp4',
            'thumbnail': 'images/English-for-Beginners.jpg'
            
        },
        {
            'title': 'Lesson 1: ',
            'url': 'video/English Consonants + Vowels.mp4',
            'thumbnail': 'images/English-for-Beginners.jpg'
        },
        {
            'title': 'Lesson 2: ',
            'url': 'video/English Grammar： a ⧸ an + Noun.mp4',
            'thumbnail': 'images/English-for-Beginners.jpg'
        },
{
            'title': 'Lesson 3: ',
            'url': 'video/English Grammar： Singular + Plural Nouns.mp4',
            'thumbnail': 'images/English-for-Beginners.jpg'
            
        },
        {
            'title': 'Lesson 4: ',
            'url': 'videos/English Grammar： Subjective Pronouns.mp4',
            'thumbnail': 'images/English-for-Beginners.jpg'
        },
        {
            'title': 'Lesson 5: ',
            'url': 'video/English Grammar Subjective Pronouns +  Verb.mp4',
            'thumbnail': 'images/English-for-Beginners.jpg'
        },
{
            'title': 'Lesson 6:  ',
            'url': 'video/English Grammar： Subjective Pronouns + Be + Not.mp4',
            'thumbnail': 'images/English-for-Beginners.jpg'
            
        },
        {
            'title': 'Lesson 7: ',
            'url': 'video/English Grammar： Be Verb Pronoun Questions.mp4',
            'thumbnail': 'images/English-for-Beginners.jpg'
        },
        {
            'title': 'Lesson 8: ',
            'url': 'video/English Grammar： Review #1 - Subjective Pronouns.mp4',
            'thumbnail': 'images/English-for-Beginners.jpg'
        },
{
            'title': 'Lesson 9: ',
            'url': 'video/Grammar Check Up #1.mp4',
            'thumbnail': 'images/English-for-Beginners.jpg'
        },
{
            'title': 'Lesson 10: ',
            'url': 'video/English Grammar： What + Be Verb Questions.mp4',
            'thumbnail': 'images/English-for-Beginners.jpg'
        }
    ]

    context = {'videos': videos}

    return render(request, 'BeginersCourse.html', context)
def Intermedait(request):
    videos = [
        {
            'title': 'Introduction',
            'url': 'video2/B1-B2 Intermediate Level ENGLISH Course - Complete Grammar, Vocabulary, Pronunciation and Structures.mp4',
            'thumbnail': 'images/English-for-intermidiate.png'
                
        },
        {
            'title': 'Lesson 1: ',
            'url': 'video2/Lesson 1- B1-B2 Intermediate Level English - Present Simple and Continuous Tense - Udemy English.mp4',
            'thumbnail': 'images/English-for-intermidiate.png'
        },
        {
            'title': 'Lesson 2: ',
            'url': 'video2/Lesson 2 - B1-B2 Intermediate Level English - Action and Non-Action Verbs - Udemy English Lessons.mp4',
            'thumbnail': 'images/English-for-intermidiate.png'
        },
        {
            'title': 'Lesson 3: ',
            'url': 'video2/Lesson 3 - B1-B2 Intermediate Level English - Frequency Adverbs and Time Expressions- English Course.mp4',
            'thumbnail': 'images/English-for-intermidiate.png'
                
        },
        {
            'title': 'Lesson 4: ',
            'url': 'video2/Lesson 4 - B1-B2 Intermediate Level English - Simple Past Tense - English Course - Udemy English.mp4',
            'thumbnail': 'images/English-for-intermidiate.png'
        },
        {
            'title': 'Lesson 5: ',
            'url': 'video2/Lesson 5 - B1-B2 Intermediate Level English - Regular and Irregular Verbs in the Past Simple ｜ UDEMY.mp4',
            'thumbnail': 'images/English-for-intermidiate.png'
        },
        {
            'title': 'Lesson 6: ',
            'url': 'video2/Lesson 6 - B1-B2 Intermediate Level ENGLISH Course - Past Progressive ⧸ Continuous Tense ｜ Grammar.mp4',
            'thumbnail': 'images/English-for-intermidiate.png'
                
        },
        {
            'title': 'Lesson 7: ',
            'url': 'video2/Lesson 7- B1-B2 Intermediate Level English - Simple Past and Past Continuous Tenses - Udemy English.mp4',
            'thumbnail': 'images/English-for-intermidiate.png'
        },
        {
            'title': 'Lesson 8: ',
            'url': 'video2/Lesson 8- B1-B2 Intermediate Level English - Future Tense - Will - Be Going to-Verb ｜ Udemy English.mp4',
            'thumbnail': 'images/English-for-intermidiate.png'
        },
        {
            'title': 'Lesson 9:  ',
            'url': 'video2/Lesson 9- B1-B2 Intermediate Level English - Compare WILL and BE GOING TO future time- Udemy English.mp4',
            'thumbnail': 'images/English-for-intermidiate.png'
        },
        {
            'title': 'Lesson 10:',
            'url': 'video2/Lesson 10- B1-B2 Level English - Present Simple and Continuous Tense Future time- Udemy English.mp4',
            'thumbnail': 'images/English-for-intermidiate.png'
        }
    ]
    context = {'videos': videos}
    return render(request,'IntermediateCourses.html',context)
def Advance(request):
    videos = [
        {
            'title': 'Lesson 1',
            'url': 'video3/Advanced English (Level C1) 01 - Adverbs.mp4',
            'thumbnail': 'images/English-for-advance.jpg'
                
        },
        {
            'title': 'Lesson 2: ',
            'url': 'video3/Advanced English (Level C1) 02 - The Perfect Tenses.mp4',
            'thumbnail': 'images/English-for-advance.jpg'
        },
        {
            'title': 'Lesson 3: ',
            'url': 'video3/Advanced English (Level C1) 03 - Vocabulary Work.mp4',
            'thumbnail': 'images/English-for-advance.jpg'
        },
        {
            'title': 'Lesson 4:',
            'url': 'video3/Advanced Level English (Level C1) 04： Discourse Markers So, Therefore, Because, In Order To etc.mp4',
            'thumbnail': 'images/English-for-advance.jpg'
                
        },
        {
            'title': 'Lesson 5: ',
            'url': 'video3/Advanced English (Level C1) -  Class 05 - Comparison.mp4',
            'thumbnail': 'images/English-for-advance.jpg'
        },
        {
            'title': 'Lesson 6:',
            'url': 'video3/Advanced Level English (Level C1) - Class 06 - The Verb Have.mp4',
            'thumbnail': 'images/English-for-advance.jpg'
        },
        {
            'title': 'Lesson 7:  ',
            'url': 'video3/Advanced Level English (Level C1) -  Class 07 - Vocabulary   The Family.mp4',
            'thumbnail': 'images/English-for-advance.jpg'
                
        },
        {
            'title': 'Lesson 8:',
            'url': 'video3/Advanced English Course (Level C1) - Class 08 - Pronouns.mp4',
            'thumbnail': 'images/English-for-advance.jpg'
        },
        {
            'title': 'Lesson 9: ',
            'url': 'video3/Advanced English (Level C1) - Class 09 - The Narrative Tenses.mp4',
            'thumbnail': 'images/English-for-advance.jpg'
        },
        {
            'title': 'Lesson 10: ',
            'url': 'video3/Advanced English (Level C1) - Class 10 - Verbs of Movement.mp4',
            'thumbnail': 'images/English-for-advance.jpg'
        },
    ]
    context = {'videos': videos}
    return render(request,'AdvanceCourse.html',context)
def IELS(request):
    videos = [
        {
            'title': 'Lesson 1',
            'url': 'video4/IELTS Preparation Course - Introduction - Part 1.mp4',
            'thumbnail': 'images/English-for-IELS-1.png'
                
        },
        {
            'title': 'Lesson 2: ',
            'url': 'video4/IELTS Preparation Course - Introduction - Part 2.mp4',
            'thumbnail': 'images/English-for-IELS-1.png'
        },
        {
            'title': 'Lesson 3: ',
            'url': 'video4/IELTS Preparation Course - Introduction - Part 3.mp4',
            'thumbnail': 'images/English-for-IELS-1.png'
        },
        {
            'title': 'Lesson 4:',
            'url': 'video4/IELTS Preparation Course - Introduction - Part 4.mp4',
            'thumbnail': 'images/English-for-IELS-1.png'
                
        },
        {
            'title': 'Lesson 5: ',
            'url': 'video4/IELTS Preparation Course - Writing - Part 1.mp4',
            'thumbnail': 'images/English-for-IELS-1.png'
        },
        {
            'title': 'Lesson 6:',
            'url': 'video4/IELTS Preparation Course - Writing - Part 2.mp4',
            'thumbnail': 'images/English-for-IELS-1.png'
        },
        {
            'title': 'Lesson 7:  ',
            'url': 'video4/IELTS Preparation Course - Writing - Part 3.mp4',
            'thumbnail': 'images/English-for-IELS-1.png'
                
        },
        {
            'title': 'Lesson 8:',
            'url': 'video4/IELTS Preparation Course - Writing - Part 4.mp4',
            'thumbnail': 'images/English-for-IELS-1.png'
        },
        {
            'title': 'Lesson 9: ',
            'url': 'video4/IELTS Preparation Course - Writing - Part 5.mp4',
            'thumbnail': 'images/English-for-IELS-1.png'
        },
        {
            'title': 'Lesson 10: ',
            'url': 'video4/IELTS Preparation Course - Writing - Part 6.mp4',
            'thumbnail': 'images/English-for-IELS-1.png'
        },
    ]
    context = {'videos': videos}
    return render(request,'IELScourse.html',context)
def TourGuide(request):
    return render(request,'EnglishForTour.html')
def Politic(request):
    return render(request,'EnglishForpolotic.html')
def Tech(request):
    return render(request,'EnglishForTech.html')
def Bussiness(request):
    return render(request,'EnglishForBussiness.html')
def Contact(request):
    return render(request,'Contact.html')
def Aboutus(request):
    return render(request,'Aboutus.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("Homepage")

        else:
            return render(request, "login.html", {
                "error": "Invalid username or password"
            })

    return render(request, "login.html")


def Home(request):
    if request.user.is_authenticated:
        return render(request, 'Homepage.html')

    return redirect('login')
