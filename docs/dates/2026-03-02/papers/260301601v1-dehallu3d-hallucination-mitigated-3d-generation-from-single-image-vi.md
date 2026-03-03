---
layout: default
title: Dehallu3D: Hallucination-Mitigated 3D Generation from Single Image via Cyclic View Consistency Refinement
---

# Dehallu3D: Hallucination-Mitigated 3D Generation from Single Image via Cyclic View Consistency Refinement
**arXiv**：[2603.01601v1](https://arxiv.org/abs/2603.01601) · [PDF](https://arxiv.org/pdf/2603.01601.pdf)  
**作者**：Xiwen Wang, Shichao Zhang, Hailun Zhang, Ruowei Wang, Mao Li, Chenyu Zhou, Qijun Zhao, Ji-Zhe Zhou  

**一句话要点**：提出Dehallu3D通过循环视角一致性优化缓解单图像3D生成中的幻觉问题

**关键词**：3D生成, 幻觉缓解, 多视图一致性, 几何优化, 单图像重建, 虚拟现实

## 3 点简述
- 核心问题：大型3D重建模型因稀疏多视图图像生成导致结构异常（如孔洞或突起），影响3D打印和虚拟现实应用。
- 方法要点：设计平衡的多视图连续性约束，结合相邻一致性和自适应平滑度，以插件式优化模块消除幻觉并保留细节。
- 实验或效果：提出Outlier Risk Measure量化几何保真度，实验显示Dehallu3D能有效去除幻觉异常并保持结构细节，实现高保真3D生成。

## 摘要（原文）

> Large 3D reconstruction models have revolutionized the 3D content generation field, enabling broad applications in virtual reality and gaming. Just like other large models, large 3D reconstruction models suffer from hallucinations as well, introducing structural outliers (e.g., odd holes or protrusions) that deviate from the input data. However, unlike other large models, hallucinations in large 3D reconstruction models remain severely underexplored, leading to malformed 3D-printed objects or insufficient immersion in virtual scenes. Such hallucinations majorly originate from that existing methods reconstruct 3D content from sparsely generated multi-view images which suffer from large viewpoint gaps and discontinuities. To mitigate hallucinations by eliminating the outliers, we propose Dehallu3D for 3D mesh generation. Our key idea is to design a balanced multi-view continuity constraint to enforce smooth transitions across dense intermediate viewpoints, while avoiding over-smoothing that could erase sharp geometric features. Therefore, Dehallu3D employs a plug-and-play optimization module with two key constraints: (i) adjacent consistency to ensure geometric continuity across views, and (ii) adaptive smoothness to retain fine details.We further propose the Outlier Risk Measure (ORM) metric to quantify geometric fidelity in 3D generation from the perspective of outliers. Extensive experiments show that Dehallu3D achieves high-fidelity 3D generation by effectively preserving structural details while removing hallucinated outliers.

