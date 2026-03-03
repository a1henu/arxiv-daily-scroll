---
layout: default
title: Sparse View Distractor-Free Gaussian Splatting
---

# Sparse View Distractor-Free Gaussian Splatting
**arXiv**：[2603.01603v1](https://arxiv.org/abs/2603.01603) · [PDF](https://arxiv.org/pdf/2603.01603.pdf)  
**作者**：Yi Gu, Zhaorui Wang, Jiahang Cao, Jiaxu Wang, Mingle Zhao, Dongjun Ye, Renjing Xu  

**一句话要点**：提出融合先验信息的框架以增强稀疏视图下的无干扰3D高斯溅射

**关键词**：3D高斯溅射, 稀疏视图重建, 无干扰场景建模, 先验信息融合, 视觉语言模型, 语义匹配

## 3 点简述
- 核心问题：稀疏视图条件下，现有无干扰3D高斯溅射方法因颜色残差启发式不可靠而性能下降。
- 方法要点：利用VGGT估计相机参数和初始点云，结合其注意力图进行语义匹配，并集成视觉语言模型识别静态区域。
- 实验或效果：广泛实验验证了该方法在稀疏视图训练中有效抑制瞬态干扰，提升鲁棒性。

## 摘要（原文）

> 3D Gaussian Splatting (3DGS) enables efficient training and fast novel view synthesis in static environments. To address challenges posed by transient objects, distractor-free 3DGS methods have emerged and shown promising results when dense image captures are available. However, their performance degrades significantly under sparse input conditions. This limitation primarily stems from the reliance on the color residual heuristics to guide the training, which becomes unreliable with limited observations. In this work, we propose a framework to enhance distractor-free 3DGS under sparse-view conditions by incorporating rich prior information. Specifically, we first adopt the geometry foundation model VGGT to estimate camera parameters and generate a dense set of initial 3D points. Then, we harness the attention maps from VGGT for efficient and accurate semantic entity matching. Additionally, we utilize Vision-Language Models (VLMs) to further identify and preserve the large static regions in the scene. We also demonstrate how these priors can be seamlessly integrated into existing distractor-free 3DGS methods. Extensive experiments confirm the effectiveness and robustness of our approach in mitigating transient distractors for sparse-view 3DGS training.

