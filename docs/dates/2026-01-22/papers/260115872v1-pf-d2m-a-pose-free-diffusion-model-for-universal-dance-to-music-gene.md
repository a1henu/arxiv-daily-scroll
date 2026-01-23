---
layout: default
title: PF-D2M: A Pose-free Diffusion Model for Universal Dance-to-Music Generation
---

# PF-D2M: A Pose-free Diffusion Model for Universal Dance-to-Music Generation
**arXiv**：[2601.15872v1](https://arxiv.org/abs/2601.15872) · [PDF](https://arxiv.org/pdf/2601.15872.pdf)  
**作者**：Jaekwon Im, Natalia Polouliakh, Taketo Akama  

**一句话要点**：提出PF-D2M扩散模型，以解决多舞者与非人舞者场景下的舞蹈到音乐生成问题。

**关键词**：舞蹈到音乐生成, 扩散模型, 视觉特征提取, 渐进训练, 多舞者场景

## 3 点简述
- 核心问题：现有方法依赖单舞者运动特征和有限数据集，限制其在多舞者与非人舞者场景的适用性。
- 方法要点：采用基于扩散的模型，结合舞蹈视频视觉特征，通过渐进训练策略应对数据稀缺和泛化挑战。
- 实验或效果：客观与主观评估显示，PF-D2M在舞蹈-音乐对齐和音乐质量上达到先进水平。

## 摘要（原文）

> Dance-to-music generation aims to generate music that is aligned with dance movements. Existing approaches typically rely on body motion features extracted from a single human dancer and limited dance-to-music datasets, which restrict their performance and applicability to real-world scenarios involving multiple dancers and non-human dancers. In this paper, we propose PF-D2M, a universal diffusion-based dance-to-music generation model that incorporates visual features extracted from dance videos. PF-D2M is trained with a progressive training strategy that effectively addresses data scarcity and generalization challenges. Both objective and subjective evaluations show that PF-D2M achieves state-of-the-art performance in dance-music alignment and music quality.

