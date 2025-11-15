---
layout: default
title: Compensating Distribution Drifts in Class-incremental Learning of Pre-trained Vision Transformers
---

# Compensating Distribution Drifts in Class-incremental Learning of Pre-trained Vision Transformers
**arXiv**：[2511.09926v1](https://arxiv.org/abs/2511.09926) · [PDF](https://arxiv.org/pdf/2511.09926.pdf)  
**作者**：Xuan Rao, Simian Xu, Zheng Li, Bo Zhao, Derong Liu, Mingming Ha, Cesare Alippi  

**一句话要点**：提出SLDC方法以补偿类增量学习中的分布漂移

**关键词**：类增量学习, 分布漂移补偿, 知识蒸馏, 序列微调, 特征对齐

## 3 点简述
- 核心问题：序列微调导致特征分布漂移，影响分类器性能
- 方法要点：引入线性与弱非线性算子对齐特征分布，结合知识蒸馏
- 实验或效果：在标准基准上显著提升性能，接近联合训练效果

## 摘要（原文）

> Recent advances have shown that sequential fine-tuning (SeqFT) of pre-trained vision transformers (ViTs), followed by classifier refinement using approximate distributions of class features, can be an effective strategy for class-incremental learning (CIL). However, this approach is susceptible to distribution drift, caused by the sequential optimization of shared backbone parameters. This results in a mismatch between the distributions of the previously learned classes and that of the updater model, ultimately degrading the effectiveness of classifier performance over time. To address this issue, we introduce a latent space transition operator and propose Sequential Learning with Drift Compensation (SLDC). SLDC aims to align feature distributions across tasks to mitigate the impact of drift. First, we present a linear variant of SLDC, which learns a linear operator by solving a regularized least-squares problem that maps features before and after fine-tuning. Next, we extend this with a weakly nonlinear SLDC variant, which assumes that the ideal transition operator lies between purely linear and fully nonlinear transformations. This is implemented using learnable, weakly nonlinear mappings that balance flexibility and generalization. To further reduce representation drift, we apply knowledge distillation (KD) in both algorithmic variants. Extensive experiments on standard CIL benchmarks demonstrate that SLDC significantly improves the performance of SeqFT. Notably, by combining KD to address representation drift with SLDC to compensate distribution drift, SeqFT achieves performance comparable to joint training across all evaluated datasets. Code: https://github.com/raoxuan98-hash/sldc.git.

