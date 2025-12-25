---
layout: default
title: DGSAN: Dual-Graph Spatiotemporal Attention Network for Pulmonary Nodule Malignancy Prediction
---

# DGSAN: Dual-Graph Spatiotemporal Attention Network for Pulmonary Nodule Malignancy Prediction
**arXiv**：[2512.20898v1](https://arxiv.org/abs/2512.20898) · [PDF](https://arxiv.org/pdf/2512.20898.pdf)  
**作者**：Xiao Yu, Zhaojie Fang, Guanyu Zhou, Yin Shen, Huoling Luo, Ye Li, Ahmed Elazab, Xiang Wan, Ruiquan Ge, Changmiao Wang  

**一句话要点**：提出双图时空注意力网络以提升肺结节恶性预测的准确性和效率。

**关键词**：肺结节恶性预测, 多模态融合, 图神经网络, 时空注意力, 医学影像分析

## 3 点简述
- 核心问题：现有肺结节恶性预测方法在融合多模态和多时间点信息时，依赖低效的向量拼接和简单互注意力，限制了性能提升。
- 方法要点：设计全局-局部特征编码器捕获结节特征，构建双图组织模态内和模态间关系，并引入分层跨模态图融合模块优化特征集成。
- 实验或效果：在NLST-cmst和CSTL数据集上验证，DGSAN在分类性能和计算效率上显著优于现有方法。

## 摘要（原文）

> Lung cancer continues to be the leading cause of cancer-related deaths globally. Early detection and diagnosis of pulmonary nodules are essential for improving patient survival rates. Although previous research has integrated multimodal and multi-temporal information, outperforming single modality and single time point, the fusion methods are limited to inefficient vector concatenation and simple mutual attention, highlighting the need for more effective multimodal information fusion. To address these challenges, we introduce a Dual-Graph Spatiotemporal Attention Network, which leverages temporal variations and multimodal data to enhance the accuracy of predictions. Our methodology involves developing a Global-Local Feature Encoder to better capture the local, global, and fused characteristics of pulmonary nodules. Additionally, a Dual-Graph Construction method organizes multimodal features into inter-modal and intra-modal graphs. Furthermore, a Hierarchical Cross-Modal Graph Fusion Module is introduced to refine feature integration. We also compiled a novel multimodal dataset named the NLST-cmst dataset as a comprehensive source of support for related research. Our extensive experiments, conducted on both the NLST-cmst and curated CSTL-derived datasets, demonstrate that our DGSAN significantly outperforms state-of-the-art methods in classifying pulmonary nodules with exceptional computational efficiency.

