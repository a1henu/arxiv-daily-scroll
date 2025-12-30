---
layout: default
title: RealX3D: A Physically-Degraded 3D Benchmark for Multi-view Visual Restoration and Reconstruction
---

# RealX3D: A Physically-Degraded 3D Benchmark for Multi-view Visual Restoration and Reconstruction
**arXiv**：[2512.23437v1](https://arxiv.org/abs/2512.23437) · [PDF](https://arxiv.org/pdf/2512.23437.pdf)  
**作者**：Shuhong Liu, Chenyu Bao, Ziteng Cui, Yun Liu, Xuangeng Chu, Lin Gu, Marcos V. Conde, Ryo Umagami, Tomohiro Hashimoto, Zijian Hu, Tianhan Xu, Yuan Gan, Yusuke Kurose, Tatsuya Harada  

**一句话要点**：提出RealX3D基准，用于多视角视觉恢复与三维重建在物理退化下的评估。

**关键词**：多视角视觉恢复, 三维重建基准, 物理退化数据集

## 3 点简述
- 核心问题：现有多视角方法在真实世界物理退化（如光照、散射）下重建质量显著下降。
- 方法要点：构建包含多种物理退化类型和严重级别的真实捕获数据集，提供像素对齐的低质量/高质量视图。
- 实验或效果：基准测试显示优化和前馈方法在物理退化下性能大幅降低，突显当前方法的脆弱性。

## 摘要（原文）

> We introduce RealX3D, a real-capture benchmark for multi-view visual restoration and 3D reconstruction under diverse physical degradations. RealX3D groups corruptions into four families, including illumination, scattering, occlusion, and blurring, and captures each at multiple severity levels using a unified acquisition protocol that yields pixel-aligned LQ/GT views. Each scene includes high-resolution capture, RAW images, and dense laser scans, from which we derive world-scale meshes and metric depth. Benchmarking a broad range of optimization-based and feed-forward methods shows substantial degradation in reconstruction quality under physical corruptions, underscoring the fragility of current multi-view pipelines in real-world challenging environments.

