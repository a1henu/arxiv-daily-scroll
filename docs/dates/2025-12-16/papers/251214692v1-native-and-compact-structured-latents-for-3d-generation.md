---
layout: default
title: Native and Compact Structured Latents for 3D Generation
---

# Native and Compact Structured Latents for 3D Generation
**arXiv**：[2512.14692v1](https://arxiv.org/abs/2512.14692) · [PDF](https://arxiv.org/pdf/2512.14692.pdf)  
**作者**：Jianfeng Xiang, Xiaoxue Chen, Sicheng Xu, Ruicheng Wang, Zelong Lv, Yu Deng, Hongyuan Zhu, Yue Dong, Hao Zhao, Nicholas Jing Yuan, Jiaolong Yang  

**一句话要点**：提出O-Voxel稀疏体素表示与稀疏压缩VAE，以解决3D生成中复杂拓扑与细节外观建模的挑战。

**关键词**：3D生成建模, 稀疏体素表示, 变分自编码器, 流匹配, 几何建模, 材质渲染

## 3 点简述
- 核心问题：现有3D表示难以捕获复杂拓扑和详细外观，限制生成质量。
- 方法要点：基于O-Voxel稀疏体素表示，设计稀疏压缩VAE实现高空间压缩和紧凑潜在空间。
- 实验或效果：训练4B参数流匹配模型，生成资产在几何和材质质量上远超现有模型，推理高效。

## 摘要（原文）

> Recent advancements in 3D generative modeling have significantly improved the generation realism, yet the field is still hampered by existing representations, which struggle to capture assets with complex topologies and detailed appearance. This paper present an approach for learning a structured latent representation from native 3D data to address this challenge. At its core is a new sparse voxel structure called O-Voxel, an omni-voxel representation that encodes both geometry and appearance. O-Voxel can robustly model arbitrary topology, including open, non-manifold, and fully-enclosed surfaces, while capturing comprehensive surface attributes beyond texture color, such as physically-based rendering parameters. Based on O-Voxel, we design a Sparse Compression VAE which provides a high spatial compression rate and a compact latent space. We train large-scale flow-matching models comprising 4B parameters for 3D generation using diverse public 3D asset datasets. Despite their scale, inference remains highly efficient. Meanwhile, the geometry and material quality of our generated assets far exceed those of existing models. We believe our approach offers a significant advancement in 3D generative modeling.

