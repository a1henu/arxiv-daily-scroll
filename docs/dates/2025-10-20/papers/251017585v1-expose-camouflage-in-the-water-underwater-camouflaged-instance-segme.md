---
layout: default
title: Expose Camouflage in the Water: Underwater Camouflaged Instance Segmentation and Dataset
---

# Expose Camouflage in the Water: Underwater Camouflaged Instance Segmentation and Dataset
**arXiv**：[2510.17585v1](https://arxiv.org/abs/2510.17585) · [PDF](https://arxiv.org/pdf/2510.17585.pdf)  
**作者**：Chuhong Wang, Hua Li, Chongyi Li, Huazhong Liu, Xiongxin Tang, Sam Kwong  

**一句话要点**：提出UCIS-SAM网络与UCIS4K数据集以解决水下伪装实例分割挑战

**关键词**：水下伪装实例分割, UCIS4K数据集, UCIS-SAM网络, 通道平衡优化, 频域特征集成, 多尺度特征聚合

## 3 点简述
- 核心问题：水下环境退化与伪装对象融合导致实例分割困难
- 方法要点：基于SAM设计CBOM、FDTIM和MFFAM模块提升特征学习与分割精度
- 实验或效果：在UCIS4K和公共基准上优于现有方法

## 摘要（原文）

> With the development of underwater exploration and marine protection,
> underwater vision tasks are widespread. Due to the degraded underwater
> environment, characterized by color distortion, low contrast, and blurring,
> camouflaged instance segmentation (CIS) faces greater challenges in accurately
> segmenting objects that blend closely with their surroundings. Traditional
> camouflaged instance segmentation methods, trained on terrestrial-dominated
> datasets with limited underwater samples, may exhibit inadequate performance in
> underwater scenes. To address these issues, we introduce the first underwater
> camouflaged instance segmentation (UCIS) dataset, abbreviated as UCIS4K, which
> comprises 3,953 images of camouflaged marine organisms with instance-level
> annotations. In addition, we propose an Underwater Camouflaged Instance
> Segmentation network based on Segment Anything Model (UCIS-SAM). Our UCIS-SAM
> includes three key modules. First, the Channel Balance Optimization Module
> (CBOM) enhances channel characteristics to improve underwater feature learning,
> effectively addressing the model's limited understanding of underwater
> environments. Second, the Frequency Domain True Integration Module (FDTIM) is
> proposed to emphasize intrinsic object features and reduce interference from
> camouflage patterns, enhancing the segmentation performance of camouflaged
> objects blending with their surroundings. Finally, the Multi-scale Feature
> Frequency Aggregation Module (MFFAM) is designed to strengthen the boundaries
> of low-contrast camouflaged instances across multiple frequency bands,
> improving the model's ability to achieve more precise segmentation of
> camouflaged objects. Extensive experiments on the proposed UCIS4K and public
> benchmarks show that our UCIS-SAM outperforms state-of-the-art approaches.

