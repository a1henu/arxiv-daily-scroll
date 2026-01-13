---
layout: default
title: WaveMan: mmWave-Based Room-Scale Human Interaction Perception for Humanoid Robots
---

# WaveMan: mmWave-Based Room-Scale Human Interaction Perception for Humanoid Robots
**arXiv**：[2601.07454v1](https://arxiv.org/abs/2601.07454) · [PDF](https://arxiv.org/pdf/2601.07454.pdf)  
**作者**：Yuxuan Hu, Kuangji Zuo, Boyu Ma, Shihao Li, Zhaoyang Xia, Feng Xu, Jianfei Yang  

**一句话要点**：提出WaveMan系统，通过空间自适应毫米波感知解决人形机器人在家庭环境中跨任意位置的人机交互问题。

**关键词**：毫米波感知, 人机交互, 空间自适应, 隐私保护, 人形机器人, 特征提取

## 3 点简述
- 核心问题：现有毫米波交互感知系统在未见距离或视角下空间泛化能力差，影响人形机器人家庭交互的可靠性。
- 方法要点：集成视角对齐和频谱图增强以保持空间一致性，并采用双通道注意力机制进行鲁棒特征提取。
- 实验或效果：在随机自由位置测试中，准确率从33.00%提升至94.33%，且固定位置评估下用更少训练位置达到基线相同精度。

## 摘要（原文）

> Reliable humanoid-robot interaction (HRI) in household environments is constrained by two fundamental requirements, namely robustness to unconstrained user positions and preservation of user privacy. Millimeter-wave (mmWave) sensing inherently supports privacy-preserving interaction, making it a promising modality for room-scale HRI. However, existing mmWave-based interaction-sensing systems exhibit poor spatial generalization at unseen distances or viewpoints. To address this challenge, we introduce WaveMan, a spatially adaptive room-scale perception system that restores reliable human interaction sensing across arbitrary user positions. WaveMan integrates viewpoint alignment and spectrogram enhancement for spatial consistency, with dual-channel attention for robust feature extraction. Experiments across five participants show that, under fixed-position evaluation, WaveMan achieves the same cross-position accuracy as the baseline with five times fewer training positions. In random free-position testing, accuracy increases from 33.00% to 94.33%, enabled by the proposed method. These results demonstrate the feasibility of reliable, privacy-preserving interaction for household humanoid robots across unconstrained user positions.

