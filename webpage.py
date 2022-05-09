# encoding: utf-8
import streamlit as st
import numpy as np
import pandas as pd
#from keybert import KeyBERT
# For Flair (Keybert)
#from flair.embeddings import TransformerDocumentEmbeddings
import seaborn as sns
# For download buttons
#from functionforDownloadButtons import download_button
import os
import json

st.set_page_config(
    page_title="Malicious web detection",
    page_icon="🎈",
)

#c30, c31, c32 = st.columns([2.5, 1, 3])

#with c30:
#st.image("title.png", width=200)
st.title("🔑 Malicious web detection")
st.header("")



with st.expander("ℹ️ - 关于", expanded=True):

    st.write(
        """     
-   恶意网页检测系统为基于streamlit搭建的易于使用的恶意url检测网站。
-   仅需键入您希望检测的网址就可以识别该网址是否可以安全访问。 🤗 
	    """
    )

    #st.markdown("")
st.markdown("### ***📌 粘贴需要检测的网址***")
with st.form(key="my_form"):
    c1,c2= st.columns([2,5])
    with c1:
        ModelType = st.radio(
            "选择模型",
            ["BERT", "CNN"],
            help="该网站提供了两种模型对未知网站进行安全性预测，您可以选择一种算法来检测是否为恶意网页",
        )


        

    with c2:
        doc = st.text_area(
            "请输入待检测的网址",
            height=100,
        )

        MAX_WORDS = 500
        import re
        res = len(re.findall(r"\w+", doc))
        if res > MAX_WORDS:
            st.warning(
                "⚠️ Your text contains "
                + str(res)
                + " words."
                + " Only the first 500 words will be reviewed. Stay tuned as increased allowance is coming! 😊"
            )

            doc = doc[:MAX_WORDS]

        submit_button = st.form_submit_button(label="✨ 点击查看结果")


if not submit_button:
    st.stop()


st.markdown("### ***🎈 Check results***")

#st.header("")

#cs, c1, c2, c3, cLast = st.columns([2, 1.5, 1.5, 1.5, 2])


#st.header("")
doc
#df=st.text_area(doc)
#df = pd.DataFrame(doc, columns=["website"])
#st.table(df)

st.success("safe")
#st.error("可疑恶意网页")
#st.warning("输入不合法，请重新输入正确地址！")
st.balloons()
