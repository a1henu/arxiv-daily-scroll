---
layout: default
title: Physics-Inspired Gaussian Kolmogorov-Arnold Networks for X-ray Scatter Correction in Cone-Beam CT
---

# Physics-Inspired Gaussian Kolmogorov-Arnold Networks for X-ray Scatter Correction in Cone-Beam CT
**arXiv**：[2510.24579v1](https://arxiv.org/abs/2510.24579) · [PDF](https://arxiv.org/pdf/2510.24579.pdf)  
**作者**：Xu Jiang, Huiying Pan, Ligen Shi, Jianing Sun, Wenfeng Xu, Xing Zhao  

**一句话要点**：提出基于物理先验的Gaussian KAN网络以校正锥束CT中的X射线散射伪影

**关键词**：锥束CT, 散射校正, 高斯径向基函数, Kolmogorov-Arnold网络, 物理先验, 深度学习

## 3 点简述
- 锥束CT成像中散射导致CT值偏差和组织对比度降低，影响诊断准确性。
- 方法利用散射概率分布的旋转对称性，用高斯RBF建模并嵌入KAN层学习高维特征。
- 合成和真实扫描实验验证模型有效校正散射伪影，定量指标优于现有方法。

## 摘要（原文）

> Cone-beam CT (CBCT) employs a flat-panel detector to achieve
> three-dimensional imaging with high spatial resolution. However, CBCT is
> susceptible to scatter during data acquisition, which introduces CT value bias
> and reduced tissue contrast in the reconstructed images, ultimately degrading
> diagnostic accuracy. To address this issue, we propose a deep learning-based
> scatter artifact correction method inspired by physical prior knowledge.
> Leveraging the fact that the observed point scatter probability density
> distribution exhibits rotational symmetry in the projection domain. The method
> uses Gaussian Radial Basis Functions (RBF) to model the point scatter function
> and embeds it into the Kolmogorov-Arnold Networks (KAN) layer, which provides
> efficient nonlinear mapping capabilities for learning high-dimensional scatter
> features. By incorporating the physical characteristics of the scattered photon
> distribution together with the complex function mapping capacity of KAN, the
> model improves its ability to accurately represent scatter. The effectiveness
> of the method is validated through both synthetic and real-scan experiments.
> Experimental results show that the model can effectively correct the scatter
> artifacts in the reconstructed images and is superior to the current methods in
> terms of quantitative metrics.

