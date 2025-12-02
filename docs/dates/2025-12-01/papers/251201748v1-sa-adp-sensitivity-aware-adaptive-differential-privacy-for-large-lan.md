---
layout: default
title: SA-ADP: Sensitivity-Aware Adaptive Differential Privacy for Large Language Models
---

# SA-ADP: Sensitivity-Aware Adaptive Differential Privacy for Large Language Models
**arXiv**：[2512.01748v1](https://arxiv.org/abs/2512.01748) · [PDF](https://arxiv.org/pdf/2512.01748.pdf)  
**作者**：Stella Etuk, Ashraf Matrawy  

**一句话要点**：提出SA-ADP方法，基于PII敏感度分配噪声以解决大语言模型训练中的隐私-效用权衡问题。

**关键词**：大语言模型, 差分隐私, 隐私保护, 敏感度感知, 自适应噪声分配, 模型效用

## 3 点简述
- 核心问题：大语言模型训练中PII记忆引发隐私担忧，传统DP-SGD方法因均匀加噪导致模型效用下降。
- 方法要点：SA-ADP根据个人可识别信息的敏感度自适应分配噪声，而非统一处理。
- 实验或效果：在四个数据集上评估，SA-ADP在保持强隐私保护的同时，模型效用未降低，与无隐私保护和DP-SGD基线相当。

## 摘要（原文）

> Despite advances in the use of large language models (LLMs) in downstream tasks, their ability to memorize information has raised privacy concerns. Therefore, protecting personally identifiable information (PII) during LLM training remains a fundamental challenge. Conventional methods like Differential Privacy-Stochastic Gradient Descent (DP-SGD) provide robust privacy protection via uniform noising, protecting PII regardless of its distinct sensitivity. This comes at the expense of the model's utility, leading to a trade-off. In this paper, we propose SA-ADP, a sensitivity-aware approach that allocates noise based on the sensitivity of individual PII. We evaluated our method on four datasets (ABCD, CUSTOMERSIM, Wikitext-2, and UNSW-NB15 ). Our results show that SA-ADP achieves results comparable to the baseline (No-DP) and the conventional DP-SGD. This means that our method did not degrade the model's utility while still maintaining strong privacy protection.

