---
layout: default
title: G3Splat: Geometrically Consistent Generalizable Gaussian Splatting
---

# G3Splat: Geometrically Consistent Generalizable Gaussian Splatting
**arXiv**：[2512.17547v1](https://arxiv.org/abs/2512.17547) · [PDF](https://arxiv.org/pdf/2512.17547.pdf)  
**作者**：Mehdi Hosseinzadeh, Shin-Fang Chng, Yi Xu, Simon Lucey, Ian Reid, Ravi Garg  

**一句话要点**：提出G3Splat以解决自监督下3D高斯溅射的几何模糊问题，实现几何一致的可泛化场景表示。

**关键词**：3D高斯溅射, 几何一致性, 自监督学习, 新视图合成, 相对姿态估计, 零样本泛化

## 3 点简述
- 核心问题：仅依赖视图合成损失无法恢复几何有意义的3D高斯溅射，存在几何模糊。
- 方法要点：引入几何先验，强制几何一致性，提升自监督下3D高斯溅射的几何重建质量。
- 实验或效果：在RE10K上训练，在几何重建、相对姿态估计和新视图合成方面达到SOTA，并在ScanNet上展示强零样本泛化能力。

## 摘要（原文）

> 3D Gaussians have recently emerged as an effective scene representation for real-time splatting and accurate novel-view synthesis, motivating several works to adapt multi-view structure prediction networks to regress per-pixel 3D Gaussians from images. However, most prior work extends these networks to predict additional Gaussian parameters -- orientation, scale, opacity, and appearance -- while relying almost exclusively on view-synthesis supervision. We show that a view-synthesis loss alone is insufficient to recover geometrically meaningful splats in this setting. We analyze and address the ambiguities of learning 3D Gaussian splats under self-supervision for pose-free generalizable splatting, and introduce G3Splat, which enforces geometric priors to obtain geometrically consistent 3D scene representations. Trained on RE10K, our approach achieves state-of-the-art performance in (i) geometrically consistent reconstruction, (ii) relative pose estimation, and (iii) novel-view synthesis. We further demonstrate strong zero-shot generalization on ScanNet, substantially outperforming prior work in both geometry recovery and relative pose estimation. Code and pretrained models are released on our project page (https://m80hz.github.io/g3splat/).

