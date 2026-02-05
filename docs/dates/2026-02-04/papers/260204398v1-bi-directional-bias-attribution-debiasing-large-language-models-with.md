---
layout: default
title: Bi-directional Bias Attribution: Debiasing Large Language Models without Modifying Prompts
---

# Bi-directional Bias Attribution: Debiasing Large Language Models without Modifying Prompts
**arXiv**：[2602.04398v1](https://arxiv.org/abs/2602.04398) · [PDF](https://arxiv.org/pdf/2602.04398.pdf)  
**作者**：Yujie Lin, Kunquan Li, Yixuan Liao, Xiaoxin Chen, Jinsong Su  

**一句话要点**：提出双向偏差归因框架，在不修改提示词的情况下减少大语言模型的社会偏见。

**关键词**：大语言模型去偏, 偏差归因, 神经元干预, 社会偏见检测, 积分梯度

## 3 点简述
- 核心问题：大语言模型输出存在社会偏见，现有去偏方法面临可扩展性或用户体验问题。
- 方法要点：通过跨群体比较识别刻板印象词汇，基于积分梯度归因神经元偏差，并在投影层干预激活。
- 实验或效果：在三个大语言模型上验证，有效降低偏见同时保持整体性能。

## 摘要（原文）

> Large language models (LLMs) have demonstrated impressive capabilities across a wide range of natural language processing tasks. However, their outputs often exhibit social biases, raising fairness concerns. Existing debiasing methods, such as fine-tuning on additional datasets or prompt engineering, face scalability issues or compromise user experience in multi-turn interactions. To address these challenges, we propose a framework for detecting stereotype-inducing words and attributing neuron-level bias in LLMs, without the need for fine-tuning or prompt modification. Our framework first identifies stereotype-inducing adjectives and nouns via comparative analysis across demographic groups. We then attribute biased behavior to specific neurons using two attribution strategies based on integrated gradients. Finally, we mitigate bias by directly intervening on their activations at the projection layer. Experiments on three widely used LLMs demonstrate that our method effectively reduces bias while preserving overall model performance. Code is available at the github link: https://github.com/XMUDeepLIT/Bi-directional-Bias-Attribution.

