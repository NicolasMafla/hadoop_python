hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar \
-files ./hadoop_python/scripts/exercise_2/mapper.py,./hadoop_python/scripts/exercise_2/reducer.py \
-mapper ./hadoop_python/scripts/exercise_2/mapper.py \
-reducer ./hadoop_python/scripts/exercise_2/reducer.py \
-input ./hadoop_python/data/cite75_99.txt -output ./hadoop_python/outputs/exercise_2