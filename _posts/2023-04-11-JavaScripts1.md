---
layout: single
title: " JavaScript 1일차 "
categories: keduit
tags: [ JavaScript, ]
toc: true 
comments: true
author_profile: true
sidebar:
    nav: "docs"
---

# Javascript

## 기본 용어

* 표현식 : 값을 만들어 내는 간단한 코드.
* 문장 : 프로그래밍 언어에 실행할 수 있는 코드의 최소 단위.
* 종결 : 문장 마지막에 ; 또는 줄바꿈.

* 숫자와 문자의 차이 : 문자가 되면 연산에 참여할 수 없다.

```
273 : 연산 참여 O
'273' : 문자로써, 연산 참여 X
```

* 키워드 : 자바스크립트를 처음 만들 때 정해진 특별한 의미가 부여된 단어.

```
break, else, instanceof, true, case, false
new, try, catch, finally, null, typeof
continue, for, return, var, default, function
switch, void, delete, if, this, while, do
in, throw, with, const, class
```

* 식별자 : 바바스크립트에서 변수나 함수 등에 이름을 붙일 때 사용하는 단어.

```
# 식별자 생성 규칙

- 키워드를 사용X
- 특수 문자는 _과 $만 허용.
- 숫자로 시작 X
- 공백 입력 X

- 생성자 함수 이름은 항상 대문자로 시작.
- 변수, 인스턴스, 함수, 메서드의 이름은 항상 소문자로 시작.
- 여러 단어로 된 식별자는 각 단어의 첫 글자를 대문자로 한다.
```

```
Num = 273  => num에다가 273을 넣어라 라는뜻.
컴퓨터언어에서의 =  넣어라.
컴퓨터언어에서의 같다라는 뜻은 == 으로 사용.
```

### 자바스크립트 출력 연습

* 가장 기본적인 출력 방법 중 하나인 ALERT() 함수를 사용해 웹 브라우저에 경고 창을 띄우기.

```
