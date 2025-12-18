---
layout: default
title: Time-Varying Audio Effect Modeling by End-to-End Adversarial Training
---

# Time-Varying Audio Effect Modeling by End-to-End Adversarial Training
**arXiv**：[2512.15313v1](https://arxiv.org/abs/2512.15313) · [PDF](https://arxiv.org/pdf/2512.15313.pdf)  
**作者**：Yann Bourdin, Pierrick Legrand, Fanny Roche  

**一句话要点**：提出基于GAN的端到端对抗训练框架，以解决时变音频效果建模中无需调制信号提取的问题。

**关键词**：时变音频效果建模, 生成对抗网络, 端到端训练, 调制信号提取, 卷积-循环架构, 啁啾信号评估

## 3 点简述
- 核心问题：时变音频效果建模需调制信号对齐，传统黑盒方法难以处理时间变化系统。
- 方法要点：采用卷积-循环架构，通过两阶段训练（对抗训练与监督微调）学习调制行为分布。
- 实验或效果：以硬件移相器为例，验证方法能捕获时变动态，并开发基于啁啾信号的客观指标评估调制精度。

## 摘要（原文）

> Deep learning has become a standard approach for the modeling of audio effects, yet strictly black-box modeling remains problematic for time-varying systems. Unlike time-invariant effects, training models on devices with internal modulation typically requires the recording or extraction of control signals to ensure the time-alignment required by standard loss functions. This paper introduces a Generative Adversarial Network (GAN) framework to model such effects using only input-output audio recordings, removing the need for modulation signal extraction. We propose a convolutional-recurrent architecture trained via a two-stage strategy: an initial adversarial phase allows the model to learn the distribution of the modulation behavior without strict phase constraints, followed by a supervised fine-tuning phase where a State Prediction Network (SPN) estimates the initial internal states required to synchronize the model with the target. Additionally, a new objective metric based on chirp-train signals is developed to quantify modulation accuracy. Experiments modeling a vintage hardware phaser demonstrate the method's ability to capture time-varying dynamics in a fully black-box context.

