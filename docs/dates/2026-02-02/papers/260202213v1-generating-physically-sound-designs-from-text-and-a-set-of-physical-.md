---
layout: default
title: Generating Physically Sound Designs from Text and a Set of Physical Constraints
---

# Generating Physically Sound Designs from Text and a Set of Physical Constraints
**arXiv**：[2602.02213v1](https://arxiv.org/abs/2602.02213) · [PDF](https://arxiv.org/pdf/2602.02213.pdf)  
**作者**：Gregory Barber, Todd C. Henry, Mulugeta A. Haile  

**一句话要点**：提出TIDES方法，基于文本描述和物理约束生成物理合理的设计。

**关键词**：文本到设计生成, 物理约束优化, 可微分物理模拟, 结构拓扑优化, 多目标优化

## 3 点简述
- 核心问题：如何从文本描述和物理约束生成物理合理的设计。
- 方法要点：联合优化结构拓扑和视觉属性，使用文本-图像模型和可微分物理模拟器。
- 实验或效果：在结构优化问题中评估，通过3D打印和三点弯曲测试验证设计性能。

## 摘要（原文）

> We present TIDES, a text informed design approach for generating physically sound designs based on a textual description and a set of physical constraints. TIDES jointly optimizes structural (topology) and visual properties. A pre-trained text-image model is used to measure the design's visual alignment with a text prompt and a differentiable physics simulator is used to measure its physical performance. We evaluate TIDES on a series of structural optimization problems operating under different load and support conditions, at different resolutions, and experimentally in the lab by performing the 3-point bending test on 2D beam designs that are extruded and 3D printed. We find that it can jointly optimize the two objectives and return designs that satisfy engineering design requirements (compliance and density) while utilizing features specified by text.

