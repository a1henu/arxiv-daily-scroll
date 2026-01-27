---
layout: default
title: Estimating Dense-Packed Zone Height in Liquid-Liquid Separation: A Physics-Informed Neural Network Approach
---

# Estimating Dense-Packed Zone Height in Liquid-Liquid Separation: A Physics-Informed Neural Network Approach
**arXiv**：[2601.18399v1](https://arxiv.org/abs/2601.18399) · [PDF](https://arxiv.org/pdf/2601.18399.pdf)  
**作者**：Mehmet Velioglu, Song Zhai, Alexander Mitsos, Adel Mhamdi, Andreas Jupke, Manuel Dahmen  

**一句话要点**：提出基于物理信息神经网络的液-液分离密集区高度估计方法，以解决测量成本高的问题。

**关键词**：物理信息神经网络, 液-液分离, 密集区高度估计, 扩展卡尔曼滤波器, 两阶段训练

## 3 点简述
- 核心问题：液-液分离中密集区高度测量昂贵且受光学限制，需低成本估计。
- 方法要点：使用物理信息神经网络，先基于低精度机理模型预训练，再用少量实验数据微调。
- 实验或效果：结合扩展卡尔曼滤波器框架，两阶段训练网络在估计精度上优于纯数据驱动方法。

## 摘要（原文）

> Separating liquid-liquid dispersions in gravity settlers is critical in chemical, pharmaceutical, and recycling processes. The dense-packed zone height is an important performance and safety indicator but it is often expensive and impractical to measure due to optical limitations. We propose to estimate phase heights using only inexpensive volume flow measurements. To this end, a physics-informed neural network (PINN) is first pretrained on synthetic data and physics equations derived from a low-fidelity (approximate) mechanistic model to reduce the need for extensive experimental data. While the mechanistic model is used to generate synthetic training data, only volume balance equations are used in the PINN, since the integration of submodels describing droplet coalescence and sedimentation into the PINN would be computationally prohibitive. The pretrained PINN is then fine-tuned with scarce experimental data to capture the actual dynamics of the separator. We then employ the differentiable PINN as a predictive model in an Extended Kalman Filter inspired state estimation framework, enabling the phase heights to be tracked and updated from flow-rate measurements. We first test the two-stage trained PINN by forward simulation from a known initial state against the mechanistic model and a non-pretrained PINN. We then evaluate phase height estimation performance with the filter, comparing the two-stage trained PINN with a two-stage trained purely data-driven neural network. All model types are trained and evaluated using ensembles to account for model parameter uncertainty. In all evaluations, the two-stage trained PINN yields the most accurate phase-height estimates.

