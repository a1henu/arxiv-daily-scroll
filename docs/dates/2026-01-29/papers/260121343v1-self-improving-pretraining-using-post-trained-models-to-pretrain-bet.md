---
layout: default
title: Self-Improving Pretraining: using post-trained models to pretrain better models
---

# Self-Improving Pretraining: using post-trained models to pretrain better models
**arXiv**：[2601.21343v1](https://arxiv.org/abs/2601.21343) · [PDF](https://arxiv.org/pdf/2601.21343.pdf)  
**作者**：Ellen Xiaoqing Tan, Shehzaad Dhuliawala, Jing Xu, Ping Yu, Sainbayar Sukhbaatar, Jason Weston, Olga Golovneva  

**一句话要点**：提出自改进预训练方法，使用后训练模型通过强化学习提升大语言模型的安全性、事实性和生成质量。

**关键词**：自改进预训练, 强化学习, 大语言模型, 事实性增强, 安全性提升, 生成质量优化

## 3 点简述
- 核心问题：大语言模型在预训练阶段学习到的模式可能导致生成内容不安全、不真实，现有微调方法难以根除。
- 方法要点：采用流式文档输入，利用后训练模型评估生成质量，通过强化学习优化模型在预训练中的生成行为。
- 实验或效果：相比标准预训练，事实性和安全性分别提升36.2%和18.5%，整体生成质量胜率最高提升86.3%。

## 摘要（原文）

> Ensuring safety, factuality and overall quality in the generations of large language models is a critical challenge, especially as these models are increasingly deployed in real-world applications. The prevailing approach to addressing these issues involves collecting expensive, carefully curated datasets and applying multiple stages of fine-tuning and alignment. However, even this complex pipeline cannot guarantee the correction of patterns learned during pretraining. Therefore, addressing these issues during pretraining is crucial, as it shapes a model's core behaviors and prevents unsafe or hallucinated outputs from becoming deeply embedded. To tackle this issue, we introduce a new pretraining method that streams documents and uses reinforcement learning (RL) to improve the next K generated tokens at each step. A strong, post-trained model judges candidate generations -- including model rollouts, the original suffix, and a rewritten suffix -- for quality, safety, and factuality. Early in training, the process relies on the original and rewritten suffixes; as the model improves, RL rewards high-quality rollouts. This approach builds higher quality, safer, and more factual models from the ground up. In experiments, our method gives 36.2% and 18.5% relative improvements over standard pretraining in terms of factuality and safety, and up to 86.3% win rate improvements in overall generation quality.

