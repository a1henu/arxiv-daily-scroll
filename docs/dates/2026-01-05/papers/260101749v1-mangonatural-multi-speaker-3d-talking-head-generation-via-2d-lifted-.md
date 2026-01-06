---
layout: default
title: MANGO:Natural Multi-speaker 3D Talking Head Generation via 2D-Lifted Enhancement
---

# MANGO:Natural Multi-speaker 3D Talking Head Generation via 2D-Lifted Enhancement
**arXiv**：[2601.01749v1](https://arxiv.org/abs/2601.01749) · [PDF](https://arxiv.org/pdf/2601.01749.pdf)  
**作者**：Lei Zhu, Lijian Lin, Ye Zhu, Jiahao Wu, Xuehan Hou, Yu Li, Yunfei Liu, Jie Chen  

**一句话要点**：提出MANGO框架以解决多说话人3D对话头像生成中自然交互与伪3D标签噪声问题

**关键词**：3D对话头像生成, 多说话人音频驱动, 扩散变换器, 3D高斯渲染, 图像级监督, 交替训练

## 3 点简述
- 核心问题：现有方法依赖伪3D标签，难以实现自然的多说话人双向对话交互。
- 方法要点：采用两阶段框架，结合扩散变换器与3D高斯渲染器，通过交替训练利用纯图像级监督。
- 实验或效果：在MANGO-Dialog数据集上验证，显著提升3D对话运动的准确性和真实感。

## 摘要（原文）

> Current audio-driven 3D head generation methods mainly focus on single-speaker scenarios, lacking natural, bidirectional listen-and-speak interaction. Achieving seamless conversational behavior, where speaking and listening states transition fluidly remains a key challenge. Existing 3D conversational avatar approaches rely on error-prone pseudo-3D labels that fail to capture fine-grained facial dynamics. To address these limitations, we introduce a novel two-stage framework MANGO, which leveraging pure image-level supervision by alternately training to mitigate the noise introduced by pseudo-3D labels, thereby achieving better alignment with real-world conversational behaviors. Specifically, in the first stage, a diffusion-based transformer with a dual-audio interaction module models natural 3D motion from multi-speaker audio. In the second stage, we use a fast 3D Gaussian Renderer to generate high-fidelity images and provide 2D-level photometric supervision for the 3D motions through alternate training. Additionally, we introduce MANGO-Dialog, a high-quality dataset with over 50 hours of aligned 2D-3D conversational data across 500+ identities. Extensive experiments demonstrate that our method achieves exceptional accuracy and realism in modeling two-person 3D dialogue motion, significantly advancing the fidelity and controllability of audio-driven talking heads.

