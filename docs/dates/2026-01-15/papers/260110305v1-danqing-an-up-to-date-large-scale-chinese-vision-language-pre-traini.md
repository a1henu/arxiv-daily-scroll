---
layout: default
title: DanQing: An Up-to-Date Large-Scale Chinese Vision-Language Pre-training Dataset
---

# DanQing: An Up-to-Date Large-Scale Chinese Vision-Language Pre-training Dataset
**arXiv**：[2601.10305v1](https://arxiv.org/abs/2601.10305) · [PDF](https://arxiv.org/pdf/2601.10305.pdf)  
**作者**：Hengyu Shen, Tiancheng Gu, Bin Qin, Lan Wu, Yuling Wu, Shuo Tan, Zelong Sun, Jun Wang, Nan Wu, Xiang An, Weidong Cai, Ziyong Feng, Kaicheng Yang  

**一句话要点**：提出DanQing大规模中文视觉-语言预训练数据集以解决高质量数据稀缺问题

**关键词**：视觉-语言预训练, 中文数据集, 跨模态检索, 零样本分类, 数据质量筛选

## 3 点简述
- 核心问题：中文视觉-语言预训练因高质量图像-文本对数据稀缺而发展滞后
- 方法要点：通过严格筛选流程从Common Crawl构建1亿对高质量中文图像-文本数据，主要基于2024-2025年网络数据
- 实验或效果：基于SigLIP2模型的持续预训练实验显示，DanQing在零样本分类、跨模态检索等中文下游任务中表现优异

## 摘要（原文）

> Vision-Language Pre-training (VLP) models demonstrate strong performance across various downstream tasks by learning from large-scale image-text pairs through contrastive pretraining. The release of extensive English image-text datasets (e.g., COYO-700M and LAION-400M) has enabled widespread adoption of models such as CLIP and SigLIP in tasks including cross-modal retrieval and image captioning. However, the advancement of Chinese vision-language pretraining has substantially lagged behind, due to the scarcity of high-quality Chinese image-text data. To address this gap, we develop a comprehensive pipeline for constructing a high-quality Chinese cross-modal dataset. As a result, we propose DanQing, which contains 100 million image-text pairs collected from Common Crawl. Different from existing datasets, DanQing is curated through a more rigorous selection process, yielding superior data quality. Moreover, DanQing is primarily built from 2024-2025 web data, enabling models to better capture evolving semantic trends and thus offering greater practical utility. We compare DanQing with existing datasets by continual pre-training of the SigLIP2 model. Experimental results show that DanQing consistently achieves superior performance across a range of Chinese downstream tasks, including zero-shot classification, cross-modal retrieval, and LMM-based evaluations. To facilitate further research in Chinese vision-language pre-training, we will open-source the DanQing dataset under the Creative Common CC-BY 4.0 license.

