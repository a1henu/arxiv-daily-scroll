---
layout: default
title: A Spatial Semantics and Continuity Perception Attention for Remote Sensing Water Body Change Detection
---

# A Spatial Semantics and Continuity Perception Attention for Remote Sensing Water Body Change Detection
**arXiv**：[2511.16143v1](https://arxiv.org/abs/2511.16143) · [PDF](https://arxiv.org/pdf/2511.16143.pdf)  
**作者**：Quanqing Ma, Jiaen Chen, Peng Wang, Yao Zheng, Qingzhan Zhao, Yuchen Zheng  

**一句话要点**：提出SSCP注意力模块和HSRW-CD数据集以解决遥感水体变化检测中空间语义与结构利用不足的问题

**关键词**：遥感水体变化检测, 空间语义注意力, 结构连续性感知, 高分辨率数据集, 深度学习模块, 变化检测网络

## 3 点简述
- 核心问题：高分辨率数据集稀缺，现有方法未充分利用深度特征的空间语义与结构信息
- 方法要点：设计SSCP模块，集成多语义空间、结构关系全局和通道自注意力，提升水体特征判别力
- 实验或效果：在HSRW-CD和Water-CD数据集上验证SSCP的有效性和泛化性，代码与数据集开源

## 摘要（原文）

> Remote sensing Water Body Change Detection (WBCD) aims to detect water body surface changes from bi-temporal images of the same geographic area. Recently, the scarcity of high spatial resolution datasets for WBCD restricts its application in urban and rural regions, which require more accurate positioning. Meanwhile, previous deep learning-based methods fail to comprehensively exploit the spatial semantic and structural information in deep features in the change detection networks. To resolve these concerns, we first propose a new dataset, HSRW-CD, with a spatial resolution higher than 3 meters for WBCD. Specifically, it contains a large number of image pairs, widely covering various water body types. Besides, a Spatial Semantics and Continuity Perception (SSCP) attention module is designed to fully leverage both the spatial semantics and structure of deep features in the WBCD networks, significantly improving the discrimination capability for water body. The proposed SSCP has three components: the Multi-Semantic spatial Attention (MSA), the Structural Relation-aware Global Attention (SRGA), and the Channel-wise Self-Attention (CSA). The MSA enhances the spatial semantics of water body features and provides precise spatial semantic priors for the CSA. Then, the SRGA further extracts spatial structure to learn the spatial continuity of the water body. Finally, the CSA utilizes the spatial semantic and structural priors from the MSA and SRGA to compute the similarity across channels. Specifically designed as a plug-and-play module for water body deep features, the proposed SSCP allows integration into existing WBCD models. Numerous experiments conducted on the proposed HSRW-CD and Water-CD datasets validate the effectiveness and generalization of the SSCP. The code of this work and the HSRW-CD dataset will be accessed at https://github.com/QingMa1/SSCP.

