---
layout: default
title: Building temporally coherent 3D maps with VGGT for memory-efficient Semantic SLAM
---

# Building temporally coherent 3D maps with VGGT for memory-efficient Semantic SLAM
**arXiv**：[2511.16282v1](https://arxiv.org/abs/2511.16282) · [PDF](https://arxiv.org/pdf/2511.16282.pdf)  
**作者**：Gergely Dinya, Péter Halász, András Lőrincz, Kristóf Karacs, Anna Gelencsér-Horváth  

**一句话要点**：提出基于VGGT的快速时空场景理解框架，用于构建时间一致的3D地图以支持辅助导航。

**关键词**：语义SLAM, 3D地图构建, 视觉门控生成变换器, 时空一致性, 辅助导航, 内存优化

## 3 点简述
- 核心问题：VGGT内存需求高，难以实时构建时间一致的3D语义地图。
- 方法要点：使用滑动窗口处理图像流，对齐子图以降低内存，并聚合2D语义掩码为3D对象。
- 实验或效果：在标准基准和自定义数据集上评估，证明适用于真实世界辅助导航场景。

## 摘要（原文）

> We present a fast, spatio-temporal scene understanding framework based on Vision Gated Generative Transformers (VGGT). The proposed pipeline is designed to enable efficient, close to real-time performance, supporting applications including assistive navigation. To achieve continuous updates of the 3D scene representation, we process the image flow with a sliding window, aligning submaps, thereby overcoming VGGT's high memory demands. We exploit the VGGT tracking head to aggregate 2D semantic instance masks into 3D objects. To allow for temporal consistency and richer contextual reasoning the system stores timestamps and instance-level identities, thereby enabling the detection of changes in the environment. We evaluate the approach on well-known benchmarks and custom datasets specifically designed for assistive navigation scenarios. The results demonstrate the applicability of the framework to real-world scenarios.

