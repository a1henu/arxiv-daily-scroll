---
layout: default
title: MagicQuillV2: Precise and Interactive Image Editing with Layered Visual Cues
---

# MagicQuillV2: Precise and Interactive Image Editing with Layered Visual Cues
**arXiv**：[2512.03046v1](https://arxiv.org/abs/2512.03046) · [PDF](https://arxiv.org/pdf/2512.03046.pdf)  
**作者**：Zichen Liu, Yue Yu, Hao Ouyang, Qiuyu Wang, Shuailei Ma, Ka Leong Cheng, Wen Wang, Qingyan Bai, Yuxuan Zhang, Yanhong Zeng, Yixuan Li, Xing Zhu, Yujun Shen, Qifeng Chen  

**一句话要点**：提出MagicQuill V2系统，通过分层组合范式解决扩散模型在图像编辑中用户意图控制不足的问题。

**关键词**：图像编辑, 扩散模型, 分层组合, 用户意图控制, 局部编辑

## 3 点简述
- 核心问题：扩散模型使用单一提示难以解耦内容、位置和外观等用户意图，导致编辑控制粒度不足。
- 方法要点：将创意意图分解为内容、空间、结构和颜色层，结合数据生成管道和统一控制模块实现精确编辑。
- 实验或效果：广泛实验验证分层方法有效弥合用户意图差距，支持直观控制，包括对象移除等局部编辑。

## 摘要（原文）

> We propose MagicQuill V2, a novel system that introduces a \textbf{layered composition} paradigm to generative image editing, bridging the gap between the semantic power of diffusion models and the granular control of traditional graphics software. While diffusion transformers excel at holistic generation, their use of singular, monolithic prompts fails to disentangle distinct user intentions for content, position, and appearance. To overcome this, our method deconstructs creative intent into a stack of controllable visual cues: a content layer for what to create, a spatial layer for where to place it, a structural layer for how it is shaped, and a color layer for its palette. Our technical contributions include a specialized data generation pipeline for context-aware content integration, a unified control module to process all visual cues, and a fine-tuned spatial branch for precise local editing, including object removal. Extensive experiments validate that this layered approach effectively resolves the user intention gap, granting creators direct, intuitive control over the generative process.

