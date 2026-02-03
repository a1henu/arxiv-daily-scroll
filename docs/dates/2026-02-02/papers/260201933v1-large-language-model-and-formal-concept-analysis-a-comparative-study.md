---
layout: default
title: Large Language Model and Formal Concept Analysis: a comparative study for Topic Modeling
---

# Large Language Model and Formal Concept Analysis: a comparative study for Topic Modeling
**arXiv**：[2602.01933v1](https://arxiv.org/abs/2602.01933) · [PDF](https://arxiv.org/pdf/2602.01933.pdf)  
**作者**：Fabrice Boissier, Monica Sen, Irina Rychkova  

**一句话要点**：比较大语言模型与形式概念分析在主题建模中的性能与适用性

**关键词**：主题建模, 大语言模型, 形式概念分析, 零样本学习, 文本处理

## 3 点简述
- 核心问题：评估LLM和FCA在主题建模任务中的有效性，缺乏实际应用案例研究
- 方法要点：使用GPT-5进行零样本提示策略，对比CREA管道中的FCA方法
- 实验或效果：通过教学材料和信息系统研究文章数据集，分析提取主题的准确性

## 摘要（原文）

> Topic modeling is a research field finding increasing applications: historically from document retrieving, to sentiment analysis and text summarization. Large Language Models (LLM) are currently a major trend in text processing, but few works study their usefulness for this task. Formal Concept Analysis (FCA) has recently been presented as a candidate for topic modeling, but no real applied case study has been conducted. In this work, we compare LLM and FCA to better understand their strengths and weakneses in the topic modeling field. FCA is evaluated through the CREA pipeline used in past experiments on topic modeling and visualization, whereas GPT-5 is used for the LLM. A strategy based on three prompts is applied with GPT-5 in a zero-shot setup: topic generation from document batches, merging of batch results into final topics, and topic labeling. A first experiment reuses the teaching materials previously used to evaluate CREA, while a second experiment analyzes 40 research articles in information systems to compare the extracted topics with the underling subfields.

