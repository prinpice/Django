# Settings

c9의 workspace에서 작성됨

### pyenv

* 다양한 버전의 파이썬을 관리하는 도구

* terminal에 pyenv, pyenv-virtualenv 설치

  ```git
  git clone https://github.com/pyenv/pyenv.git ~/.pyenv
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
  exec "$SHELL"
  
  git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
  echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
  exec "$SHELL"
  ```

  * `exec "$SHELL"` : reload (창을 껏다가 킨 것과 같은 기능)

### python 설치

* pyenv를 사용하여 원하는 버전 다운로드

  ```git
  $ pyenv install [version]
  ```

* 3.6 버전부터 fstring이 사용 가능함

* 현재 전역으로 설정되어 있는 버전 확인

  ```git
  $ python --version
  ```

* 원하는 버전을 설치해도 전역으로 바꿔주지 않으면 기존 버전을 사용하므로 전역 설정이 필요함

* 전역 설정

  ```git
  $ pyenv global [version]
  ```

* 정리하면

  ```git
  pyenv install 3.6.7
  pyenv global 3.6.7
  ```



### 프로젝트 생성 및 환경 설정

* (전체)폴더 == 프로젝트

* 프로젝트 진행할 폴더 생성 및 해당 폴더로 이동

  ```git
  $ mkdir [폴더이름]
  $ cd [폴더이름]
  ```

  * mkdir :  폴더를 생성하는 명령어
  * cd : 특정 위치로 이동하는 명령어

* 가상환경 생성 및 설정

  ```git
  $ pyenv virtualenv 3.6.7 [가상환경 이름]
  $ pyenv local [가상환경 이름]
  ```

  * pyenv virtualenv : 가상 환경 생성
  * pyenv local : 해당 디렉토리에 특정 가상환경을 지정함

* django 설치

  * python 3.6.7과 호환되는 django버전은 2.1.7이기 때문에 버전을 지정하여 설치함

  ```git
  $ pip install django==2.1.7
  ```

  