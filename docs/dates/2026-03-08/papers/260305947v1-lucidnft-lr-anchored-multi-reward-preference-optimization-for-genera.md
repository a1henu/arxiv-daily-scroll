---
layout: default
title: LucidNFT: LR-Anchored Multi-Reward Preference Optimization for Generative Real-World Super-Resolution
---

# LucidNFT: LR-Anchored Multi-Reward Preference Optimization for Generative Real-World Super-Resolution
**arXiv**：[2603.05947v1](https://arxiv.org/abs/2603.05947) · [PDF](https://arxiv.org/pdf/2603.05947.pdf)  
**作者**：Song Fei, Tian Ye, Sixiang Chen, Zhaohu Xing, Jianyu Lai, Lei Zhu  

**一句话要点**：提出LucidNFT框架，通过LR锚定多奖励优化解决生成式真实世界超分辨率中的忠实性问题。

**关键词**：真实世界超分辨率, 多奖励强化学习, 流匹配, 忠实性评估, 优势归一化, 数据集构建

## 3 点简述
- 核心问题：生成式真实世界超分辨率易产生语义和结构幻觉，缺乏LR锚定的忠实性评估信号。
- 方法要点：引入LucidConsistency评估器、解耦优势归一化策略和LucidLR数据集，优化多奖励RL框架。
- 实验或效果：在真实场景中稳定提升感知-忠实性权衡，改进流匹配超分辨率基线。

## 摘要（原文）

> Generative real-world image super-resolution (Real-ISR) can synthesize visually convincing details from severely degraded low-resolution (LR) inputs, yet its stochastic sampling makes a critical failure mode hard to avoid: outputs may look sharp but be unfaithful to the LR evidence (semantic and structural hallucination), while such LR-anchored faithfulness is difficult to assess without HR ground truth. Preference-based reinforcement learning (RL) is a natural fit because each LR input yields a rollout group of candidates to compare. However, effective alignment in Real-ISR is hindered by (i) the lack of a degradation-robust LR-referenced faithfulness signal, and (ii) a rollout-group optimization bottleneck where naive multi-reward scalarization followed by normalization compresses objective-wise contrasts, causing advantage collapse and weakening the reward-weighted updates in DiffusionNFT-style forward fine-tuning. Moreover, (iii) limited coverage of real degradations restricts rollout diversity and preference signal quality. We propose LucidNFT, a multi-reward RL framework for flow-matching Real-ISR. LucidNFT introduces LucidConsistency, a degradation-robust semantic evaluator that makes LR-anchored faithfulness measurable and optimizable; a decoupled advantage normalization strategy that preserves objective-wise contrasts within each LR-conditioned rollout group before fusion, preventing advantage collapse; and LucidLR, a large-scale collection of real-world degraded images to support robust RL fine-tuning. Experiments show that LucidNFT consistently improves strong flow-based Real-ISR baselines, achieving better perceptual-faithfulness trade-offs with stable optimization dynamics across diverse real-world scenarios.

