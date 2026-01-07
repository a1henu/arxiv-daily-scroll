---
layout: default
title: Flow Matching and Diffusion Models via PointNet for Generating Fluid Fields on Irregular Geometries
---

# Flow Matching and Diffusion Models via PointNet for Generating Fluid Fields on Irregular Geometries
**arXiv**：[2601.03030v1](https://arxiv.org/abs/2601.03030) · [PDF](https://arxiv.org/pdf/2601.03030.pdf)  
**作者**：Ali Kashefi  

**一句话要点**：提出Flow Matching PointNet和Diffusion PointNet，用于不规则几何上流体场的生成预测。

**关键词**：流体场生成, 点云处理, 几何深度学习, 流匹配模型, 扩散模型, 不规则几何

## 3 点简述
- 核心问题：传统方法将几何投影到均匀网格上存在像素化限制，且基于图神经网络的扩散模型易产生高频噪声。
- 方法要点：将PointNet融入流匹配和扩散模型，直接处理点云表示，无需辅助网络，简化架构。
- 实验或效果：在圆柱绕流数据集上，相比基线PointNet，预测更准确，对不完整几何更鲁棒。

## 摘要（原文）

> We present two novel generative geometric deep learning frameworks, termed Flow Matching PointNet and Diffusion PointNet, for predicting fluid flow variables on irregular geometries by incorporating PointNet into flow matching and diffusion models, respectively. In these frameworks, a reverse generative process reconstructs physical fields from standard Gaussian noise conditioned on unseen geometries. The proposed approaches operate directly on point-cloud representations of computational domains (e.g., grid vertices of finite-volume meshes) and therefore avoid the limitations of pixelation used to project geometries onto uniform lattices. In contrast to graph neural network-based diffusion models, Flow Matching PointNet and Diffusion PointNet do not exhibit high-frequency noise artifacts in the predicted fields. Moreover, unlike such approaches, which require auxiliary intermediate networks to condition geometry, the proposed frameworks rely solely on PointNet, resulting in a simple and unified architecture. The performance of the proposed frameworks is evaluated on steady incompressible flow past a cylinder, using a geometric dataset constructed by varying the cylinder's cross-sectional shape and orientation across samples. The results demonstrate that Flow Matching PointNet and Diffusion PointNet achieve more accurate predictions of velocity and pressure fields, as well as lift and drag forces, and exhibit greater robustness to incomplete geometries compared to a vanilla PointNet with the same number of trainable parameters.

