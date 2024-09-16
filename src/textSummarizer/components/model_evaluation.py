from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from datasets import load_dataset, load_from_disk, load_metric
import torch
import pandas as pd
from tqdm import tqdm
import evaluate
from src.textSummarizer.entity import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self,config : ModelEvaluationConfig):
        self.config = config

    def generate_batch_sized_chunks(self,list_of_elements,batch_size):
        for i in range(0,len(list_of_elements),batch_size):
            yield list_of_elements[i:i+batch_size]
    
    def calculate_metric_on_test_ds(self,dataset,metric,model,tokenizer,
                               batch_size=16,device="cuda",
                               column_text="article",
                               column_summary="highlights"):
        article_batches = list(self.generate_batch_sized_chunks(dataset[column_text],batch_size))
        target_batches = list(self.generate_batch_sized_chunks(dataset[column_summary],batch_size))

        for article_batch, target_batch in tqdm(zip(article_batches,target_batches)):
            inputs = tokenizer(article_batch,max_length=1024,truncation=True,  #generates token for each word
                            padding="max_length",return_tensors="pt")

            summaries = model.generate(input_ids=inputs["input_ids"].to(device),
                                    attention_mask=inputs["attention_mask"].to(device),  # genrated word tokens from decoder side 
                                    length_penalty=0.8,num_beams=8,max_length=128)

            decoded_summaries = [tokenizer.decode(s,skip_special_tokens=True,           # converts tokens to words
                                                clean_up_tokenization_spaces=True)
                                for s in summaries]

            decoded_summaries = [d.replace("", " ") for d in decoded_summaries]

            metric.add_batch(predictions=decoded_summaries,references=target_batch)
        score = metric.compute()
        return score
    

    def evaluate(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path).to(device)

        data_samsum_pt = load_from_disk(self.config.data_path)

        rough_names = ["rouge1","rouge2","rougeL","rougeLsum"]

        rough_metric = evaluate.load('rouge')

        score = self.calculate_metric_on_test_ds(
            dataset = data_samsum_pt['test'][0:1],
            metric = rough_metric,
            model = model_pegasus,
            tokenizer = tokenizer,
            batch_size = 4,
            device = device,
            column_text = "dialogue",
            column_summary = "summary"
        )

        rough_dict = dict((rn,score[rn]) for rn in rough_names)

        df = pd.DataFrame(rough_dict,  index = ['pegasus'])
        df.to_csv(self.config.metric_file_name,index=False)