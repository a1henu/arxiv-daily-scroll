---
layout: default
title: LATO: 3D Mesh Flow Matching with Structured TOpology Preserving LAtents
---

# LATO: 3D Mesh Flow Matching with Structured TOpology Preserving LAtents
**arXiv**：[2603.06357v1](https://arxiv.org/abs/2603.06357) · [PDF](https://arxiv.org/pdf/2603.06357.pdf)  
**作者**：Tianhao Zhao, Youjia Zhang, Hang Long, Jinshen Zhang, Wenbing Li, Yang Yang, Gongbo Zhang, Jozef Hladký, Matthias Nießner, Wei Yang  

**一句话要点**：提出LATO以通过结构化拓扑感知潜在表示实现高效3D网格生成

**关键词**：3D网格生成, 拓扑保持, 流匹配, 顶点位移场, 稀疏体素VAE

## 3 点简述
- 核心问题：现有3D网格生成方法依赖等值面提取或启发式网格化，效率低且拓扑结构易受损。
- 方法要点：使用顶点位移场和稀疏体素VAE构建拓扑感知潜在，通过连接头直接预测边连接性。
- 实验或效果：相比基于等值面/三角形的扩散模型和自回归方法，LATO生成复杂几何、拓扑良好的网格，推理高效。

## 摘要（原文）

> In this paper, we introduce LATO, a novel topology-preserving latent representation that enables scalable, flow matching-based synthesis of explicit 3D meshes. LATO represents a mesh as a Vertex Displacement Field (VDF) anchored on surface, incorporating a sparse voxel Variational Autoencoder (VAE) to compress this explicit signal into a structured, topology-aware voxel latent. To decapsulate the mesh, the VAE decoder progressively subdivides and prunes latent voxels to instantiate precise vertex locations. In the end, a dedicated connection head queries the voxel latent to predict edge connectivity between vertex pairs directly, allowing mesh topology to be recovered without isosurface extraction or heuristic meshing. For generative modeling, LATO adopts a two-stage flow matching process, first synthesizing the structure voxels and subsequently refining the voxel-wise topology features. Compared to prior isosurface/triangle-based diffusion models and autoregressive generation approaches, LATO generates meshes with complex geometry, well-formed topology while being highly efficient in inference.

