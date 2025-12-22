---
layout: default
title: Pix2NPHM: Learning to Regress NPHM Reconstructions From a Single Image
---

# Pix2NPHM: Learning to Regress NPHM Reconstructions From a Single Image
**arXiv**：[2512.17773v1](https://arxiv.org/abs/2512.17773) · [PDF](https://arxiv.org/pdf/2512.17773.pdf)  
**作者**：Simon Giebenhain, Tobias Kirschstein, Liam Schoneveld, Davide Davoli, Zhe Chen, Matthias Nießner  

**一句话要点**：提出Pix2NPHM以从单张图像回归NPHM参数，实现高保真面部重建

**关键词**：单图像三维重建, 神经参数化头部模型, 视觉Transformer, 几何预测, 面部表情重建, 交互式帧率

## 3 点简述
- 核心问题：NPHM拟合视觉输入困难，因其潜在空间表达性强，导致重建挑战
- 方法要点：使用ViT网络直接回归NPHM参数，结合几何预测预训练和混合数据训练
- 实验或效果：在交互帧率下实现高质量重建，通过优化提升几何保真度，适用于野外数据

## 摘要（原文）

> Neural Parametric Head Models (NPHMs) are a recent advancement over mesh-based 3d morphable models (3DMMs) to facilitate high-fidelity geometric detail. However, fitting NPHMs to visual inputs is notoriously challenging due to the expressive nature of their underlying latent space. To this end, we propose Pix2NPHM, a vision transformer (ViT) network that directly regresses NPHM parameters, given a single image as input. Compared to existing approaches, the neural parametric space allows our method to reconstruct more recognizable facial geometry and accurate facial expressions. For broad generalization, we exploit domain-specific ViTs as backbones, which are pretrained on geometric prediction tasks. We train Pix2NPHM on a mixture of 3D data, including a total of over 100K NPHM registrations that enable direct supervision in SDF space, and large-scale 2D video datasets, for which normal estimates serve as pseudo ground truth geometry. Pix2NPHM not only allows for 3D reconstructions at interactive frame rates, it is also possible to improve geometric fidelity by a subsequent inference-time optimization against estimated surface normals and canonical point maps. As a result, we achieve unprecedented face reconstruction quality that can run at scale on in-the-wild data.

