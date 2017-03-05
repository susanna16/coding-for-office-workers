# 클래스 class
    # C언어에서는 존재하지 않는 개념.
    # 많은 코드를 짠 후 쉽게 고칠 때 사용하는 것
    #

##### Article variables
title1="개발"
author1="Sujin"
content1="개발은 쉬워요"
view_count1=0

title2="코칭"
author2="Sujin"
content2="코칭은 쉬워요"
view_count2=0

title3="창업"
author3="Sujin"
content3="창업은 쉬워요"
view_count3=0

##### Article class : 클래스는 일반적으로 대문자로 시작함
# class Article:
#     title="개발"
#     author="Sujin"
#     content="개발은 쉬워요"
#     view_count=0
#
# article1=Article()
# print(article1.title)
# article2=Article()
# article2.title="코칭"
# print(article1.title)
# print(article2.title)


#article1이라는 변수를 만들고
# Article이라는 clss이름을 그대로 적고 ()하면
# 이 클래스에 해당하는 설계도면대로 객체를 만드는 것.
#객체를 만들었다는 것은
# 이 클래스에 정보를 담고 있는 접근가능한 변수를 만든 것
# 클래스를 활성화시켜준것 만으로도 4줄을 1줄로 처리 가능

##### Article class with __init__
class Article:
    author="Sujin"
    view_count=0

    def __init__(self, title, content):
        self.title=title
        self.content=content

    def read(self):
        self.view_count=self.view_count+1

# self는 클래스 안에 있는 변수에 접근을 하겠다는 약속
    # 클래스 안에서 만든 함수라는 것을 보여주기 위한 것
    # 클래스 안의 함수에 접근하기 위해 self가 필요
    #어떤 클래스의 객체(인스턴스)를 생성하려면 변수명=클래스명()
#__init__은 클래스 안에 내장된 함수
#직접 read함수를 만드는 것. 조회수를 증가할 때마다 표시하는 것.

article1=Article("개발", "개발은 쉬워요")
article2=Article("코칭", "코칭은 쉬워요")
article3=Article("창업", "창업은 쉬워요")
#
# print(article1.view_count)
# article1.read()
# print(article1.view_count)

##### Article class ingeritace 상속
class BrunchArticle(Article):
    source="브런치"

    def read(self):
        self.view_count=self.view_count+2
        #오버라이드했다. 부모가 가진 함수를 그대로 이용하지만
        # 새로 정의할 경우 새로정의한 내용을 반영

brunch_article=BrunchArticle("개발", "개발은 쉬워요")
#활성화 시킨 것. 인스턴스
#그리고 __init__ 에 항상 해당하는 내용을 넣어줘야함.
print(brunch_article.title)
#부모클래스에서 입력한것이 나옴
print(brunch_article.source)
#새로 추가한 변수를 확인
print(brunch_article.view_count)
brunch_article.read()
print(brunch_article.view_count)
