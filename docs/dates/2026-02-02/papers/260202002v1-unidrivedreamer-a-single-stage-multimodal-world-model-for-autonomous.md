---
layout: default
title: UniDriveDreamer: A Single-Stage Multimodal World Model for Autonomous Driving
---

# UniDriveDreamer: A Single-Stage Multimodal World Model for Autonomous Driving
**arXiv**：[2602.02002v1](https://arxiv.org/abs/2602.02002) · [PDF](https://arxiv.org/pdf/2602.02002.pdf)  
**作者**：Guosheng Zhao, Yaozeng Wang, Xiaofeng Wang, Zheng Zhu, Tingdong Yu, Guan Huang, Yongchen Zai, Ji Jiao, Changliang Xue, Xiaole Wang, Zhen Yang, Futang Zhu, Xingang Wang  

**一句话要点**：提出UniDriveDreamer，一个单阶段统一多模态世界模型，用于自动驾驶中的多模态未来观测生成。

**关键词**：自动驾驶世界模型, 多模态生成, 统一潜在锚定, 扩散变换器, LiDAR序列合成, 多摄像头视频生成

## 3 点简述
- 现有方法主要关注单模态生成，如多摄像头视频或LiDAR序列合成，缺乏统一多模态处理。
- 引入LiDAR和视频VAE，通过统一潜在锚定对齐多模态潜在分布，并使用扩散变换器联合建模几何对应和时间演化。
- 实验表明，UniDriveDreamer在视频和LiDAR生成上优于先前方法，并提升下游任务性能。

## 摘要（原文）

> World models have demonstrated significant promise for data synthesis in autonomous driving. However, existing methods predominantly concentrate on single-modality generation, typically focusing on either multi-camera video or LiDAR sequence synthesis. In this paper, we propose UniDriveDreamer, a single-stage unified multimodal world model for autonomous driving, which directly generates multimodal future observations without relying on intermediate representations or cascaded modules. Our framework introduces a LiDAR-specific variational autoencoder (VAE) designed to encode input LiDAR sequences, alongside a video VAE for multi-camera images. To ensure cross-modal compatibility and training stability, we propose Unified Latent Anchoring (ULA), which explicitly aligns the latent distributions of the two modalities. The aligned features are fused and processed by a diffusion transformer that jointly models their geometric correspondence and temporal evolution. Additionally, structured scene layout information is projected per modality as a conditioning signal to guide the synthesis. Extensive experiments demonstrate that UniDriveDreamer outperforms previous state-of-the-art methods in both video and LiDAR generation, while also yielding measurable improvements in downstream

