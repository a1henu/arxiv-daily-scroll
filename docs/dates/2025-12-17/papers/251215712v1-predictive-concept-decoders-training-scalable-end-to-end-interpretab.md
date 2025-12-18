---
layout: default
title: Predictive Concept Decoders: Training Scalable End-to-End Interpretability Assistants
---

# Predictive Concept Decoders: Training Scalable End-to-End Interpretability Assistants
**arXiv**：[2512.15712v1](https://arxiv.org/abs/2512.15712) · [PDF](https://arxiv.org/pdf/2512.15712.pdf)  
**作者**：Vincent Huang, Dami Choi, Daniel D. Johnson, Sarah Schwettmann, Jacob Steinhardt  

**一句话要点**：提出预测性概念解码器，通过端到端训练实现神经网络内部激活的可扩展解释

**关键词**：神经网络解释性, 端到端训练, 概念解码器, 激活分析, 可扩展解释, 预测模型行为

## 3 点简述
- 核心问题：神经网络内部激活空间复杂，现有可扩展解释方法依赖手工设计代理，难以高效关联激活与外部行为。
- 方法要点：训练解释助手，通过编码器压缩激活为稀疏概念列表，解码器基于此列表预测模型行为，形成端到端训练目标。
- 实验或效果：预训练后微调，概念瓶颈的自动解释评分随数据提升，能检测越狱、秘密提示和植入概念，并准确揭示潜在用户属性。

## 摘要（原文）

> Interpreting the internal activations of neural networks can produce more faithful explanations of their behavior, but is difficult due to the complex structure of activation space. Existing approaches to scalable interpretability use hand-designed agents that make and test hypotheses about how internal activations relate to external behavior. We propose to instead turn this task into an end-to-end training objective, by training interpretability assistants to accurately predict model behavior from activations through a communication bottleneck. Specifically, an encoder compresses activations to a sparse list of concepts, and a decoder reads this list and answers a natural language question about the model. We show how to pretrain this assistant on large unstructured data, then finetune it to answer questions. The resulting architecture, which we call a Predictive Concept Decoder, enjoys favorable scaling properties: the auto-interp score of the bottleneck concepts improves with data, as does the performance on downstream applications. Specifically, PCDs can detect jailbreaks, secret hints, and implanted latent concepts, and are able to accurately surface latent user attributes.

