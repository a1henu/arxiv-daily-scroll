---
layout: default
title: Efficient Bayesian Inference from Noisy Pairwise Comparisons
---

# Efficient Bayesian Inference from Noisy Pairwise Comparisons
**arXiv**：[2510.09333v1](https://arxiv.org/abs/2510.09333) · [PDF](https://arxiv.org/pdf/2510.09333.pdf)  
**作者**：Till Aczel, Lucas Theis, Wattenhofer Roger  

**一句话要点**：提出BBQ贝叶斯Bradley-Terry模型以解决生成模型评估中噪声成对比较的聚合问题

**关键词**：贝叶斯推断, 成对比较, Bradley-Terry模型, 生成模型评估, EM算法, 评分者质量建模

## 3 点简述
- 核心问题：生成模型评估中人类评价成本高、噪声大，标准指标难以反映偏好
- 方法要点：BBQ模型显式建模评分者质量，使用EM算法保证单调似然收敛
- 实验或效果：BBQ收敛更快，提供校准不确定性估计和鲁棒排名，优于基线模型

## 摘要（原文）

> Evaluating generative models is challenging because standard metrics often
> fail to reflect human preferences. Human evaluations are more reliable but
> costly and noisy, as participants vary in expertise, attention, and diligence.
> Pairwise comparisons improve consistency, yet aggregating them into overall
> quality scores requires careful modeling. Bradley-Terry-based methods update
> item scores from comparisons, but existing approaches either ignore rater
> variability or lack convergence guarantees, limiting robustness and
> interpretability. We introduce BBQ, a Bayesian Bradley-Terry variant that
> explicitly models rater quality, downweighting or removing unreliable
> participants, and provides guaranteed monotonic likelihood convergence through
> an Expectation-Maximization algorithm. Empirical results show that BBQ achieves
> faster convergence, well-calibrated uncertainty estimates, and more robust,
> interpretable rankings compared to baseline Bradley-Terry models, even with
> noisy or crowdsourced raters. This framework enables more reliable and
> cost-effective human evaluation of generative models.

