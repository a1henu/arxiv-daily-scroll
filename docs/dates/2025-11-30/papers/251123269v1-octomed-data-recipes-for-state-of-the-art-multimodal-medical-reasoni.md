---
layout: default
title: OctoMed: Data Recipes for State-of-the-Art Multimodal Medical Reasoning
---

# OctoMed: Data Recipes for State-of-the-Art Multimodal Medical Reasoning
**arXiv**：[2511.23269v1](https://arxiv.org/abs/2511.23269) · [PDF](https://arxiv.org/pdf/2511.23269.pdf)  
**作者**：Timothy Ossowski, Sheng Zhang, Qianchu Liu, Guanghui Qin, Reuben Tan, Tristan Naumann, Junjie Hu, Hoifung Poon  

**一句话要点**：提出OctoMed数据配方，通过结构化推理轨迹提升医疗多模态推理模型的泛化与鲁棒性。

**关键词**：医疗多模态推理, 数据策展, 结构化推理轨迹, 监督微调, 泛化能力, 鲁棒性

## 3 点简述
- 核心问题：高质量数据对医疗大语言模型的泛化和鲁棒性至关重要，需优化训练与数据策展策略。
- 方法要点：采用监督微调，设计数据配方利用结构化推理轨迹，策展多样训练数据集。
- 实验或效果：在超800万样本数据集上实现开源模型中的最先进性能，模型能自校准推理轨迹长度。

## 摘要（原文）

> High-quality and carefully curated data is a cornerstone of training medical large language models, as it directly impacts both generalization and robustness to unseen clinical tasks. We investigate strategies for training and data curation to develop a robust multimodal reasoning model in the medical domain. Our work focuses on supervised fine-tuning (SFT) and explores data recipes that leverage structured reasoning traces. Using our proposed data recipe, we scale experiments to a dataset of over 8 million examples and 6.8 billion response tokens, achieving state-of-the-art performance among open-source models across diverse out-of-distribution medical benchmark tasks. Our results further indicate that curating a high-quality, diverse training dataset with varying structured reasoning trace lengths enables the fine-tuned model to self-calibrate its reasoning trajectory lengths based on the downstream task, without explicit supervision. We present key insights, describe the data curation strategy, and outline next steps toward developing robust medical vision-language reasoning system.

