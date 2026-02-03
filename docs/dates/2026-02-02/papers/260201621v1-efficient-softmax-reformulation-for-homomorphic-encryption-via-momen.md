---
layout: default
title: Efficient Softmax Reformulation for Homomorphic Encryption via Moment Generating Function
---

# Efficient Softmax Reformulation for Homomorphic Encryption via Moment Generating Function
**arXiv**：[2602.01621v1](https://arxiv.org/abs/2602.01621) · [PDF](https://arxiv.org/pdf/2602.01621.pdf)  
**作者**：Hanjun Park, Byeong-Seo Min, Jiheon Woo, Min-Wook Jeong, Jongho Shin, Yongwoo Lee, Young-Sik Kim, Yongjune Kim  

**一句话要点**：提出基于矩生成函数的MGF-softmax，以降低同态加密中softmax的计算深度

**关键词**：同态加密, softmax近似, 矩生成函数, 隐私保护机器学习, Transformer架构

## 3 点简述
- 同态加密中softmax评估困难，因指数函数动态范围大和除法需求
- MGF-softmax用矩生成函数替换分母，减少乘法深度并保持关键性质
- 实验显示在Vision Transformers和大型语言模型中，实现高效准确近似

## 摘要（原文）

> Homomorphic encryption (HE) is a prominent framework for privacy-preserving machine learning, enabling inference directly on encrypted data. However, evaluating softmax, a core component of transformer architectures, remains particularly challenging in HE due to its multivariate structure, the large dynamic range induced by exponential functions, and the need for accurate division during normalization. In this paper, we propose MGF-softmax, a novel softmax reformulation based on the moment generating function (MGF) that replaces the softmax denominator with its moment-based counterpart. This reformulation substantially reduces multiplicative depth while preserving key properties of softmax and asymptotically converging to the exact softmax as the number of input tokens increases. Extensive experiments on Vision Transformers and large language models show that MGF-softmax provides an efficient and accurate approximation of softmax in encrypted inference. In particular, it achieves inference accuracy close to that of high-depth exact methods, while requiring substantially lower computational cost through reduced multiplicative depth.

