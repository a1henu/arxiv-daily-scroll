---
layout: default
title: GaussianDWM: 3D Gaussian Driving World Model for Unified Scene Understanding and Multi-Modal Generation
---

# GaussianDWM: 3D Gaussian Driving World Model for Unified Scene Understanding and Multi-Modal Generation
**arXiv**：[2512.23180v1](https://arxiv.org/abs/2512.23180) · [PDF](https://arxiv.org/pdf/2512.23180.pdf)  
**作者**：Tianchen Deng, Xuefeng Chen, Yi Chen, Qu Chen, Yuyao Xu, Lijin Yang, Le Xu, Yu Zhang, Bo Zhang, Wuxiong Huang, Hesheng Wang  

**一句话要点**：提出基于3D高斯场景表示的驾驶世界模型，实现统一场景理解与多模态生成。

**关键词**：驾驶世界模型, 3D高斯表示, 多模态生成, 场景理解, 模态对齐

## 3 点简述
- 现有驾驶世界模型缺乏3D场景理解能力，且文本与3D场景对齐不准确。
- 通过将语言特征嵌入高斯基元实现早期模态对齐，并设计任务感知语言引导采样策略。
- 在nuScenes和NuInteract数据集上验证，达到未知性能水平。

## 摘要（原文）

> Driving World Models (DWMs) have been developing rapidly with the advances of generative models. However, existing DWMs lack 3D scene understanding capabilities and can only generate content conditioned on input data, without the ability to interpret or reason about the driving environment. Moreover, current approaches represent 3D spatial information with point cloud or BEV features do not accurately align textual information with the underlying 3D scene. To address these limitations, we propose a novel unified DWM framework based on 3D Gaussian scene representation, which enables both 3D scene understanding and multi-modal scene generation, while also enabling contextual enrichment for understanding and generation tasks. Our approach directly aligns textual information with the 3D scene by embedding rich linguistic features into each Gaussian primitive, thereby achieving early modality alignment. In addition, we design a novel task-aware language-guided sampling strategy that removes redundant 3D Gaussians and injects accurate and compact 3D tokens into LLM. Furthermore, we design a dual-condition multi-modal generation model, where the information captured by our vision-language model is leveraged as a high-level language condition in combination with a low-level image condition, jointly guiding the multi-modal generation process. We conduct comprehensive studies on the nuScenes, and NuInteract datasets to validate the effectiveness of our framework. Our method achieves state-of-the-art performance. We will release the code publicly on GitHub https://github.com/dtc111111/GaussianDWM.

