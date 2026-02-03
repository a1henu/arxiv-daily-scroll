---
layout: default
title: ProxyImg: Towards Highly-Controllable Image Representation via Hierarchical Disentangled Proxy Embedding
---

# ProxyImg: Towards Highly-Controllable Image Representation via Hierarchical Disentangled Proxy Embedding
**arXiv**：[2602.01881v1](https://arxiv.org/abs/2602.01881) · [PDF](https://arxiv.org/pdf/2602.01881.pdf)  
**作者**：Ye Chen, Yupeng Zhu, Xiongzhen Zhang, Zhewen Wan, Yingzhe Li, Wenjun Zhang, Bingbing Ni  

**一句话要点**：提出分层解耦代理嵌入方法以解决图像表示冗余和细粒度编辑困难问题

**关键词**：图像表示, 分层解耦, 代理嵌入, 可控编辑, 实时动画, 高保真重建

## 3 点简述
- 核心问题：现有图像表示方法存在冗余或缺乏语义到实例的直接映射，阻碍可控编辑
- 方法要点：通过语义分解、自适应贝塞尔拟合和代理节点嵌入，解耦语义、几何和纹理属性
- 实验或效果：在ImageNet等基准上实现高保真重建和直观编辑，参数更少且支持实时物理动画

## 摘要（原文）

> Prevailing image representation methods, including explicit representations such as raster images and Gaussian primitives, as well as implicit representations such as latent images, either suffer from representation redundancy that leads to heavy manual editing effort, or lack a direct mapping from latent variables to semantic instances or parts, making fine-grained manipulation difficult. These limitations hinder efficient and controllable image and video editing. To address these issues, we propose a hierarchical proxy-based parametric image representation that disentangles semantic, geometric, and textural attributes into independent and manipulable parameter spaces. Based on a semantic-aware decomposition of the input image, our representation constructs hierarchical proxy geometries through adaptive Bezier fitting and iterative internal region subdivision and meshing. Multi-scale implicit texture parameters are embedded into the resulting geometry-aware distributed proxy nodes, enabling continuous high-fidelity reconstruction in the pixel domain and instance- or part-independent semantic editing. In addition, we introduce a locality-adaptive feature indexing mechanism to ensure spatial texture coherence, which further supports high-quality background completion without relying on generative models. Extensive experiments on image reconstruction and editing benchmarks, including ImageNet, OIR-Bench, and HumanEdit, demonstrate that our method achieves state-of-the-art rendering fidelity with significantly fewer parameters, while enabling intuitive, interactive, and physically plausible manipulation. Moreover, by integrating proxy nodes with Position-Based Dynamics, our framework supports real-time physics-driven animation using lightweight implicit rendering, achieving superior temporal consistency and visual realism compared with generative approaches.

