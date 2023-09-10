# 2022_Hanium_Project
우리 동네산불지키미
**웹 화면**

1. 메인화면
    - 웹페이지의 첫 화면으로 산 검색 창 구현
    - 상단 메뉴바를 통해 원하는 서비스를 클릭하면 바로 이동할 수 있도록 구현
    
    ![Uploading Untitled (6).png…]()

    
2.  산 정보 전달 화면
    - 산 위치를 보여주는 대시보드 구현
        - 데이터 : 카카오 지도  API
    - 날씨 정보와 특정 산에 대한 산불위험지수 보여주는 대시보드 구현
        - 데이터: 산불위험지수 API ( 크롤링하여 DB에 저장)
        - 산악기상관측시스템 ( 크롤링하여 DB에 저장)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/63bb0fb7-317a-4dfc-8c90-839adddff6cc/Untitled.png)
    

1. 산불 발생 피해 정보 제공 화면
    - 예상 피해 면적을 나타내는 대시보드 구현
        - 데이터 : 과거 산불 데이터(DB에 저장)
        - 알고리즘 : Ridge regression
    - 산불 피해 예방방법에 대한 안내 대시보드 구현
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/92402a2a-a53b-4dd7-9cb5-59bcfb8906e5/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/33b50dc9-f5bd-4b0e-9e4b-03a56cf01476/Untitled.png)
    
2.  산불 위험 지역 정보 제공 화면
    - 강원도의 모든 지역에 대한 산불 위험지수를 보여주는 대시보드 구현
        - 데이터 : 산불위험지수 API (크롤링하여 DB에 저장)
    - 산불위험지수 개념 설명 대시보드를 구현
    - 원하는 지역의 산불위험지수를 볼 수 있도록 검색창 구현
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fd9011f3-fdf9-414d-815a-27d47b12530c/Untitled.png)
    
3.  주변 소방서 정보 제공 화면
    - 인근 소방서의 위치와 세부 정보를 보여주는 대시보드 구현
        - 데이터 : 소방서 데이터 (DB에 저장)
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/38cd6720-74b3-41b3-a053-dc4c6b3aa436/Untitled.png)
        
4.  과거 산불 통계 시각화 제공 화면
    - 과거 산불 데이터를 기반으로 웹 사용자가 한눈에 알아보기 쉽게끔 시각화하여 보여주는 대시보드 구현
        - 데이터 : 과거 산불 데이터(DB에 저장)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d8f0b62a-e143-43ad-8565-b4260a0f69eb/Untitled.png)
    

### 결과물 및 결과

- 입선

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/19990e5a-479b-4ad1-b3e8-09603049b880/Untitled.png)

### 성과물 등록

- 우리가 구현한 ‘우리 동네 산불지키미’ 웹페이지를 저작권 등록을 진행하였다
    
    [접수증.pdf](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/afcfe166-05e4-4c2e-ae4f-a18a9b5d5d5e/%EC%A0%91%EC%88%98%EC%A6%9D.pdf)
    
    ![CB36AB67-609D-49E9-AD6B-0D3F34F074F2.jpeg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e68a26ac-d78f-4ea4-91bb-6ec5aac2efdc/CB36AB67-609D-49E9-AD6B-0D3F34F074F2.jpeg)
    
    ![BB51A2BC-E940-44A6-BF2D-E8F8D229EE37.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/088b8466-edb3-4c44-976e-eb4a1f8910fc/BB51A2BC-E940-44A6-BF2D-E8F8D229EE37.png)
    
    ![A27879D1-C7D1-4C38-BC46-ECB61E1E0AAE.jpeg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6843ce0b-35c6-4580-93f4-2dc80e2f6042/A27879D1-C7D1-4C38-BC46-ECB61E1E0AAE.jpeg)
