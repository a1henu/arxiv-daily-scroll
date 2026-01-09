---
layout: default
title: RL-AWB: Deep Reinforcement Learning for Auto White Balance Correction in Low-Light Night-time Scenes
---

# RL-AWB: Deep Reinforcement Learning for Auto White Balance Correction in Low-Light Night-time Scenes
**arXiv**：[2601.05249v1](https://arxiv.org/abs/2601.05249) · [PDF](https://arxiv.org/pdf/2601.05249.pdf)  
**作者**：Yuan-Kang Lee, Kuan-Lin Chen, Chia-Che Chang, Yu-Lun Liu  

**一句话要点**：提出RL-AWB框架，结合统计方法与深度强化学习解决低光夜间场景的白平衡校正问题。

**关键词**：白平衡校正, 深度强化学习, 夜间场景, 色彩恒常性, 多传感器数据集

## 3 点简述
- 核心问题：夜间场景因低光噪声和复杂光照导致色彩恒常性挑战。
- 方法要点：基于统计算法检测显著灰度像素和估计光照，并首次引入深度强化学习动态优化参数。
- 实验或效果：引入多传感器夜间数据集，实验显示在低光和良好光照图像上具有优越泛化能力。

## 摘要（原文）

> Nighttime color constancy remains a challenging problem in computational photography due to low-light noise and complex illumination conditions. We present RL-AWB, a novel framework combining statistical methods with deep reinforcement learning for nighttime white balance. Our method begins with a statistical algorithm tailored for nighttime scenes, integrating salient gray pixel detection with novel illumination estimation. Building on this foundation, we develop the first deep reinforcement learning approach for color constancy that leverages the statistical algorithm as its core, mimicking professional AWB tuning experts by dynamically optimizing parameters for each image. To facilitate cross-sensor evaluation, we introduce the first multi-sensor nighttime dataset. Experiment results demonstrate that our method achieves superior generalization capability across low-light and well-illuminated images. Project page: https://ntuneillee.github.io/research/rl-awb/

