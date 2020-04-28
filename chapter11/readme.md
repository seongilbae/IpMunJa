|번호|파일 명|설명|비고|
|:---:|:---:|:---:|:---:|
|#1|opcode_benign.txt<br>opcode_malware.txt|IDA Pro, IDA Python을 이용해 정상파일과 악성코드에서 추출한 opcode 텍스트 파일| - |
|#2|init.csv|사용되는 모든 opcode 리스트를 저장해둔 csv 파일| - |
|#3|result.csv|init.csv, opcode_benign.txt, opcode_malware.txt를 하나로 모아 라벨링한 csv 파일<br>머신러닝 코드에 입력 예정| - |
|#4|parser.py|opcode_benign.txt, opcode_malware.txt를 result.csv 파일로 만드는 파이썬 스크립트<br>opcode 텍스트 파일에서 ','를 기준으로 파싱을 해서 각각의 opcode들을 csv 파일에 입력| csv 파일이 아니어도 무관 |
|#5|MLcode.py|랜덤 포레스트, 서포트 벡터 머신, KNN 머신러닝 기법을 사용해 학습 및 분류하는 소스코드|trainingdata() 함수를 통해서 머신러닝 기법에 따른 학습 진행<br>predictdata() 함수를 통해서 각 머신러닝 기법으로 예측 진행|
