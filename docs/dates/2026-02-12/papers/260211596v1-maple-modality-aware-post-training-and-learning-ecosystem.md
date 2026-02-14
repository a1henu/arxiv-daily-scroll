---
layout: default
title: MAPLE: Modality-Aware Post-training and Learning Ecosystem
---

# MAPLE: Modality-Aware Post-training and Learning Ecosystem
**arXiv**：[2602.11596v1](https://arxiv.org/abs/2602.11596) · [PDF](https://arxiv.org/pdf/2602.11596.pdf)  
**作者**：Nikhil Verma, Minjung Kim, JooYoung Yoo, Kyung-Min Jin, Manasa Bharadwaj, Kevin Ferreira, Ko Keun Kim, Youngjoon Kim  

**一句话要点**：提出MAPLE模态感知后训练生态系统，以解决多模态RL中模态无关训练导致的梯度方差大和鲁棒性差问题。

**关键词**：多模态语言模型, 强化学习后训练, 模态感知优化, 梯度方差减少, 鲁棒性增强, 自适应课程学习

## 3 点简述
- 核心问题：现有RL后训练忽视任务所需模态，导致梯度方差大、收敛慢和鲁棒性差。
- 方法要点：引入MAPLE-bench基准、MAPO模态感知策略优化框架及自适应加权与课程调度。
- 实验或效果：缩小模态间准确率差距30.24%，收敛速度提升3.18倍，并在信号缺失下保持稳定。

## 摘要（原文）

> Multimodal language models now integrate text, audio, and video for unified reasoning. Yet existing RL post-training pipelines treat all input signals as equally relevant, ignoring which modalities each task actually requires. This modality-blind training inflates policy-gradient variance, slows convergence, and degrades robustness to real-world distribution shifts where signals may be missing, added, or reweighted. We introduce MAPLE, a complete modality-aware post-training and learning ecosystem comprising: (1) MAPLE-bench, the first benchmark explicitly annotating minimal signal combinations required per task; (2) MAPO, a modality-aware policy optimization framework that stratifies batches by modality requirement to reduce gradient variance from heterogeneous group advantages; (3) Adaptive weighting and curriculum scheduling that balances and prioritizes harder signal combinations. Systematic analysis across loss aggregation, clipping, sampling, and curriculum design establishes MAPO's optimal training strategy. Adaptive weighting and curriculum focused learning further boost performance across signal combinations. MAPLE narrows uni/multi-modal accuracy gaps by 30.24%, converges 3.18x faster, and maintains stability across all modality combinations under realistic reduced signal access. MAPLE constitutes a complete recipe for deployment-ready multimodal RL post-training.

