---
layout: default
title: An Empirical Study on Noisy Data and LLM Pretraining Loss Divergence
---

# An Empirical Study on Noisy Data and LLM Pretraining Loss Divergence
**arXiv**：[2602.02400v1](https://arxiv.org/abs/2602.02400) · [PDF](https://arxiv.org/pdf/2602.02400.pdf)  
**作者**：Qizhen Zhang, Ankush Garg, Jakob Foerster, Niladri Chatterji, Kshitiz Malik, Mike Lewis  

**一句话要点**：通过注入合成噪声实证研究噪声数据如何导致大语言模型预训练损失发散

**关键词**：大语言模型预训练, 噪声数据, 损失发散, 训练动态分析, 合成噪声注入, 模型规模影响

## 3 点简述
- 核心问题：噪声数据是否及如何导致大语言模型预训练损失发散，此现象先前理解不足。
- 方法要点：在干净数据集中注入受控合成均匀随机噪声，分析480M至5.2B参数模型的训练动态。
- 实验或效果：噪声确实诱导损失发散，发散概率取决于噪声类型、量和模型规模，并提供诊断区分不同失败模式。

## 摘要（原文）

> Large-scale pretraining datasets drive the success of large language models (LLMs). However, these web-scale corpora inevitably contain large amounts of noisy data due to unregulated web content or randomness inherent in data. Although LLM pretrainers often speculate that such noise contributes to instabilities in large-scale LLM pretraining and, in the worst cases, loss divergence, this phenomenon remains poorly understood.In this work, we present a systematic empirical study of whether noisy data causes LLM pretraining divergences and how it does so. By injecting controlled synthetic uniformly random noise into otherwise clean datasets, we analyze training dynamics across model sizes ranging from 480M to 5.2B parameters. We show that noisy data indeed induces training loss divergence, and that the probability of divergence depends strongly on the noise type, amount of noise, and model scale. We further find that noise-induced divergences exhibit activation patterns distinct from those caused by high learning rates, and we provide diagnostics that differentiate these two failure modes. Together, these results provide a large-scale, controlled characterization of how noisy data affects loss divergence in LLM pretraining.

