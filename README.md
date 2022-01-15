# Openfaas-kubernates project

--------------------------------------------------------------
 - 설치
   1. **arkade**
      1. `$ curl -sLS https://dl.get-arkade.dev | sh`
      2. `$ curl -sLS https://dl.get-arkade.dev | sudo sh`
   2. **kubectl**
      1. `$ arkade get kubectl`
   3. **kind**
      1. `$ arkade get kind`
   4. **faas-cli**
      1. `$ arkade get faas-cli`
   5. **kind-with-registry**
      1. `wget https://kind.sigs.k8s.io/examples/kind-with-registry.sh`
      2. `./kind-with-registry.sh`
   6. **openfaas**
      1. `arkade install openfaas`

---------------------------------------------------------------

 - 실행
   1. template 설치
      1. `faas-cli template store pull python3-flask`
   2. 함수 추가
      1. `faas-cli new 함수이름 --lang python3-flask-debian`
   3. docker 이미지 빌드
      1. `faas-cli build -f pydict.yml`
   4. 포트 포워딩
      1. `kubectl port-forward -n openfaas svc/gateway 8080:8080 `
   5. 어드민 정보
      1. `kubectl get secret -n openfaas basic-auth -o json`
      2. `base64 --decode; password`
   6. 배포
      1. `faas-cli deploy -f pydict.yml`
   7. 함수 추가 시
      1. `faas-cli up -f pydict.yml --filter=함수명`

---------------------------------------------------------------