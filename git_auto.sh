
## using this you can automate your git actions..happy GITTING!!

git status

if [ -z "$1"]; then
	echo "Usage: ./git_auto.sh \"Your commit message\""
	exit 1
fi

git add -A
git status
git commit -m "$1"
git push -u origin master
git status

