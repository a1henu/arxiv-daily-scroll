---
layout: default
title: Unraveling MMDiT Blocks: Training-free Analysis and Enhancement of Text-conditioned Diffusion
---

# Unraveling MMDiT Blocks: Training-free Analysis and Enhancement of Text-conditioned Diffusion
**arXiv**：[2601.02211v1](https://arxiv.org/abs/2601.02211) · [PDF](https://arxiv.org/pdf/2601.02211.pdf)  
**作者**：Binglei Li, Mengping Yang, Zhiyu Tan, Junping Zhang, Hao Li  

**一句话要点**：提出训练自由策略以分析并增强基于MMDiT的文本条件扩散模型

**关键词**：文本到图像生成, 扩散模型, 训练自由分析, 多模态变换器, 文本对齐

## 3 点简述
- 核心问题：现有方法未全面理解MMDiT块在文本条件合成中的作用与交互机制
- 方法要点：通过移除、禁用和增强文本隐藏状态，系统分析各块功能，揭示语义与细节生成规律
- 实验或效果：在SD3.5上提升T2I-Combench++和GenEval分数，支持生成、编辑和加速任务

## 摘要（原文）

> Recent breakthroughs of transformer-based diffusion models, particularly with Multimodal Diffusion Transformers (MMDiT) driven models like FLUX and Qwen Image, have facilitated thrilling experiences in text-to-image generation and editing. To understand the internal mechanism of MMDiT-based models, existing methods tried to analyze the effect of specific components like positional encoding and attention layers. Yet, a comprehensive understanding of how different blocks and their interactions with textual conditions contribute to the synthesis process remains elusive. In this paper, we first develop a systematic pipeline to comprehensively investigate each block's functionality by removing, disabling and enhancing textual hidden-states at corresponding blocks. Our analysis reveals that 1) semantic information appears in earlier blocks and finer details are rendered in later blocks, 2) removing specific blocks is usually less disruptive than disabling text conditions, and 3) enhancing textual conditions in selective blocks improves semantic attributes. Building on these observations, we further propose novel training-free strategies for improved text alignment, precise editing, and acceleration. Extensive experiments demonstrated that our method outperforms various baselines and remains flexible across text-to-image generation, image editing, and inference acceleration. Our method improves T2I-Combench++ from 56.92% to 63.00% and GenEval from 66.42% to 71.63% on SD3.5, without sacrificing synthesis quality. These results advance understanding of MMDiT models and provide valuable insights to unlock new possibilities for further improvements.

