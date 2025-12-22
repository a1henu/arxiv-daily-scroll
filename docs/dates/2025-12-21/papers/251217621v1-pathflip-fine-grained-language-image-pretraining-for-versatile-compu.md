---
layout: default
title: PathFLIP: Fine-grained Language-Image Pretraining for Versatile Computational Pathology
---

# PathFLIP: Fine-grained Language-Image Pretraining for Versatile Computational Pathology
**arXiv**：[2512.17621v1](https://arxiv.org/abs/2512.17621) · [PDF](https://arxiv.org/pdf/2512.17621.pdf)  
**作者**：Fengchun Liu, Songhan Jiang, Linghan Cai, Ziyue Wang, Yongbing Zhang  

**一句话要点**：提出PathFLIP框架，通过细粒度语言-图像预训练解决全切片图像多模态理解难题

**关键词**：计算病理学, 视觉语言模型, 全切片图像, 细粒度对齐, 指令跟随, 区域级嵌入

## 3 点简述
- 现有方法难以捕捉全切片图像中文本与数千个图像块间的细粒度对应关系
- PathFLIP将幻灯片级描述分解为区域级子描述，生成文本条件区域嵌入以增强视觉-语言对齐
- 在四个基准测试中优于现有大规模病理视觉语言模型，且训练数据需求显著减少

## 摘要（原文）

> While Vision-Language Models (VLMs) have achieved notable progress in computational pathology (CPath), the gigapixel scale and spatial heterogeneity of Whole Slide Images (WSIs) continue to pose challenges for multimodal understanding. Existing alignment methods struggle to capture fine-grained correspondences between textual descriptions and visual cues across thousands of patches from a slide, compromising their performance on downstream tasks. In this paper, we propose PathFLIP (Pathology Fine-grained Language-Image Pretraining), a novel framework for holistic WSI interpretation. PathFLIP decomposes slide-level captions into region-level subcaptions and generates text-conditioned region embeddings to facilitate precise visual-language grounding. By harnessing Large Language Models (LLMs), PathFLIP can seamlessly follow diverse clinical instructions and adapt to varied diagnostic contexts. Furthermore, it exhibits versatile capabilities across multiple paradigms, efficiently handling slide-level classification and retrieval, fine-grained lesion localization, and instruction following. Extensive experiments demonstrate that PathFLIP outperforms existing large-scale pathological VLMs on four representative benchmarks while requiring significantly less training data, paving the way for fine-grained, instruction-aware WSI interpretation in clinical practice.

