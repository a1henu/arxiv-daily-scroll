---
layout: default
title: From Frames to Sequences: Temporally Consistent Human-Centric Dense Prediction
---

# From Frames to Sequences: Temporally Consistent Human-Centric Dense Prediction
**arXiv**：[2602.01661v1](https://arxiv.org/abs/2602.01661) · [PDF](https://arxiv.org/pdf/2602.01661.pdf)  
**作者**：Xingyu Miao, Junting Dong, Qin Zhao, Yuhang Yang, Junhao Chen, Yang Long  

**一句话要点**：提出基于合成数据和ViT的统一密集预测模型，以解决视频中人中心密集预测的时间一致性问题。

**关键词**：时间一致性, 人中心密集预测, 合成数据生成, ViT模型, 视频序列学习

## 3 点简述
- 核心问题：现有模型在视频中处理人中心密集预测时，存在时间不一致性，如闪烁，且缺乏多任务监督数据。
- 方法要点：使用可扩展合成数据管道生成帧级和序列级标签，结合ViT模型注入几何先验和通道重加权模块。
- 实验或效果：在THuman2.1和Hi4D上达到SOTA，并有效泛化到野外视频。

## 摘要（原文）

> In this work, we focus on the challenge of temporally consistent human-centric dense prediction across video sequences. Existing models achieve strong per-frame accuracy but often flicker under motion, occlusion, and lighting changes, and they rarely have paired human video supervision for multiple dense tasks. We address this gap with a scalable synthetic data pipeline that generates photorealistic human frames and motion-aligned sequences with pixel-accurate depth, normals, and masks. Unlike prior static data synthetic pipelines, our pipeline provides both frame-level labels for spatial learning and sequence-level supervision for temporal learning. Building on this, we train a unified ViT-based dense predictor that (i) injects an explicit human geometric prior via CSE embeddings and (ii) improves geometry-feature reliability with a lightweight channel reweighting module after feature fusion. Our two-stage training strategy, combining static pretraining with dynamic sequence supervision, enables the model first to acquire robust spatial representations and then refine temporal consistency across motion-aligned sequences. Extensive experiments show that we achieve state-of-the-art performance on THuman2.1 and Hi4D and generalize effectively to in-the-wild videos.

