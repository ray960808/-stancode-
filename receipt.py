"""
File: receipt.py
Name:Ray
-------------------------
這是利用前面的範例外加設計收據系統
"""


def main():
   customer_name = input("請輸入顧客英文姓名:")
   """
   這邊利用前面hello_world.py的基礎
   建立一個名稱系統
   """
   items = []
   """
   利用列表來使多項商品得以藉由詢問列出收據所需的內容
   """
   while True:
       name = input("商品英文名稱（輸入 q 結束）：")
       if name == 'q':
           break
       price = float(input("單價：(請輸入數字)"))
       quantity = int(input("數量：(請輸入數字)"))

       items.append((name, price, quantity))

   print("\n====== 收據 ======")
   print(f"顧客姓名：{customer_name}")

   total = 0
   """
   歸零價值
   """
   for name, price, quantity in items:
       subtotal = price * quantity
       total += subtotal
       print(f"{name} x {quantity} = {subtotal}")

   print("-----------------")
   print(f"總金額：{total}")


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
