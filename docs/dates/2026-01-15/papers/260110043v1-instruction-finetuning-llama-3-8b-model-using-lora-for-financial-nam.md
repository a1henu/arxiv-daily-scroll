---
layout: default
title: Instruction Finetuning LLaMA-3-8B Model Using LoRA for Financial Named Entity Recognition
---

# Instruction Finetuning LLaMA-3-8B Model Using LoRA for Financial Named Entity Recognition
**arXiv**：[2601.10043v1](https://arxiv.org/abs/2601.10043) · [PDF](https://arxiv.org/pdf/2601.10043.pdf)  
**作者**：Zhiming Lian  

**一句话要点**：提出结合指令微调与LoRA的LLaMA-3-8B模型，用于金融命名实体识别任务。

**关键词**：金融命名实体识别, 指令微调, LoRA, LLaMA-3-8B, 参数高效微调

## 3 点简述
- 金融NER中，免费大模型常混淆实体类型或忽略关键信息，如金额。
- 采用指令微调与LoRA，将标注句子转为指令-输入-输出三元组，仅更新低秩矩阵参数。
- 在1,693句语料上，微F1达0.894，优于多个基线模型，实现领域敏感NER的先进性能。

## 摘要（原文）

> Particularly, financial named-entity recognition (NER) is one of the many important approaches to translate unformatted reports and news into structured knowledge graphs. However, free, easy-to-use large language models (LLMs) often fail to differentiate organisations as people, or disregard an actual monetary amount entirely. This paper takes Meta's Llama 3 8B and applies it to financial NER by combining instruction fine-tuning and Low-Rank Adaptation (LoRA). Each annotated sentence is converted into an instruction-input-output triple, enabling the model to learn task descriptions while fine-tuning with small low-rank matrices instead of updating all weights. Using a corpus of 1,693 sentences, our method obtains a micro-F1 score of 0.894 compared with Qwen3-8B, Baichuan2-7B, T5, and BERT-Base. We present dataset statistics, describe training hyperparameters, and perform visualizations of entity density, learning curves, and evaluation metrics. Our results show that instruction tuning combined with parameter-efficient fine-tuning enables state-of-the-art performance on domain-sensitive NER.

