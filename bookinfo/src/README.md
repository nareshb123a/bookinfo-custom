Custom changes:
---------------
[root@ip-172-31-36-236 productpage-custom-files]# ls
productpage.html  productpage.py
[root@ip-172-31-36-236 productpage-custom-files]# kubectl create cm productpage-html --from-file=./productpage.html
configmap/productpage-html created
[root@ip-172-31-36-236 productpage-custom-files]# kubectl create cm productpage --from-file=./productpage.py
configmap/productpage created

