#음료수의 갯수는 무작위로 입력한다 (음료수의 재고)
stock=[2,4,4,3,3,7,5,2,8,7,3,2,5,8,2,4,1,6,3,5,5]
#자판기가 판매중인 음료수의 종류를 리스트로 입력한다
goods=["코카콜라","스프라이트","오렌지","사과","코코팜 화이트","순수 (물)","옥수수 수염차","토레타","씨그램","메론소다","자몽소다","알로에","파워에이드","코코팜","식혜","조지아 카페","조지아 S","카페라떼","조지아 L","유자차","닥터페퍼"]
#음료수의 가격을 입력한다
price=[1000,600,500,500,700,500,1000,1300,1000,1000,1000,1000,1000,700,700,500,500,500,700,700,1000]
money=0 #아직 금액이 투입되지 않은 상태이므로 0으로 둔다
want=0 

def viewMenu():
    print("┌---------------------------------------┐")
    print("│   한국산업기술대학교 E동 5층 자판기   │")
    print("│1.   코카콜라  ",price[0],"원 (남은 갯수:",stock[0],")│")
    print("│2.  스프라이트  ",price[1],"원 (남은 갯수:",stock[1],")│")
    print("│3.    오렌지    ",price[2],"원 (남은 갯수:",stock[2],")│")
    print("│4.     사과     ",price[3],"원 (남은 갯수:",stock[3],")│")
    print("│5. 코코팜 화이트",price[4],"원 (남은 갯수:",stock[4],")│")
    print("│6.  순수 (물)   ",price[5],"원 (남은 갯수:",stock[5],")│")
    print("│7. 옥수수수염차",price[6],"원 (남은 갯수:",stock[6],")│")
    print("│8.    토레타   ",price[7],"원 (남은 갯수:",stock[7],")│")
    print("│9.    씨그램   ",price[8],"원 (남은 갯수:",stock[8],")│")
    print("│10.    메론    ",price[9],"원 (남은 갯수:",stock[9],")│")
    print("│11.    자몽    ",price[10],"원 (남은 갯수:",stock[10],")│")
    print("│12.   알로에   ",price[11],"원 (남은 갯수:",stock[11],")│")
    print("│13. 파워에이드 ",price[12],"원 (남은 갯수:",stock[12],")│")
    print("│14.   코코팜    ",price[13],"원 (남은 갯수:",stock[13],")│")
    print("│15.    식혜     ",price[14],"원 (남은 갯수:",stock[14],")│")
    print("│16. 조지아 카페 ",price[15],"원 (남은 갯수:",stock[15],")│")
    print("│17.  조지아 S   ",price[16],"원 (남은 갯수:",stock[16],")│")
    print("│18.  카페라떼   ",price[17],"원 (남은 갯수:",stock[17],")│")
    print("│19.  조지아 L   ",price[18],"원 (남은 갯수:",stock[18],")│")
    print("│20.   유자차    ",price[19],"원 (남은 갯수:",stock[19],")│")
    print("│21.  닥터페퍼  ",price[20],"원 (남은 갯수:",stock[20],")│")
    print("└---------------------------------------┘")

viewMenu()

while True :
    for i in range (0, 19) :
        if money >= price[i] :
            print(i+1,"번",goods[i],"구매가능")
            
    if money < 500 :
        print("구매 가능한 상품이 없습니다. 현금을 투입해 주세요.")

        print("현재 잔액 :",money,"원")
        print("1번 메뉴 : 메뉴 보기")
        print("2번 메뉴 : 금액 투입")
        print("3번 메뉴 : 상품 선택")
        print("4번 메뉴 : 잔돈 반환")
        print("9번 메뉴 : 사용 종료")

    menu = int(input("원하시는 기능을 입력하여 주세요. (ex. 현금 투입 -> \'2\' 입력)"))

    if menu == 1:
        viewMenu()

    elif menu == 2 :
        inputMoney = int(input("투입할 현금을 입력해주세요."))

        if inputMoney < 10 :
            print("10원 미만의 금액은 투입되지 않습니다.")
            inputMoney = 0

        elif inputMoney >= 10 :
            money += inputMoney

    elif menu == 3 :
        want = int(input("구매하실 음료의 번호를 입력하세요. (ex. 코카콜라 -> \'1\' 입력)"))
        want = want - 1
        if money >= price[want] :
            print("선택하신",goods[want],"가(이) 나왔습니다. 배출구를 확인하여 주세요.")
            stock[want] = stock[want] - 1
            money = money - price[want]

        elif price[want] > money :
            print("잔액이 부족합니다.")

    elif menu == 4:
        fiveHundred = int(money // 500)
        oneHundred = int((money % 500)//100)
        fifty = int(((money % 500) % 100) // 50)
        ten = int((((money % 500) % 100) % 50) // 10)
        print("잔돈",money,"원이 반환되었습니다. 배출구를 확인하여 주세요.")
        print("500원 :",fiveHundred,"개, 100원:",oneHundred,"개, 50원:",fifty,"개, 10원:",ten,"개")
        money = 0
        print("현재 투입금액은",money,"원 입니다.")

    elif menu == 9:
        print("이용해주셔서 감사합니다. - E동 5층 자판기")
        break

    else :
        print("ERROR! 잘못된 명령입니다.")
            
            
            
