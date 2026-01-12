---
layout: default
title: Tracing Stereotypes in Pre-trained Transformers: From Biased Neurons to Fairer Models
---

# Tracing Stereotypes in Pre-trained Transformers: From Biased Neurons to Fairer Models
**arXiv**：[2601.05663v1](https://arxiv.org/abs/2601.05663) · [PDF](https://arxiv.org/pdf/2601.05663.pdf)  
**作者**：Gianmario Voria, Moses Openja, Foutse Khomh, Gemma Catolino, Fabio Palomba  

**一句话要点**：提出基于偏置神经元追踪与抑制的方法，以提升预训练Transformer在软件工程中的公平性

**关键词**：Transformer模型, 偏置神经元, 神经元编辑, 软件工程公平性, 神经元归因

## 3 点简述
- 预训练Transformer模型在软件工程中可能放大社会偏见，引发公平性问题
- 假设存在偏置神经元，构建偏置关系数据集并采用神经元归因策略进行追踪与抑制
- 实验表明抑制偏置神经元能显著减少偏见，且对任务性能影响较小

## 摘要（原文）

> The advent of transformer-based language models has reshaped how AI systems process and generate text. In software engineering (SE), these models now support diverse activities, accelerating automation and decision-making. Yet, evidence shows that these models can reproduce or amplify social biases, raising fairness concerns. Recent work on neuron editing has shown that internal activations in pre-trained transformers can be traced and modified to alter model behavior. Building on the concept of knowledge neurons, neurons that encode factual information, we hypothesize the existence of biased neurons that capture stereotypical associations within pre-trained transformers. To test this hypothesis, we build a dataset of biased relations, i.e., triplets encoding stereotypes across nine bias types, and adapt neuron attribution strategies to trace and suppress biased neurons in BERT models. We then assess the impact of suppression on SE tasks. Our findings show that biased knowledge is localized within small neuron subsets, and suppressing them substantially reduces bias with minimal performance loss. This demonstrates that bias in transformers can be traced and mitigated at the neuron level, offering an interpretable approach to fairness in SE.

