---
layout: default
title: Dual-Branch Center-Surrounding Contrast: Rethinking Contrastive Learning for 3D Point Clouds
---

# Dual-Branch Center-Surrounding Contrast: Rethinking Contrastive Learning for 3D Point Clouds
**arXiv**：[2512.08673v1](https://arxiv.org/abs/2512.08673) · [PDF](https://arxiv.org/pdf/2512.08673.pdf)  
**作者**：Shaofeng Zhang, Xuanqi Chen, Xiangdong Zhang, Sitong Wu, Junchi Yan  

**一句话要点**：提出双分支中心-周围对比框架以改进3D点云的自监督学习

**关键词**：3D点云, 自监督学习, 对比学习, 双分支架构, 几何特征学习

## 3 点简述
- 问题：现有3D点云自监督学习以生成方法为主，但难以捕获高层判别特征，对比方法在3D中应用不足且直接迁移2D方法效果不佳。
- 方法：通过分别掩码中心和周围部分构建双分支输入，结合补丁级对比损失增强几何信息捕获和局部敏感性。
- 效果：在多个协议下达到与生成方法相当或更优性能，尤其在MLP-LINEAR协议下显著超越基线方法。

## 摘要（原文）

> Most existing self-supervised learning (SSL) approaches for 3D point clouds are dominated by generative methods based on Masked Autoencoders (MAE). However, these generative methods have been proven to struggle to capture high-level discriminative features effectively, leading to poor performance on linear probing and other downstream tasks. In contrast, contrastive methods excel in discriminative feature representation and generalization ability on image data. Despite this, contrastive learning (CL) in 3D data remains scarce. Besides, simply applying CL methods designed for 2D data to 3D fails to effectively learn 3D local details. To address these challenges, we propose a novel Dual-Branch \textbf{C}enter-\textbf{S}urrounding \textbf{Con}trast (CSCon) framework. Specifically, we apply masking to the center and surrounding parts separately, constructing dual-branch inputs with center-biased and surrounding-biased representations to better capture rich geometric information. Meanwhile, we introduce a patch-level contrastive loss to further enhance both high-level information and local sensitivity. Under the FULL and ALL protocols, CSCon achieves performance comparable to generative methods; under the MLP-LINEAR, MLP-3, and ONLY-NEW protocols, our method attains state-of-the-art results, even surpassing cross-modal approaches. In particular, under the MLP-LINEAR protocol, our method outperforms the baseline (Point-MAE) by \textbf{7.9\%}, \textbf{6.7\%}, and \textbf{10.3\%} on the three variants of ScanObjectNN, respectively. The code will be made publicly available.

