---
layout: default
title: RobIA: Robust Instance-aware Continual Test-time Adaptation for Deep Stereo
---

# RobIA: Robust Instance-aware Continual Test-time Adaptation for Deep Stereo
**arXiv**：[2511.10107v1](https://arxiv.org/abs/2511.10107) · [PDF](https://arxiv.org/pdf/2511.10107.pdf)  
**作者**：Jueun Ko, Hyewon Park, Hyesong Choi, Dongbo Min  

**一句话要点**：提出RobIA框架以解决立体深度估计中的持续域适应问题

**关键词**：立体深度估计, 持续测试时适应, 混合专家, 伪监督, 域偏移, 参数高效微调

## 3 点简述
- 立体深度估计面临动态域偏移和稀疏监督的挑战
- 结合AttEx-MoE和Robust AdaptBN Teacher实现输入特定适应
- 实验显示在动态目标域中性能优越且计算高效

## 摘要（原文）

> Stereo Depth Estimation in real-world environments poses significant challenges due to dynamic domain shifts, sparse or unreliable supervision, and the high cost of acquiring dense ground-truth labels. While recent Test-Time Adaptation (TTA) methods offer promising solutions, most rely on static target domain assumptions and input-invariant adaptation strategies, limiting their effectiveness under continual shifts. In this paper, we propose RobIA, a novel Robust, Instance-Aware framework for Continual Test-Time Adaptation (CTTA) in stereo depth estimation. RobIA integrates two key components: (1) Attend-and-Excite Mixture-of-Experts (AttEx-MoE), a parameter-efficient module that dynamically routes input to frozen experts via lightweight self-attention mechanism tailored to epipolar geometry, and (2) Robust AdaptBN Teacher, a PEFT-based teacher model that provides dense pseudo-supervision by complementing sparse handcrafted labels. This strategy enables input-specific flexibility, broad supervision coverage, improving generalization under domain shift. Extensive experiments demonstrate that RobIA achieves superior adaptation performance across dynamic target domains while maintaining computational efficiency.

