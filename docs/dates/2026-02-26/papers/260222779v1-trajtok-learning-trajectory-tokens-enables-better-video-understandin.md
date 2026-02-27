---
layout: default
title: TrajTok: Learning Trajectory Tokens enables better Video Understanding
---

# TrajTok: Learning Trajectory Tokens enables better Video Understanding
**arXiv**：[2602.22779v1](https://arxiv.org/abs/2602.22779) · [PDF](https://arxiv.org/pdf/2602.22779.pdf)  
**作者**：Chenhao Zheng, Jieyu Zhang, Jianing Zhang, Weikai Huang, Ashutosh Kumar, Quan Kong, Oncel Tuzel, Chun-Liang Li, Ranjay Krishna  

**一句话要点**：提出TrajTok端到端视频分词器，通过动态适应语义复杂度提升视频理解效率与性能。

**关键词**：视频分词, 轨迹学习, 端到端训练, 视频理解, 长视频推理, 视觉语言模型

## 3 点简述
- 视频模型分词通常产生冗余令牌，限制效率与可扩展性。
- TrajTok集成统一分割器，在时空上隐式聚类像素，直接生成对象轨迹。
- 实验显示TrajTok在分类和检索基准上实现最佳精度，同时保持高效。

## 摘要（原文）

> Tokenization in video models, typically through patchification, generates an excessive and redundant number of tokens. This severely limits video efficiency and scalability. While recent trajectory-based tokenizers offer a promising solution by decoupling video duration from token count, they rely on complex external segmentation and tracking pipelines that are slow and task-agnostic. We propose TrajTok, an end-to-end video tokenizer module that is fully integrated and co-trained with video models for a downstream objective, dynamically adapting its token granularity to semantic complexity, independent of video duration. TrajTok contains a unified segmenter that performs implicit clustering over pixels in both space and time to directly produce object trajectories in a single forward pass. By prioritizing downstream adaptability over pixel-perfect segmentation fidelity, TrajTok is lightweight and efficient, yet empirically improves video understanding performance. With TrajTok, we implement a video CLIP model trained from scratch (TrajViT2). It achieves the best accuracy at scale across both classification and retrieval benchmarks, while maintaining efficiency comparable to the best token-merging methods. TrajTok also proves to be a versatile component beyond its role as a tokenizer. We show that it can be seamlessly integrated as either a probing head for pretrained visual features (TrajAdapter) or an alignment connector in vision-language models (TrajVLM) with especially strong performance in long-video reasoning.

