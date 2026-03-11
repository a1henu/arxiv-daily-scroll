---
layout: default
title: World2Mind: Cognition Toolkit for Allocentric Spatial Reasoning in Foundation Models
---

# World2Mind: Cognition Toolkit for Allocentric Spatial Reasoning in Foundation Models
**arXiv**：[2603.09774v1](https://arxiv.org/abs/2603.09774) · [PDF](https://arxiv.org/pdf/2603.09774.pdf)  
**作者**：Shouwei Ruan, Bin Wang, Zhenyu Wu, Qihui Zhu, Yuxiang Zhang, Hang Su, Yubin Wang  

**一句话要点**：提出World2Mind工具包，通过构建空间认知地图提升多模态基础模型的空间推理能力

**关键词**：空间推理, 多模态基础模型, 3D重建, 认知地图, 几何拓扑先验, 训练免费工具包

## 3 点简述
- 核心问题：现有多模态基础模型在空间推理中易过拟合或局限于2D感知，泛化能力不足
- 方法要点：利用3D重建和实例分割构建结构化认知地图，并引入椭圆参数化Allocentric-Spatial Tree提供几何拓扑先验
- 实验或效果：在GPT-5.2等前沿模型上提升性能5%~18%，仅基于文本的模型也能实现复杂3D空间推理

## 摘要（原文）

> Achieving robust spatial reasoning remains a fundamental challenge for current Multimodal Foundation Models (MFMs). Existing methods either overfit statistical shortcuts via 3D grounding data or remain confined to 2D visual perception, limiting both spatial reasoning accuracy and generalization in unseen scenarios. Inspired by the spatial cognitive mapping mechanisms of biological intelligence, we propose World2Mind, a training-free spatial intelligence toolkit. At its core, World2Mind leverages 3D reconstruction and instance segmentation models to construct structured spatial cognitive maps, empowering MFMs to proactively acquire targeted spatial knowledge regarding interested landmarks and routes of interest. To provide robust geometric-topological priors, World2Mind synthesizes an Allocentric-Spatial Tree (AST) that uses elliptical parameters to model the top-down layout of landmarks accurately. To mitigate the inherent inaccuracies of 3D reconstruction, we introduce a three-stage reasoning chain comprising tool invocation assessment, modality-decoupled cue collection, and geometry-semantics interwoven reasoning. Extensive experiments demonstrate that World2Mind boosts the performance of frontier models, such as GPT-5.2, by 5%~18%. Astonishingly, relying solely on the AST-structured text, purely text-only foundation models can perform complex 3D spatial reasoning, achieving performance approaching that of advanced multimodal models.

