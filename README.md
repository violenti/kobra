## Kobra 

A simple tool for search DNS registers. 


## Instalation

You just Python3 :snake: and pipenv

`pipenv install `

## Usage


Short Form    | Long Form     | Description
------------- | ------------- |-------------
-i            | --input      | file from will your list with domain
-r            | --resolver  | dns server for resolver
-t            | --type      | type of dns records


Create a file with the domains that like know the register .

Execute for example:

```
python3 kobra.py -i domain.txt -r 8.8.8.8 -t cname

```

You could create a file of domains and subdomains with a tool like [Sublist3r](https://github.com/aboul3la/Sublist3r)


## Feature :hammer_and_wrench:	 and Bug report :bug:

You can do create an [issue](https://github.com/violenti/kobra/issues), please with as much as information.  

## License

[LICENSE](https://github.com/violenti/kobra/blob/master/LICENSE)
