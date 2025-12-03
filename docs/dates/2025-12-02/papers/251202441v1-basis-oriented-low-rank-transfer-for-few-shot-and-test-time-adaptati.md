---
layout: default
title: Basis-Oriented Low-rank Transfer for Few-Shot and Test-Time Adaptation
---

# Basis-Oriented Low-rank Transfer for Few-Shot and Test-Time Adaptation
**arXiv**：[2512.02441v1](https://arxiv.org/abs/2512.02441) · [PDF](https://arxiv.org/pdf/2512.02441.pdf)  
**作者**：Junghwan Park, Woojin Cho, Junhyuk Heo, Darongsae Kwon, Kookjin Lee  

**一句话要点**：提出BOLT框架，通过提取正交任务谱基实现少样本和测试时适应

**关键词**：少样本适应, 测试时适应, 低秩迁移, 正交谱基, 参数高效微调

## 3 点简述
- 核心问题：在数据与计算受限下，如何高效迁移预训练模型到新任务，避免元学习的高成本与不稳定性
- 方法要点：离线阶段从多任务向量提取正交谱基，在线阶段冻结基并训练少量对角系数进行低秩更新
- 实验或效果：在实验中，BOLT提供强初始化，参数高效微调性能优于常见PEFT基线和元学习初始化

## 摘要（原文）

> Adapting large pre-trained models to unseen tasks under tight data and compute budgets remains challenging. Meta-learning approaches explicitly learn good initializations, but they require an additional meta-training phase over many tasks, incur high training cost, and can be unstable. At the same time, the number of task-specific pre-trained models continues to grow, yet the question of how to transfer them to new tasks with minimal additional training remains relatively underexplored. We propose BOLT (Basis-Oriented Low-rank Transfer), a framework that reuses existing fine-tuned models not by merging weights, but instead by extracting an orthogonal, task-informed spectral basis and adapting within that subspace. In the offline phase, BOLT collects dominant singular directions from multiple task vectors and orthogonalizes them per layer to form reusable bases. In the online phase, we freeze these bases and train only a small set of diagonal coefficients per layer for the new task, yielding a rank-controlled update with very few trainable parameters. This design provides (i) a strong, training-free initialization for unseen tasks, obtained by pooling source-task coefficients, along with a lightweight rescaling step while leveraging the shared orthogonal bases, and (ii) a parameter-efficient fine-tuning (PEFT) path that, in our experiments, achieves robust performance compared to common PEFT baselines as well as a representative meta-learned initialization. Our results show that constraining adaptation to a task-informed orthogonal subspace provides an effective alternative for unseen-task transfer.

