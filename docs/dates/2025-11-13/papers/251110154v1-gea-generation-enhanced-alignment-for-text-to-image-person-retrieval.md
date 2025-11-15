---
layout: default
title: GEA: Generation-Enhanced Alignment for Text-to-Image Person Retrieval
---

# GEA: Generation-Enhanced Alignment for Text-to-Image Person Retrieval
**arXiv**：[2511.10154v1](https://arxiv.org/abs/2511.10154) · [PDF](https://arxiv.org/pdf/2511.10154.pdf)  
**作者**：Hao Zou, Runqing Zhang, Xue Zhou, Jianxiao Zou  

**一句话要点**：提出生成增强对齐方法以解决文本到图像行人检索中的模态差距问题

**关键词**：文本到图像检索, 行人检索, 跨模态对齐, 生成模型, 扩散模型

## 3 点简述
- 核心问题：文本查询无法准确反映图像内容，导致跨模态对齐差和数据集过拟合
- 方法要点：引入文本引导令牌增强和生成中间融合模块，利用生成图像桥接模态差距
- 实验或效果：在多个公开数据集上验证有效性，提升检索性能

## 摘要（原文）

> Text-to-Image Person Retrieval (TIPR) aims to retrieve person images based on natural language descriptions. Although many TIPR methods have achieved promising results, sometimes textual queries cannot accurately and comprehensively reflect the content of the image, leading to poor cross-modal alignment and overfitting to limited datasets. Moreover, the inherent modality gap between text and image further amplifies these issues, making accurate cross-modal retrieval even more challenging. To address these limitations, we propose the Generation-Enhanced Alignment (GEA) from a generative perspective. GEA contains two parallel modules: (1) Text-Guided Token Enhancement (TGTE), which introduces diffusion-generated images as intermediate semantic representations to bridge the gap between text and visual patterns. These generated images enrich the semantic representation of text and facilitate cross-modal alignment. (2) Generative Intermediate Fusion (GIF), which combines cross-attention between generated images, original images, and text features to generate a unified representation optimized by triplet alignment loss. We conduct extensive experiments on three public TIPR datasets, CUHK-PEDES, RSTPReid, and ICFG-PEDES, to evaluate the performance of GEA. The results justify the effectiveness of our method. More implementation details and extended results are available at https://github.com/sugelamyd123/Sup-for-GEA.

