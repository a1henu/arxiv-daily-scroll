---
layout: default
title: Multi-Modal Soccer Scene Analysis with Masked Pre-Training
---

# Multi-Modal Soccer Scene Analysis with Masked Pre-Training
**arXiv**：[2512.19528v1](https://arxiv.org/abs/2512.19528) · [PDF](https://arxiv.org/pdf/2512.19528.pdf)  
**作者**：Marc Peral, Guillem Capellera, Luis Ferraz, Antonio Rubio, Antonio Agudo  

**一句话要点**：提出多模态架构与CropDrop预训练策略，用于足球战术视频的球轨迹推断、状态分类和持球者识别。

**关键词**：多模态学习, 足球场景分析, Transformer架构, 掩码预训练, 球轨迹推断, 持球者识别

## 3 点简述
- 核心问题：从足球战术视频中分析球轨迹、状态和持球者，无需直接球位置输入，处理噪声和遮挡。
- 方法要点：整合球员轨迹、类型和图像裁剪，使用社会时空Transformer块，引入CropDrop预训练防止过度依赖图像特征。
- 实验或效果：在大规模数据集上验证，所有任务优于现有基线，强调结构化与视觉线索结合及现实掩码策略的重要性。

## 摘要（原文）

> In this work we propose a multi-modal architecture for analyzing soccer scenes from tactical camera footage, with a focus on three core tasks: ball trajectory inference, ball state classification, and ball possessor identification. To this end, our solution integrates three distinct input modalities (player trajectories, player types and image crops of individual players) into a unified framework that processes spatial and temporal dynamics using a cascade of sociotemporal transformer blocks. Unlike prior methods, which rely heavily on accurate ball tracking or handcrafted heuristics, our approach infers the ball trajectory without direct access to its past or future positions, and robustly identifies the ball state and ball possessor under noisy or occluded conditions from real top league matches. We also introduce CropDrop, a modality-specific masking pre-training strategy that prevents over-reliance on image features and encourages the model to rely on cross-modal patterns during pre-training. We show the effectiveness of our approach on a large-scale dataset providing substantial improvements over state-of-the-art baselines in all tasks. Our results highlight the benefits of combining structured and visual cues in a transformer-based architecture, and the importance of realistic masking strategies in multi-modal learning.

