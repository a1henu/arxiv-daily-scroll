---
layout: default
title: Dropping Anchor and Spherical Harmonics for Sparse-view Gaussian Splatting
---

# Dropping Anchor and Spherical Harmonics for Sparse-view Gaussian Splatting
**arXiv**：[2602.20933v1](https://arxiv.org/abs/2602.20933) · [PDF](https://arxiv.org/pdf/2602.20933.pdf)  
**作者**：Shuangkang Fang, I-Chao Shen, Xuanyang Zhang, Zesheng Wang, Yufeng Wang, Wenrui Ding, Gang Yu, Takeo Igarashi  

**一句话要点**：提出DropAnSH-GS以解决稀疏视图下3D高斯泼溅的过拟合问题

**关键词**：3D高斯泼溅, 稀疏视图重建, Dropout正则化, 球谐系数, 模型压缩, 过拟合缓解

## 3 点简述
- 现有Dropout方法存在邻居补偿效应，削弱正则化效果
- DropAnSH-GS基于锚点同时移除空间邻居，破坏局部冗余
- 实验显示方法显著提升性能，支持灵活模型压缩

## 摘要（原文）

> Recent 3D Gaussian Splatting (3DGS) Dropout methods address overfitting under sparse-view conditions by randomly nullifying Gaussian opacities. However, we identify a neighbor compensation effect in these approaches: dropped Gaussians are often compensated by their neighbors, weakening the intended regularization. Moreover, these methods overlook the contribution of high-degree spherical harmonic coefficients (SH) to overfitting. To address these issues, we propose DropAnSH-GS, a novel anchor-based Dropout strategy. Rather than dropping Gaussians independently, our method randomly selects certain Gaussians as anchors and simultaneously removes their spatial neighbors. This effectively disrupts local redundancies near anchors and encourages the model to learn more robust, globally informed representations. Furthermore, we extend the Dropout to color attributes by randomly dropping higher-degree SH to concentrate appearance information in lower-degree SH. This strategy further mitigates overfitting and enables flexible post-training model compression via SH truncation. Experimental results demonstrate that DropAnSH-GS substantially outperforms existing Dropout methods with negligible computational overhead, and can be readily integrated into various 3DGS variants to enhance their performances. Project Website: https://sk-fun.fun/DropAnSH-GS

