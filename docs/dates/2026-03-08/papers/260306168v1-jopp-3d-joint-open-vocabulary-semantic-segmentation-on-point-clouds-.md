---
layout: default
title: JOPP-3D: Joint Open Vocabulary Semantic Segmentation on Point Clouds and Panoramas
---

# JOPP-3D: Joint Open Vocabulary Semantic Segmentation on Point Clouds and Panoramas
**arXiv**：[2603.06168v1](https://arxiv.org/abs/2603.06168) · [PDF](https://arxiv.org/pdf/2603.06168.pdf)  
**作者**：Sandeep Inuganti, Hideaki Kanayama, Kanta Shimizu, Mahdi Chamseddine, Soichiro Yokota, Didier Stricker, Jason Rambach  

**一句话要点**：提出JOPP-3D框架，通过联合全景图像和点云数据实现开放词汇语义分割。

**关键词**：开放词汇语义分割, 点云处理, 全景图像分析, 视觉语言对齐, 多模态融合

## 3 点简述
- 核心问题：3D点云和全景图像的语义分割面临标注数据稀缺和固定标签模型适应性有限的问题。
- 方法要点：将RGB-D全景图像转换为切向透视图像和点云，提取对齐视觉语言特征以支持自然语言查询生成语义掩码。
- 实验或效果：在Stanford-2D-3D-s和ToF-360数据集上验证，相比SOTA在开放和封闭词汇2D和3D分割中取得显著提升。

## 摘要（原文）

> Semantic segmentation across visual modalities such as 3D point clouds and panoramic images remains a challenging task, primarily due to the scarcity of annotated data and the limited adaptability of fixed-label models. In this paper, we present JOPP-3D, an open-vocabulary semantic segmentation framework that jointly leverages panoramic and point cloud data to enable language-driven scene understanding. We convert RGB-D panoramic images into their corresponding tangential perspective images and 3D point clouds, then use these modalities to extract and align foundational vision-language features. This allows natural language querying to generate semantic masks on both input modalities. Experimental evaluation on the Stanford-2D-3D-s and ToF-360 datasets demonstrates the capability of JOPP-3D to produce coherent and semantically meaningful segmentations across panoramic and 3D domains. Our proposed method achieves a significant improvement compared to the SOTA in open and closed vocabulary 2D and 3D semantic segmentation.

