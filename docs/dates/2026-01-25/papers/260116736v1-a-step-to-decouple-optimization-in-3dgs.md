---
layout: default
title: A Step to Decouple Optimization in 3DGS
---

# A Step to Decouple Optimization in 3DGS
**arXiv**：[2601.16736v1](https://arxiv.org/abs/2601.16736) · [PDF](https://arxiv.org/pdf/2601.16736.pdf)  
**作者**：Renjie Ding, Yaonan Wang, Min Liu, Jialin Zhu, Jiazheng Wang, Jiahao Zhao, Wenting Shen, Feixiang He, Xiang Che  

**一句话要点**：提出AdamW-GS以优化3D高斯泼溅的耦合问题，提升效率与表示效果

**关键词**：3D高斯泼溅, 优化解耦, AdamW-GS, 正则化, 实时新视角合成, 梯度耦合

## 3 点简述
- 核心问题：3DGS优化中存在更新步耦合与梯度耦合，导致效率低下与正则化不当
- 方法要点：通过稀疏Adam、重状态正则化和解耦属性正则化来分解优化过程
- 实验或效果：在3DGS和3DGS-MCMC框架下验证，AdamW-GS同时提升优化效率和表示有效性

## 摘要（原文）

> 3D Gaussian Splatting (3DGS) has emerged as a powerful technique for real-time novel view synthesis. As an explicit representation optimized through gradient propagation among primitives, optimization widely accepted in deep neural networks (DNNs) is actually adopted in 3DGS, such as synchronous weight updating and Adam with the adaptive gradient. However, considering the physical significance and specific design in 3DGS, there are two overlooked details in the optimization of 3DGS: (i) update step coupling, which induces optimizer state rescaling and costly attribute updates outside the viewpoints, and (ii) gradient coupling in the moment, which may lead to under- or over-effective regularization. Nevertheless, such a complex coupling is under-explored. After revisiting the optimization of 3DGS, we take a step to decouple it and recompose the process into: Sparse Adam, Re-State Regularization and Decoupled Attribute Regularization. Taking a large number of experiments under the 3DGS and 3DGS-MCMC frameworks, our work provides a deeper understanding of these components. Finally, based on the empirical analysis, we re-design the optimization and propose AdamW-GS by re-coupling the beneficial components, under which better optimization efficiency and representation effectiveness are achieved simultaneously.

