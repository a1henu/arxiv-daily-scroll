---
layout: default
title: Data-Free Privacy-Preserving for LLMs via Model Inversion and Selective Unlearning
---

# Data-Free Privacy-Preserving for LLMs via Model Inversion and Selective Unlearning
**arXiv**：[2601.15595v1](https://arxiv.org/abs/2601.15595) · [PDF](https://arxiv.org/pdf/2601.15595.pdf)  
**作者**：Xinjie Zhou, Zhihui Yang, Lechao Cheng, Sai Wu, Gang Chen  

**一句话要点**：提出数据自由选择性遗忘框架，以解决大语言模型隐私保护中训练数据不可访问的问题。

**关键词**：大语言模型隐私保护, 数据自由遗忘, 模型反演, 选择性遗忘, 低秩适应, 令牌级掩码

## 3 点简述
- 核心问题：大语言模型可能记忆训练数据中的敏感个人信息，但传统遗忘技术依赖训练数据访问，这在现实部署中常不可行。
- 方法要点：通过语言模型反演合成伪敏感信息，构建令牌级隐私掩码，并在低秩适应子空间中使用对比掩码损失进行选择性遗忘。
- 实验或效果：在AI4Privacy PII-Masking数据集上使用Pythia模型实验，显示方法能有效移除目标敏感信息并保持模型效用。

## 摘要（原文）

> Large language models (LLMs) exhibit powerful capabilities but risk memorizing sensitive personally identifiable information (PII) from their training data, posing significant privacy concerns. While machine unlearning techniques aim to remove such data, they predominantly depend on access to the training data. This requirement is often impractical, as training data in real-world deployments is commonly proprietary or inaccessible. To address this limitation, we propose Data-Free Selective Unlearning (DFSU), a novel privacy-preserving framework that removes sensitive PII from an LLM without requiring its training data. Our approach first synthesizes pseudo-PII through language model inversion, then constructs token-level privacy masks for these synthetic samples, and finally performs token-level selective unlearning via a contrastive mask loss within a low-rank adaptation (LoRA) subspace. Extensive experiments on the AI4Privacy PII-Masking dataset using Pythia models demonstrate that our method effectively removes target PII while maintaining model utility.

