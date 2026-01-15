---
layout: default
title: OpenVoxel: Training-Free Grouping and Captioning Voxels for Open-Vocabulary 3D Scene Understanding
---

# OpenVoxel: Training-Free Grouping and Captioning Voxels for Open-Vocabulary 3D Scene Understanding
**arXiv**：[2601.09575v1](https://arxiv.org/abs/2601.09575) · [PDF](https://arxiv.org/pdf/2601.09575.pdf)  
**作者**：Sheng-Yu Huang, Jaesung Choe, Yu-Chiang Frank Wang, Cheng Sun  

**一句话要点**：提出OpenVoxel，一种免训练算法，用于开放词汇3D场景理解中的体素分组与描述。

**关键词**：开放词汇3D场景理解, 免训练算法, 稀疏体素分组, 多模态大语言模型, 指代表达分割

## 3 点简述
- 核心问题：开放词汇3D场景理解需要从稀疏体素中分组和描述对象，传统方法依赖训练或文本编码器嵌入。
- 方法要点：基于稀疏体素栅格化模型，利用视觉语言模型和多模态大语言模型进行免训练分组和文本到文本搜索描述。
- 实验或效果：在复杂指代表达分割任务中表现优异，优于现有方法，代码将开源。

## 摘要（原文）

> We propose OpenVoxel, a training-free algorithm for grouping and captioning sparse voxels for the open-vocabulary 3D scene understanding tasks. Given the sparse voxel rasterization (SVR) model obtained from multi-view images of a 3D scene, our OpenVoxel is able to produce meaningful groups that describe different objects in the scene. Also, by leveraging powerful Vision Language Models (VLMs) and Multi-modal Large Language Models (MLLMs), our OpenVoxel successfully build an informative scene map by captioning each group, enabling further 3D scene understanding tasks such as open-vocabulary segmentation (OVS) or referring expression segmentation (RES). Unlike previous methods, our method is training-free and does not introduce embeddings from a CLIP/BERT text encoder. Instead, we directly proceed with text-to-text search using MLLMs. Through extensive experiments, our method demonstrates superior performance compared to recent studies, particularly in complex referring expression segmentation (RES) tasks. The code will be open.

