# car-plate-number-extracter

## 주요 확인 사항

### easyocr 을 통한 텍스트 추출

- easyocr 을 통해 추출한 텍스트는 array 형태로 값을 추출한다. 이때 detail 파라미터를 `0`으로 주어 추출된 텍스트 값 만을 획득한다.

### 자동차 번호판 유형 텍스트 추출
- 정규식을 통해 번호판을 얻을 수 있다.

> 주의사항: 추출된 텍스트에서 의도치 않는 blank 나 특수문자가 포함될 수 있음으로 한번 필터링을 필요로하여 처리한후 번호판 텍스트를 추추할 수 있게끔 하였다.
