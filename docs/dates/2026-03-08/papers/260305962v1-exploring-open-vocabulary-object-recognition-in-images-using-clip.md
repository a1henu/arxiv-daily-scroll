---
layout: default
title: Exploring Open-Vocabulary Object Recognition in Images using CLIP
---

# Exploring Open-Vocabulary Object Recognition in Images using CLIP
**arXiv**：[2603.05962v1](https://arxiv.org/abs/2603.05962) · [PDF](https://arxiv.org/pdf/2603.05962.pdf)  
**作者**：Wei Yu Chen, Ying Dai  

**一句话要点**：提出基于CLIP的两阶段开放词汇物体识别框架，以简化系统并提升泛化能力。

**关键词**：开放词汇物体识别, CLIP, 两阶段策略, CNN/MLP编码, 嵌入相似性匹配

## 3 点简述
- 核心问题：现有开放词汇物体识别方法系统复杂、训练成本高且泛化有限。
- 方法要点：采用物体分割后识别的两阶段策略，结合CLIP生成嵌入，并引入CNN/MLP编码增强灵活性。
- 实验或效果：在COCO等数据集上，免训练的CLIP编码方法取得最高平均AP，优于当前先进方法。

## 摘要（原文）

> To address the limitations of existing open-vocabulary object recognition methods, specifically high system complexity, substantial training costs, and limited generalization, this paper proposes a novel Open-Vocabulary Object Recognition (OVOR) framework based on a streamlined two-stage strategy: object segmentation followed by recognition. The framework eliminates the need for complex retraining and labor-intensive annotation. After cropping object regions, we generate object-level image embeddings alongside category-level text embeddings using CLIP, which facilitates arbitrary vocabularies. To reduce reliance on CLIP and enhance encoding flexibility, we further introduce a CNN/MLP-based method that extracts convolutional neural network (CNN) feature maps and utilizes a multilayer perceptron (MLP) to align visual features with text embeddings. These embeddings are concatenated and processed via Singular Value Decomposition (SVD) to construct a shared representation space. Finally, recognition is performed through embedding similarity matching. Experiments on COCO, Pascal VOC, and ADE20K demonstrate that training-free, CLIP-based encoding without SVD achieves the highest average AP, outperforming current state-of-the-art methods. Simultaneously, the results highlight the potential of CNN/MLP-based image encoding for OVOR.

