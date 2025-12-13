---
layout: default
title: mmCounter: Static People Counting in Dense Indoor Scenarios Using mmWave Radar
---

# mmCounter: Static People Counting in Dense Indoor Scenarios Using mmWave Radar
**arXiv**：[2512.10357v1](https://arxiv.org/abs/2512.10357) · [PDF](https://arxiv.org/pdf/2512.10357.pdf)  
**作者**：Tarik Reza Toha, Shao-Jung, Lu, Shahriar Nirjon  

**一句话要点**：提出mmCounter以解决毫米波雷达在密集静态人群计数中的难题

**关键词**：毫米波雷达, 静态人群计数, 密集室内场景, 超低频信号处理, 呼吸检测, 微动分析

## 3 点简述
- 核心问题：毫米波雷达因空间分辨率限制和依赖运动检测，难以计数密集静态人群。
- 方法要点：提取超低频呼吸和微动信号，通过多阶段信号处理区分噪声并映射到个体。
- 实验或效果：在熟悉环境中平均F1分数87%，平均绝对误差0.6；可计数3平方米内最多7人。

## 摘要（原文）

> mmWave radars struggle to detect or count individuals in dense, static (non-moving) groups due to limitations in spatial resolution and reliance on movement for detection. We present mmCounter, which accurately counts static people in dense indoor spaces (up to three people per square meter). mmCounter achieves this by extracting ultra-low frequency (< 1 Hz) signals, primarily from breathing and micro-scale body movements such as slight torso shifts, and applying novel signal processing techniques to differentiate these subtle signals from background noise and nearby static objects. Our problem differs significantly from existing studies on breathing rate estimation, which assume the number of people is known a priori. In contrast, mmCounter utilizes a novel multi-stage signal processing pipeline to extract relevant low-frequency sources along with their spatial information and map these sources to individual people, enabling accurate counting. Extensive evaluations in various environments demonstrate that mmCounter delivers an 87% average F1 score and 0.6 mean absolute error in familiar environments, and a 60% average F1 score and 1.1 mean absolute error in previously untested environments. It can count up to seven individuals in a three square meter space, such that there is no side-by-side spacing and only a one-meter front-to-back distance.

