---
layout: default
title: Protecting Private Code in IDE Autocomplete using Differential Privacy
---

# Protecting Private Code in IDE Autocomplete using Differential Privacy
**arXiv**：[2601.22935v1](https://arxiv.org/abs/2601.22935) · [PDF](https://arxiv.org/pdf/2601.22935.pdf)  
**作者**：Evgeny Grigorenko, David Stanojević, David Ilić, Egor Bogomolov, Kostadin Cvejoski  

**一句话要点**：提出差分隐私训练方法以保护IDE代码自动补全中的私有代码

**关键词**：差分隐私, 代码自动补全, 成员推理攻击, Kotlin编程, IDE安全, 大语言模型微调

## 3 点简述
- 核心问题：IDE中基于LLM的代码自动补全训练存在隐私风险，易受成员推理攻击。
- 方法要点：使用差分隐私微调Kotlin代码补全模型，平衡隐私与性能。
- 实验或效果：DP显著降低攻击成功率至接近随机猜测，且模型性能损失小，数据效率高。

## 摘要（原文）

> Modern Integrated Development Environments (IDEs) increasingly leverage Large Language Models (LLMs) to provide advanced features like code autocomplete. While powerful, training these models on user-written code introduces significant privacy risks, making the models themselves a new type of data vulnerability. Malicious actors can exploit this by launching attacks to reconstruct sensitive training data or infer whether a specific code snippet was used for training. This paper investigates the use of Differential Privacy (DP) as a robust defense mechanism for training an LLM for Kotlin code completion. We fine-tune a \texttt{Mellum} model using DP and conduct a comprehensive evaluation of its privacy and utility. Our results demonstrate that DP provides a strong defense against Membership Inference Attacks (MIAs), reducing the attack's success rate close to a random guess (AUC from 0.901 to 0.606). Furthermore, we show that this privacy guarantee comes at a minimal cost to model performance, with the DP-trained model achieving utility scores comparable to its non-private counterpart, even when trained on 100x less data. Our findings suggest that DP is a practical and effective solution for building private and trustworthy AI-powered IDE features.

