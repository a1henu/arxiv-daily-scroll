---
layout: default
title: CaRF: Enhancing Multi-View Consistency in Referring 3D Gaussian Splatting Segmentation
---

# CaRF: Enhancing Multi-View Consistency in Referring 3D Gaussian Splatting Segmentation
**arXiv**：[2511.03992v1](https://arxiv.org/abs/2511.03992) · [PDF](https://arxiv.org/pdf/2511.03992.pdf)  
**作者**：Yuwen Tao, Kanglei Zhou, Xin Tan, Yuan Xie  

**一句话要点**：提出CaRF框架以增强多视图一致性在参考3D高斯溅射分割中

**关键词**：3D高斯溅射分割, 多视图一致性, 相机几何编码, 跨模态对齐, 视图监督优化

## 3 点简述
- 核心问题：现有方法依赖2D渲染伪监督和视图特定特征，导致跨视图一致性差。
- 方法要点：引入高斯场相机编码和训练配对视图监督，直接建模视图依赖变化。
- 实验或效果：在多个基准测试中mIoU平均提升16.8%、4.3%和2.0%。

## 摘要（原文）

> Referring 3D Gaussian Splatting Segmentation (R3DGS) aims to interpret
> free-form language expressions and localize the corresponding 3D regions in
> Gaussian fields. While recent advances have introduced cross-modal alignment
> between language and 3D geometry, existing pipelines still struggle with
> cross-view consistency due to their reliance on 2D rendered pseudo supervision
> and view specific feature learning. In this work, we present Camera Aware
> Referring Field (CaRF), a fully differentiable framework that operates directly
> in the 3D Gaussian space and achieves multi view consistency. Specifically,
> CaRF introduces Gaussian Field Camera Encoding (GFCE), which incorporates
> camera geometry into Gaussian text interactions to explicitly model view
> dependent variations and enhance geometric reasoning. Building on this, In
> Training Paired View Supervision (ITPVS) is proposed to align per Gaussian
> logits across calibrated views during training, effectively mitigating single
> view overfitting and exposing inter view discrepancies for optimization.
> Extensive experiments on three representative benchmarks demonstrate that CaRF
> achieves average improvements of 16.8%, 4.3%, and 2.0% in mIoU over state of
> the art methods on the Ref LERF, LERF OVS, and 3D OVS datasets, respectively.
> Moreover, this work promotes more reliable and view consistent 3D scene
> understanding, with potential benefits for embodied AI, AR/VR interaction, and
> autonomous perception.

