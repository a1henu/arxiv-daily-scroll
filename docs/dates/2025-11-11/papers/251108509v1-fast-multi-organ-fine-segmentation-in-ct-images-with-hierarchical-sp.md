---
layout: default
title: Fast Multi-Organ Fine Segmentation in CT Images with Hierarchical Sparse Sampling and Residual Transformer
---

# Fast Multi-Organ Fine Segmentation in CT Images with Hierarchical Sparse Sampling and Residual Transformer
**arXiv**：[2511.08509v1](https://arxiv.org/abs/2511.08509) · [PDF](https://arxiv.org/pdf/2511.08509.pdf)  
**作者**：Xueqi Guo, Halid Ziya Yerebakan, Yoshihisa Shinagawa, Kritika Iyer, Gerardo Hermosillo Valadez  

**一句话要点**：提出基于分层稀疏采样和残差Transformer的快速多器官精细分割方法，以解决CT图像分割中速度与精度的权衡问题。

**关键词**：多器官分割, 分层稀疏采样, 残差Transformer, CT图像, 实时分割, 医学图像分析

## 3 点简述
- 核心问题：3D医学图像多器官分割中，逐体素分割方法计算成本高，速度与精度难以兼顾。
- 方法要点：采用分层稀疏采样策略减少计算时间，并利用残差Transformer网络提取多级信息。
- 实验或效果：在内部和公共数据集上，分割性能优于现有快速分类器，CPU上速度约2.24秒。

## 摘要（原文）

> Multi-organ segmentation of 3D medical images is fundamental with meaningful applications in various clinical automation pipelines. Although deep learning has achieved superior performance, the time and memory consumption of segmenting the entire 3D volume voxel by voxel using neural networks can be huge. Classifiers have been developed as an alternative in cases with certain points of interest, but the trade-off between speed and accuracy remains an issue. Thus, we propose a novel fast multi-organ segmentation framework with the usage of hierarchical sparse sampling and a Residual Transformer. Compared with whole-volume analysis, the hierarchical sparse sampling strategy could successfully reduce computation time while preserving a meaningful hierarchical context utilizing multiple resolution levels. The architecture of the Residual Transformer segmentation network could extract and combine information from different levels of information in the sparse descriptor while maintaining a low computational cost. In an internal data set containing 10,253 CT images and the public dataset TotalSegmentator, the proposed method successfully improved qualitative and quantitative segmentation performance compared to the current fast organ classifier, with fast speed at the level of ~2.24 seconds on CPU hardware. The potential of achieving real-time fine organ segmentation is suggested.

