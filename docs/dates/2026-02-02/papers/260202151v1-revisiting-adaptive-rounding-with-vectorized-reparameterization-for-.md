---
layout: default
title: Revisiting Adaptive Rounding with Vectorized Reparameterization for LLM Quantization
---

# Revisiting Adaptive Rounding with Vectorized Reparameterization for LLM Quantization
**arXiv**：[2602.02151v1](https://arxiv.org/abs/2602.02151) · [PDF](https://arxiv.org/pdf/2602.02151.pdf)  
**作者**：Yuli Zhou, Qingxuan Chen, Luca Benini, Guolei Sun, Yawei Li  

**一句话要点**：提出VQRound以高效实现大语言模型的自适应舍入量化

**关键词**：大语言模型量化, 自适应舍入, 向量化重参数化, 码本优化, 轻量级微调, 后训练量化

## 3 点简述
- 核心问题：自适应舍入在十亿参数大语言模型中因密集舍入矩阵计算成本过高而不实用
- 方法要点：通过向量化重参数化将舍入矩阵压缩为码本，并优化L∞范数下的最坏情况误差
- 实验或效果：在OPT、LLaMA等模型上，仅用0.2%可训练参数和128样本实现快速收敛，优于传统方法

## 摘要（原文）

> Adaptive Rounding has emerged as an alternative to round-to-nearest (RTN) for post-training quantization by enabling cross-element error cancellation. Yet, dense and element-wise rounding matrices are prohibitively expensive for billion-parameter large language models (LLMs). We revisit adaptive rounding from an efficiency perspective and propose VQRound, a parameter-efficient optimization framework that reparameterizes the rounding matrix into a compact codebook. Unlike low-rank alternatives, VQRound minimizes the element-wise worst-case error under $L_\infty$ norm, which is critical for handling heavy-tailed weight distributions in LLMs. Beyond reparameterization, we identify rounding initialization as a decisive factor and develop a lightweight end-to-end finetuning pipeline that optimizes codebooks across all layers using only 128 samples. Extensive experiments on OPT, LLaMA, LLaMA2, and Qwen3 models demonstrate that VQRound achieves better convergence than traditional adaptive rounding at the same number of steps while using as little as 0.2% of the trainable parameters. Our results show that adaptive rounding can be made both scalable and fast-fitting. The code is available at https://github.com/zhoustan/VQRound.

