---
layout: default
title: SNOW: Spatio-Temporal Scene Understanding with World Knowledge for Open-World Embodied Reasoning
---

# SNOW: Spatio-Temporal Scene Understanding with World Knowledge for Open-World Embodied Reasoning
**arXiv**：[2512.16461v1](https://arxiv.org/abs/2512.16461) · [PDF](https://arxiv.org/pdf/2512.16461.pdf)  
**作者**：Tin Stribor Sohn, Maximilian Dillitzer, Jason J. Corso, Eric Sax  

**一句话要点**：提出SNOW框架，集成视觉语言模型语义与点云几何，实现免训练的统一4D场景理解以支持具身推理。

**关键词**：4D场景理解, 视觉语言模型, 点云几何, 时空一致性, 具身推理, 开放世界语义

## 3 点简述
- 核心问题：视觉语言模型缺乏3D几何与时间动态基础，几何感知语义稀疏，阻碍开放世界具身推理。
- 方法要点：通过HDBSCAN聚类和SAM2分割生成对象提案，使用STEP编码多模态令牌，构建4D场景图作为先验。
- 实验或效果：在多个基准测试中实现精确4D场景理解和空间基础推理，达到新最优性能。

## 摘要（原文）

> Autonomous robotic systems require spatio-temporal understanding of dynamic environments to ensure reliable navigation and interaction. While Vision-Language Models (VLMs) provide open-world semantic priors, they lack grounding in 3D geometry and temporal dynamics. Conversely, geometric perception captures structure and motion but remains semantically sparse. We propose SNOW (Scene Understanding with Open-World Knowledge), a training-free and backbone-agnostic framework for unified 4D scene understanding that integrates VLM-derived semantics with point cloud geometry and temporal consistency. SNOW processes synchronized RGB images and 3D point clouds, using HDBSCAN clustering to generate object-level proposals that guide SAM2-based segmentation. Each segmented region is encoded through our proposed Spatio-Temporal Tokenized Patch Encoding (STEP), producing multimodal tokens that capture localized semantic, geometric, and temporal attributes. These tokens are incrementally integrated into a 4D Scene Graph (4DSG), which serves as 4D prior for downstream reasoning. A lightweight SLAM backend anchors all STEP tokens spatially in the environment, providing the global reference alignment, and ensuring unambiguous spatial grounding across time. The resulting 4DSG forms a queryable, unified world model through which VLMs can directly interpret spatial scene structure and temporal dynamics. Experiments on a diverse set of benchmarks demonstrate that SNOW enables precise 4D scene understanding and spatially grounded inference, thereby setting new state-of-the-art performance in several settings, highlighting the importance of structured 4D priors for embodied reasoning and autonomous robotics.

