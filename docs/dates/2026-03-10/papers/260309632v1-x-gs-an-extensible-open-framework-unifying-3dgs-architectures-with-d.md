---
layout: default
title: X-GS: An Extensible Open Framework Unifying 3DGS Architectures with Downstream Multimodal Models
---

# X-GS: An Extensible Open Framework Unifying 3DGS Architectures with Downstream Multimodal Models
**arXiv**：[2603.09632v1](https://arxiv.org/abs/2603.09632) · [PDF](https://arxiv.org/pdf/2603.09632.pdf)  
**作者**：Yueen Ma, Irwin King  

**一句话要点**：提出X-GS框架以统一3D高斯泼溅架构并连接下游多模态模型，实现实时语义增强的在线SLAM。

**关键词**：3D高斯泼溅, 在线SLAM, 语义增强, 多模态模型, 实时处理, 蒸馏训练

## 3 点简述
- 核心问题：现有3DGS方法孤立，缺乏统一框架支持实时语义增强的在线SLAM。
- 方法要点：通过X-GS-Perceiver高效管道，从无位姿视频流中联合优化几何与位姿，并蒸馏视觉基础模型语义特征到3D高斯。
- 实验或效果：在真实数据集上验证了框架的有效性、效率和新解锁的多模态能力，如物体检测和零样本字幕生成。

## 摘要（原文）

> 3D Gaussian Splatting (3DGS) has emerged as a powerful technique for novel view synthesis, subsequently extending into numerous spatial AI applications. However, most existing 3DGS methods are isolated, focusing on specific domains such as online SLAM, semantic enrichment, or 3DGS for unposed images. In this paper, we introduce X-GS, an extensible open framework that unifies a broad range of techniques to enable real-time 3DGS-based online SLAM enriched with semantics, bridging the gap to downstream multimodal models. At the core of X-GS is a highly efficient pipeline called X-GS-Perceiver, capable of taking unposed RGB (or optionally RGB-D) video streams as input to co-optimize geometry and poses, and distill high-dimensional semantic features from vision foundation models into the 3D Gaussians. We achieve real-time performance through a novel online Vector Quantization (VQ) module, a GPU-accelerated grid-sampling scheme, and a highly parallelized pipeline design. The semantic 3D Gaussians can then be utilized by vision-language models within the X-GS-Thinker component, enabling downstream tasks such as object detection, zero-shot caption generation, and potentially embodied tasks. Experimental results on real-world datasets showcase the efficacy, efficiency, and newly unlocked multimodal capabilities of the X-GS framework.

