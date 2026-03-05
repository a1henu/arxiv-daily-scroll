---
layout: default
title: Efficient Point Cloud Processing with High-Dimensional Positional Encoding and Non-Local MLPs
---

# Efficient Point Cloud Processing with High-Dimensional Positional Encoding and Non-Local MLPs
**arXiv**：[2603.04099v1](https://arxiv.org/abs/2603.04099) · [PDF](https://arxiv.org/pdf/2603.04099.pdf)  
**作者**：Yanmei Zou, Hongshan Yu, Yaonan Wang, Zhengeng Yang, Xieyuanli Chen, Kailun Yang, Naveed Akhtar  

**一句话要点**：提出高维位置编码与非局部MLP以高效处理点云，基于ABS-REF范式提升性能与效率。

**关键词**：点云处理, 高维位置编码, 非局部MLP, ABS-REF范式, 效率优化

## 3 点简述
- 核心问题：MLP模型架构复杂，性能来源不明确，且局部操作耗时，限制点云处理应用。
- 方法要点：引入ABS-REF视图模块化特征提取，设计高维位置编码模块显式利用位置信息，用非局部MLP替换局部MLP以高效捕获非局部关系。
- 实验或效果：在多个数据集和任务上，HPENets在效率和效果间取得平衡，FLOPs显著降低，性能指标优于PointNeXt等基线。

## 摘要（原文）

> Multi-Layer Perceptron (MLP) models are the foundation of contemporary point cloud processing. However, their complex network architectures obscure the source of their strength and limit the application of these models. In this article, we develop a two-stage abstraction and refinement (ABS-REF) view for modular feature extraction in point cloud processing. This view elucidates that whereas the early models focused on ABS stages, the more recent techniques devise sophisticated REF stages to attain performance advantages. Then, we propose a High-dimensional Positional Encoding (HPE) module to explicitly utilize intrinsic positional information, extending the ``positional encoding'' concept from Transformer literature. HPE can be readily deployed in MLP-based architectures and is compatible with transformer-based methods. Within our ABS-REF view, we rethink local aggregation in MLP-based methods and propose replacing time-consuming local MLP operations, which are used to capture local relationships among neighbors. Instead, we use non-local MLPs for efficient non-local information updates, combined with the proposed HPE for effective local information representation. We leverage our modules to develop HPENets, a suite of MLP networks that follow the ABS-REF paradigm, incorporating a scalable HPE-based REF stage. Extensive experiments on seven public datasets across four different tasks show that HPENets deliver a strong balance between efficiency and effectiveness. Notably, HPENet surpasses PointNeXt, a strong MLP-based counterpart, by 1.1% mAcc, 4.0% mIoU, 1.8% mIoU, and 0.2% Cls. mIoU, with only 50.0%, 21.5%, 23.1%, 44.4% of FLOPs on ScanObjectNN, S3DIS, ScanNet, and ShapeNetPart, respectively. Source code is available at https://github.com/zouyanmei/HPENet_v2.git.

