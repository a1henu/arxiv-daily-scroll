---
layout: default
title: Beyond Variance: Knowledge-Aware LLM Compression via Fisher-Aligned Subspace Diagnostics
---

# Beyond Variance: Knowledge-Aware LLM Compression via Fisher-Aligned Subspace Diagnostics
**arXiv**：[2601.07197v1](https://arxiv.org/abs/2601.07197) · [PDF](https://arxiv.org/pdf/2601.07197.pdf)  
**作者**：Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma  

**一句话要点**：提出Fisher对齐子空间压缩以解决大语言模型后训练激活压缩中知识保留不足的问题。

**关键词**：大语言模型压缩, 后训练激活压缩, Fisher信息矩阵, 知识保留, 子空间选择, 依赖违反分数

## 3 点简述
- 核心问题：标准压缩方法如奇异值分解忽略梯度信息，可能损害事实知识保留。
- 方法要点：利用Fisher信息矩阵选择关键子空间，最小化损失函数的二阶代理，引入依赖违反分数作为诊断指标。
- 实验或效果：在Mistral-7B和Llama-3-8B上，相比基于方差的方法，在50%秩减少时知识密集型基准准确率提升6-8%。

## 摘要（原文）

> Post-training activation compression is essential for deploying Large Language Models (LLMs) on resource-constrained hardware. However, standard methods like Singular Value Decomposition (SVD) are gradient-blind: they preserve high-variance dimensions regardless of their impact on factual knowledge preservation. We introduce Fisher-Aligned Subspace Compression (FASC), a knowledge-aware compression framework that selects subspaces by directly modeling activation-gradient coupling, minimizing a second-order surrogate of the loss function. FASC leverages the Fisher Information Matrix to identify dimensions critical for factual knowledge, which often reside in low-variance but high-gradient-sensitivity subspaces. We propose the Dependence Violation Score (\r{ho}) as a general-purpose diagnostic metric that quantifies activation-gradient coupling, revealing where factual knowledge is stored within transformer architectures. Extensive experiments on Mistral-7B and Llama-3-8B demonstrate that FASC preserves 6-8% more accuracy on knowledge-intensive benchmarks (MMLU, LAMA) compared to variance-based methods at 50% rank reduction, effectively enabling a 7B model to match the factual recall of a 13B uncompressed model. Our analysis reveals that \r{ho} serves as a fundamental signal of stored knowledge, with high-\r{ho} layers emerging only when models internalize factual associations during training.

