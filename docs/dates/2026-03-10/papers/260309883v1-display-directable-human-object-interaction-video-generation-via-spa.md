---
layout: default
title: DISPLAY: Directable Human-Object Interaction Video Generation via Sparse Motion Guidance and Multi-Task Auxiliary
---

# DISPLAY: Directable Human-Object Interaction Video Generation via Sparse Motion Guidance and Multi-Task Auxiliary
**arXiv**：[2603.09883v1](https://arxiv.org/abs/2603.09883) · [PDF](https://arxiv.org/pdf/2603.09883.pdf)  
**作者**：Jiazhi Guan, Quanwei Yang, Luying Huang, Junhao Liang, Borong Liang, Haocheng Feng, Wei He, Kaisiyuan Wang, Hang Zhou, Jingdong Wang  

**一句话要点**：提出DISPLAY框架，通过稀疏运动引导和多任务辅助训练，实现可控的人-物交互视频生成。

**关键词**：人-物交互视频生成, 稀疏运动引导, 对象强调注意力, 多任务辅助训练, 可控视频生成

## 3 点简述
- 核心问题：现有方法依赖密集控制信号或模板，难以生成可控且物理一致的人-物交互视频。
- 方法要点：使用稀疏运动引导（手腕关节坐标和物体边界框）和对象强调注意力机制，提升生成质量。
- 实验或效果：通过多任务辅助训练策略，在多样化任务中实现高保真、可控的视频生成。

## 摘要（原文）

> Human-centric video generation has advanced rapidly, yet existing methods struggle to produce controllable and physically consistent Human-Object Interaction (HOI) videos. Existing works rely on dense control signals, template videos, or carefully crafted text prompts, which limit flexibility and generalization to novel objects. We introduce a framework, namely DISPLAY, guided by Sparse Motion Guidance, composed only of wrist joint coordinates and a shape-agnostic object bounding box. This lightweight guidance alleviates the imbalance between human and object representations and enables intuitive user control. To enhance fidelity under such sparse conditions, we propose an Object-Stressed Attention mechanism that improves object robustness. To address the scarcity of high-quality HOI data, we further develop a Multi-Task Auxiliary Training strategy with a dedicated data curation pipeline, allowing the model to benefit from both reliable HOI samples and auxiliary tasks. Comprehensive experiments show that our method achieves high-fidelity, controllable HOI generation across diverse tasks. The project page can be found at \href{https://mumuwei.github.io/DISPLAY/}.

