---
layout: default
title: FacEDiT: Unified Talking Face Editing and Generation via Facial Motion Infilling
---

# FacEDiT: Unified Talking Face Editing and Generation via Facial Motion Infilling
**arXiv**：[2512.14056v1](https://arxiv.org/abs/2512.14056) · [PDF](https://arxiv.org/pdf/2512.14056.pdf)  
**作者**：Kim Sung-Bin, Joohyun Chang, David Harwath, Tae-Hyun Oh  

**一句话要点**：提出FacEDiT，通过语音条件面部运动填充统一处理说话人脸编辑与生成。

**关键词**：说话人脸编辑, 面部运动填充, 扩散Transformer, 语音条件生成, 自监督学习

## 3 点简述
- 核心问题：说话人脸编辑与生成常被视为独立任务，缺乏统一框架。
- 方法要点：基于扩散Transformer和流匹配，以掩码自编码方式学习语音条件面部运动填充。
- 实验或效果：引入FacEDiTBench数据集，验证方法在编辑和生成任务中实现准确语音对齐和视觉连续性。

## 摘要（原文）

> Talking face editing and face generation have often been studied as distinct problems. In this work, we propose viewing both not as separate tasks but as subtasks of a unifying formulation, speech-conditional facial motion infilling. We explore facial motion infilling as a self-supervised pretext task that also serves as a unifying formulation of dynamic talking face synthesis. To instantiate this idea, we propose FacEDiT, a speech-conditional Diffusion Transformer trained with flow matching. Inspired by masked autoencoders, FacEDiT learns to synthesize masked facial motions conditioned on surrounding motions and speech. This formulation enables both localized generation and edits, such as substitution, insertion, and deletion, while ensuring seamless transitions with unedited regions. In addition, biased attention and temporal smoothness constraints enhance boundary continuity and lip synchronization. To address the lack of a standard editing benchmark, we introduce FacEDiTBench, the first dataset for talking face editing, featuring diverse edit types and lengths, along with new evaluation metrics. Extensive experiments validate that talking face editing and generation emerge as subtasks of speech-conditional motion infilling; FacEDiT produces accurate, speech-aligned facial edits with strong identity preservation and smooth visual continuity while generalizing effectively to talking face generation.

