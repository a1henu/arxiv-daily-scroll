---
layout: default
title: SPARKLING: Balancing Signal Preservation and Symmetry Breaking for Width-Progressive Learning
---

# SPARKLING: Balancing Signal Preservation and Symmetry Breaking for Width-Progressive Learning
**arXiv**：[2602.02472v1](https://arxiv.org/abs/2602.02472) · [PDF](https://arxiv.org/pdf/2602.02472.pdf)  
**作者**：Qifan Yu, Xinyu Ma, Zhijian Zhuo, Minrui Wang, Deyi Liu, Shiyi Zhan, Yiyuan Ma, Liang Xiang, Xingyan Bin, Di He  

**一句话要点**：提出SPARKLING框架以解决宽度渐进学习中信号保持与对称性打破的平衡问题

**关键词**：宽度渐进学习, 信号保持, 对称性打破, 训练稳定性, 混合专家模型, 优化器重置

## 3 点简述
- 核心问题：宽度扩展在训练中期引发激活统计破坏和梯度对称，导致不稳定
- 方法要点：通过RMS尺度一致性保持信号，非对称优化器状态重置和学习率重预热打破对称
- 实验或效果：在MoE模型上优于从头训练，2倍宽度扩展下训练成本降低高达35%

## 摘要（原文）

> Progressive Learning (PL) reduces pre-training computational overhead by gradually increasing model scale. While prior work has extensively explored depth expansion, width expansion remains significantly understudied, with the few existing methods limited to the early stages of training. However, expanding width during the mid-stage is essential for maximizing computational savings, yet it remains a formidable challenge due to severe training instabilities. Empirically, we show that naive initialization at this stage disrupts activation statistics, triggering loss spikes, while copy-based initialization introduces gradient symmetry that hinders feature diversity. To address these issues, we propose SPARKLING (balancing {S}ignal {P}reservation {A}nd symmet{R}y brea{K}ing for width-progressive {L}earn{ING}), a novel framework for mid-stage width expansion. Our method achieves signal preservation via RMS-scale consistency, stabilizing activation statistics during expansion. Symmetry breaking is ensured through asymmetric optimizer state resetting and learning rate re-warmup. Extensive experiments on Mixture-of-Experts (MoE) models demonstrate that, across multiple width axes and optimizer families, SPARKLING consistently outperforms training from scratch and reduces training cost by up to 35% under $2\times$ width expansion.

