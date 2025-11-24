---
layout: default
title: An Artificial Intelligence Framework for Measuring Human Spine Aging Using MRI
---

# An Artificial Intelligence Framework for Measuring Human Spine Aging Using MRI
**arXiv**：[2511.17485v1](https://arxiv.org/abs/2511.17485) · [PDF](https://arxiv.org/pdf/2511.17485.pdf)  
**作者**：Roozbeh Bazargani, Saqib Abdullah Basar, Daniel Daly-Grafstein, Rodrigo Solis Pompa, Soojin Lee, Saurabh Garg, Yuntong Ma, John A. Carrino, Siavash Khallaghi, Sam Hashemi  

**一句话要点**：提出基于深度学习的MRI脊柱年龄估计框架以评估脊柱健康

**关键词**：脊柱年龄估计, 深度学习, MRI分析, 退行性疾病, 生物标志物

## 3 点简述
- 核心问题：脊柱随年龄退化影响健康，需从MRI图像中量化评估。
- 方法要点：使用UMAP和HDBSCAN聚类筛选数据，并通过消融研究优化模型。
- 实验效果：脊柱年龄差与退行性疾病及生活方式因素显著相关。

## 摘要（原文）

> The human spine is a complex structure composed of 33 vertebrae. It holds the body and is important for leading a healthy life. The spine is vulnerable to age-related degenerations that can be identified through magnetic resonance imaging (MRI). In this paper we propose a novel computer-vison-based deep learning method to estimate spine age using images from over 18,000 MRI series. Data are restricted to subjects with only age-related spine degeneration. Eligibility criteria are created by identifying common age-based clusters of degenerative spine conditions using uniform manifold approximation and projection (UMAP) and hierarchical density-based spatial clustering of applications with noise (HDBSCAN). Model selection is determined using a detailed ablation study on data size, loss, and the effect of different spine regions. We evaluate the clinical utility of our model by calculating the difference between actual spine age and model-predicted age, the spine age gap (SAG), and examining the association between these differences and spine degenerative conditions and lifestyle factors. We find that SAG is associated with conditions including disc bulges, disc osteophytes, spinal stenosis, and fractures, as well as lifestyle factors like smoking and physically demanding work, and thus may be a useful biomarker for measuring overall spine health.

