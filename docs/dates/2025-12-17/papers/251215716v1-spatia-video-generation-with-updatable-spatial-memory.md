---
layout: default
title: Spatia: Video Generation with Updatable Spatial Memory
---

# Spatia: Video Generation with Updatable Spatial Memory
**arXiv**：[2512.15716v1](https://arxiv.org/abs/2512.15716) · [PDF](https://arxiv.org/pdf/2512.15716.pdf)  
**作者**：Jinjing Zhao, Fangyun Wei, Zhening Liu, Hongyang Zhang, Chang Xu, Yan Lu  

**一句话要点**：提出Spatia框架，通过可更新的空间记忆解决视频生成中的长期时空一致性问题。

**关键词**：视频生成, 空间记忆, 视觉SLAM, 3D场景点云, 时空一致性, 交互编辑

## 3 点简述
- 现有视频生成模型因视频信号高维密集，难以保持长期时空一致性。
- Spatia使用3D场景点云作为空间记忆，迭代生成视频片段并基于视觉SLAM更新记忆。
- 该框架支持显式相机控制和3D感知交互编辑，提升生成视频的空间一致性和可扩展性。

## 摘要（原文）

> Existing video generation models struggle to maintain long-term spatial and temporal consistency due to the dense, high-dimensional nature of video signals. To overcome this limitation, we propose Spatia, a spatial memory-aware video generation framework that explicitly preserves a 3D scene point cloud as persistent spatial memory. Spatia iteratively generates video clips conditioned on this spatial memory and continuously updates it through visual SLAM. This dynamic-static disentanglement design enhances spatial consistency throughout the generation process while preserving the model's ability to produce realistic dynamic entities. Furthermore, Spatia enables applications such as explicit camera control and 3D-aware interactive editing, providing a geometrically grounded framework for scalable, memory-driven video generation.

