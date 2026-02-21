---
layout: default
title: 2Mamba2Furious: Linear in Complexity, Competitive in Accuracy
---

# 2Mamba2Furious: Linear in Complexity, Competitive in Accuracy
**arXiv**：[2602.17363v1](https://arxiv.org/abs/2602.17363) · [PDF](https://arxiv.org/pdf/2602.17363.pdf)  
**作者**：Gabriel Mongaras, Eric C. Larson  

**一句话要点**：提出2Mamba方法，通过改进Mamba-2以缩小线性注意力与softmax注意力的精度差距，同时保持长上下文的高效性。

**关键词**：线性注意力, Mamba-2, 长上下文处理, 注意力机制优化, Transformer效率

## 3 点简述
- 核心问题：线性注意力在效率上优于softmax注意力，但表达力较弱，导致精度降低。
- 方法要点：简化Mamba-2为Mamba-2S，优化A-mask并增加隐藏状态阶数，提升精度。
- 实验或效果：2Mamba在精度上接近softmax注意力，且在长上下文下内存效率更高。

## 摘要（原文）

> Linear attention transformers have become a strong alternative to softmax attention due to their efficiency. However, linear attention tends to be less expressive and results in reduced accuracy compared to softmax attention. To bridge the accuracy gap between softmax attention and linear attention, we manipulate Mamba-2, a very strong linear attention variant. We first simplify Mamba-2 down to its most fundamental and important components, evaluating which specific choices make it most accurate. From this simplified Mamba variant (Mamba-2S), we improve the A-mask and increase the order of the hidden state, resulting in a method, which we call 2Mamba, that is nearly as accurate as softmax attention, yet much more memory efficient for long context lengths. We also investigate elements to Mamba-2 that help surpass softmax attention accuracy. Code is provided for all our experiments

