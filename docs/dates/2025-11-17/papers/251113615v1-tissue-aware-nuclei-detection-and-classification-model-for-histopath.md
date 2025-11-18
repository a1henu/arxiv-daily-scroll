---
layout: default
title: Tissue Aware Nuclei Detection and Classification Model for Histopathology Images
---

# Tissue Aware Nuclei Detection and Classification Model for Histopathology Images
**arXiv**：[2511.13615v1](https://arxiv.org/abs/2511.13615) · [PDF](https://arxiv.org/pdf/2511.13615.pdf)  
**作者**：Kesi Xu, Eleni Chiou, Ali Varamesh, Laura Acqualagna, Nasir Rajpoot  

**一句话要点**：提出TAND框架以解决组织病理图像中细胞检测与分类的标注依赖问题

**关键词**：组织病理图像, 细胞检测与分类, 点级监督, 组织掩码条件, Spatial-FiLM, ConvNeXt

## 3 点简述
- 核心问题：现有方法依赖专家详细标注且未充分利用组织上下文
- 方法要点：结合ConvNeXt编码-解码器与Virchow-2组织分割，通过Spatial-FiLM调制分类流
- 实验或效果：在PUMA基准上实现SOTA，显著提升组织依赖细胞类型分类

## 摘要（原文）

> Accurate nuclei detection and classification are fundamental to computational pathology, yet existing approaches are hindered by reliance on detailed expert annotations and insufficient use of tissue context. We present Tissue-Aware Nuclei Detection (TAND), a novel framework achieving joint nuclei detection and classification using point-level supervision enhanced by tissue mask conditioning. TAND couples a ConvNeXt-based encoder-decoder with a frozen Virchow-2 tissue segmentation branch, where semantic tissue probabilities selectively modulate the classification stream through a novel multi-scale Spatial Feature-wise Linear Modulation (Spatial-FiLM). On the PUMA benchmark, TAND achieves state-of-the-art performance, surpassing both tissue-agnostic baselines and mask-supervised methods. Notably, our approach demonstrates remarkable improvements in tissue-dependent cell types such as epithelium, endothelium, and stroma. To the best of our knowledge, this is the first method to condition per-cell classification on learned tissue masks, offering a practical pathway to reduce annotation burden.

