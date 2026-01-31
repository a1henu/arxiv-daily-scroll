---
layout: default
title: MGSM-Pro: A Simple Strategy for Robust Multilingual Mathematical Reasoning Evaluation
---

# MGSM-Pro: A Simple Strategy for Robust Multilingual Mathematical Reasoning Evaluation
**arXiv**：[2601.21225v1](https://arxiv.org/abs/2601.21225) · [PDF](https://arxiv.org/pdf/2601.21225.pdf)  
**作者**：Tianyi Xu, Kosei Uemura, Alfred Malengo Kondoro, Tadesse Destaw Belay, Catherine Nana Nyaah Essuman, Ifeoma Okoh, Ganiyat Afolabi, Ayodele Awokoya, David Ifeoluwa Adelani  

**一句话要点**：提出MGSM-Pro数据集以增强多语言数学推理评估的鲁棒性

**关键词**：多语言数学推理, 评估鲁棒性, 数据集扩展, 实例化变化, 低资源语言, 模型比较

## 3 点简述
- 核心问题：多语言数学推理基准在难度和时效性上落后于英语，且评估结果对问题实例化敏感
- 方法要点：扩展MGSM数据集，采用GSM-Symbolic方法，为每个问题提供五种实例化，包括名称、数字和无关上下文的变化
- 实验或效果：在九种语言上评估，发现低资源语言对数字实例化变化敏感，部分模型鲁棒性差异显著，建议使用至少五种数字变化实例化进行评估

## 摘要（原文）

> Large language models have made substantial progress in mathematical reasoning. However, benchmark development for multilingual evaluation has lagged behind English in both difficulty and recency. Recently, GSM-Symbolic showed a strong evidence of high variance when models are evaluated on different instantiations of the same question; however, the evaluation was conducted only in English. In this paper, we introduce MGSM-Pro, an extension of MGSM dataset with GSM-Symbolic approach. Our dataset provides five instantiations per MGSM question by varying names, digits and irrelevant context. Evaluations across nine languages reveal that many low-resource languages suffer large performance drops when tested on digit instantiations different from those in the original test set. We further find that some proprietary models, notably Gemini 2.5 Flash and GPT-4.1, are less robust to digit instantiation, whereas Claude 4.0 Sonnet is more robust. Among open models, GPT-OSS 120B and DeepSeek V3 show stronger robustness. Based on these findings, we recommend evaluating each problem using at least five digit-varying instantiations to obtain a more robust and realistic assessment of math reasoning.

