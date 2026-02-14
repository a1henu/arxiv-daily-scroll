---
layout: default
title: Learning Perceptual Representations for Gaming NR-VQA with Multi-Task FR Signals
---

# Learning Perceptual Representations for Gaming NR-VQA with Multi-Task FR Signals
**arXiv**：[2602.11903v1](https://arxiv.org/abs/2602.11903) · [PDF](https://arxiv.org/pdf/2602.11903.pdf)  
**作者**：Yu-Chih Chen, Michael Wang, Chieh-Dun Wen, Kai-Siang Ma, Avinab Saha, Li-Heng Chen, Alan Bovik  

**一句话要点**：提出MTL-VQA框架，利用多任务全参考信号学习感知特征，以解决游戏视频无参考质量评估的挑战。

**关键词**：无参考视频质量评估, 多任务学习, 游戏视频, 感知特征学习, 全参考信号

## 3 点简述
- 核心问题：游戏视频无参考质量评估因数据集有限和内容特性（如快速运动、风格化图形）而困难。
- 方法要点：通过多任务学习，联合优化全参考目标并自适应加权，学习可迁移的共享表示。
- 实验或效果：在游戏视频数据集上，MTL-VQA在监督和自监督设置下均达到先进性能。

## 摘要（原文）

> No-reference video quality assessment (NR-VQA) for gaming videos is challenging due to limited human-rated datasets and unique content characteristics including fast motion, stylized graphics, and compression artifacts. We present MTL-VQA, a multi-task learning framework that uses full-reference metrics as supervisory signals to learn perceptually meaningful features without human labels for pretraining. By jointly optimizing multiple full-reference (FR) objectives with adaptive task weighting, our approach learns shared representations that transfer effectively to NR-VQA. Experiments on gaming video datasets show MTL-VQA achieves performance competitive with state-of-the-art NR-VQA methods across both MOS-supervised and label-efficient/self-supervised settings.

