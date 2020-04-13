# 파일 설명

## opcode_benign.txt
IDA Pro, IDAPython을 이용해 정상파일에서 추출한 opcode

## opcode_malware.txt
IDA Pro, IDAPython을 이용해 악성코드에서 추출한 opcode

## init.csv
사용되는 모든 opcode 리스트

## result.csv
init.csv, opcode_benign.txt, opcode_malware.txt를 하나로 모아 라벨링한 csv 파일
머신러닝 코드에 입력

## parser.py
opcode_benign.txt, opcode_malware.txt를 result.csv 파일로 만드는 파이썬 스크립트
조금 더 상세한 설명 
## MLcode.py
result.csv를 입력받아 머신러닝 학습 및 분류하는 파이썬 스크립트
