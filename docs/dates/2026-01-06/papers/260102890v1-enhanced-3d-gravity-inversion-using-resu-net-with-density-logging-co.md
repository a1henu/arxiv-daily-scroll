---
layout: default
title: Enhanced 3D Gravity Inversion Using ResU-Net with Density Logging Constraints: A Dual-Phase Training Approach
---

# Enhanced 3D Gravity Inversion Using ResU-Net with Density Logging Constraints: A Dual-Phase Training Approach
**arXiv**：[2601.02890v1](https://arxiv.org/abs/2601.02890) · [PDF](https://arxiv.org/pdf/2601.02890.pdf)  
**作者**：Siyuan Dong, Jinghuai Gao, Shuai Zhou, Baohai Wu, Hongfa Jia  

**一句话要点**：提出基于ResU-Net和密度测井约束的双阶段训练方法，以增强3D重力反演精度

**关键词**：3D重力反演, 深度学习, 密度测井约束, 双阶段训练, ResU-Net, 地球物理勘探

## 3 点简述
- 现有数据驱动深度学习重力反演方法因先验信息不足，导致数据拟合误差大和结果不可靠
- 引入深度加权函数和密度测井信息，通过双阶段训练优化网络，提升反演性能
- 在合成模型和实测数据上验证，相比无约束方法显著改善反演质量，并与传统方法对比分析

## 摘要（原文）

> Gravity exploration has become an important geophysical method due to its low cost and high efficiency. With the rise of artificial intelligence, data-driven gravity inversion methods based on deep learning (DL) possess physical property recovery capabilities that conventional regularization methods lack. However, existing DL methods suffer from insufficient prior information constraints, which leads to inversion models with large data fitting errors and unreliable results. Moreover, the inversion results lack constraints and matching from other exploration methods, leading to results that may contradict known geological conditions. In this study, we propose a novel approach that integrates prior density well logging information to address the above issues. First, we introduce a depth weighting function to the neural network (NN) and train it in the weighted density parameter domain. The NN, under the constraint of the weighted forward operator, demonstrates improved inversion performance, with the resulting inversion model exhibiting smaller data fitting errors. Next, we divide the entire network training into two phases: first training a large pre-trained network Net-I, and then using the density logging information as the constraint to get the optimized fine-tuning network Net-II. Through testing and comparison in synthetic models and Bishop Model, the inversion quality of our method has significantly improved compared to the unconstrained data-driven DL inversion method. Additionally, we also conduct a comparison and discussion between our method and both the conventional focusing inversion (FI) method and its well logging constrained variant. Finally, we apply this method to the measured data from the San Nicolas mining area in Mexico, comparing and analyzing it with two recent gravity inversion methods based on DL.

