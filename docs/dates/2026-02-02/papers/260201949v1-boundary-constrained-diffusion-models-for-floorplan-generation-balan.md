---
layout: default
title: Boundary-Constrained Diffusion Models for Floorplan Generation: Balancing Realism and Diversity
---

# Boundary-Constrained Diffusion Models for Floorplan Generation: Balancing Realism and Diversity
**arXiv**：[2602.01949v1](https://arxiv.org/abs/2602.01949) · [PDF](https://arxiv.org/pdf/2602.01949.pdf)  
**作者**：Leonardo Stoppani, Davide Bacciu, Shahab Mokarizadeh  

**一句话要点**：提出边界约束扩散模型与多样性评分，以平衡建筑平面图生成的真实性与多样性。

**关键词**：扩散模型, 建筑平面图生成, 边界约束, 多样性评估, 几何一致性, 生成对抗网络

## 3 点简述
- 核心问题：扩散模型在建筑平面图生成中，优化FID导致设计多样性受限，且几何一致性不足。
- 方法要点：引入边界交叉注意力模块增强边界一致性，并提出多样性评分量化约束下的布局多样性。
- 实验或效果：BCA显著提升边界遵循，长时间训练揭示真实性与多样性的权衡，模型依赖数据集先验。

## 摘要（原文）

> Diffusion models have become widely popular for automated floorplan generation, producing highly realistic layouts conditioned on user-defined constraints. However, optimizing for perceptual metrics such as the Fréchet Inception Distance (FID) causes limited design diversity. To address this, we propose the Diversity Score (DS), a metric that quantifies layout diversity under fixed constraints. Moreover, to improve geometric consistency, we introduce a Boundary Cross-Attention (BCA) module that enables conditioning on building boundaries. Our experiments show that BCA significantly improves boundary adherence, while prolonged training drives diversity collapse undiagnosed by FID, revealing a critical trade-off between realism and diversity. Out-Of-Distribution evaluations further demonstrate the models' reliance on dataset priors, emphasizing the need for generative systems that explicitly balance fidelity, diversity, and generalization in architectural design tasks.

