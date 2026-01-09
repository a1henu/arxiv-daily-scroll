---
layout: default
title: Vision-Language Agents for Interactive Forest Change Analysis
---

# Vision-Language Agents for Interactive Forest Change Analysis
**arXiv**：[2601.04497v1](https://arxiv.org/abs/2601.04497) · [PDF](https://arxiv.org/pdf/2601.04497.pdf)  
**作者**：James Brock, Ce Zhang, Nantheera Anantrasirichai  

**一句话要点**：提出基于LLM驱动的视觉语言代理系统，用于交互式森林变化分析

**关键词**：遥感图像变化解释, 视觉语言模型, 大语言模型代理, 森林变化分析, 多级变化检测

## 3 点简述
- 核心问题：遥感图像变化解释中像素级变化检测与语义变化描述准确性不足
- 方法要点：构建多级变化解释视觉语言骨干，结合LLM编排支持自然语言查询
- 实验或效果：在Forest-Change数据集上mIoU达67.10%，BLEU-4达40.17%

## 摘要（原文）

> Modern forest monitoring workflows increasingly benefit from the growing availability of high-resolution satellite imagery and advances in deep learning. Two persistent challenges in this context are accurate pixel-level change detection and meaningful semantic change captioning for complex forest dynamics. While large language models (LLMs) are being adapted for interactive data exploration, their integration with vision-language models (VLMs) for remote sensing image change interpretation (RSICI) remains underexplored. To address this gap, we introduce an LLM-driven agent for integrated forest change analysis that supports natural language querying across multiple RSICI tasks. The proposed system builds upon a multi-level change interpretation (MCI) vision-language backbone with LLM-based orchestration. To facilitate adaptation and evaluation in forest environments, we further introduce the Forest-Change dataset, which comprises bi-temporal satellite imagery, pixel-level change masks, and multi-granularity semantic change captions generated using a combination of human annotation and rule-based methods. Experimental results show that the proposed system achieves mIoU and BLEU-4 scores of 67.10% and 40.17% on the Forest-Change dataset, and 88.13% and 34.41% on LEVIR-MCI-Trees, a tree-focused subset of LEVIR-MCI benchmark for joint change detection and captioning. These results highlight the potential of interactive, LLM-driven RSICI systems to improve accessibility, interpretability, and efficiency of forest change analysis. All data and code are publicly available at https://github.com/JamesBrockUoB/ForestChat.

