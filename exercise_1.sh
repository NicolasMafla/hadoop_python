hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar \
-D stream.map.output.field.separator="\t" \
-D stream.num.map.output.key.fields=2 \
-files ./hadoop_python/scripts/exercise_1/mapper.py,./hadoop_python/scripts/exercise_1/reducer.py,./hadoop_python/scripts/exercise_1/combiner.py \
-mapper ./hadoop_python/scripts/exercise_1/mapper.py \
-combiner ./hadoop_python/scripts/exercise_1/combiner.py \
-reducer ./hadoop_python/scripts/exercise_1/reducer.py \
-input ./hadoop_python/data/casoDePruebaEJ1.txt \
-output ./hadoop_python/outputs/exercise_1