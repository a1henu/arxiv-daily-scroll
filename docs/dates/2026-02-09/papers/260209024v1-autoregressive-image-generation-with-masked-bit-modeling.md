---
layout: default
title: Autoregressive Image Generation with Masked Bit Modeling
---

# Autoregressive Image Generation with Masked Bit Modeling
**arXiv**：[2602.09024v1](https://arxiv.org/abs/2602.09024) · [PDF](https://arxiv.org/pdf/2602.09024.pdf)  
**作者**：Qihang Yu, Qihao Liu, Ju He, Xinyang Zhang, Yang Liu, Liang-Chieh Chen, Xi Chen  

**一句话要点**：提出掩码位自回归建模以解决离散生成方法在扩展码本时的性能与成本问题

**关键词**：图像生成, 自回归建模, 离散表示, 码本扩展, 掩码预测

## 3 点简述
- 核心问题：离散与连续视觉生成方法的性能差距源于潜在空间比特分配而非离散化本身
- 方法要点：通过掩码位自回归建模支持任意码本大小，预测离散令牌的组成比特
- 实验或效果：在ImageNet-256上实现gFID 0.99，超越现有方法，降低采样成本并加速收敛

## 摘要（原文）

> This paper challenges the dominance of continuous pipelines in visual generation. We systematically investigate the performance gap between discrete and continuous methods. Contrary to the belief that discrete tokenizers are intrinsically inferior, we demonstrate that the disparity arises primarily from the total number of bits allocated in the latent space (i.e., the compression ratio). We show that scaling up the codebook size effectively bridges this gap, allowing discrete tokenizers to match or surpass their continuous counterparts. However, existing discrete generation methods struggle to capitalize on this insight, suffering from performance degradation or prohibitive training costs with scaled codebook. To address this, we propose masked Bit AutoRegressive modeling (BAR), a scalable framework that supports arbitrary codebook sizes. By equipping an autoregressive transformer with a masked bit modeling head, BAR predicts discrete tokens through progressively generating their constituent bits. BAR achieves a new state-of-the-art gFID of 0.99 on ImageNet-256, outperforming leading methods across both continuous and discrete paradigms, while significantly reducing sampling costs and converging faster than prior continuous approaches. Project page is available at https://bar-gen.github.io/

