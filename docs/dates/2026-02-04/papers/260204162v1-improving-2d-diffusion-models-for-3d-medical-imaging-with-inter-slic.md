---
layout: default
title: Improving 2D Diffusion Models for 3D Medical Imaging with Inter-Slice Consistent Stochasticity
---

# Improving 2D Diffusion Models for 3D Medical Imaging with Inter-Slice Consistent Stochasticity
**arXiv**：[2602.04162v1](https://arxiv.org/abs/2602.04162) · [PDF](https://arxiv.org/pdf/2602.04162.pdf)  
**作者**：Chenhe Du, Qing Wu, Xuanyu Tian, Jingyi Yu, Hongjiang Wei, Yuyao Zhang  

**一句话要点**：提出ISCS方法以解决基于2D扩散模型的3D医学成像中切片间不连续性问题

**关键词**：3D医学成像, 扩散模型, 切片一致性, 随机性控制, 图像重建

## 3 点简述
- 核心问题：2D扩散模型重建3D医学图像时，扩散采样的随机性导致切片间严重不连续
- 方法要点：通过控制扩散采样中随机噪声成分的一致性，实现切片间对齐，无需额外损失或优化
- 实验或效果：在多个医学成像任务中有效提升性能，方法即插即用且无额外计算成本

## 摘要（原文）

> 3D medical imaging is in high demand and essential for clinical diagnosis and scientific research. Currently, diffusion models (DMs) have become an effective tool for medical imaging reconstruction thanks to their ability to learn rich, high-quality data priors. However, learning the 3D data distribution with DMs in medical imaging is challenging, not only due to the difficulties in data collection but also because of the significant computational burden during model training. A common compromise is to train the DMs on 2D data priors and reconstruct stacked 2D slices to address 3D medical inverse problems. However, the intrinsic randomness of diffusion sampling causes severe inter-slice discontinuities of reconstructed 3D volumes. Existing methods often enforce continuity regularizations along the z-axis, which introduces sensitive hyper-parameters and may lead to over-smoothing results. In this work, we revisit the origin of stochasticity in diffusion sampling and introduce Inter-Slice Consistent Stochasticity (ISCS), a simple yet effective strategy that encourages interslice consistency during diffusion sampling. Our key idea is to control the consistency of stochastic noise components during diffusion sampling, thereby aligning their sampling trajectories without adding any new loss terms or optimization steps. Importantly, the proposed ISCS is plug-and-play and can be dropped into any 2D trained diffusion based 3D reconstruction pipeline without additional computational cost. Experiments on several medical imaging problems show that our method can effectively improve the performance of medical 3D imaging problems based on 2D diffusion models. Our findings suggest that controlling inter-slice stochasticity is a principled and practically attractive route toward high-fidelity 3D medical imaging with 2D diffusion priors. The code is available at: https://github.com/duchenhe/ISCS

