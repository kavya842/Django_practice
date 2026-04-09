from django.shortcuts import render , HttpResponse

# Create your views here.
def display(request):
    return HttpResponse('''<main style="height:3508px;width:60%; margin-left:20%">
                         <h1 style="text-align:center"> KAVYA VANKAYALAPATI </h1>
                            <h4 style="text-align:center"> +91 8919951981 </h4>
                        <h4 style="text-align:center"> kavyavankayalapati9999@gmail.com | Hyderabad, Telangana  </h4>
                            <h2>CAREER OBJECTIVE</h2>
                        <hr>
                            <p>Motivated and detail-oriented aspiring Software Engineer with strong skills in Python, Full Stack Development, and
                             Cloud Technologies. Seeking an opportunity to contribute to real-world product development, enhance technical
                            expertise, and grow in a dynamic and performance-driven organization</p>
                            <h2>EDUCATION</h2>
                        <hr>
                        <pre style="font-family: Times New Roman;">
DVR & Dr. HS MIC College of Technology                                                                                                                                                      Expected  May 2026
B. Tech - Information Technology                                                                                                                                                                                 CGPA:9.10/10
Sri Padmavathi Junior College                                                                                                                                                                                         2020 - 2022
Intermediate (MPC)                                                                                                                                                                                                      CGPA: 9.1/10
Z.P. High School, Kamepalli                                                                                                                                                                                           2019 - 2020
SSC                                                                                                                                                                                                                               CGPA:9.8/10</pre> 

                       <h2> TECHNICAL SKILLS</h2> <hr>
                         <pre style="font-family: Times New Roman">
Languages                                    :Python, Java (Basic), SQL
Web Technologies                        : HTML5, CSS3, JavaScript, Bootstrap
Frameworks & Databases            : Django, Flask, MySQL, MongoDB
Cloud & Tools                               : Git, Github, VS Code,n8n
Concepts                                       : Data Annotation, Problem Solving, Computer Networks, OOPS, SDLC, DBMS
APIs                                              : RESTful APIs Development, CI/CD Basics
                        </pre>

                        <h2> PROJECTS </h2><hr>
                        <p><b>Smart Blood Donation Management System </b><br>
                       • Designed a Scalable full-stack web application to manage blood donor and blood request management.<br>
• Built RESTful APIs using Node.js to handle CRUD operations for donors and their requests.<br>
• Integrated MongoDB database for efficient storage and retrieval of donor and blood inventory data.<br>
• Implemented role-based access and request tracking system to improve blood availability coordination.</p>
                        <p><b> Automation AI Email Negotiation System</b><br>
                        • Enhanced an AI-driven backend system for automated email classification and negotiation workflows.<br>
• Improved REST APIs using Python frameworks to process incoming email data.<br>
• Integrated n8n workflow automation tool to trigger automated responses and negotiation pipelines.<br>
• Focused on automation, email processing, and backend API performance optimization.</p>
                        
                        <h2>INTERNSHIPS</h2><hr>
                        <p><b>Generative AI Virtual Internship AICTE</b>
                        • Explored real-world applications of Generative AI including text-based models<br>
• Practiced prompt engineering techniques to generate accurate AI responses<br>
• Understood data annotation and labeling processes used in training AI models<br>
• Strengthened attention to detail and data evaluation skills
                        <p><b>Python Full Stack Virtual Internship  AICTE</b> <br>
                        • Developed a full-stack web applications using Python, Django<br>
• Built and integrate REST APIs for dynamic data handling<br>
• Worked with MYSQL/MongoDB for backend data Management and implement frontend interfaces
                        
                    <h2>CERTIFICATIONS & ACHIEVEMENTS</h2><hr>
                        <pre style="font-family: Times New Roman">
                        <p>• Gold Level Accenture Go for Gold Contest 2024<br>
• Python Full Stack Virtual Internship AICTE<br>    
• Generative AI Virtual Internship AICTE    </p></pre>
                           </main>          
                        ''')



