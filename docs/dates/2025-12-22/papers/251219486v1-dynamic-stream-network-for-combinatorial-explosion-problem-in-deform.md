---
layout: default
title: Dynamic Stream Network for Combinatorial Explosion Problem in Deformable Medical Image Registration
---

# Dynamic Stream Network for Combinatorial Explosion Problem in Deformable Medical Image Registration
**arXiv**：[2512.19486v1](https://arxiv.org/abs/2512.19486) · [PDF](https://arxiv.org/pdf/2512.19486.pdf)  
**作者**：Shaochen Bi, Yuting He, Weiming Wang, Hao Chen  

**一句话要点**：提出动态流网络以解决可变形医学图像配准中的组合爆炸问题

**关键词**：可变形医学图像配准, 组合爆炸问题, 动态网络, 自适应感受野, 动态注意力, 特征建模

## 3 点简述
- 核心问题：双输入导致特征组合关系指数增长，干扰特征建模。
- 方法要点：通过自适应流池模块和动态流注意力机制动态调整感受野和权重。
- 实验或效果：在可变形医学图像配准任务中优于现有先进方法，展现强泛化能力。

## 摘要（原文）

> Combinatorial explosion problem caused by dual inputs presents a critical challenge in Deformable Medical Image Registration (DMIR). Since DMIR processes two images simultaneously as input, the combination relationships between features has grown exponentially, ultimately the model considers more interfering features during the feature modeling process. Introducing dynamics in the receptive fields and weights of the network enable the model to eliminate the interfering features combination and model the potential feature combination relationships. In this paper, we propose the Dynamic Stream Network (DySNet), which enables the receptive fields and weights to be dynamically adjusted. This ultimately enables the model to ignore interfering feature combinations and model the potential feature relationships. With two key innovations: 1) Adaptive Stream Basin (AdSB) module dynamically adjusts the shape of the receptive field, thereby enabling the model to focus on the feature relationships with greater correlation. 2) Dynamic Stream Attention (DySA) mechanism generates dynamic weights to search for more valuable feature relationships. Extensive experiments have shown that DySNet consistently outperforms the most advanced DMIR methods, highlighting its outstanding generalization ability. Our code will be released on the website: https://github.com/ShaochenBi/DySNet.

