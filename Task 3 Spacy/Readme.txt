Task 3 Usnig Spacy 3.0
There are many models available in Spacy 3.0 for custom training,
I have chosen en_core_web_sm. It is a small model and trains relativly fast.
To produce better results bigger and pre-trained transformer based models can be used.

To re-train model:
 1. provide paths for data files in first cell.
 2. keep the base_config.cfg in your working directory if you plan to retrain the model.
To predict:
 1. provide "\content\ner_demo\training\model-best" path to the prediction function.
 2. The function will load the saved trained model from the directory.
 3. Input the sentence on which you desire NER. 
 4. Voila, there is no step 4. :P