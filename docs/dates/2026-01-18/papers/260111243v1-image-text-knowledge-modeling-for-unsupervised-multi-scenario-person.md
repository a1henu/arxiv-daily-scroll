---
layout: default
title: Image-Text Knowledge Modeling for Unsupervised Multi-Scenario Person Re-Identification
---

# Image-Text Knowledge Modeling for Unsupervised Multi-Scenario Person Re-Identification
**arXiv**：[2601.11243v1](https://arxiv.org/abs/2601.11243) · [PDF](https://arxiv.org/pdf/2601.11243.pdf)  
**作者**：Zhiqi Pang, Lingling Zhao, Yang Liu, Chunyu Wang, Gaurav Sharma  

**一句话要点**：提出图像-文本知识建模框架，以解决无监督多场景行人重识别任务。

**关键词**：无监督学习, 多场景行人重识别, 图像-文本建模, CLIP模型, 异构匹配

## 3 点简述
- 核心问题：无监督多场景行人重识别，涵盖跨分辨率、换装等多样场景。
- 方法要点：三阶段框架，利用CLIP模型，引入场景嵌入、文本嵌入优化和异构匹配模块。
- 实验或效果：在多个场景中优于现有方法，通过整合多场景知识提升整体性能。

## 摘要（原文）

> We propose unsupervised multi-scenario (UMS) person re-identification (ReID) as a new task that expands ReID across diverse scenarios (cross-resolution, clothing change, etc.) within a single coherent framework. To tackle UMS-ReID, we introduce image-text knowledge modeling (ITKM) -- a three-stage framework that effectively exploits the representational power of vision-language models. We start with a pre-trained CLIP model with an image encoder and a text encoder. In Stage I, we introduce a scenario embedding in the image encoder and fine-tune the encoder to adaptively leverage knowledge from multiple scenarios. In Stage II, we optimize a set of learned text embeddings to associate with pseudo-labels from Stage I and introduce a multi-scenario separation loss to increase the divergence between inter-scenario text representations. In Stage III, we first introduce cluster-level and instance-level heterogeneous matching modules to obtain reliable heterogeneous positive pairs (e.g., a visible image and an infrared image of the same person) within each scenario. Next, we propose a dynamic text representation update strategy to maintain consistency between text and image supervision signals. Experimental results across multiple scenarios demonstrate the superiority and generalizability of ITKM; it not only outperforms existing scenario-specific methods but also enhances overall performance by integrating knowledge from multiple scenarios.

