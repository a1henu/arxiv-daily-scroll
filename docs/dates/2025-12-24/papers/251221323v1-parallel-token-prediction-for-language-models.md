---
layout: default
title: Parallel Token Prediction for Language Models
---

# Parallel Token Prediction for Language Models
**arXiv**：[2512.21323v1](https://arxiv.org/abs/2512.21323) · [PDF](https://arxiv.org/pdf/2512.21323.pdf)  
**作者**：Felix Draxler, Justus Will, Farrin Marouf Sofian, Theofanis Karaletsos, Sameer Singh, Stephan Mandt  

**一句话要点**：提出并行令牌预测框架，以并行生成序列解决自回归解码延迟瓶颈。

**关键词**：并行序列生成, 自回归解码, 推测解码, Transformer模型, 蒸馏训练, 逆自回归训练

## 3 点简述
- 核心问题：自回归解码在语言模型中导致高延迟，现有多令牌预测方法依赖独立性假设。
- 方法要点：通过将采样过程融入模型，单次Transformer调用联合预测多个依赖令牌，避免独立性限制。
- 实验或效果：在Vicuna-7B上实现最先进的推测解码性能，Spec-Bench上每步接受超过四个令牌。

## 摘要（原文）

> We propose Parallel Token Prediction (PTP), a universal framework for parallel sequence generation in language models. PTP jointly predicts multiple dependent tokens in a single transformer call by incorporating the sampling procedure into the model. This reduces the latency bottleneck of autoregressive decoding, and avoids the restrictive independence assumptions common in existing multi-token prediction methods. We prove that PTP can represent arbitrary autoregressive sequence distributions. PTP is trained either by distilling an existing model or through inverse autoregressive training without a teacher. Experimentally, we achieve state-of-the-art speculative decoding performance on Vicuna-7B by accepting over four tokens per step on Spec-Bench. The universality of our framework indicates that parallel generation of long sequences is feasible without loss of modeling power.

