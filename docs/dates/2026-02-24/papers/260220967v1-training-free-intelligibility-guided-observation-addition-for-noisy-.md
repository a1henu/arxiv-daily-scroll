---
layout: default
title: Training-Free Intelligibility-Guided Observation Addition for Noisy ASR
---

# Training-Free Intelligibility-Guided Observation Addition for Noisy ASR
**arXiv**：[2602.20967v1](https://arxiv.org/abs/2602.20967) · [PDF](https://arxiv.org/pdf/2602.20967.pdf)  
**作者**：Haoyang Li, Changsong Liu, Wei Rao, Hao Shi, Sakriani Sakti, Eng Siong Chng  

**一句话要点**：提出免训练可懂度引导的观测融合方法，以提升噪声环境下自动语音识别的鲁棒性。

**关键词**：自动语音识别, 语音增强, 观测融合, 可懂度估计, 免训练方法, 噪声鲁棒性

## 3 点简述
- 核心问题：噪声环境中自动语音识别性能下降，传统语音增强前端引入伪影损害识别。
- 方法要点：基于后端ASR直接估计可懂度，引导融合噪声与增强语音，无需训练神经网络预测器。
- 实验或效果：在多种SE-ASR组合和数据集上验证，优于现有观测融合基线，增强泛化能力。

## 摘要（原文）

> Automatic speech recognition (ASR) degrades severely in noisy environments. Although speech enhancement (SE) front-ends effectively suppress background noise, they often introduce artifacts that harm recognition. Observation addition (OA) addressed this issue by fusing noisy and SE enhanced speech, improving recognition without modifying the parameters of the SE or ASR models. This paper proposes an intelligibility-guided OA method, where fusion weights are derived from intelligibility estimates obtained directly from the backend ASR. Unlike prior OA methods based on trained neural predictors, the proposed method is training-free, reducing complexity and enhances generalization. Extensive experiments across diverse SE-ASR combinations and datasets demonstrate strong robustness and improvements over existing OA baselines. Additional analyses of intelligibility-guided switching-based alternatives and frame versus utterance-level OA further validate the proposed design.

