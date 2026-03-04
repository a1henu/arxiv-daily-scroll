---
layout: default
title: Understanding and Mitigating Dataset Corruption in LLM Steering
---

# Understanding and Mitigating Dataset Corruption in LLM Steering
**arXiv**：[2603.03206v1](https://arxiv.org/abs/2603.03206) · [PDF](https://arxiv.org/pdf/2603.03206.pdf)  
**作者**：Cullen Anderson, Narmeen Oozeer, Foad Namjoo, Remy Ogasawara, Amirali Abdullah, Jeff M. Phillips  

**一句话要点**：分析对比引导在数据集污染下的鲁棒性并提出稳健均值估计器作为缓解措施

**关键词**：对比引导, 数据集污染, 鲁棒性分析, 稳健均值估计, AI安全, LLM推理

## 3 点简述
- 核心问题：对比引导方法在AI安全应用中面临训练数据污染时的鲁棒性未知
- 方法要点：研究数据污染对引导方向的影响，分析污染几何特性并引入稳健均值估计器
- 实验或效果：发现适度污染下方法稳健，但严重污染可引发恶意副作用，稳健估计器能有效缓解

## 摘要（原文）

> Contrastive steering has been shown as a simple and effective method to adjust the generative behavior of LLMs at inference time. It uses examples of prompt responses with and without a trait to identify a direction in an intermediate activation layer, and then shifts activations in this 1-dimensional subspace. However, despite its growing use in AI safety applications, the robustness of contrastive steering to noisy or adversarial data corruption is poorly understood. We initiate a study of the robustness of this process with respect to corruption of the dataset of examples used to train the steering direction. Our first observation is that contrastive steering is quite robust to a moderate amount of corruption, but unwanted side effects can be clearly and maliciously manifested when a non-trivial fraction of the training data is altered. Second, we analyze the geometry of various types of corruption, and identify some safeguards. Notably, a key step in learning the steering direction involves high-dimensional mean computation, and we show that replacing this step with a recently developed robust mean estimator often mitigates most of the unwanted effects of malicious corruption.

