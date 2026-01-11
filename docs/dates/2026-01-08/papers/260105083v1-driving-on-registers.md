---
layout: default
title: Driving on Registers
---

# Driving on Registers
**arXiv**：[2601.05083v1](https://arxiv.org/abs/2601.05083) · [PDF](https://arxiv.org/pdf/2601.05083.pdf)  
**作者**：Ellington Kirby, Alexandre Boulch, Yihong Xu, Yuan Yin, Gilles Puy, Éloi Zablocki, Andrei Bursuc, Spyros Gidaris, Renaud Marlet, Florent Bartoccioni, Anh-Quan Cao, Nermin Samet, Tuan-Hung VU, Matthieu Cord  

**一句话要点**：提出DrivoR，一种基于Transformer的端到端自动驾驶架构，通过相机感知寄存器令牌压缩多相机特征。

**关键词**：端到端自动驾驶, Transformer架构, 多相机特征压缩, 轨迹生成, 行为条件驾驶, 轻量解码器

## 3 点简述
- 核心问题：端到端自动驾驶中多相机特征处理的计算效率与准确性平衡。
- 方法要点：引入相机感知寄存器令牌压缩特征，驱动轻量Transformer解码器生成和评分轨迹。
- 实验或效果：在NAVSIM和HUGSIM基准上优于或匹配基线，实现高效自适应驾驶。

## 摘要（原文）

> We present DrivoR, a simple and efficient transformer-based architecture for end-to-end autonomous driving. Our approach builds on pretrained Vision Transformers (ViTs) and introduces camera-aware register tokens that compress multi-camera features into a compact scene representation, significantly reducing downstream computation without sacrificing accuracy. These tokens drive two lightweight transformer decoders that generate and then score candidate trajectories. The scoring decoder learns to mimic an oracle and predicts interpretable sub-scores representing aspects such as safety, comfort, and efficiency, enabling behavior-conditioned driving at inference. Despite its minimal design, DrivoR outperforms or matches strong contemporary baselines across NAVSIM-v1, NAVSIM-v2, and the photorealistic closed-loop HUGSIM benchmark. Our results show that a pure-transformer architecture, combined with targeted token compression, is sufficient for accurate, efficient, and adaptive end-to-end driving. Code and checkpoints will be made available via the project page.

