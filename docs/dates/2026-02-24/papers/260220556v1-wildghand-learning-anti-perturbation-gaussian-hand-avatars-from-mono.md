---
layout: default
title: WildGHand: Learning Anti-Perturbation Gaussian Hand Avatars from Monocular In-the-Wild Videos
---

# WildGHand: Learning Anti-Perturbation Gaussian Hand Avatars from Monocular In-the-Wild Videos
**arXiv**：[2602.20556v1](https://arxiv.org/abs/2602.20556) · [PDF](https://arxiv.org/pdf/2602.20556.pdf)  
**作者**：Hanhui Li, Xuan Huang, Wanquan Liu, Yuhao Cheng, Long Chen, Yiqiang Yan, Xiaodan Liang, Chenqiang Gao  

**一句话要点**：提出WildGHand框架，通过动态扰动解耦和扰动感知优化，从单目野外视频中学习抗扰动的3D高斯手部化身。

**关键词**：3D手部重建, 高斯溅射, 扰动解耦, 单目视频, 野外场景, 优化框架

## 3 点简述
- 核心问题：现有方法在野外视频中因手-物交互、极端姿态等扰动而性能下降。
- 方法要点：引入动态扰动解耦模块和扰动感知优化策略，在时空维度抑制扰动。
- 实验或效果：在自建和公共数据集上实现SOTA，PSNR相对提升达15.8%，LPIPS相对降低23.1%。

## 摘要（原文）

> Despite recent progress in 3D hand reconstruction from monocular videos, most existing methods rely on data captured in well-controlled environments and therefore degrade in real-world settings with severe perturbations, such as hand-object interactions, extreme poses, illumination changes, and motion blur. To tackle these issues, we introduce WildGHand, an optimization-based framework that enables self-adaptive 3D Gaussian splatting on in-the-wild videos and produces high-fidelity hand avatars. WildGHand incorporates two key components: (i) a dynamic perturbation disentanglement module that explicitly represents perturbations as time-varying biases on 3D Gaussian attributes during optimization, and (ii) a perturbation-aware optimization strategy that generates per-frame anisotropic weighted masks to guide optimization. Together, these components allow the framework to identify and suppress perturbations across both spatial and temporal dimensions. We further curate a dataset of monocular hand videos captured under diverse perturbations to benchmark in-the-wild hand avatar reconstruction. Extensive experiments on this dataset and two public datasets demonstrate that WildGHand achieves state-of-the-art performance and substantially improves over its base model across multiple metrics (e.g., up to a $15.8\%$ relative gain in PSNR and a $23.1\%$ relative reduction in LPIPS). Our implementation and dataset are available at https://github.com/XuanHuang0/WildGHand.

