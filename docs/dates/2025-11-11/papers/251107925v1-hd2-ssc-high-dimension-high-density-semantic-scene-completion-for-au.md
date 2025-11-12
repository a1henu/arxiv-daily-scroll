---
layout: default
title: HD$^2$-SSC: High-Dimension High-Density Semantic Scene Completion for Autonomous Driving
---

# HD$^2$-SSC: High-Dimension High-Density Semantic Scene Completion for Autonomous Driving
**arXiv**：[2511.07925v1](https://arxiv.org/abs/2511.07925) · [PDF](https://arxiv.org/pdf/2511.07925.pdf)  
**作者**：Zhiwen Yang, Yuxin Peng  

**一句话要点**：提出HD²-SSC框架以解决自动驾驶中语义场景完成的维度与密度差距问题

**关键词**：语义场景完成, 自动驾驶, 3D场景理解, 体素化表示, 高维特征扩展, 密度优化

## 3 点简述
- 核心问题：现有方法存在2D输入与3D输出维度差距及标注稀疏与真实密集的密度差距
- 方法要点：设计高维语义解耦模块扩展2D特征，高密度占用细化模块检测并修正体素
- 实验或效果：在SemanticKITTI和SSCBench-KITTI-360数据集上验证有效性

## 摘要（原文）

> Camera-based 3D semantic scene completion (SSC) plays a crucial role in autonomous driving, enabling voxelized 3D scene understanding for effective scene perception and decision-making. Existing SSC methods have shown efficacy in improving 3D scene representations, but suffer from the inherent input-output dimension gap and annotation-reality density gap, where the 2D planner view from input images with sparse annotated labels leads to inferior prediction of real-world dense occupancy with a 3D stereoscopic view. In light of this, we propose the corresponding High-Dimension High-Density Semantic Scene Completion (HD$^2$-SSC) framework with expanded pixel semantics and refined voxel occupancies. To bridge the dimension gap, a High-dimension Semantic Decoupling module is designed to expand 2D image features along a pseudo third dimension, decoupling coarse pixel semantics from occlusions, and then identify focal regions with fine semantics to enrich image features. To mitigate the density gap, a High-density Occupancy Refinement module is devised with a "detect-and-refine" architecture to leverage contextual geometric and semantic structures for enhanced semantic density with the completion of missing voxels and correction of erroneous ones. Extensive experiments and analyses on the SemanticKITTI and SSCBench-KITTI-360 datasets validate the effectiveness of our HD$^2$-SSC framework.

