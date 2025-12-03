---
layout: default
title: Unrolled Networks are Conditional Probability Flows in MRI Reconstruction
---

# Unrolled Networks are Conditional Probability Flows in MRI Reconstruction
**arXiv**：[2512.03020v1](https://arxiv.org/abs/2512.03020) · [PDF](https://arxiv.org/pdf/2512.03020.pdf)  
**作者**：Kehan Qi, Saumya Gupta, Qingqiao Hu, Weimin Lyu, Chao Chen  

**一句话要点**：提出流对齐训练以提升MRI重建中展开网络的稳定性和效率

**关键词**：MRI重建, 展开网络, 条件概率流ODE, 流对齐训练, 稳定性提升

## 3 点简述
- 核心问题：展开网络在MRI重建中因中间步骤参数自由学习导致演化不稳定
- 方法要点：理论证明展开网络是条件概率流ODE的离散实现，并基于此提出流对齐训练
- 实验或效果：在三个MRI数据集上，流对齐训练比扩散模型迭代少3倍，比展开网络更稳定

## 摘要（原文）

> Magnetic Resonance Imaging (MRI) offers excellent soft-tissue contrast without ionizing radiation, but its long acquisition time limits clinical utility. Recent methods accelerate MRI by under-sampling $k$-space and reconstructing the resulting images using deep learning. Unrolled networks have been widely used for the reconstruction task due to their efficiency, but suffer from unstable evolving caused by freely-learnable parameters in intermediate steps. In contrast, diffusion models based on stochastic differential equations offer theoretical stability in both medical and natural image tasks but are computationally expensive. In this work, we introduce flow ODEs to MRI reconstruction by theoretically proving that unrolled networks are discrete implementations of conditional probability flow ODEs. This connection provides explicit formulations for parameters and clarifies how intermediate states should evolve. Building on this insight, we propose Flow-Aligned Training (FLAT), which derives unrolled parameters from the ODE discretization and aligns intermediate reconstructions with the ideal ODE trajectory to improve stability and convergence. Experiments on three MRI datasets show that FLAT achieves high-quality reconstructions with up to $3\times$ fewer iterations than diffusion-based generative models and significantly greater stability than unrolled networks.

