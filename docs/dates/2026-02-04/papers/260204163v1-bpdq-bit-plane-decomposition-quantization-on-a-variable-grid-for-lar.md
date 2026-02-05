---
layout: default
title: BPDQ: Bit-Plane Decomposition Quantization on a Variable Grid for Large Language Models
---

# BPDQ: Bit-Plane Decomposition Quantization on a Variable Grid for Large Language Models
**arXiv**：[2602.04163v1](https://arxiv.org/abs/2602.04163) · [PDF](https://arxiv.org/pdf/2602.04163.pdf)  
**作者**：Junyu Chen, Jungang Li, Jing Xiong, Wenjie Wang, Qingyao Yang, He Xiao, Zhen Li, Taiqiang Wu, Mengzhao Chen, Zhen Peng, Chaofan Tao, Long Shi, Hongxia Yang, Ngai Wong  

**一句话要点**：提出BPDQ量化方法，通过可变网格优化大语言模型在2-3位下的推理效率

**关键词**：大语言模型量化, 后训练量化, 位平面分解, 可变量化网格, 二阶优化, 推理效率

## 3 点简述
- 核心问题：现有后训练量化在2-3位精度下性能下降，因固定量化网格限制误差最小化
- 方法要点：基于位平面和标量系数构建可变量化网格，利用近似二阶信息迭代优化以最小化输出差异
- 实验或效果：在2位量化下，Qwen2.5-72B模型在单RTX 3090上实现83.85% GSM8K准确率，接近16位性能

## 摘要（原文）

> Large language model (LLM) inference is often bounded by memory footprint and memory bandwidth in resource-constrained deployments, making quantization a fundamental technique for efficient serving. While post-training quantization (PTQ) maintains high fidelity at 4-bit, it deteriorates at 2-3 bits. Fundamentally, existing methods enforce a shape-invariant quantization grid (e.g., the fixed uniform intervals of UINT2) for each group, severely restricting the feasible set for error minimization. To address this, we propose Bit-Plane Decomposition Quantization (BPDQ), which constructs a variable quantization grid via bit-planes and scalar coefficients, and iteratively refines them using approximate second-order information while progressively compensating quantization errors to minimize output discrepancy. In the 2-bit regime, BPDQ enables serving Qwen2.5-72B on a single RTX 3090 with 83.85% GSM8K accuracy (vs. 90.83% at 16-bit). Moreover, we provide theoretical analysis showing that the variable grid expands the feasible set, and that the quantization process consistently aligns with the optimization objective in Hessian-induced geometry. Code: github.com/KingdalfGoodman/BPDQ.

