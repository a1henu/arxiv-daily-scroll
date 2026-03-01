---
layout: default
title: An automatic counting algorithm for the quantification and uncertainty analysis of the number of microglial cells trainable in small and heterogeneous datasets
---

# An automatic counting algorithm for the quantification and uncertainty analysis of the number of microglial cells trainable in small and heterogeneous datasets
**arXiv**：[2602.22974v1](https://arxiv.org/abs/2602.22974) · [PDF](https://arxiv.org/pdf/2602.22974.pdf)  
**作者**：L. Martino, M. M. Garcia, P. S. Paradas, E. Curbelo  

**一句话要点**：提出自动核计数算法以解决小数据集下微胶质细胞计数及不确定性分析问题

**关键词**：微胶质细胞计数, 小数据集训练, 非参数方法, 不确定性分析, 图像预处理, 核计数算法

## 3 点简述
- 核心问题：自动计数微胶质细胞，避免手动标注耗时且需专业训练，传统方法仅量化面积和强度，不提供细胞数。
- 方法要点：通过预处理过滤噪声，设计非参数非线性核计数算法，仅依赖一个超参数，易于小数据集训练，并能处理专家意见不确定性。
- 实验或效果：在人工和真实数据集上实验显示结果良好，提供相关Matlab代码。

## 摘要（原文）

> Counting immunopositive cells on biological tissues generally requires either manual annotation or (when available) automatic rough systems, for scanning signal surface and intensity in whole slide imaging. In this work, we tackle the problem of counting microglial cells in lumbar spinal cord cross-sections of rats by omitting cell detection and focusing only on the counting task. Manual cell counting is, however, a time-consuming task and additionally entails extensive personnel training. The classic automatic color-based methods roughly inform about the total labeled area and intensity (protein quantification) but do not specifically provide information on cell number. Since the images to be analyzed have a high resolution but a huge amount of pixels contain just noise or artifacts, we first perform a pre-processing generating several filtered images {(providing a tailored, efficient feature extraction)}. Then, we design an automatic kernel counter that is a non-parametric and non-linear method. The proposed scheme can be easily trained in small datasets since, in its basic version, it relies only on one hyper-parameter. However, being non-parametric and non-linear, the proposed algorithm is flexible enough to express all the information contained in rich and heterogeneous datasets as well (providing the maximum overfit if required). Furthermore, the proposed kernel counter also provides uncertainty estimation of the given prediction, and can directly tackle the case of receiving several expert opinions over the same image. Different numerical experiments with artificial and real datasets show very promising results. Related Matlab code is also provided.

