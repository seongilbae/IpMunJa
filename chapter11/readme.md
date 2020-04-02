opcode.txt는 정상파일에서 추출한 것과 악성코드에서 추출한 것 두 가지가 있기 때문에 opcode_malware.txt, opcode_benign.txt로 구분해놨습니다.

opcode.txt가 opcode_malware.txt, opcode_benign.txt이므로 착오가 길 바랍니다.

parsing.py 코드는 그대로 사용하시면 opcode.txt를 파싱한 것처럼 정상파일과 악성코드의 opcode를 하나의 result.csv 파일로 생성합니다.

나머지는 동일하기 때문에 그대로 사용하시면 됩니다. 
