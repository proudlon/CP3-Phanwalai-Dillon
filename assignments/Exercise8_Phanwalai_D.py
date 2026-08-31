'''
เมื่อเลือกสินค้าที่ต้องการเรียบร้อยแล้ว โปรแกรมจะถามจำนวนที่ต้องการซื้อ
หลังจากผู้ซื้อเลือกเรียบร้อยแล้ว โปรแกรมจะทำการแสดงสรุปราคารวมของรายการสั่งซื้อทั้งหมด

*หมายเหตุ Exercise นี้เป็นการให้ผู้เรียนได้นำความรู้จากบทเรียนมาใช้งานจริง
เพื่อให้เข้าใจการทำงานของคอมพิวเตอร์และสามารถนำมาประยุกต์ปรับใช้งานได้จริง
ซึ่งจะไม่มีการกำหนดรูปแบบโปรแกรมที่ตายตัว โจทย์จะถูกออกแบบมาในรูปแบบกว้าง ๆ เพื่อสื่อถึงฟังก์ชัน
และ หน้าที่ของโปรแกรม ผู้เรียนจำเป็นที่จะต้องพัฒนาโปรแกรมให้มีความสมบูรณ์ทั้งในส่วนของชุดคำสั่ง
(เช่น การตั้งชื่อตัวแปร ฟังก์ชันที่สื่อความหมาย, การไม่ใช้งานคำสั่งซ้ำซ้อนจนเกินไป, การเว้นวรรค เว้นบรรทัดที่เป็นระเบียบ) และ การที่ทำให้ผู้ใช้งานเข้าใจ / ใช้งานโปรแกรมได้ง่าย (เช่น มีการระบุว่าจะต้อง Input อะไรเข้าไป และ Output อะไรออกมา) ทั้งหมดนี้เพื่อจำลอง และ สร้างลักษณะการทำงานที่เป็นพื้นฐานที่ดีต่อไป

*การส่งโปรแกรมของ Exercise ให้ผู้เรียนใช้ Github ในการเก็บโปรแกรมแล้วทำการ
Comment ลิงค์ของโปรแกรมลงใต้คลิปวิดีโอเพื่อส่ง Exercise ได้เลย
'''

usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "Ai234" and passwordInput == "00St69":
    print("Login Successful !")
    print("--------------------------------")
    print("Welcome to idShop !")
    print("--------------------------------")
    print("รายชื่อสินค้า")
    print("รหัสสินค้า", "รายชื่อสินค้า  ", "ราคาต่อสินค้า (THB)")
    price1 = 1200
    price2 = 300
    price3 = 450
    price4 = 990
    print("A001   ", "กระเป๋าเดินทาง", price1)
    print("A002   ", "ผ้าห่ม        ", price2)
    print("A003   ", "รองเท้า      ", price3)
    print("A004   ", "ชุดปฐมพยาบาล ", price4)
    print("--------------------------------")
    idProductInput = input("รหัสสินค้า : ")
    if idProductInput == "A001":
        numProductInput = int(input("จำนวนสินค้า : "))
        product1price = numProductInput * price1
        print("รวมราคาสุทธิ (THB) :", product1price)
    elif idProductInput == "A002":
        numProductInput = int(input("จำนวนสินค้า : "))
        product2price = numProductInput * price2
        print("รวมราคาสุทธิ (THB) :", product2price)
    elif idProductInput == "A003":
        numProductInput = int(input("จำนวนสินค้า : "))
        product3price = numProductInput * price3
        print("รวมราคาสุทธิ (THB) :", product3price)
    elif idProductInput == "A004":
        numProductInput = int(input("จำนวนสินค้า : "))
        product4price = numProductInput * price4
        print("รวมราคาสุทธิ (THB) :", product4price)
        print("--------------------------------")
    else:
        print("รหัสสินค้าไม่ถูกต้อง")
    vat = 7/100
    if idProductInput == "A001":
        vatPrice = product1price * vat
        print("รวมทั้งหมด (THB) :", product1price + vatPrice)
    elif idProductInput == "A002":
        vatPrice = product2price * vat
        print("รวมทั้งหมด (THB) :", product2price + vatPrice)
    elif idProductInput == "A003":
        vatPrice = product3price * vat
        print("รวมทั้งหมด (THB) :", product3price + vatPrice)
    elif idProductInput == "A004":
        vatPrice = product4price * vat
        print("รวมทั้งหมด (THB) :", product4price + vatPrice)
    print("--------------------------------")
    if idProductInput == "A001" or idProductInput == "A002" or idProductInput == "A003" or idProductInput == "A004":
        print("โปรดชำระเงินภายใน 30 นาที")
    else:
        print("โปรดกรอกรหัสสินค้าใหม่")
else:
    print("Login Failed !")
