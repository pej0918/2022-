# 2022_Hanium_Project
## 우리 동네산불지키미

### 웹 화면

1. 메인화면
    - 웹페이지의 첫 화면으로 산 검색 창 구현
    - 상단 메뉴바를 통해 원하는 서비스를 클릭하면 바로 이동할 수 있도록 구현
    
    ![Untitled (6)](https://github.com/pej0918/2022_Hanium_Project/assets/79118751/075455e3-0ce8-43a8-b658-62fbe8cdf338)

    
2.  산 정보 전달 화면
    - 산 위치를 보여주는 대시보드 구현
        - 데이터 : 카카오 지도  API
    - 날씨 정보와 특정 산에 대한 산불위험지수 보여주는 대시보드 구현
        - 데이터: 산불위험지수 API ( 크롤링하여 DB에 저장)
        - 산악기상관측시스템 ( 크롤링하여 DB에 저장)
    
    ![Untitled (7)](https://github.com/pej0918/2022_Hanium_Project/assets/79118751/ffb7fa18-2972-4dbf-ab33-2cee40d4b1cc)
    

1. 산불 발생 피해 정보 제공 화면
    - 예상 피해 면적을 나타내는 대시보드 구현
        - 데이터 : 과거 산불 데이터(DB에 저장)
        - 알고리즘 : Ridge regression
    - 산불 피해 예방방법에 대한 안내 대시보드 구현
    
    ![Untitled (8)](https://github.com/pej0918/2022_Hanium_Project/assets/79118751/07d56a20-4a46-4f5e-a0c6-e6331cdf598f)



    ![Untitled (9)](https://github.com/pej0918/2022_Hanium_Project/assets/79118751/2789e703-370a-4bc6-ada9-587703922752)

    
3.  산불 위험 지역 정보 제공 화면
    - 강원도의 모든 지역에 대한 산불 위험지수를 보여주는 대시보드 구현
        - 데이터 : 산불위험지수 API (크롤링하여 DB에 저장)
    - 산불위험지수 개념 설명 대시보드를 구현
    - 원하는 지역의 산불위험지수를 볼 수 있도록 검색창 구현
    
    ![Untitled (10)](https://github.com/pej0918/2022_Hanium_Project/assets/79118751/60a4b042-22c0-4318-8cc5-e406857d2c1a)

    
4.  주변 소방서 정보 제공 화면
    - 인근 소방서의 위치와 세부 정보를 보여주는 대시보드 구현
        - 데이터 : 소방서 데이터 (DB에 저장)
        
        ![Untitled (11)](https://github.com/pej0918/2022_Hanium_Project/assets/79118751/1f00a5a4-fac5-4119-8926-b6ea0c7bdd29)

        
5.  과거 산불 통계 시각화 제공 화면
    - 과거 산불 데이터를 기반으로 웹 사용자가 한눈에 알아보기 쉽게끔 시각화하여 보여주는 대시보드 구현
        - 데이터 : 과거 산불 데이터(DB에 저장)
    
    ![Untitled (12)](https://github.com/pej0918/2022_Hanium_Project/assets/79118751/7bb7949b-d5dc-4ab1-92b4-90c0d896f2ab)


### 결과물 및 결과

- 입선

![Untitled (13)](https://github.com/pej0918/2022_Hanium_Project/assets/79118751/2e471ed3-ddfa-490a-b049-4553d204b9b3)
