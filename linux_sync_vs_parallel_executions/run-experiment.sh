
for i in {1..10};
do
  time find ./* -maxdepth 0 -type d -exec git -C {} pull \;
done

for i in {1..10};
do
  time find ./* -maxdepth 0 -type d | parallel git -C {} pull
done
