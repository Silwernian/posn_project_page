import streamlit as st


st.header(':violet[**Project: Mastering Physics**]')

st.divider()

st.subheader(':blue[Objectives and Student Progression]')
st.markdown(
    '''
|Phase|Time Frame|Objectives|สิ่งที่ลูกค้าได้|Pass|Failed|Retry Time|
|:-:|:----:|:----:|:----:|:----:|:----:|:----:|
|  :green[**E0.**] | Instant. |Test พื้นฐาน Math และ Physics   | รู้พื้นฐานตัวเองและจุดที่ต้องแก้ไข |E1| Choose HB or EVD (Consult)   |1.5 Monts Until Ready|   
|  :green[**E1.**] | 2 Months.|Calculus and Basic Physics (ฟิสิกส์ท่องจำ)  |  รู้จักและใช้งาน Calculus พื้นฐานได้  |E2| Diagnose and Retry (1 Months)   |1 Months|   
|  :green[**E2.**] | 3 Months|Elementary Physics (Mechanics)   |  สอวน. ค่าย 1 (40%) |E3|Retry|1 Months|   
|  :green[**E3.**] | 2 Months|Elementary Physics (Electrodynamics)   |  สอวน. ค่าย 1(80%) |E4|Retry|0.5 Months|   
|  :green[**E4.**] | 1 Months|Elementary Physics (Thermodynamics)  |  สอวน. ค่าย 1 (90%) |E5|Retry|0.5 Months|   
|  :green[**E5.**] | 1 Months|Elementary Physics (Waves and Optics), optional  |  สอวน. ค่าย 1 (การันตีผล) |E6| Retry or Skip|0.5 Months|   
| :green[**E6.**] | 2 Months|Elementary Physics  (Modern Physics), optional (Not for IJSO)  | เปิดโลกฟิสิกส์  |A1|Retry or Skip|0.5 Months|   
|:blue[**A1.**]|3 Months|Classical Mechanics|ผู้แทนศูนย์ (25%)|A2|Retry|1 Months|
|:blue[**A2.**]|3 Months|Classical Electrodynamics|ผู้แทนศูนย์ (50%)|A|Retry|1 Months|
|:blue[**A3.**]|3 Months|Classical Thermodynamics|ผู้แทนศูนย์ (75%)|A4|Retry|1 Months|
|:blue[**A4.**]|2 Months|Final Preparation|ผู้แทนศูนย์ (การันตี :red[**ระวังเรื่องแข่งกันเอง**])|S1|Retry|1 Months|
|:red[**S1**]|3 Months|Selective Advanced Subject|เตรียมไป TPhO|S2|Retry or Change Subject| Months|   
   
Note: Zone A และ S เรียนแบบ Dual Slot  ได้ (เรียนสองวิชาพร้อมกัน)
'''
) 
st.subheader(':blue[Selective Subjects]')
st.markdown(
    '''
|Zone|Subject|PR|
|:----:|:----:|:----:|
|:blue[**A**]|Waves and Optics|Classical Mechanics|
|:blue[**A**]|Introduction to Special Relativity|Classical Mechanics and Electrodynamics|
|:blue[**A**]|Computer Programming in Physics|Elementary Physics|
|:blue[**A**]|Mathematical Methods for Physics I|Calculus|
|:blue[**A**]|Introduction to Quantum Mechanics|Calculus, Classical Mechancis and Electrodynamics|
|:red[**S**]|Advanced Mechanics|Calculus, Classical Mechancis and Electrodynamics|
|:red[**S**]|Advanced Electrodynamics|Calculus, Classical Mechancis and Electrodynamics|
|:red[**S**]|Quantum Mechanics|Calculus, Classical Mechancis and Electrodynamics|
|:red[**S**]|Statistical and Thermal Physics|Calculus, Classical Mechancis and Electrodynamics|
'''
)

st.divider()

st.subheader(':blue[Internal Details]')

st.markdown(
    '''
:blue[ระบบการเรียน]
* อัดวีดีโอไว้ล่วงหน้า แล้วให้นักเรียบนเปิดดูได้ (VDO นี้ควรอยู่บน everyday เพราะ Control เรื่องเด็กเอาวีดีโอไปแจกเพื่อนได้)
* บน EVD มีระบบ UnLocked Content ไหม เช่น เด็กคนนี้สอบผ่านเรื่องนี้แล้ว Unlock เรื่องถัดไปให้
* ตัววีดีโอบนเว็บขายแยกแบบไม่ต้องมาเรียน Offline ได้ ??
* อีกแนวคิดคือเด็กทุดคนต้องมีรหัส Everyday เพื่อเรียนส่วน Elementary แต่ถ้าอยากมา Offline ต้องสมัครกับ MKMK อีกคอร์สเพื่อ  Unlock
* ตัว VDO จะมีแค่ Core Concepts และ Simple Example ดูอย่างเดียวไม่พอใช้งานจริง
* เมื่ออยู่ใน Class เด็กจะได้รับ Assignment เพื่อไปทำ สร้าง Skill และทดสอง Concepts ที่เรียนมา
* เมื่อเรียนจบแต่ละหัวข้อ นัดสอบปากเปล่าทดลอง Concepts
* สอบข้อเขียนทำในระดับ Level (ลด Laod งาน) ตรงนี้จะตรวจทุกอย่าง ต่อให้คำตอบถูกหมดแต่วิธีเขียนไม่ดีพอก็ไม่ไห้ผ่าน
'''
)

st.markdown(
    '''
:blue[ขายที่ไหน]
* บนเว็บ EVD: ตรงนี้ขาย Online เนื้อหา Elementary ที่มีแค่วีดีโอเท่านั้น
* ขายในแง่ที่ว่า ต่อให้ไม่สนใจ สอวน. แต่แค่เรียน Elementary เสร็จก็ไม่ต้องสนใจฟิสิกส์ม.ปลายอีกเลย (ได้เรื่อง A-level ไปในตัว)
* ขายว่ามี Offline ถ้าอยากสมัครมาติดต่อ MKMK หรือซื้อในนั้นเลย (เสียตรงทีไม่ได้มาคุยแบบตัวต่อตัว) ??
* ระวังเรื่องโปรโมทว่าการันตี ไม่ควรโปรโมทออกเว็บ ควรการันตีแบบต่อหน้า Offline เท่านั้น (วงการมีลับหลังเยอะ)
'''
)

st.markdown(
    '''
:blue[User Flow]
- สมัคร EVD ต้องสมัครก่อนทุกกรณี
- ถ้าสนใจสมัครคอร์ส Offline ให้มาที่ MKMK มาคุยรายละเอียดก่อน (การันตีให้ตรงนี้ อธิบายระบบการลงทะเบียนราย Quarter และระบบเลือกวิชา)
- น้องมาเรียนตามเวลาที่เลือก (เด็กข้างนอกมากี่วันก็ได้แต่ต้องแจ้งก่อน)
- Evaluate ท้ายคอร์ส หรือเมื่อจบวิชาหนึ่งๆ ถ้ามีปัญหาเรียกเข้ามา Consult / Adjust   

Question:
* เริ่มได้เร็วที่สุดเมื่อไหร่ ประกาศขายเมื่อไหร่ถ้าจะเริ่มเลย
* 
'''
)