---
layout: default
title: Beyond Amplitude: Channel State Information Phase-Aware Deep Fusion for Robotic Activity Recognition
---

# Beyond Amplitude: Channel State Information Phase-Aware Deep Fusion for Robotic Activity Recognition
**arXiv**：[2603.09047v1](https://arxiv.org/abs/2603.09047) · [PDF](https://arxiv.org/pdf/2603.09047.pdf)  
**作者**：Rojin Zandi, Hojjat Salehinejad, Milad Siami  

**一句话要点**：提出GF-BiLSTM网络，通过门控融合CSI幅度与相位，提升机器人活动识别的准确性和跨速度鲁棒性。

**关键词**：Wi-Fi信道状态信息, 机器人活动识别, 门控融合网络, 双向长短期记忆网络, 相位信息利用

## 3 点简述
- 核心问题：现有Wi-Fi CSI机器人活动识别方法主要依赖幅度，相位信息利用不足。
- 方法要点：设计两流门控融合网络，分别编码幅度和相位，自适应整合特征。
- 实验或效果：在LOVO协议下评估，结合相位显著提高识别精度，GF-BiLSTM表现最佳。

## 摘要（原文）

> Wi-Fi Channel State Information (CSI) has emerged as a promising non-line-of-sight sensing modality for human and robotic activity recognition. However, prior work has predominantly relied on CSI amplitude while underutilizing phase information, particularly in robotic arm activity recognition. In this paper, we present GateFusion-Bidirectional Long Short-Term Memory network (GF-BiLSTM) for WiFi sensing in robotic activity recognition. GF-BiLSTM is a two-stream gated fusion network that encodes amplitude and phase separately and adaptively integrates per-time features through a learned gating mechanism. We systematically evaluate state-of-the-art deep learning models under a Leave-One-Velocity-Out (LOVO) protocol across four input configurations: amplitude only, phase only, amplitude + unwrapped phase, and amplitude + sanitized phase. Experimental results demonstrate that incorporating phase alongside amplitude consistently improves recognition accuracy and cross-speed robustness, with GF-BiLSTM achieving the best performance. To the best of our knowledge, this work provides the first systematic exploration of CSI phase for robotic activity recognition, establishing its critical role in Wi-Fi-based sensing.

