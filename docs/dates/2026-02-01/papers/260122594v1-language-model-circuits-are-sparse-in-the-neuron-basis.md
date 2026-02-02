---
layout: default
title: Language Model Circuits Are Sparse in the Neuron Basis
---

# Language Model Circuits Are Sparse in the Neuron Basis
**arXiv**：[2601.22594v1](https://arxiv.org/abs/2601.22594) · [PDF](https://arxiv.org/pdf/2601.22594.pdf)  
**作者**：Aryaman Arora, Zhengxuan Wu, Jacob Steinhardt, Sarah Schwettmann  

**一句话要点**：提出基于MLP神经元稀疏性的电路追踪方法，用于语言模型自动可解释性。

**关键词**：语言模型可解释性, 电路追踪, 稀疏特征基, MLP神经元, 梯度归因

## 3 点简述
- 核心问题：神经网络高层概念与神经元不对齐，传统方法依赖稀疏自编码器分解。
- 方法要点：首次实证MLP神经元与稀疏自编码器同样稀疏，开发梯度归因的端到端电路追踪流程。
- 实验或效果：在主语-动词一致性和多跳推理任务中，定位小规模神经元电路控制模型行为。

## 摘要（原文）

> The high-level concepts that a neural network uses to perform computation need not be aligned to individual neurons (Smolensky, 1986). Language model interpretability research has thus turned to techniques such as \textit{sparse autoencoders} (SAEs) to decompose the neuron basis into more interpretable units of model computation, for tasks such as \textit{circuit tracing}. However, not all neuron-based representations are uninterpretable. For the first time, we empirically show that \textbf{MLP neurons are as sparse a feature basis as SAEs}. We use this finding to develop an end-to-end pipeline for circuit tracing on the MLP neuron basis, which locates causal circuitry on a variety of tasks using gradient-based attribution. On a standard subject-verb agreement benchmark (Marks et al., 2025), a circuit of $\approx 10^2$ MLP neurons is enough to control model behaviour. On the multi-hop city $\to$ state $\to$ capital task from Lindsey et al., 2025, we find a circuit in which small sets of neurons encode specific latent reasoning steps (e.g.~`map city to its state'), and can be steered to change the model's output. This work thus advances automated interpretability of language models without additional training costs.

