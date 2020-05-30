# Kobra is a simple tool for find register dns 



You just Python 3 and run `pip -r requeriments.txt`

## USAGE


Short Form    | Long Form     | Description
------------- | ------------- |-------------
-i            | --input      | file from will your list with domain
-r            | --resolver  | dns name for resolver
-t            | --type      | type of dns records

Create a file with domains that like know the register .

Execute for example:

```
python3 kobra.py -i domain.txt -r 8.8.8.8 -t cname

```
You can get a file domains with your subdomains if use [Sublist3r](https://github.com/aboul3la/Sublist3r)

## LICENSE

[LICENSE] (https://github.com/violenti/kobra/blob/master/LICENSE)
