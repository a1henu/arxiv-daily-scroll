---
layout: default
title: RobustSplat++: Decoupling Densification, Dynamics, and Illumination for In-the-Wild 3DGS
---

# RobustSplat++: Decoupling Densification, Dynamics, and Illumination for In-the-Wild 3DGS
**arXiv**：[2512.04815v1](https://arxiv.org/abs/2512.04815) · [PDF](https://arxiv.org/pdf/2512.04815.pdf)  
**作者**：Chuanyu Fu, Guanying Chen, Yuqi Zhang, Kunbin Yao, Yuan Xiong, Chuan Huang, Shuguang Cui, Yasuyuki Matsushita, Xiaochun Cao  

**一句话要点**：提出RobustSplat++以解决野外场景中瞬态物体和光照变化导致的3D高斯溅射渲染伪影问题

**关键词**：3D高斯溅射, 野外场景建模, 瞬态物体处理, 光照变化建模, 延迟高斯增长, 掩码引导

## 3 点简述
- 核心问题：现有3DGS方法在野外场景中因高斯致密化过程无意建模瞬态扰动和光照变化，导致渲染伪影
- 方法要点：采用延迟高斯增长策略优先优化静态结构，结合尺度级联掩码引导提升瞬态掩码估计精度
- 实验或效果：在多个挑战性数据集上超越现有方法，验证了方法的鲁棒性和有效性

## 摘要（原文）

> 3D Gaussian Splatting (3DGS) has gained significant attention for its real-time, photo-realistic rendering in novel-view synthesis and 3D modeling. However, existing methods struggle with accurately modeling in-the-wild scenes affected by transient objects and illuminations, leading to artifacts in the rendered images. We identify that the Gaussian densification process, while enhancing scene detail capture, unintentionally contributes to these artifacts by growing additional Gaussians that model transient disturbances and illumination variations. To address this, we propose RobustSplat++, a robust solution based on several critical designs. First, we introduce a delayed Gaussian growth strategy that prioritizes optimizing static scene structure before allowing Gaussian splitting/cloning, mitigating overfitting to transient objects in early optimization. Second, we design a scale-cascaded mask bootstrapping approach that first leverages lower-resolution feature similarity supervision for reliable initial transient mask estimation, taking advantage of its stronger semantic consistency and robustness to noise, and then progresses to high-resolution supervision to achieve more precise mask prediction. Third, we incorporate the delayed Gaussian growth strategy and mask bootstrapping with appearance modeling to handling in-the-wild scenes including transients and illuminations. Extensive experiments on multiple challenging datasets show that our method outperforms existing methods, clearly demonstrating the robustness and effectiveness of our method.

