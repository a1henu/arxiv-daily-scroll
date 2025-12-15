---
layout: default
title: Cross-modal Context-aware Learning for Visual Prompt Guided Multimodal Image Understanding in Remote Sensing
---

# Cross-modal Context-aware Learning for Visual Prompt Guided Multimodal Image Understanding in Remote Sensing
**arXiv**：[2512.11680v1](https://arxiv.org/abs/2512.11680) · [PDF](https://arxiv.org/pdf/2512.11680.pdf)  
**作者**：Xu Zhang, Jiabin Fang, Zhuoming Ding, Jin Yuan, Xuan Liu, Qianjun Zhang, Zhiyong Li  

**一句话要点**：提出CLV-Net以解决遥感图像中视觉提示引导的多模态理解问题

**关键词**：遥感图像理解, 视觉提示引导, 上下文感知学习, 多模态对齐, 目标分割, 关系建模

## 3 点简述
- 现有方法在简单文本提示下难以引导模型关注用户相关区域
- CLV-Net通过视觉提示和上下文感知解码器增强目标表示与掩码质量
- 在基准数据集上超越现有方法，实现用户意图对齐的多模态输出

## 摘要（原文）

> Recent advances in image understanding have enabled methods that leverage large language models for multimodal reasoning in remote sensing. However, existing approaches still struggle to steer models to the user-relevant regions when only simple, generic text prompts are available. Moreover, in large-scale aerial imagery many objects exhibit highly similar visual appearances and carry rich inter-object relationships, which further complicates accurate recognition. To address these challenges, we propose Cross-modal Context-aware Learning for Visual Prompt-Guided Multimodal Image Understanding (CLV-Net). CLV-Net lets users supply a simple visual cue, a bounding box, to indicate a region of interest, and uses that cue to guide the model to generate correlated segmentation masks and captions that faithfully reflect user intent. Central to our design is a Context-Aware Mask Decoder that models and integrates inter-object relationships to strengthen target representations and improve mask quality. In addition, we introduce a Semantic and Relationship Alignment module: a Cross-modal Semantic Consistency Loss enhances fine-grained discrimination among visually similar targets, while a Relationship Consistency Loss enforces alignment between textual relations and visual interactions. Comprehensive experiments on two benchmark datasets show that CLV-Net outperforms existing methods and establishes new state-of-the-art results. The model effectively captures user intent and produces precise, intention-aligned multimodal outputs.

