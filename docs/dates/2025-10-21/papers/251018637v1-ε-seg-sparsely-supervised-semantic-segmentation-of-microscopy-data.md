---
layout: default
title: ε-Seg: Sparsely Supervised Semantic Segmentation of Microscopy Data
---

# ε-Seg: Sparsely Supervised Semantic Segmentation of Microscopy Data
**arXiv**：[2510.18637v1](https://arxiv.org/abs/2510.18637) · [PDF](https://arxiv.org/pdf/2510.18637.pdf)  
**作者**：Sheida Rahnamai Kordasiabi, Damian Dalle Nogare, Florian Jug  

**一句话要点**：提出ε-Seg方法，基于HVAE和稀疏标签，解决生物显微镜图像语义分割问题

**关键词**：语义分割, 稀疏监督学习, 层次变分自编码器, 对比学习, 显微镜图像分析

## 3 点简述
- 核心问题：电子显微镜图像语义分割困难，标签稀疏（≤0.05%）且结构复杂
- 方法要点：使用中心区域掩码、稀疏标签对比学习和GMM先验，优化HVAE潜在空间
- 实验或效果：在生物组织EM数据集上，实现竞争性稀疏监督分割结果

## 摘要（原文）

> Semantic segmentation of electron microscopy (EM) images of biological
> samples remains a challenge in the life sciences. EM data captures details of
> biological structures, sometimes with such complexity that even human observers
> can find it overwhelming. We introduce {\epsilon}-Seg, a method based on
> hierarchical variational autoencoders (HVAEs), employing center-region masking,
> sparse label contrastive learning (CL), a Gaussian mixture model (GMM) prior,
> and clustering-free label prediction. Center-region masking and the inpainting
> loss encourage the model to learn robust and representative embeddings to
> distinguish the desired classes, even if training labels are sparse (0.05% of
> the total image data or less). For optimal performance, we employ CL and a GMM
> prior to shape the latent space of the HVAE such that encoded input patches
> tend to cluster wrt. the semantic classes we wish to distinguish. Finally,
> instead of clustering latent embeddings for semantic segmentation, we propose a
> MLP semantic segmentation head to directly predict class labels from latent
> embeddings. We show empirical results of {\epsilon}-Seg and baseline methods on
> 2 dense EM datasets of biological tissues and demonstrate the applicability of
> our method also on fluorescence microscopy data. Our results show that
> {\epsilon}-Seg is capable of achieving competitive sparsely-supervised
> segmentation results on complex biological image data, even if only limited
> amounts of training labels are available.

