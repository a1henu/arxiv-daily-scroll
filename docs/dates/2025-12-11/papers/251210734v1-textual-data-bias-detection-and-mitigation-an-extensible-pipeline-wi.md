---
layout: default
title: Textual Data Bias Detection and Mitigation - An Extensible Pipeline with Experimental Evaluation
---

# Textual Data Bias Detection and Mitigation - An Extensible Pipeline with Experimental Evaluation
**arXiv**：[2512.10734v1](https://arxiv.org/abs/2512.10734) · [PDF](https://arxiv.org/pdf/2512.10734.pdf)  
**作者**：Rebekka Görge, Sujan Sai Gannamaneni, Tabea Naeven, Hammam Abdelwahab, Héctor Allende-Cid, Armin B. Cremers, Lennard Helmer, Michael Mock, Anna Schmitz, Songkai Xue, Elif Yildirir, Maximilian Poretschkin, Stefan Wrobel  

**一句话要点**：提出可扩展的文本数据偏见检测与缓解管道，用于减少大语言模型训练数据中的偏见。

**关键词**：文本数据偏见检测, 偏见缓解管道, 大语言模型去偏见, 表示偏见量化, 刻板印象过滤, 数据增强

## 3 点简述
- 核心问题：文本数据存在表示偏见和刻板印象，缺乏实践指导以符合法规要求。
- 方法要点：基于LLM生成词表检测群体标签，量化表示偏见，过滤刻板印象，并通过数据增强补偿偏见。
- 实验或效果：在性别、宗教和年龄示例中验证了数据去偏见效果，但模型微调后偏见基准表现不一致。

## 摘要（原文）

> Textual data used to train large language models (LLMs) exhibits multifaceted bias manifestations encompassing harmful language and skewed demographic distributions. Regulations such as the European AI Act require identifying and mitigating biases against protected groups in data, with the ultimate goal of preventing unfair model outputs. However, practical guidance and operationalization are lacking. We propose a comprehensive data bias detection and mitigation pipeline comprising four components that address two data bias types, namely representation bias and (explicit) stereotypes for a configurable sensitive attribute. First, we leverage LLM-generated word lists created based on quality criteria to detect relevant group labels. Second, representation bias is quantified using the Demographic Representation Score. Third, we detect and mitigate stereotypes using sociolinguistically informed filtering. Finally, we compensate representation bias through Grammar- and Context-Aware Counterfactual Data Augmentation. We conduct a two-fold evaluation using the examples of gender, religion and age. First, the effectiveness of each individual component on data debiasing is evaluated through human validation and baseline comparison. The findings demonstrate that we successfully reduce representation bias and (explicit) stereotypes in a text dataset. Second, the effect of data debiasing on model bias reduction is evaluated by bias benchmarking of several models (0.6B-8B parameters), fine-tuned on the debiased text dataset. This evaluation reveals that LLMs fine-tuned on debiased data do not consistently show improved performance on bias benchmarks, exposing critical gaps in current evaluation methodologies and highlighting the need for targeted data manipulation to address manifested model bias.

