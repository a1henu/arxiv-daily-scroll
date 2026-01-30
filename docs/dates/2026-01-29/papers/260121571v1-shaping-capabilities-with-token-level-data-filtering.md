---
layout: default
title: Shaping capabilities with token-level data filtering
---

# Shaping capabilities with token-level data filtering
**arXiv**：[2601.21571v1](https://arxiv.org/abs/2601.21571) · [PDF](https://arxiv.org/pdf/2601.21571.pdf)  
**作者**：Neil Rathi, Alec Radford  

**一句话要点**：提出基于令牌级数据过滤的方法，在预训练中有效移除语言模型的不良能力

**关键词**：令牌级数据过滤, 预训练能力塑造, 稀疏自编码器, 蒸馏分类器, 医疗能力移除, 计算效率

## 3 点简述
- 核心问题：现有方法多为事后处理，易被对抗攻击绕过，需在预训练阶段塑造模型能力
- 方法要点：通过令牌级数据过滤，结合稀疏自编码器标记令牌和蒸馏高质量分类器，比文档过滤更高效
- 实验或效果：在医疗能力移除任务中，令牌过滤实现7000倍计算减速，且对噪声标签鲁棒，可保持良性能力

## 摘要（原文）

> Current approaches to reducing undesired capabilities in language models are largely post hoc, and can thus be easily bypassed by adversaries. A natural alternative is to shape capabilities during pretraining itself. On the proxy task of removing medical capabilities, we show that the simple intervention of filtering pretraining data is highly effective, robust, and inexpensive at scale. Inspired by work on data attribution, we show that filtering tokens is more effective than filtering documents, achieving the same hit to undesired capabilities at a lower cost to benign ones. Training models spanning two orders of magnitude, we then demonstrate that filtering gets more effective with scale: for our largest models, token filtering leads to a 7000x compute slowdown on the forget domain. We also show that models trained with token filtering can still be aligned on the forget domain. Along the way, we introduce a methodology for labeling tokens with sparse autoencoders and distilling cheap, high-quality classifiers. We also demonstrate that filtering can be robust to noisy labels with sufficient pretraining compute.

