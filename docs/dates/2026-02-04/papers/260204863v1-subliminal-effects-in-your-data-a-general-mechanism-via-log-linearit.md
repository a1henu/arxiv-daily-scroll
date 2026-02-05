---
layout: default
title: Subliminal Effects in Your Data: A General Mechanism via Log-Linearity
---

# Subliminal Effects in Your Data: A General Mechanism via Log-Linearity
**arXiv**：[2602.04863v1](https://arxiv.org/abs/2602.04863) · [PDF](https://arxiv.org/pdf/2602.04863.pdf)  
**作者**：Ishaq Aden-Ali, Noah Golowich, Allen Liu, Abhishek Shetty, Ankur Moitra, Nika Haghtalab  

**一句话要点**：提出Logit-Linear-Selection方法以揭示通用数据集中隐藏子文本的生成机制

**关键词**：大语言模型训练, 数据集效应, 隐藏子文本, Logit-Linear-Selection, 模型行为控制

## 3 点简述
- 核心问题：数据集如何传递不可直接观察的信号，影响大语言模型行为，挑战基于数据集的训练理解
- 方法要点：基于大语言模型的线性结构，提出Logit-Linear-Selection方法，通过选择数据子集来引发隐藏效应
- 实验或效果：应用于真实数据集，使模型表现出特定偏好、跨语言响应或不同人格，效应在不同架构模型中普遍存在

## 摘要（原文）

> Training modern large language models (LLMs) has become a veritable smorgasbord of algorithms and datasets designed to elicit particular behaviors, making it critical to develop techniques to understand the effects of datasets on the model's properties. This is exacerbated by recent experiments that show datasets can transmit signals that are not directly observable from individual datapoints, posing a conceptual challenge for dataset-centric understandings of LLM training and suggesting a missing fundamental account of such phenomena. Towards understanding such effects, inspired by recent work on the linear structure of LLMs, we uncover a general mechanism through which hidden subtexts can arise in generic datasets.
>   We introduce Logit-Linear-Selection (LLS), a method that prescribes how to select subsets of a generic preference dataset to elicit a wide range of hidden effects. We apply LLS to discover subsets of real-world datasets so that models trained on them exhibit behaviors ranging from having specific preferences, to responding to prompts in a different language not present in the dataset, to taking on a different persona. Crucially, the effect persists for the selected subset, across models with varying architectures, supporting its generality and universality.

