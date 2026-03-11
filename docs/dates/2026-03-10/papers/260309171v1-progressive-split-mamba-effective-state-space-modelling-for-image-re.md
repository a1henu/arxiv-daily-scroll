---
layout: default
title: Progressive Split Mamba: Effective State Space Modelling for Image Restoration
---

# Progressive Split Mamba: Effective State Space Modelling for Image Restoration
**arXiv**：[2603.09171v1](https://arxiv.org/abs/2603.09171) · [PDF](https://arxiv.org/pdf/2603.09171.pdf)  
**作者**：Mohammed Hassanin, Nour Moustafa, Weijian Deng, Ibrahim Radwan  

**一句话要点**：提出渐进分割Mamba以解决图像恢复中状态空间模型的局部失真与长程衰减问题

**关键词**：图像恢复, 状态空间模型, 渐进分割, 长程依赖建模, 局部结构保持, 线性复杂度

## 3 点简述
- 核心问题：Mamba直接应用于2D图像导致空间拓扑破坏和长程信息衰减，限制高保真恢复效果
- 方法要点：通过几何一致分割和渐进层次结构，保持局部邻域完整性并引入跨尺度捷径以稳定全局信息流
- 实验或效果：在超分辨率、去噪和JPEG伪影减少任务中，相比基于Mamba和注意力的模型有显著提升

## 摘要（原文）

> Image restoration requires simultaneously preserving fine-grained local structures and maintaining long-range spatial coherence. While convolutional networks struggle with limited receptive fields, and Transformers incur quadratic complexity for global attention, recent State Space Models (SSMs), such as Mamba, provide an appealing linear-time alternative for long-range dependency modelling. However, naively extending Mamba to 2D images exposes two intrinsic shortcomings. First, flattening 2D feature maps into 1D sequences disrupts spatial topology, leading to locality distortion that hampers precise structural recovery. Second, the stability-driven recurrent dynamics of SSMs induce long-range decay, progressively attenuating information across distant spatial positions and weakening global consistency. Together, these effects limit the effectiveness of state-space modelling in high-fidelity restoration. We propose Progressive Split-Mamba (PS-Mamba), a topology-aware hierarchical state-space framework designed to reconcile locality preservation with efficient global propagation. Instead of sequentially flattening entire feature maps, PS-Mamba performs geometry-consistent partitioning, maintaining neighbourhood integrity prior to state-space processing. A progressive split hierarchy (halves, quadrants, octants) enables structured multi-scale modelling while retaining linear complexity. To counteract long-range decay, we introduce symmetric cross-scale shortcut pathways that directly transmit low-frequency global context across hierarchical levels, stabilising information flow over large spatial extents. Extensive experiments on super-resolution, denoising, and JPEG artifact reduction show consistent improvements over recent Mamba-based and attention-based models with a clear margin.

