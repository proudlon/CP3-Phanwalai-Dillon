'''
"หากผู้เรียนกำลังศึกษาอยู่ในชั้นปีที่ 2 มหาวิทยาลัยชื่อดังย่านกลางเมืองที่ตอนนี้กำลังสอบเก็บคะแนนกันอย่างสนุกสนาน
แล้ววันนึงได้รับมอบหมายจากอาจารย์ที่ปรึกษาให้พัฒนาโปรแกรมให้กับทางคณะ โดย ระบบดังกล่าวจะมีการเก็บคะแนน
รายบุคคลของผู้เรียนแต่ละท่าน ของนักศึกษาชั้นปีที่ 2 เทอม 1" โดยมีรายชื่อวิชาดังนี้
Foundation English
General Business
Introduction to Computer Systems
Computer Programming

โดยให้ผู้เรียนพัฒนาโปรแกรมโดยสร้างตัวแปรสำหรับเก็บคะแนนผู้เรียนในรายวิชาดังกล่าว โดยคะแนนจะสามารถเป็นตัวเลขทศนิยมได้
และ เมื่อได้ตัวแปรมาแล้วให้ทำการแสดงผลออกมาให้ผู้ใช้งานได้เห็นในรูปแบบ
--- Your Score ---
Foundation English : คะแนนที่ได้
General Business : คะแนนที่ได้
Introduction to Computer Systems : คะแนนที่ได้
Computer Programming : คะแนนที่ได้
'''

FoundationEnglishScore = float(input())
GeneralBusinessScore = float(input())
IntroductionToComputerSystemsScore = float(input())
ComputerProgrammingScore = float(input())

print("--- Your Score ---")
print("Foundation English :", FoundationEnglishScore)
print("General Business :", GeneralBusinessScore)
print("Introduction to Computer Systems :", IntroductionToComputerSystemsScore)
print("Computer Programming :", ComputerProgrammingScore)
