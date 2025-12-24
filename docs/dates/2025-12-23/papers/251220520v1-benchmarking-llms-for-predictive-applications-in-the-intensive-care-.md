---
layout: default
title: Benchmarking LLMs for Predictive Applications in the Intensive Care Units
---

# Benchmarking LLMs for Predictive Applications in the Intensive Care Units
**arXiv**：[2512.20520v1](https://arxiv.org/abs/2512.20520) · [PDF](https://arxiv.org/pdf/2512.20520.pdf)  
**作者**：Chehak Malhotra, Mehak Gopal, Akshaya Devadiga, Pradeep Singh, Ridam Pal, Ritwik Kashyap, Tavpritesh Sethi  

**一句话要点**：比较LLMs与SLMs在ICU休克预测中的性能，发现两者表现相当。

**关键词**：重症监护预测, 大型语言模型, 休克指数, MIMIC III数据库, 类别不平衡处理, 临床轨迹预测

## 3 点简述
- 核心问题：评估LLMs在ICU临床事件预测任务中的有效性，对比传统SLMs。
- 方法要点：使用MIMIC III数据库数据，微调GatorTron-Base、Llama 8B、Mistral 7B等模型，采用焦点和交叉熵损失处理类别不平衡。
- 实验或效果：GatorTron-Base加权召回率最高达80.5%，但LLMs整体性能未显著优于SLMs，提示需关注临床轨迹预测。

## 摘要（原文）

> With the advent of LLMs, various tasks across the natural language processing domain have been transformed. However, their application in predictive tasks remains less researched. This study compares large language models, including GatorTron-Base (trained on clinical data), Llama 8B, and Mistral 7B, against models like BioBERT, DocBERT, BioClinicalBERT, Word2Vec, and Doc2Vec, setting benchmarks for predicting Shock in critically ill patients. Timely prediction of shock can enable early interventions, thus improving patient outcomes. Text data from 17,294 ICU stays of patients in the MIMIC III database were scored for length of stay > 24 hours and shock index (SI) > 0.7 to yield 355 and 87 patients with normal and abnormal SI-index, respectively. Both focal and cross-entropy losses were used during finetuning to address class imbalances. Our findings indicate that while GatorTron Base achieved the highest weighted recall of 80.5%, the overall performance metrics were comparable between SLMs and LLMs. This suggests that LLMs are not inherently superior to SLMs in predicting future clinical events despite their strong performance on text-based tasks. To achieve meaningful clinical outcomes, future efforts in training LLMs should prioritize developing models capable of predicting clinical trajectories rather than focusing on simpler tasks such as named entity recognition or phenotyping.

