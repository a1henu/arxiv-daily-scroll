---
layout: default
title: Instruction Tuning of Large Language Models for Tabular Data Generation-in One Day
---

# Instruction Tuning of Large Language Models for Tabular Data Generation-in One Day
**arXiv**：[2511.23220v1](https://arxiv.org/abs/2511.23220) · [PDF](https://arxiv.org/pdf/2511.23220.pdf)  
**作者**：Milad Abdollahzadeh, Abdul Raheem, Zilong Zhao, Uzair Javaid, Kevin Yee, Nalam Venkata Abhishek, Tram Truong-Huu, Biplab Sikdar  

**一句话要点**：提出基于高质量指令数据集的指令调优方法，以有限资源提升LLM的表格数据生成能力。

**关键词**：表格数据生成, 指令调优, 大型语言模型, 有限资源训练, 高质量数据集

## 3 点简述
- 核心问题：现有表格指令调优研究多关注问答与推理，忽略表格数据生成任务。
- 方法要点：创建高质量表格指令数据集，对开源LLM进行指令调优，仅需7K指令和A100 GPU在6小时内完成。
- 实验或效果：调优后模型在表格数据生成性能上媲美GPT-4o，验证了资源有限下的可行性。

## 摘要（原文）

> Tabular instruction tuning has emerged as a promising research direction for improving LLMs understanding of tabular data. However, the majority of existing works only consider question-answering and reasoning tasks over tabular data, leaving tabular data generation largely unnoticed. In this work, for the first time, we explore the efficacy of instruction tuning in improving LLMs tabular data generation capabilities. More specifically, given the high data and computation requirements of tabular instruction tuning, we aim to address the possibility of instruction tuning for tabular data generation with limited data and computational resources. To achieve this, we first create a high-quality instruction dataset for tabular data, enabling efficient LLM comprehension. We then instruction-tune an open-source LLM (Llama3.1-8B-Instruct) on the training set of this dataset to improve its tabular data generation performance. Our experimental results show that by using our high-quality dataset and instruction-tuning on only 7K instructions with an A100 GPU, for less than 6 hours, we achieve tabular data generation performance on par with the most capable commercial LLM, GPT-4o.

