---
layout: default
title: HiDrop: Hierarchical Vision Token Reduction in MLLMs via Late Injection, Concave Pyramid Pruning, and Early Exit
---

# HiDrop: Hierarchical Vision Token Reduction in MLLMs via Late Injection, Concave Pyramid Pruning, and Early Exit
**arXiv**：[2602.23699v1](https://arxiv.org/abs/2602.23699) · [PDF](https://arxiv.org/pdf/2602.23699.pdf)  
**作者**：Hao Wu, Yingqi Fan, Jinyang Dai, Junlong Tong, Yunpu Ma, Xiaoyu Shen  

**一句话要点**：提出HiDrop框架以解决MLLMs中视觉令牌二次计算成本问题

**关键词**：多模态大语言模型, 视觉令牌剪枝, 高效训练, 分层融合, 动态优化, 计算加速

## 3 点简述
- 核心问题：MLLMs处理视觉令牌的二次计算成本阻碍应用，现有剪枝方法误解浅层功能且调度僵化。
- 方法要点：采用Late Injection和Concave Pyramid Pruning with Early Exit，动态调整剪枝率，优化跨层相似度和可微top-k操作。
- 实验或效果：压缩约90%视觉令牌，性能匹配原始模型，训练加速1.72倍，代码已开源。

## 摘要（原文）

> The quadratic computational cost of processing vision tokens in Multimodal Large Language Models (MLLMs) hinders their widespread adoption. While progressive vision token pruning offers a promising solution, current methods misinterpret shallow layer functions and use rigid schedules, which fail to unlock the full efficiency potential. To address these issues, we propose HiDrop, a framework that aligns token pruning with the true hierarchical function of MLLM layers. HiDrop features two key innovations: (1) Late Injection, which bypasses passive shallow layers to introduce visual tokens exactly where active fusion begins; and (2) Concave Pyramid Pruning with an Early Exit mechanism to dynamically adjust pruning rates across middle and deep layers. This process is optimized via an inter-layer similarity measure and a differentiable top-k operator. To ensure practical efficiency, HiDrop further incorporates persistent positional encoding, FlashAttention-compatible token selection, and parallel decoupling of vision computation to eliminate hidden overhead associated with dynamic token reduction. Extensive experiments show that HiDrop compresses about 90% visual tokens while matching the original performance and accelerating training by 1.72 times. Our work not only sets a new state-of-the-art for efficient MLLM training and inference but also provides valuable insights into the hierarchical nature of multimodal fusion. The code is released at https://github.com/EIT-NLP/HiDrop.

