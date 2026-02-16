---
layout: default
title: LiDAR-Anchored Collaborative Distillation for Robust 2D Representations
---

# LiDAR-Anchored Collaborative Distillation for Robust 2D Representations
**arXiv**：[2602.12524v1](https://arxiv.org/abs/2602.12524) · [PDF](https://arxiv.org/pdf/2602.12524.pdf)  
**作者**：Wonjun Jo, Hyunwoo Ha, Kim Ji-Yeon, Hawook Jeong, Tae-Hyun Oh  

**一句话要点**：提出基于LiDAR锚定的协同蒸馏方法，以增强2D图像编码器在噪声和恶劣天气下的鲁棒性。

**关键词**：自监督学习, LiDAR锚定, 协同蒸馏, 2D图像编码器, 鲁棒视觉感知, 恶劣天气条件

## 3 点简述
- 核心问题：预训练2D图像编码器在噪声和恶劣天气条件下性能不足，影响视觉感知的鲁棒性。
- 方法要点：利用3D LiDAR作为自监督信号，通过协同蒸馏提升2D编码器的鲁棒性，同时保留其原有能力。
- 实验或效果：在多种下游任务和条件下优于竞争方法，展现出强泛化能力和3D感知提升。

## 摘要（原文）

> As deep learning continues to advance, self-supervised learning has made considerable strides. It allows 2D image encoders to extract useful features for various downstream tasks, including those related to vision-based systems. Nevertheless, pre-trained 2D image encoders fall short in conducting the task under noisy and adverse weather conditions beyond clear daytime scenes, which require for robust visual perception. To address these issues, we propose a novel self-supervised approach, \textbf{Collaborative Distillation}, which leverages 3D LiDAR as self-supervision to improve robustness to noisy and adverse weather conditions in 2D image encoders while retaining their original capabilities. Our method outperforms competing methods in various downstream tasks across diverse conditions and exhibits strong generalization ability. In addition, our method also improves 3D awareness stemming from LiDAR's characteristics. This advancement highlights our method's practicality and adaptability in real-world scenarios.

