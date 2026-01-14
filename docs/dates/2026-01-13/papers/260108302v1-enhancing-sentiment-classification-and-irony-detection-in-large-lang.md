---
layout: default
title: Enhancing Sentiment Classification and Irony Detection in Large Language Models through Advanced Prompt Engineering Techniques
---

# Enhancing Sentiment Classification and Irony Detection in Large Language Models through Advanced Prompt Engineering Techniques
**arXiv**：[2601.08302v1](https://arxiv.org/abs/2601.08302) · [PDF](https://arxiv.org/pdf/2601.08302.pdf)  
**作者**：Marvin Schmitt, Anne Schwerk, Sebastian Lempert  

**一句话要点**：通过高级提示工程增强大语言模型在情感分类与反讽检测中的性能

**关键词**：提示工程, 情感分析, 大语言模型, 反讽检测, 少样本学习, 思维链提示

## 3 点简述
- 研究核心问题：如何利用提示工程提升大语言模型在情感分析任务中的表现，包括情感分类、方面级情感分析和反讽检测。
- 方法要点：评估少样本学习、思维链提示和自一致性等高级提示技术，对比基线方法，针对GPT-4o-mini和gemini-1.5-flash模型进行定制化策略设计。
- 实验效果：高级提示显著改善性能，少样本提示在GPT-4o-mini中表现最佳，思维链提示在gemini-1.5-flash中提升反讽检测达46%，强调提示策略需适配模型与任务。

## 摘要（原文）

> This study investigates the use of prompt engineering to enhance large language models (LLMs), specifically GPT-4o-mini and gemini-1.5-flash, in sentiment analysis tasks. It evaluates advanced prompting techniques like few-shot learning, chain-of-thought prompting, and self-consistency against a baseline. Key tasks include sentiment classification, aspect-based sentiment analysis, and detecting subtle nuances such as irony. The research details the theoretical background, datasets, and methods used, assessing performance of LLMs as measured by accuracy, recall, precision, and F1 score. Findings reveal that advanced prompting significantly improves sentiment analysis, with the few-shot approach excelling in GPT-4o-mini and chain-of-thought prompting boosting irony detection in gemini-1.5-flash by up to 46%. Thus, while advanced prompting techniques overall improve performance, the fact that few-shot prompting works best for GPT-4o-mini and chain-of-thought excels in gemini-1.5-flash for irony detection suggests that prompting strategies must be tailored to both the model and the task. This highlights the importance of aligning prompt design with both the LLM's architecture and the semantic complexity of the task.

