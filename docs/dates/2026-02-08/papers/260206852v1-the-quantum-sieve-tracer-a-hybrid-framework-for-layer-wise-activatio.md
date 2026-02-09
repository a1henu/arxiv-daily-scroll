---
layout: default
title: The Quantum Sieve Tracer: A Hybrid Framework for Layer-Wise Activation Tracing in Large Language Models
---

# The Quantum Sieve Tracer: A Hybrid Framework for Layer-Wise Activation Tracing in Large Language Models
**arXiv**：[2602.06852v1](https://arxiv.org/abs/2602.06852) · [PDF](https://arxiv.org/pdf/2602.06852.pdf)  
**作者**：Jonathan Pan  

**一句话要点**：提出量子筛追踪器，以混合量子-经典框架解决大语言模型中稀疏语义信号与高维多义噪声分离的挑战。

**关键词**：大语言模型, 机制可解释性, 量子计算, 注意力机制, 因果追踪

## 3 点简述
- 核心问题：大语言模型内部计算的反向工程中，稀疏语义信号与高维多义噪声难以分离。
- 方法要点：采用模块化流程，先经典因果追踪定位关键层，再映射注意力头激活到量子希尔伯特空间。
- 实验或效果：在开源模型上揭示架构差异，量子核能区分构建性（回忆）和还原性（抑制）机制。

## 摘要（原文）

> Mechanistic interpretability aims to reverse-engineer the internal computations of Large Language Models (LLMs), yet separating sparse semantic signals from high-dimensional polysemantic noise remains a significant challenge. This paper introduces the Quantum Sieve Tracer, a hybrid quantum-classical framework designed to characterize factual recall circuits. We implement a modular pipeline that first localizes critical layers using classical causal tracing, then maps specific attention head activations into an exponentially large quantum Hilbert space. Using open-weight models (Meta Llama-3.2-1B and Alibaba Qwen2.5-1.5B-Instruct), we perform a two-stage analysis that reveals a fundamental architectural divergence. While Qwen's layer 7 circuit functions as a classic Recall Hub, we discover that Llama's layer 9 acts as an Interference Suppression circuit, where ablating the identified heads paradoxically improves factual recall. Our results demonstrate that quantum kernels can distinguish between these constructive (recall) and reductive (suppression) mechanisms, offering a high-resolution tool for analyzing the fine-grained topology of attention.

