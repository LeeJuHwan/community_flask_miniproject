# community_flask_miniproject  
가상화 전 파일 공유  

# Windows Git Setting  
git clone https://github.com/LeeJuHwan/community_flask_miniproject.git  
cd community_flask_miniproject/flask_web  
python -m venv win_env  
activate_win.ps1    
pip install flask flask-wtf pymysql email_validator cryptography  
cd web_project  
(데이터 베이스 셋팅 - root/1111 데이터베이스이름:project)   
flask run  

# Branch Setting  

git branch [브랜치명]  
git checkout [브랜치명]  
git push --set-upstream origin [브랜치명]  


이후 개발하기...
