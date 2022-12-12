hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar \
-files ./hadoop_python/scripts/exercise_1/mapper.py,./hadoop_python/scripts/exercise_1/reducer.py \
-mapper ./hadoop_python/scripts/exercise_1/mapper.py \
-reducer ./hadoop_python/scripts/exercise_1/reducer.py \
-input ./hadoop_python/data/casoDePruebaEJ1.txt \
-output ./hadoop_python/outputs/exercise_1