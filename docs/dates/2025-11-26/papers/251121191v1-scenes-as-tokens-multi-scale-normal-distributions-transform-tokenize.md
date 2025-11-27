---
layout: default
title: Scenes as Tokens: Multi-Scale Normal Distributions Transform Tokenizer for General 3D Vision-Language Understanding
---

# Scenes as Tokens: Multi-Scale Normal Distributions Transform Tokenizer for General 3D Vision-Language Understanding
**arXiv**：[2511.21191v1](https://arxiv.org/abs/2511.21191) · [PDF](https://arxiv.org/pdf/2511.21191.pdf)  
**作者**：Yutao Tang, Cheng Zhao, Gaurav Mittal, Rohith Kukkala, Rama Chellappa, Cheng Peng, Mei Chen  

**一句话要点**：提出NDTokenizer3D以解决3D场景多任务理解中的有效tokenization问题

**关键词**：3D视觉语言模型, 场景tokenization, 多尺度NDT表示, 统一架构, 3D场景理解

## 3 点简述
- 核心问题：3D场景难以token化为整体场景token，并应用于多样化理解任务
- 方法要点：基于多尺度NDT表示的三阶段tokenization流程，融合跨尺度特征生成场景token
- 实验或效果：在3D Referring Segmentation、VQA和Dense Captioning任务中取得显著提升

## 摘要（原文）

> Recent advances in 3D vision-language models (VLMs) highlight a strong potential for 3D scene understanding and reasoning. However, effectively tokenizing 3D scenes into holistic scene tokens, and leveraging these tokens across diverse 3D understanding tasks, remain highly challenging. We present NDTokenizer3D, a generalist 3D VLM that performs a wide range of 3D scene understanding tasks while naturally supporting human interactions, thereby bridging language-level reasoning with 3D spatial understanding. The core of our approach is a novel three-stage scene tokenization pipeline built upon a Multi-Scale Normal Distributions Transform (NDT) representation, paired with a Multi-Scale NDT Decoder (MSDec). Specifically, NDTokenizer3D first constructs a multi-scale NDT representation from raw high-resolution point clouds, preserving both global context and fine-grained geometric details. Next, the MSDec progressively fuses cross-scale NDT features, producing holistic scene tokens consumable by LLM endpoints. Beyond tokenization, MSDec is repurposed as a general interface for human-interactive prompting (points, boxes, masks) and segmentation-mask decoding, unifying diverse 3D scene understanding tasks within a single architecture. With this compact and unified design, NDTokenizer3D offers a fine-grained, general-purpose 3D VLM, achieving remarkable improvements in 3D Referring Segmentation, 3D Visual Question Answering, and 3D Dense Captioning.

