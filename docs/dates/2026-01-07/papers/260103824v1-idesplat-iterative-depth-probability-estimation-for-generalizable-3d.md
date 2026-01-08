---
layout: default
title: IDESplat: Iterative Depth Probability Estimation for Generalizable 3D Gaussian Splatting
---

# IDESplat: Iterative Depth Probability Estimation for Generalizable 3D Gaussian Splatting
**arXiv**：[2601.03824v1](https://arxiv.org/abs/2601.03824) · [PDF](https://arxiv.org/pdf/2601.03824.pdf)  
**作者**：Wei Long, Haifeng Wu, Shiyin Jiang, Jinhua Zhang, Xinchun Ji, Shuhang Gu  

**一句话要点**：提出IDESplat，通过迭代深度概率估计提升通用3D高斯泼溅的准确性

**关键词**：3D高斯泼溅, 深度概率估计, 迭代优化, 通用场景重建, 实时渲染

## 3 点简述
- 核心问题：现有方法单次扭曲估计深度概率，导致深度图不稳定且粗糙，影响高斯均值预测。
- 方法要点：引入深度概率提升单元，通过级联扭曲操作以乘法方式整合极线注意力图，并堆叠多个单元迭代优化深度候选。
- 实验或效果：在RealEstate10K等数据集上实现优异重建质量，PSNR提升0.33 dB，参数和内存使用显著减少，跨数据集泛化能力强。

## 摘要（原文）

> Generalizable 3D Gaussian Splatting aims to directly predict Gaussian parameters using a feed-forward network for scene reconstruction. Among these parameters, Gaussian means are particularly difficult to predict, so depth is usually estimated first and then unprojected to obtain the Gaussian sphere centers. Existing methods typically rely solely on a single warp to estimate depth probability, which hinders their ability to fully leverage cross-view geometric cues, resulting in unstable and coarse depth maps. To address this limitation, we propose IDESplat, which iteratively applies warp operations to boost depth probability estimation for accurate Gaussian mean prediction. First, to eliminate the inherent instability of a single warp, we introduce a Depth Probability Boosting Unit (DPBU) that integrates epipolar attention maps produced by cascading warp operations in a multiplicative manner. Next, we construct an iterative depth estimation process by stacking multiple DPBUs, progressively identifying potential depth candidates with high likelihood. As IDESplat iteratively boosts depth probability estimates and updates the depth candidates, the depth map is gradually refined, resulting in accurate Gaussian means. We conduct experiments on RealEstate10K, ACID, and DL3DV. IDESplat achieves outstanding reconstruction quality and state-of-the-art performance with real-time efficiency. On RE10K, it outperforms DepthSplat by 0.33 dB in PSNR, using only 10.7% of the parameters and 70% of the memory. Additionally, our IDESplat improves PSNR by 2.95 dB over DepthSplat on the DTU dataset in cross-dataset experiments, demonstrating its strong generalization ability.

