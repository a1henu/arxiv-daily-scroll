---
layout: default
title: Morphing Through Time: Diffusion-Based Bridging of Temporal Gaps for Robust Alignment in Change Detection
---

# Morphing Through Time: Diffusion-Based Bridging of Temporal Gaps for Robust Alignment in Change Detection
**arXiv**：[2511.07976v1](https://arxiv.org/abs/2511.07976) · [PDF](https://arxiv.org/pdf/2511.07976.pdf)  
**作者**：Seyedehanita Madani, Vishal M. Patel  

**一句话要点**：提出扩散式语义变形模块以解决遥感变化检测中的时空错位问题

**关键词**：遥感变化检测, 扩散模型, 图像配准, 时空鲁棒性, 模块化框架

## 3 点简述
- 核心问题：遥感变化检测中，双时相图像因季节或多年间隔导致空间错位，影响检测鲁棒性。
- 方法要点：集成扩散模型生成中间变形帧，结合密集配准和残差流优化，实现高保真图像配准。
- 实验或效果：在多个数据集上验证，提升配准精度和变化检测性能，无需修改现有检测网络。

## 摘要（原文）

> Remote sensing change detection is often challenged by spatial misalignment between bi-temporal images, especially when acquisitions are separated by long seasonal or multi-year gaps. While modern convolutional and transformer-based models perform well on aligned data, their reliance on precise co-registration limits their robustness in real-world conditions. Existing joint registration-detection frameworks typically require retraining and transfer poorly across domains. We introduce a modular pipeline that improves spatial and temporal robustness without altering existing change detection networks. The framework integrates diffusion-based semantic morphing, dense registration, and residual flow refinement. A diffusion module synthesizes intermediate morphing frames that bridge large appearance gaps, enabling RoMa to estimate stepwise correspondences between consecutive frames. The composed flow is then refined through a lightweight U-Net to produce a high-fidelity warp that co-registers the original image pair. Extensive experiments on LEVIR-CD, WHU-CD, and DSIFN-CD show consistent gains in both registration accuracy and downstream change detection across multiple backbones, demonstrating the generality and effectiveness of the proposed approach.

