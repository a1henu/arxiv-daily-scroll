---
layout: default
title: DyaDiT: A Multi-Modal Diffusion Transformer for Socially Favorable Dyadic Gesture Generation
---

# DyaDiT: A Multi-Modal Diffusion Transformer for Socially Favorable Dyadic Gesture Generation
**arXiv**：[2602.23165v1](https://arxiv.org/abs/2602.23165) · [PDF](https://arxiv.org/pdf/2602.23165.pdf)  
**作者**：Yichen Peng, Jyun-Ting Song, Siyeol Jung, Ruofan Liu, Haiyang Liu, Xuangeng Chu, Ruicong Liu, Erwin Wu, Hideki Koike, Kris Kitani  

**一句话要点**：提出DyaDiT多模态扩散Transformer，基于双人音频生成社交友好的对话手势

**关键词**：手势生成, 扩散Transformer, 多模态融合, 社交互动, 双人对话, 运动先验

## 3 点简述
- 核心问题：现有方法忽略社交上下文和双人互动动态，仅从单音频生成单人手势。
- 方法要点：采用多模态扩散Transformer，融合双人音频和可选社交上下文，利用运动字典编码先验，可结合对方手势生成响应性动作。
- 实验或效果：在标准指标上超越现有方法，用户研究显示其生成的手势更受偏好，体现社交友好性。

## 摘要（原文）

> Generating realistic conversational gestures are essential for achieving natural, socially engaging interactions with digital humans. However, existing methods typically map a single audio stream to a single speaker's motion, without considering social context or modeling the mutual dynamics between two people engaging in conversation. We present DyaDiT, a multi-modal diffusion transformer that generates contextually appropriate human motion from dyadic audio signals. Trained on Seamless Interaction Dataset, DyaDiT takes dyadic audio with optional social-context tokens to produce context-appropriate motion. It fuses information from both speakers to capture interaction dynamics, uses a motion dictionary to encode motion priors, and can optionally utilize the conversational partner's gestures to produce more responsive motion. We evaluate DyaDiT on standard motion generation metrics and conduct quantitative user studies, demonstrating that it not only surpasses existing methods on objective metrics but is also strongly preferred by users, highlighting its robustness and socially favorable motion generation. Code and models will be released upon acceptance.

