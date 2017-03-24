1. Clone Repo  
2. CD to the repo directory  
cp .env.sh.template .env 
modify and supply the environment variables  


3. if you want to just run the container  
follow login instructions at https://github.com/Qubeship/qube_base_python/blob/master/login-instructions.md and proceed to step 5.  


4. Build  & Bake  
scripts/docker-builder.sh  
scripts/bake.sh  

5. Run  
scripts/run.sh  

6. Create a new module
python -m qube_cli.src.qube repo create --organization Qubeship --name api_notifications --base https://github.com/qubeship/qube_base_python.git --token  --github_base https://github.com --sonar_reporting_key NOTI
python -m qube_cli.src.qube repo create --organization Qubeship --name api_auth --base https://github.com/qubeship/qube_base_python.git --token 3396c6cd4cb13a29063ce97007a0b43826b6b508 --github_base https://github.com --sonar_reporting_key AUTH --language python


## extra info 
to run sonar, flake , pylint
https://github.com/Qubeship/qube_base_python/blob/master/sonar-flake-pylint.md






