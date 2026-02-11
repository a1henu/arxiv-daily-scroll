---
layout: default
title: Circuit Fingerprints: How Answer Tokens Encode Their Geometrical Path
---

# Circuit Fingerprints: How Answer Tokens Encode Their Geometrical Path
**arXiv**：[2602.09784v1](https://arxiv.org/abs/2602.09784) · [PDF](https://arxiv.org/pdf/2602.09784.pdf)  
**作者**：Andres Saurez, Neha Sengar, Dongsoo Har  

**一句话要点**：提出电路指纹假设，通过几何对齐实现无梯度电路发现与可控转向

**关键词**：电路发现, 激活转向, 几何结构, Transformer, 无梯度方法, 可控性

## 3 点简述
- 核心问题：电路发现与激活转向是否基于同一几何结构？
- 方法要点：利用答案令牌编码几何方向，无需梯度或因果干预进行电路发现
- 实验或效果：在标准基准上验证，性能媲美梯度方法，并实现情感分类准确率提升

## 摘要（原文）

> Circuit discovery and activation steering in transformers have developed as separate research threads, yet both operate on the same representational space. Are they two views of the same underlying structure? We show they follow a single geometric principle: answer tokens, processed in isolation, encode the directions that would produce them. This Circuit Fingerprint hypothesis enables circuit discovery without gradients or causal intervention -- recovering comparable structure to gradient-based methods through geometric alignment alone. We validate this on standard benchmarks (IOI, SVA, MCQA) across four model families, achieving circuit discovery performance comparable to gradient-based methods. The same directions that identify circuit components also enable controlled steering -- achieving 69.8\% emotion classification accuracy versus 53.1\% for instruction prompting while preserving factual accuracy. Beyond method development, this read-write duality reveals that transformer circuits are fundamentally geometric structures: interpretability and controllability are two facets of the same object.

