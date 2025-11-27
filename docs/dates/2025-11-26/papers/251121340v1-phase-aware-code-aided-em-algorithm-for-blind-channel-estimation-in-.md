---
layout: default
title: Phase-Aware Code-Aided EM Algorithm for Blind Channel Estimation in PSK-Modulated OFDM
---

# Phase-Aware Code-Aided EM Algorithm for Blind Channel Estimation in PSK-Modulated OFDM
**arXiv**：[2511.21340v1](https://arxiv.org/abs/2511.21340) · [PDF](https://arxiv.org/pdf/2511.21340.pdf)  
**作者**：Chin-Hung Chen, Ivana Nikoloska, Wim van Houtum, Yan Wu, Alex Alvarado  

**一句话要点**：提出相位感知代码辅助EM算法，解决PSK-OFDM盲信道估计中的相位模糊问题

**关键词**：盲信道估计, EM算法, PSK调制, OFDM系统, 相位模糊, 代码辅助

## 3 点简述
- 核心问题：盲EM算法因相位模糊易陷入局部最优，导致信道估计失败
- 方法要点：利用解码器外信息生成候选模型，基于PSK对称性选择最可能模型
- 实验或效果：结合卷积码，将局部收敛率从80%降至近0%，复杂度可忽略

## 摘要（原文）

> This paper presents a fully blind phase-aware expectation-maximization (EM) algorithm for OFDM systems with the phase-shift keying (PSK) modulation. We address the well-known local maximum problem of the EM algorithm for blind channel estimation. This is primarily caused by the unknown phase ambiguity in the channel estimates, which conventional blind EM estimators cannot resolve. To overcome this limitation, we propose to exploit the extrinsic information from the decoder as model evidence metrics. A finite set of candidate models is generated based on the inherent symmetries of PSK modulation, and the decoder selects the most likely candidate model. Simulation results demonstrate that, when combined with a simple convolutional code, the phase-aware EM algorithm reliably resolves phase ambiguity during the initialization stage and reduces the local convergence rate from 80% to nearly 0% in frequency-selective channels with a constant phase ambiguity. The algorithm is invoked only once after the EM initialization stage, resulting in negligible additional complexity during subsequent turbo iterations.

