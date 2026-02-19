---
layout: default
title: Fast and Scalable Analytical Diffusion
---

# Fast and Scalable Analytical Diffusion
**arXiv**：[2602.16498v1](https://arxiv.org/abs/2602.16498) · [PDF](https://arxiv.org/pdf/2602.16498.pdf)  
**作者**：Xinyi Shang, Peng Sun, Jingyu Lin, Zhiqiang Shen  

**一句话要点**：提出GoldDiff框架以解决解析扩散模型推理时全数据集扫描的可扩展性瓶颈

**关键词**：解析扩散模型, 可扩展推理, 后验渐进集中, 黄金子集, 训练免费生成建模, 大规模生成模型

## 3 点简述
- 解析扩散模型推理需全数据集扫描，导致计算成本随数据集规模线性增长
- 发现后验渐进集中现象，提出动态时间感知黄金子集机制，解耦推理复杂度与数据集大小
- 在AFHQ上实现71倍加速，并首次成功扩展至ImageNet-1K，性能匹配或优于基线

## 摘要（原文）

> Analytical diffusion models offer a mathematically transparent path to generative modeling by formulating the denoising score as an empirical-Bayes posterior mean. However, this interpretability comes at a prohibitive cost: the standard formulation necessitates a full-dataset scan at every timestep, scaling linearly with dataset size. In this work, we present the first systematic study addressing this scalability bottleneck. We challenge the prevailing assumption that the entire training data is necessary, uncovering the phenomenon of Posterior Progressive Concentration: the effective golden support of the denoising score is not static but shrinks asymptotically from the global manifold to a local neighborhood as the signal-to-noise ratio increases. Capitalizing on this, we propose Dynamic Time-Aware Golden Subset Diffusion (GoldDiff), a training-free framework that decouples inference complexity from dataset size. Instead of static retrieval, GoldDiff uses a coarse-to-fine mechanism to dynamically pinpoint the ''Golden Subset'' for inference. Theoretically, we derive rigorous bounds guaranteeing that our sparse approximation converges to the exact score. Empirically, GoldDiff achieves a $\bf 71 \times$ speedup on AFHQ while matching or achieving even better performance than full-scan baselines. Most notably, we demonstrate the first successful scaling of analytical diffusion to ImageNet-1K, unlocking a scalable, training-free paradigm for large-scale generative modeling.

