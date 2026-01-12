---
layout: default
title: Do LLMs Need Inherent Reasoning Before Reinforcement Learning? A Study in Korean Self-Correction
---

# Do LLMs Need Inherent Reasoning Before Reinforcement Learning? A Study in Korean Self-Correction
**arXiv**：[2601.05459v1](https://arxiv.org/abs/2601.05459) · [PDF](https://arxiv.org/pdf/2601.05459.pdf)  
**作者**：Hongjin Kim, Jaewook Lee, Kiyoung Lee, Jong-hun Shin, Soojong Lim, Oh-Woog Kwon  

**一句话要点**：提出神经元级调优与自校正代码切换数据集，以增强韩语推理能力

**关键词**：多语言推理, 强化学习, 神经元调优, 自校正, 代码切换, 韩语处理

## 3 点简述
- 研究强化学习在韩语推理中的局限性，发现缺乏固有推理能力时效果有限
- 探索微调策略，通过调优早期层韩语特定神经元对齐推理过程
- 引入自校正代码切换数据集，在数学推理和自校正任务中实现显著性能提升

## 摘要（原文）

> Large Language Models (LLMs) demonstrate strong reasoning and self-correction abilities in high-resource languages like English, but their performance remains limited in low-resource languages such as Korean. In this study, we investigate whether reinforcement learning (RL) can enhance Korean reasoning abilities to a degree comparable to English. Our findings reveal that RL alone yields limited improvements when applied to models lacking inherent Korean reasoning capabilities. To address this, we explore several fine-tuning strategies and show that aligning the model's internal reasoning processes with Korean inputs-particularly by tuning Korean-specific neurons in early layers-is key to unlocking RL's effectiveness. We introduce a self-correction code-switching dataset to facilitate this alignment and observe significant performance gains in both mathematical reasoning and self-correction tasks. Ultimately, we conclude that the crucial factor in multilingual reasoning enhancement is not injecting new linguistic knowledge, but effectively eliciting and aligning existing reasoning capabilities. Our study provides a new perspective on how internal translation and neuron-level tuning contribute to multilingual reasoning alignment in LLMs.

