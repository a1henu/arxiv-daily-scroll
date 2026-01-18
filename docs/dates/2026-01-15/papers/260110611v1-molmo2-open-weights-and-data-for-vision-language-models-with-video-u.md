---
layout: default
title: Molmo2: Open Weights and Data for Vision-Language Models with Video Understanding and Grounding
---

# Molmo2: Open Weights and Data for Vision-Language Models with Video Understanding and Grounding
**arXiv**：[2601.10611v1](https://arxiv.org/abs/2601.10611) · [PDF](https://arxiv.org/pdf/2601.10611.pdf)  
**作者**：Christopher Clark, Jieyu Zhang, Zixian Ma, Jae Sung Park, Mohammadreza Salehi, Rohun Tripathi, Sangho Lee, Zhongzheng Ren, Chris Dongjoo Kim, Yinuo Yang, Vincent Shao, Yue Yang, Weikai Huang, Ziqi Gao, Taira Anderson, Jianrui Zhang, Jitesh Jain, George Stoica, Winson Han, Ali Farhadi, Ranjay Krishna  

**一句话要点**：提出Molmo2视觉语言模型及开源数据集，解决视频理解与像素级定位问题。

**关键词**：视频语言模型, 像素级定位, 开源数据集, 视频理解, 多模态训练

## 3 点简述
- 当前开源视频语言模型依赖闭源模型蒸馏或数据不透明，缺乏改进基础。
- 贡献7个视频和2个多图像开源数据集，采用高效训练方案提升性能。
- 在视频计数、描述和定位任务上超越开源模型，部分任务优于闭源模型。

## 摘要（原文）

> Today's strongest video-language models (VLMs) remain proprietary. The strongest open-weight models either rely on synthetic data from proprietary VLMs, effectively distilling from them, or do not disclose their training data or recipe. As a result, the open-source community lacks the foundations needed to improve on the state-of-the-art video (and image) language models. Crucially, many downstream applications require more than just high-level video understanding; they require grounding -- either by pointing or by tracking in pixels. Even proprietary models lack this capability. We present Molmo2, a new family of VLMs that are state-of-the-art among open-source models and demonstrate exceptional new capabilities in point-driven grounding in single image, multi-image, and video tasks. Our key contribution is a collection of 7 new video datasets and 2 multi-image datasets, including a dataset of highly detailed video captions for pre-training, a free-form video Q&A dataset for fine-tuning, a new object tracking dataset with complex queries, and an innovative new video pointing dataset, all collected without the use of closed VLMs. We also present a training recipe for this data utilizing an efficient packing and message-tree encoding scheme, and show bi-directional attention on vision tokens and a novel token-weight strategy improves performance. Our best-in-class 8B model outperforms others in the class of open weight and data models on short videos, counting, and captioning, and is competitive on long-videos. On video-grounding Molmo2 significantly outperforms existing open-weight models like Qwen3-VL (35.5 vs 29.6 accuracy on video counting) and surpasses proprietary models like Gemini 3 Pro on some tasks (38.4 vs 20.0 F1 on video pointing and 56.2 vs 41.1 J&F on video tracking).

