---
layout: default
title: Natural Language-Driven Global Mapping of Martian Landforms
---

# Natural Language-Driven Global Mapping of Martian Landforms
**arXiv**：[2601.15949v1](https://arxiv.org/abs/2601.15949) · [PDF](https://arxiv.org/pdf/2601.15949.pdf)  
**作者**：Yiran Wang, Shuoyuan Wang, Zhaoran Wei, Jiannan Zhao, Zhonghua Yao, Zejian Xie, Songxin Zhang, Jun Huang, Bingyi Jing, Hongxin Wei  

**一句话要点**：提出MarScope框架，通过自然语言驱动实现火星地貌的无标签全局映射

**关键词**：行星视觉语言框架, 自然语言驱动映射, 无标签语义检索, 火星地貌分析, 共享语义空间对齐

## 3 点简述
- 核心问题：行星表面分析中自然语言语义与像素级图像组织不匹配，限制可扩展探索
- 方法要点：基于20万图像-文本对训练，对齐图像与文本到共享语义空间，支持灵活语义检索
- 实验或效果：在5秒内响应全球任意查询，F1分数高达0.978，扩展至过程导向分析和相似性映射

## 摘要（原文）

> Planetary surfaces are typically analyzed using high-level semantic concepts in natural language, yet vast orbital image archives remain organized at the pixel level. This mismatch limits scalable, open-ended exploration of planetary surfaces. Here we present MarScope, a planetary-scale vision-language framework enabling natural language-driven, label-free mapping of Martian landforms. MarScope aligns planetary images and text in a shared semantic space, trained on over 200,000 curated image-text pairs. This framework transforms global geomorphic mapping on Mars by replacing pre-defined classifications with flexible semantic retrieval, enabling arbitrary user queries across the entire planet in 5 seconds with F1 scores up to 0.978. Applications further show that it extends beyond morphological classification to facilitate process-oriented analysis and similarity-based geomorphological mapping at a planetary scale. MarScope establishes a new paradigm where natural language serves as a direct interface for scientific discovery over massive geospatial datasets.

