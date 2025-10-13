---
layout: default
title: Efficient Bayesian Inference from Noisy Pairwise Comparisons
---

# Efficient Bayesian Inference from Noisy Pairwise Comparisons
**arXiv**：[2510.09333v1](https://arxiv.org/abs/2510.09333) · [PDF](https://arxiv.org/pdf/2510.09333.pdf)  
**作者**：Till Aczel, Lucas Theis, Wattenhofer Roger  
**一句话要点**：提出BBQ贝叶斯Bradley-Terry变体以解决生成模型评估中噪声成对比较的聚合问题
**关键词**：贝叶斯推断, 成对比较, Bradley-Terry模型, 评估者质量建模, 生成模型评估, EM算法

## 3 点简述
- 核心问题：标准指标难以反映人类偏好，人类评估成本高且噪声大，成对比较聚合需稳健建模
- 方法要点：BBQ显式建模评估者质量，通过EM算法保证单调似然收敛，降权不可靠参与者
- 实验或效果：BBQ收敛更快，提供校准不确定性估计，在噪声或众包评估中更稳健可解释

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

