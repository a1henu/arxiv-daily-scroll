---
layout: default
title: ReactEMG Stroke: Healthy-to-Stroke Few-shot Adaptation for sEMG-Based Intent Detection
---

# ReactEMG Stroke: Healthy-to-Stroke Few-shot Adaptation for sEMG-Based Intent Detection
**arXiv**：[2601.22090v1](https://arxiv.org/abs/2601.22090) · [PDF](https://arxiv.org/pdf/2601.22090.pdf)  
**作者**：Runsheng Wang, Katelyn Lee, Xinyue Zhu, Lauren Winterbottom, Dawn M. Nilsen, Joel Stein, Matei Ciocarlie  

**一句话要点**：提出健康到中风少样本适应方法，提升基于表面肌电的中风意图检测鲁棒性。

**关键词**：表面肌电意图检测, 少样本适应, 中风康复, 健康到中风迁移, 参数高效微调

## 3 点简述
- 核心问题：中风后表面肌电意图检测需大量个体校准，且易受变异性影响。
- 方法要点：利用健康人群大规模预训练模型初始化，通过少量中风个体数据微调适应。
- 实验或效果：在包含分布偏移的测试集上，适应方法显著提升准确率，优于零样本迁移和中风专用训练。

## 摘要（原文）

> Surface electromyography (sEMG) is a promising control signal for assist-as-needed hand rehabilitation after stroke, but detecting intent from paretic muscles often requires lengthy, subject-specific calibration and remains brittle to variability. We propose a healthy-to-stroke adaptation pipeline that initializes an intent detector from a model pretrained on large-scale able-bodied sEMG, then fine-tunes it for each stroke participant using only a small amount of subject-specific data. Using a newly collected dataset from three individuals with chronic stroke, we compare adaptation strategies (head-only tuning, parameter-efficient LoRA adapters, and full end-to-end fine-tuning) and evaluate on held-out test sets that include realistic distribution shifts such as within-session drift, posture changes, and armband repositioning. Across conditions, healthy-pretrained adaptation consistently improves stroke intent detection relative to both zero-shot transfer and stroke-only training under the same data budget; the best adaptation methods improve average transition accuracy from 0.42 to 0.61 and raw accuracy from 0.69 to 0.78. These results suggest that transferring a reusable healthy-domain EMG representation can reduce calibration burden while improving robustness for real-time post-stroke intent detection.

