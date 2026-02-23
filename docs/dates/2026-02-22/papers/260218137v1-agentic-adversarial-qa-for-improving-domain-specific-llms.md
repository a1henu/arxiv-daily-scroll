---
layout: default
title: Agentic Adversarial QA for Improving Domain-Specific LLMs
---

# Agentic Adversarial QA for Improving Domain-Specific LLMs
**arXiv**：[2602.18137v1](https://arxiv.org/abs/2602.18137) · [PDF](https://arxiv.org/pdf/2602.18137.pdf)  
**作者**：Vincent Grari, Ciprian Tomoiaga, Sylvain Lamprier, Tatsunori Hashimoto, Marcin Detyniecki  

**一句话要点**：提出对抗性问答生成框架以提升领域特定大语言模型的适应效率

**关键词**：对抗性问答生成, 领域适应, 大语言模型, 合成数据, 样本效率, 法律领域

## 3 点简述
- 核心问题：大语言模型在专业领域适应中面临高质量数据稀缺和推理能力不足的挑战
- 方法要点：通过迭代反馈比较模型与专家输出，生成紧凑的语义挑战性问题
- 实验或效果：在LegalBench子集上验证，以更少合成样本实现更高准确率

## 摘要（原文）

> Large Language Models (LLMs), despite extensive pretraining on broad internet corpora, often struggle to adapt effectively to specialized domains. There is growing interest in fine-tuning these models for such domains; however, progress is constrained by the scarcity and limited coverage of high-quality, task-relevant data. To address this, synthetic data generation methods such as paraphrasing or knowledge extraction are commonly applied. Although these approaches excel at factual recall and conceptual knowledge, they suffer from two critical shortcomings: (i) they provide minimal support for interpretive reasoning capabilities in these specialized domains, and (ii) they often produce synthetic corpora that are excessively large and redundant, resulting in poor sample efficiency. To overcome these gaps, we propose an adversarial question-generation framework that produces a compact set of semantically challenging questions. These questions are constructed by comparing the outputs of the model to be adapted and a robust expert model grounded in reference documents, using an iterative, feedback-driven process designed to reveal and address comprehension gaps. Evaluation on specialized subsets of the LegalBench corpus demonstrates that our method achieves greater accuracy with substantially fewer synthetic samples.

