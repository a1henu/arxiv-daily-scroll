---
layout: default
title: ViTNT-FIQA: Training-Free Face Image Quality Assessment with Vision Transformers
---

# ViTNT-FIQA: Training-Free Face Image Quality Assessment with Vision Transformers
**arXiv**：[2601.05741v1](https://arxiv.org/abs/2601.05741) · [PDF](https://arxiv.org/pdf/2601.05741.pdf)  
**作者**：Guray Ozgur, Eduarda Caldeira, Tahar Chettaoui, Jan Niklas Kolf, Marco Huber, Naser Damer, Fadi Boutros  

**一句话要点**：提出ViTNT-FIQA，利用ViT中间块嵌入稳定性进行免训练人脸图像质量评估。

**关键词**：人脸图像质量评估, 免训练方法, 视觉变换器, 特征稳定性, 计算效率

## 3 点简述
- 当前FIQA方法多依赖最终层表示，免训练方法需多次前向或反向传播。
- ViTNT-FIQA通过计算ViT中间块间L2归一化嵌入的欧氏距离，评估特征轨迹稳定性。
- 在八个基准测试中，该方法以单次前向实现竞争性性能，无需训练或模型修改。

## 摘要（原文）

> Face Image Quality Assessment (FIQA) is essential for reliable face recognition systems. Current approaches primarily exploit only final-layer representations, while training-free methods require multiple forward passes or backpropagation. We propose ViTNT-FIQA, a training-free approach that measures the stability of patch embedding evolution across intermediate Vision Transformer (ViT) blocks. We demonstrate that high-quality face images exhibit stable feature refinement trajectories across blocks, while degraded images show erratic transformations. Our method computes Euclidean distances between L2-normalized patch embeddings from consecutive transformer blocks and aggregates them into image-level quality scores. We empirically validate this correlation on a quality-labeled synthetic dataset with controlled degradation levels. Unlike existing training-free approaches, ViTNT-FIQA requires only a single forward pass without backpropagation or architectural modifications. Through extensive evaluation on eight benchmarks (LFW, AgeDB-30, CFP-FP, CALFW, Adience, CPLFW, XQLFW, IJB-C), we show that ViTNT-FIQA achieves competitive performance with state-of-the-art methods while maintaining computational efficiency and immediate applicability to any pre-trained ViT-based face recognition model.

