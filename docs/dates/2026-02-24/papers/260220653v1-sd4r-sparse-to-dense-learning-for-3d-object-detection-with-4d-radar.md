---
layout: default
title: SD4R: Sparse-to-Dense Learning for 3D Object Detection with 4D Radar
---

# SD4R: Sparse-to-Dense Learning for 3D Object Detection with 4D Radar
**arXiv**：[2602.20653v1](https://arxiv.org/abs/2602.20653) · [PDF](https://arxiv.org/pdf/2602.20653.pdf)  
**作者**：Xiaokai Bai, Jiahao Cheng, Songkai Wang, Yixuan Luo, Lianqing Zheng, Xiaohan Zhang, Si-Yuan Cao, Hui-Liang Shen  

**一句话要点**：提出SD4R框架，通过稀疏到稠密学习解决4D雷达点云在3D物体检测中的稀疏与噪声问题。

**关键词**：4D雷达感知, 点云稠密化, 3D物体检测, 噪声抑制, 前景点生成, 支柱化特征

## 3 点简述
- 核心问题：4D雷达点云稀疏且含噪声，现有方法难以处理极端稀疏场景，影响3D检测准确性。
- 方法要点：使用前景点生成器减少噪声传播并稠化点云，结合logit-query编码器增强支柱化特征表示。
- 实验或效果：在View-of-Delft数据集上实现先进性能，有效降低噪声并提升前景点稠密度。

## 摘要（原文）

> 4D radar measurements offer an affordable and weather-robust solution for 3D perception. However, the inherent sparsity and noise of radar point clouds present significant challenges for accurate 3D object detection, underscoring the need for effective and robust point clouds densification. Despite recent progress, existing densification methods often fail to address the extreme sparsity of 4D radar point clouds and exhibit limited robustness when processing scenes with a small number of points. In this paper, we propose SD4R, a novel framework that transforms sparse radar point clouds into dense representations. SD4R begins by utilizing a foreground point generator (FPG) to mitigate noise propagation and produce densified point clouds. Subsequently, a logit-query encoder (LQE) enhances conventional pillarization, resulting in robust feature representations. Through these innovations, our SD4R demonstrates strong capability in both noise reduction and foreground point densification. Extensive experiments conducted on the publicly available View-of-Delft dataset demonstrate that SD4R achieves state-of-the-art performance. Source code is available at https://github.com/lancelot0805/SD4R.

