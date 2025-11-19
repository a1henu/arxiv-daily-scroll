---
layout: default
title: Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs
---

# Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs
**arXiv**：[2511.14315v1](https://arxiv.org/abs/2511.14315) · [PDF](https://arxiv.org/pdf/2511.14315.pdf)  
**作者**：Yiyi Miao, Taoyu Wu, Tong Chen, Ji Jiang, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  

**一句话要点**：提出Dental3R方法，从稀疏口腔照片实现稳健3D重建，用于远程正畸

**关键词**：口腔3D重建, 稀疏视图重建, 几何感知配对, 3D高斯溅射, 小波正则化, 远程正畸

## 3 点简述
- 核心问题：稀疏口腔照片存在大基线、光照不一致和镜面反射，导致姿态和几何估计不稳定，重建细节丢失
- 方法要点：采用几何感知配对策略选择高价值图像对，结合小波正则化3D高斯溅射，提升重建稳定性和细节保留
- 实验或效果：在950临床病例和195视频测试集上验证，优于现有方法，实现高质量新视角合成

## 摘要（原文）

> Intraoral 3D reconstruction is fundamental to digital orthodontics, yet conventional methods like intraoral scanning are inaccessible for remote tele-orthodontics, which typically relies on sparse smartphone imagery. While 3D Gaussian Splatting (3DGS) shows promise for novel view synthesis, its application to the standard clinical triad of unposed anterior and bilateral buccal photographs is challenging. The large view baselines, inconsistent illumination, and specular surfaces common in intraoral settings can destabilize simultaneous pose and geometry estimation. Furthermore, sparse-view photometric supervision often induces a frequency bias, leading to over-smoothed reconstructions that lose critical diagnostic details. To address these limitations, we propose \textbf{Dental3R}, a pose-free, graph-guided pipeline for robust, high-fidelity reconstruction from sparse intraoral photographs. Our method first constructs a Geometry-Aware Pairing Strategy (GAPS) to intelligently select a compact subgraph of high-value image pairs. The GAPS focuses on correspondence matching, thereby improving the stability of the geometry initialization and reducing memory usage. Building on the recovered poses and point cloud, we train the 3DGS model with a wavelet-regularized objective. By enforcing band-limited fidelity using a discrete wavelet transform, our approach preserves fine enamel boundaries and interproximal edges while suppressing high-frequency artifacts. We validate our approach on a large-scale dataset of 950 clinical cases and an additional video-based test set of 195 cases. Experimental results demonstrate that Dental3R effectively handles sparse, unposed inputs and achieves superior novel view synthesis quality for dental occlusion visualization, outperforming state-of-the-art methods.

