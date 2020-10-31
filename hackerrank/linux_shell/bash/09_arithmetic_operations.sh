read exp
printf %.3f $(echo "scale=5; $exp" | bc -l)