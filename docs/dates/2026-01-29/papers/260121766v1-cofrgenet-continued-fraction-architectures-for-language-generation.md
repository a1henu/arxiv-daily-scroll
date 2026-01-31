---
layout: default
title: CoFrGeNet: Continued Fraction Architectures for Language Generation
---

# CoFrGeNet: Continued Fraction Architectures for Language Generation
**arXiv**：[2601.21766v1](https://arxiv.org/abs/2601.21766) · [PDF](https://arxiv.org/pdf/2601.21766.pdf)  
**作者**：Amit Dhurandhar, Vijil Chenthamarakshan, Dennis Wei, Tejaswini Pedapati, Karthikeyan Natesan Ramamurthy, Rahul Nair  

**一句话要点**：提出连分数生成网络以替代Transformer组件，减少参数并保持性能。

**关键词**：语言生成, 连分数架构, 参数效率, Transformer替代, 梯度优化

## 3 点简述
- 核心问题：Transformer在语言生成中参数多、训练成本高。
- 方法要点：基于连分数设计新架构，替换多头注意力和前馈网络。
- 实验或效果：在GPT2-xl和Llama3上验证，参数减少至2/3到1/2，性能竞争或更优。

## 摘要（原文）

> Transformers are arguably the preferred architecture for language generation. In this paper, inspired by continued fractions, we introduce a new function class for generative modeling. The architecture family implementing this function class is named CoFrGeNets - Continued Fraction Generative Networks. We design novel architectural components based on this function class that can replace Multi-head Attention and Feed-Forward Networks in Transformer blocks while requiring much fewer parameters. We derive custom gradient formulations to optimize the proposed components more accurately and efficiently than using standard PyTorch-based gradients. Our components are a plug-in replacement requiring little change in training or inference procedures that have already been put in place for Transformer-based models thus making our approach easy to incorporate in large industrial workflows. We experiment on two very different transformer architectures GPT2-xl (1.5B) and Llama3 (3.2B), where the former we pre-train on OpenWebText and GneissWeb, while the latter we pre-train on the docling data mix which consists of nine different datasets. Results show that the performance on downstream classification, Q\& A, reasoning and text understanding tasks of our models is competitive and sometimes even superior to the original models with $\frac{2}{3}$ to $\frac{1}{2}$ the parameters and shorter pre-training time. We believe that future implementations customized to hardware will further bring out the true potential of our architectures.

