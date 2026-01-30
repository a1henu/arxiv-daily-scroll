---
layout: default
title: A Low-Complexity Plug-and-Play Deep Learning Model for Generalizable Massive MIMO Precoding
---

# A Low-Complexity Plug-and-Play Deep Learning Model for Generalizable Massive MIMO Precoding
**arXiv**：[2601.21897v1](https://arxiv.org/abs/2601.21897) · [PDF](https://arxiv.org/pdf/2601.21897.pdf)  
**作者**：Ali Hasanzadeh Karkan, Ahmed Ibrahim, Jean-François Frigon, François Leduc-Primeau  

**一句话要点**：提出可插拔深度学习模型PaPP，用于通用大规模MIMO预编码以降低计算能耗

**关键词**：大规模MIMO预编码, 深度学习模型, 教师-学生蒸馏, 元学习, 计算能耗优化, 可插拔框架

## 3 点简述
- 大规模MIMO预编码面临计算复杂、部署适应性差的问题
- PaPP结合教师-学生蒸馏与元学习，支持跨场景重用
- 在未见站点上微调后，性能优于基线并减少计算能耗

## 摘要（原文）

> Massive multiple-input multiple-output (mMIMO) downlink precoding offers high spectral efficiency but remains challenging to deploy in practice because near-optimal algorithms such as the weighted minimum mean squared error (WMMSE) are computationally expensive, and sensitive to SNR and channel-estimation quality, while existing deep learning (DL)-based solutions often lack robustness and require retraining for each deployment site. This paper proposes a plug-and-play precoder (PaPP), a DL framework with a backbone that can be trained for either fully digital (FDP) or hybrid beamforming (HBF) precoding and reused across sites, transmit-power levels, and with varying amounts of channel estimation error, avoiding the need to train a new model from scratch at each deployment. PaPP combines a high-capacity teacher and a compact student with a self-supervised loss that balances teacher imitation and normalized sum-rate, trained using meta-learning domain-generalization and transmit-power-aware input normalization. Numerical results on ray-tracing data from three unseen sites show that the PaPP FDP and HBF models both outperform conventional and deep learning baselines, after fine-tuning with a small set of local unlabeled samples. Across both architectures, PaPP achieves more than 21$\times$ reduction in modeled computation energy and maintains good performance under channel-estimation errors, making it a practical solution for energy-efficient mMIMO precoding.

