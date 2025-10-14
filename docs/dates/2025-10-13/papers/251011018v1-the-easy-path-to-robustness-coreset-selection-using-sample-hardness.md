---
layout: default
title: The Easy Path to Robustness: Coreset Selection using Sample Hardness
---

# The Easy Path to Robustness: Coreset Selection using Sample Hardness
**arXiv**：[2510.11018v1](https://arxiv.org/abs/2510.11018) · [PDF](https://arxiv.org/pdf/2510.11018.pdf)  
**作者**：Pranav Ramesh, Arjun Roy, Deepak Ravikumar, Kaushik Roy, Gopalakrishnan Srinivasan  

**一句话要点**：提出EasyCore核心集选择方法，通过样本硬度提升对抗鲁棒性

**关键词**：核心集选择, 对抗鲁棒性, 样本硬度, 数据为中心方法, 平均输入梯度范数

## 3 点简述
- 核心问题：现有核心集选择方法注重干净准确率，但无法保持对抗鲁棒性
- 方法要点：基于平均输入梯度范数量化样本硬度，选择低硬度样本构建核心集
- 实验效果：在标准与对抗训练下，对抗准确率比现有方法提升高达7%和5%

## 摘要（原文）

> Designing adversarially robust models from a data-centric perspective
> requires understanding which input samples are most crucial for learning
> resilient features. While coreset selection provides a mechanism for efficient
> training on data subsets, current algorithms are designed for clean accuracy
> and fall short in preserving robustness. To address this, we propose a
> framework linking a sample's adversarial vulnerability to its
> \textit{hardness}, which we quantify using the average input gradient norm
> (AIGN) over training. We demonstrate that \textit{easy} samples (with low AIGN)
> are less vulnerable and occupy regions further from the decision boundary.
> Leveraging this insight, we present EasyCore, a coreset selection algorithm
> that retains only the samples with low AIGN for training. We empirically show
> that models trained on EasyCore-selected data achieve significantly higher
> adversarial accuracy than those trained with competing coreset methods under
> both standard and adversarial training. As AIGN is a model-agnostic dataset
> property, EasyCore is an efficient and widely applicable data-centric method
> for improving adversarial robustness. We show that EasyCore achieves up to 7\%
> and 5\% improvement in adversarial accuracy under standard training and TRADES
> adversarial training, respectively, compared to existing coreset methods.

