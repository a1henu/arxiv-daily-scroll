---
layout: default
title: TexSpot: 3D Texture Enhancement with Spatially-uniform Point Latent Representation
---

# TexSpot: 3D Texture Enhancement with Spatially-uniform Point Latent Representation
**arXiv**：[2602.12157v1](https://arxiv.org/abs/2602.12157) · [PDF](https://arxiv.org/pdf/2602.12157.pdf)  
**作者**：Ziteng Lu, Yushuang Wu, Chongjie Ye, Yuda Qiu, Jing Shao, Xiaoyang Guo, Jiaqing Zhou, Tianlei Hu, Kun Zhou, Xiaoguang Han  

**一句话要点**：提出TexSpot框架，通过Texlet表示增强多视图扩散生成的3D纹理质量

**关键词**：3D纹理生成, 纹理增强, 扩散模型, 点表示, 多视图扩散

## 3 点简述
- 核心问题：现有3D纹理生成方法存在视图不一致、UV图扭曲或点表示分辨率受限的问题
- 方法要点：引入Texlet表示，结合点基纹理的几何表达性和UV表示的紧凑性，使用扩散变换器进行纹理增强
- 实验或效果：实验显示TexSpot在视觉保真度、几何一致性和鲁棒性上优于现有方法

## 摘要（原文）

> High-quality 3D texture generation remains a fundamental challenge due to the view-inconsistency inherent in current mainstream multi-view diffusion pipelines. Existing representations either rely on UV maps, which suffer from distortion during unwrapping, or point-based methods, which tightly couple texture fidelity to geometric density that limits high-resolution texture generation. To address these limitations, we introduce TexSpot, a diffusion-based texture enhancement framework. At its core is Texlet, a novel 3D texture representation that merges the geometric expressiveness of point-based 3D textures with the compactness of UV-based representation. Each Texlet latent vector encodes a local texture patch via a 2D encoder and is further aggregated using a 3D encoder to incorporate global shape context. A cascaded 3D-to-2D decoder reconstructs high-quality texture patches, enabling the Texlet space learning. Leveraging this representation, we train a diffusion transformer conditioned on Texlets to refine and enhance textures produced by multi-view diffusion methods. Extensive experiments demonstrate that TexSpot significantly improves visual fidelity, geometric consistency, and robustness over existing state-of-the-art 3D texture generation and enhancement approaches. Project page: https://anonymous.4open.science/w/TexSpot-page-2D91.

