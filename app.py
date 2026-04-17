import streamlit as st
from PIL import Image
from api_calling import error_finder_generator,solution_generator

st.title("AI Code Debugger App")
st.markdown("correct your code")
st.divider()

with st.sidebar:
    st.header("Controlls")

    images = st.file_uploader(
        "Upload the photos of your note",
        type=['jpg','jpeg','png'],
        accept_multiple_files=True
    )

    pil_images =[]

    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)

    if images:
        if len(images)>3:
            st.error("Upload at max 3 images")
        else:
            st.subheader("Uploaded images")
            
            col = st.columns(len(images))

            

            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)

    #option bar
    selected_option = st.selectbox(
        "Choose an option",
        ("Hints","Solution with code"),
        index = None
    )
    pressed=st.button("Click to initate AI",type="primary")
                    

if pressed:
    if not images:
        st.error("You must upload 1 image")
    if not selected_option:
        st.error("You must select an option")

    if images and selected_option:

        #find mistake
        with st.container(border=True):
            st.subheader("Analize Your Code")

            with st.spinner("AI is writting for you"):
                error_finder = error_finder_generator(pil_images)
                st.markdown(error_finder)

        


        #Solution or hint
        with st.container(border=True):
            st.subheader(f"Your {selected_option} are below")

            with st.spinner("AI is writting for you"):
                solution=solution_generator(pil_images,selected_option)
                st.markdown(solution) 

                 
     


    

    

         