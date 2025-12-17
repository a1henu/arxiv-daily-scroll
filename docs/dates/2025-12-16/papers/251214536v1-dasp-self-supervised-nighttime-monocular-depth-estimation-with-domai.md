---
layout: default
title: DASP: Self-supervised Nighttime Monocular Depth Estimation with Domain Adaptation of Spatiotemporal Priors
---

# DASP: Self-supervised Nighttime Monocular Depth Estimation with Domain Adaptation of Spatiotemporal Priors
**arXiv**：[2512.14536v1](https://arxiv.org/abs/2512.14536) · [PDF](https://arxiv.org/pdf/2512.14536.pdf)  
**作者**：Yiheng Huang, Junhong Chen, Anqi Ning, Zhanhong Liang, Nick Michiels, Luc Claesen, Wenyin Liu  

**一句话要点**：提出DASP框架，利用时空先验进行自监督夜间单目深度估计

**关键词**：夜间深度估计, 自监督学习, 时空先验, 对抗网络, 3D一致性投影

## 3 点简述
- 核心问题：夜间低可见度和动态物体导致纹理缺失和模糊区域，使自监督深度估计性能下降。
- 方法要点：设计对抗分支提取时空先验，结合空间-时间学习模块和轴向空间学习模块，并引入3D一致性投影损失优化结构一致性。
- 实验或效果：在Oxford RobotCar和nuScenes数据集上实现最先进性能，消融研究验证各组件有效性。

## 摘要（原文）

> Self-supervised monocular depth estimation has achieved notable success under daytime conditions. However, its performance deteriorates markedly at night due to low visibility and varying illumination, e.g., insufficient light causes textureless areas, and moving objects bring blurry regions. To this end, we propose a self-supervised framework named DASP that leverages spatiotemporal priors for nighttime depth estimation. Specifically, DASP consists of an adversarial branch for extracting spatiotemporal priors and a self-supervised branch for learning. In the adversarial branch, we first design an adversarial network where the discriminator is composed of four devised spatiotemporal priors learning blocks (SPLB) to exploit the daytime priors. In particular, the SPLB contains a spatial-based temporal learning module (STLM) that uses orthogonal differencing to extract motion-related variations along the time axis and an axial spatial learning module (ASLM) that adopts local asymmetric convolutions with global axial attention to capture the multiscale structural information. By combining STLM and ASLM, our model can acquire sufficient spatiotemporal features to restore textureless areas and estimate the blurry regions caused by dynamic objects. In the self-supervised branch, we propose a 3D consistency projection loss to bilaterally project the target frame and source frame into a shared 3D space, and calculate the 3D discrepancy between the two projected frames as a loss to optimize the 3D structural consistency and daytime priors. Extensive experiments on the Oxford RobotCar and nuScenes datasets demonstrate that our approach achieves state-of-the-art performance for nighttime depth estimation. Ablation studies further validate the effectiveness of each component.

