from pathlib import Path
import streamlit as st
from PIL import Image


#path settings                      
current_dir= Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file= current_dir/"main.css"
resume_file= current_dir/"cv.pdf"
profile_pic= current_dir/"profile-pic.png"

#general settings

page_title ="Ramya | DigitalCV"
page_icon = ":wave:"
#name= "Ramya MohanKumar"
description= """An immediate joiner wants to learn constantly at the workplace and use the knowledge thus obtained in adding at least as much value to the Organization as I derive from it, without Compromising on Quality or Personal Ethics."""
email="ramya.mohankumar86@gmail.com"
phone = "+49 015731080133"
address="Worringer Str., Düsseldorf, Deutschland"
social_media={
    "Youtube": "https://youtube.com/",
    "LinkedIn": "https://www.linkedin.com/in/mohankumar-n/",
}
projects= {
    "Dashboards - Comparing sales across two call agents": "https://youtub/"
    "Desktop Application",
}

st.set_page_config(layout="wide",page_title=page_title,page_icon=page_icon)
st.title("Ramya MohanKumar")

#load css, pdf & profile pic
with open (css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open (resume_file,"rb") as pdf_file:
    PDFbyte=pdf_file.read()
    profile_pic=Image.open(profile_pic)
    
#hero section
col1,col2 = st.columns(2,gap="small")
with col1:
    st.image(profile_pic, width =230)

with col2:
    #st.title(name)
    st.write(description)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="applicaton/octet-stream",
    )
    st.write("...",email)
    st.write(phone)
    st.write(address)
    
    
#solical links
st.write("#")
cols=st.columns(len(social_media))
for index,(platform,link) in enumerate(social_media.items()):
    cols [index].write(f"[{platform}]({link})")
    
#HIGHLIGHTS 
st.write("#")
st.subheader("HIGHLIGHTS")
st.write("---")
c1,c2,c3=st.columns(3)
c1.write(
    """ Mergers and Acquisition   
     Cross Border Business set up    
     Contract Negotiation""")
c2.write(
    """
     Data Protection    
     Document management   
     Competition Law 
    """)
c3.write(
    """
     Liquidation Procedure   
     IP Law    
     Joint ventures 
    """)

# EDUCATION & CREDENTIAL
st.write("#")
st.subheader("EDUCATION")
st.write("---")
st.write(
    """
    - LLM, Master’s in Law, (Intellectual Property Rights and Information Technology) 
    - LLB, Bachelor’s in Law (Common Law - Gold Medalist) 
    - MA, Master’s in English 
    - B.Sc , Bachelor’s of Science 
    """
)

#work history
st.write("#")
st.subheader("CAREER PROGRESSION")
st.write("---")

#Job 1
st.markdown("**Working student  - ERGO Group AG, Dusseldorf**")
st.write("November  2021 – September 2022")
st.write(
    """
    - Mergers and acquisition, Liquidation.
    - Drafting, Reviewing and Amending Agreement, Authorisation required for Joint Ventures
    - Negotiation for Trademark usage in Joint Ventures and subsequent Infringement issues
    - Contract Negotiation for projects and share purchase/transfer

    - Specific to IT contracts and service agreements
    - Established the procedure for implementation of ERGO Group IT platform, especially in areas of Data Protection and Confidentiality.
    - Co ordination with Compliance with various projects

    - Dealt with Asian market for ERGO Group
    - Organised and conducted Legal Workshop for the Team
    - Drafting of Power of Attorney for various Shareholders and Board meetings 
    - Involved in the appointment/extension of the Board Members of the Management
    """
)

#Job 2
st.markdown("**Junior Law Trainee  - Senior Counsel, Puducherry Court**")
st.write("June 2019 – June 2020")
st.write(
    """
    - In service for CHAMBER PRACTICE as ADVOCATE-TRAINEE. 
    - Attended promptly to the Clients and office
    """
)

#Job 3
st.markdown("**Student Intern  - Legal Service Authority, Government of India**")
st.write("January 2019 – March 2019")
st.write(
    """
    - Observed and participated in Mediation, Conciliation proceedings. 
    - Participated in legal awareness programs. 
    - Volunteered for a national law council.
    """
)

#Job 4
st.markdown("**Customer Solutions Representative - Hewlett Packard (Global E business Operations), Chennai**")
st.write("January 2009 – May 2009")
st.write(
    """
    -	Introduced the new pricing method.
    -	Active participation in training new hires.
    -	Adapted quickly to the challenging process landscape.
    """
)

#Job 5
st.markdown("**Senior Contract Administrator**")
st.write("May 2006 – December 2008")
st.write(
    """
    - Single point of contact for the Back Office for Europe and Middle East Africa (EMEA) Region.
    - Worked on multiple processes in SAP (ABAP) module.
    """
)
#ADDITIONAL INFORMATION 
st.write("#")
st.subheader("ADDITIONAL INFORMATION ")
st.write("---")

#Job 1
st.write("Year of Birth :	1986")
st.write("Linguistics   :	English (C1), German(B1), French(A1) and Tamil(Native) ")
st.write("Marital Status:	Married")
st.write("Nationality   :	Indian")

#DECLARATION
st.write("#")
st.subheader("DECLARATION")
st.write("---")

#Job 1
st.write("I hereby declare that all the information contained in this resume is in accordance with facts ortruths to my knowledge.")

