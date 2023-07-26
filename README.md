
### Build and run the docker image
```
docker build -t helloworld .
docker run --rm -d -p 5000:5000 helloworld
```
If the app isn't visible to the outside world, make sure it's listening on 0.0.0.0 (any interface), and not localhost or 127.0.0.1.  For Flask, `flask run -h 0.0.0.0` does the trick.

# Handy References
When I ran into issues with the deploy, these commands came in handy...

## Kubectl cheatsheet
```
$ alias k='kubectl --kubeconfig ~/.kube/apprenticeship.tr-lab-chhq-1.yaml'

$ k config set-context --current --namespace=bg-helloworld-reference-impl-ns

# Now I don't have to say "-n bg-helloworld-reference-impl-ns" after every command

$ k get pods
NAME                                       READY   STATUS    RESTARTS   AGE
reference-helloworld-wl-597c5744b4-wbwsc   1/1     Running   0          2m14s

$ k describe pod reference-helloworld-wl-597c5744b4-wbwsc 

$ k logs reference-helloworld-wl-597c5744b4-wbwsc --all-containers

```
This revealed the problem: `exec format error`.  The following command showed that my `helloworld` image was an `arm64` image.
```
docker inspect helloworld | grep -i arch
```
I needed to tell Docker on my M2 mac to build for the linux/amd64 platform, which I did using the `--platform=linux/amd64` option to the FROM directive in my Dockerfile.

