---
layout: default
title: An Empirical Investigation of Robustness in Large Language Models under Tabular Distortions
---

# An Empirical Investigation of Robustness in Large Language Models under Tabular Distortions
**arXiv**：[2601.05009v1](https://arxiv.org/abs/2601.05009) · [PDF](https://arxiv.org/pdf/2601.05009.pdf)  
**作者**：Avik Dutta, Harshit Nigam, Hosein Hasanbeig, Arjun Radhakrishna, Sumit Gulwani  

**一句话要点**：探究大语言模型在表格数据扭曲下的鲁棒性，揭示其缺乏自主检测与纠正能力

**关键词**：大语言模型鲁棒性, 表格数据扭曲, 表格问答任务, 错误纠正, 语义结构失真, 系统提示影响

## 3 点简述
- 核心问题：大语言模型在表格数据遭受语义和结构扭曲时，缺乏内在能力检测和纠正细微失真
- 方法要点：引入专家策划的小型数据集，评估模型在表格问答任务中需先进行错误纠正的表现
- 实验或效果：即使GPT-5.2等先进模型在扭曲下准确率下降至少22%，仅通过系统提示部分调整推理策略

## 摘要（原文）

> We investigate how large language models (LLMs) fail when tabular data in an otherwise canonical representation is subjected to semantic and structural distortions. Our findings reveal that LLMs lack an inherent ability to detect and correct subtle distortions in table representations. Only when provided with an explicit prior, via a system prompt, do models partially adjust their reasoning strategies and correct some distortions, though not consistently or completely. To study this phenomenon, we introduce a small, expert-curated dataset that explicitly evaluates LLMs on table question answering (TQA) tasks requiring an additional error-correction step prior to analysis. Our results reveal systematic differences in how LLMs ingest and interpret tabular information under distortion, with even SoTA models such as GPT-5.2 model exhibiting a drop of minimum 22% accuracy under distortion. These findings raise important questions for future research, particularly regarding when and how models should autonomously decide to realign tabular inputs, analogous to human behavior, without relying on explicit prompts or tabular data pre-processing.

