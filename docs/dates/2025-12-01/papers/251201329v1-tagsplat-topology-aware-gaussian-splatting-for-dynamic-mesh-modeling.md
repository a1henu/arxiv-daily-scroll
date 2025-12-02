---
layout: default
title: TagSplat: Topology-Aware Gaussian Splatting for Dynamic Mesh Modeling and Tracking
---

# TagSplat: Topology-Aware Gaussian Splatting for Dynamic Mesh Modeling and Tracking
**arXiv**：[2512.01329v1](https://arxiv.org/abs/2512.01329) · [PDF](https://arxiv.org/pdf/2512.01329.pdf)  
**作者**：Hanzhi Guo, Dongdong Weng, Mo Su, Yixiao Chen, Xiaonuo Dongye, Chenyu Xu  

**一句话要点**：提出拓扑感知高斯泼溅框架，以解决动态网格建模中拓扑一致性的重建问题。

**关键词**：动态网格建模, 拓扑一致性, 高斯泼溅, 4D重建, 关键点跟踪

## 3 点简述
- 核心问题：现有4D重建方法难以生成高质量拓扑一致的动态网格序列。
- 方法要点：引入高斯拓扑结构，通过拓扑感知的密度调整和时域正则化确保拓扑一致性。
- 实验或效果：实验显示方法重建精度显著优于现有方法，并支持精确3D关键点跟踪。

## 摘要（原文）

> Topology-consistent dynamic model sequences are essential for applications such as animation and model editing. However, existing 4D reconstruction methods face challenges in generating high-quality topology-consistent meshes. To address this, we propose a topology-aware dynamic reconstruction framework based on Gaussian Splatting. We introduce a Gaussian topological structure that explicitly encodes spatial connectivity. This structure enables topology-aware densification and pruning, preserving the manifold consistency of the Gaussian representation. Temporal regularization terms further ensure topological coherence over time, while differentiable mesh rasterization improves mesh quality. Experimental results demonstrate that our method reconstructs topology-consistent mesh sequences with significantly higher accuracy than existing approaches. Moreover, the resulting meshes enable precise 3D keypoint tracking. Project page: https://haza628.github.io/tagSplat/

