---
layout: default
title: LatentVLA: Efficient Vision-Language Models for Autonomous Driving via Latent Action Prediction
---

# LatentVLA: Efficient Vision-Language Models for Autonomous Driving via Latent Action Prediction
**arXiv**：[2601.05611v1](https://arxiv.org/abs/2601.05611) · [PDF](https://arxiv.org/pdf/2601.05611.pdf)  
**作者**：Chengen Xie, Bin Sun, Tianyu Li, Junjie Wu, Zhihui Hao, XianPeng Lang, Hongyang Li  

**一句话要点**：提出LatentVLA框架，通过潜在动作预测训练视觉-语言-动作模型，解决自动驾驶中长尾场景和实时效率问题。

**关键词**：自动驾驶, 视觉-语言-动作模型, 潜在动作预测, 知识蒸馏, 自监督学习, 实时效率

## 3 点简述
- 核心问题：端到端自动驾驶模型在长尾场景中表现不佳，现有VLA模型存在轨迹预测不精确、语言标注依赖和计算效率低的问题。
- 方法要点：采用自监督潜在动作预测，无需语言标注，通过知识蒸馏将VLA泛化能力迁移到高效视觉网络。
- 实验或效果：在NAVSIM基准上达到92.4 PDMS分数，并在nuScenes基准上展示强零样本泛化能力。

## 摘要（原文）

> End-to-end autonomous driving models trained on largescale datasets perform well in common scenarios but struggle with rare, long-tail situations due to limited scenario diversity. Recent Vision-Language-Action (VLA) models leverage broad knowledge from pre-trained visionlanguage models to address this limitation, yet face critical challenges: (1) numerical imprecision in trajectory prediction due to discrete tokenization, (2) heavy reliance on language annotations that introduce linguistic bias and annotation burden, and (3) computational inefficiency from multi-step chain-of-thought reasoning hinders real-time deployment. We propose LatentVLA, a novel framework that employs self-supervised latent action prediction to train VLA models without language annotations, eliminating linguistic bias while learning rich driving representations from unlabeled trajectory data. Through knowledge distillation, LatentVLA transfers the generalization capabilities of VLA models to efficient vision-based networks, achieving both robust performance and real-time efficiency. LatentVLA establishes a new state-of-the-art on the NAVSIM benchmark with a PDMS score of 92.4 and demonstrates strong zeroshot generalization on the nuScenes benchmark.

