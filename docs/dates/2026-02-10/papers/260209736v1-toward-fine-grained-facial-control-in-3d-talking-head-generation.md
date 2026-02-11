---
layout: default
title: Toward Fine-Grained Facial Control in 3D Talking Head Generation
---

# Toward Fine-Grained Facial Control in 3D Talking Head Generation
**arXiv**：[2602.09736v1](https://arxiv.org/abs/2602.09736) · [PDF](https://arxiv.org/pdf/2602.09736.pdf)  
**作者**：Shaoyang Xie, Xiaofeng Cong, Baosheng Yu, Zhipeng Gui, Jie Gui, Yuan Yan Tang, James Tin-Yau Kwok  

**一句话要点**：提出FG-3DGS框架，通过频率感知解耦和细化对齐机制，实现3D说话头像的细粒度面部控制。

**关键词**：3D说话头像生成, 高斯溅射, 频率感知解耦, 唇同步, 面部控制, 后渲染对齐

## 3 点简述
- 核心问题：现有3D高斯溅射方法在说话头像生成中面临唇同步不准确和面部抖动挑战，影响真实感。
- 方法要点：引入频率感知解耦策略，分别建模低频和高频面部区域，并结合后渲染对齐机制提升唇同步精度。
- 实验或效果：在广泛数据集上验证，FG-3DGS在生成高保真、唇同步的说话头像视频方面优于现有方法。

## 摘要（原文）

> Audio-driven talking head generation is a core component of digital avatars, and 3D Gaussian Splatting has shown strong performance in real-time rendering of high-fidelity talking heads. However, achieving precise control over fine-grained facial movements remains a significant challenge, particularly due to lip-synchronization inaccuracies and facial jitter, both of which can contribute to the uncanny valley effect. To address these challenges, we propose Fine-Grained 3D Gaussian Splatting (FG-3DGS), a novel framework that enables temporally consistent and high-fidelity talking head generation. Our method introduces a frequency-aware disentanglement strategy to explicitly model facial regions based on their motion characteristics. Low-frequency regions, such as the cheeks, nose, and forehead, are jointly modeled using a standard MLP, while high-frequency regions, including the eyes and mouth, are captured separately using a dedicated network guided by facial area masks. The predicted motion dynamics, represented as Gaussian deltas, are applied to the static Gaussians to generate the final head frames, which are rendered via a rasterizer using frame-specific camera parameters. Additionally, a high-frequency-refined post-rendering alignment mechanism, learned from large-scale audio-video pairs by a pretrained model, is incorporated to enhance per-frame generation and achieve more accurate lip synchronization. Extensive experiments on widely used datasets for talking head generation demonstrate that our method outperforms recent state-of-the-art approaches in producing high-fidelity, lip-synced talking head videos.

