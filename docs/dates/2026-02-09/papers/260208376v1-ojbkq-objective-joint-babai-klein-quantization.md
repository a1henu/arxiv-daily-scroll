---
layout: default
title: OJBKQ: Objective-Joint Babai-Klein Quantization
---

# OJBKQ: Objective-Joint Babai-Klein Quantization
**arXiv**：[2602.08376v1](https://arxiv.org/abs/2602.08376) · [PDF](https://arxiv.org/pdf/2602.08376.pdf)  
**作者**：Xinyu Wang, Ziyu Zhao, Peng Lu, Yu Gu, Xiao-Wen Chang  

**一句话要点**：提出OJBKQ方法以优化大语言模型低比特量化中的权重量化问题

**关键词**：后训练量化, 权重量化, 整数最小二乘, 大语言模型, 低比特量化

## 3 点简述
- 核心问题：现有仅权重量化方法依赖启发式目标和贪婪舍入，导致低比特量化下性能显著下降
- 方法要点：将权重量化建模为激活和权重的联合优化问题，采用扩展Babai-Klein算法求解BILS子问题
- 实验或效果：在3-4比特量化下，相比现有PTQ方法，OJBKQ实现更低困惑度，计算成本未知

## 摘要（原文）

> Post-training quantization (PTQ) is widely used to compress large language models without retraining. However, many existing weight-only methods rely on heuristic objectives and greedy rounding, thus leading to noticeable degradation under low-bit quantization. In this work, we introduce OJBKQ (Objective-Joint Babai-Klein Quantization with K-Best Sampling), a layer-wise PTQ method that formulates weight quantization as a joint optimization problem over activations and weights. This formulation results in a multiple-right-hand-side box-constrained integer least squares (BILS) problem in each layer, which is NP-hard. For each column of the weight matrix, we apply an extended Babai nearest-plane algorithm and an extended version of Klein's randomized Babai algorithm to find the minimum-residual Babai-Klein point, a sub-optimal solution to the BILS problem. Experimental results on large language models show that OJBKQ achieves lower perplexity at 3-4 bits compared to existing PTQ approaches, while maintaining comparable computational cost.

