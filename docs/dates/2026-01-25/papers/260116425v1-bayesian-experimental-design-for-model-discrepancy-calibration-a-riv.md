---
layout: default
title: Bayesian Experimental Design for Model Discrepancy Calibration: A Rivalry between Kullback--Leibler Divergence and Wasserstein Distance
---

# Bayesian Experimental Design for Model Discrepancy Calibration: A Rivalry between Kullback--Leibler Divergence and Wasserstein Distance
**arXiv**：[2601.16425v1](https://arxiv.org/abs/2601.16425) · [PDF](https://arxiv.org/pdf/2601.16425.pdf)  
**作者**：Huchen Yang, Xinghao Dong, Jin-Long Wu  

**一句话要点**：比较KL散度与Wasserstein距离在贝叶斯实验设计中的效用，为模型差异校准提供选择指南

**关键词**：贝叶斯实验设计, KL散度, Wasserstein距离, 模型差异校准, 效用函数选择, 源反演问题

## 3 点简述
- 核心问题：贝叶斯实验设计中效用函数选择长期存在争议，KL散度与Wasserstein距离各有侧重
- 方法要点：通过玩具示例揭示Wasserstein距离可能产生与信息增益无关的虚假奖励，并在源反演问题中系统比较两者
- 实验或效果：KL散度在无模型差异时收敛更快，Wasserstein距离在模型差异显著时提供更稳健的序列设计结果

## 摘要（原文）

> Designing experiments that systematically gather data from complex physical systems is central to accelerating scientific discovery. While Bayesian experimental design (BED) provides a principled, information-based framework that integrates experimental planning with probabilistic inference, the selection of utility functions in BED is a long-standing and active topic, where different criteria emphasize different notions of information. Although Kullback--Leibler (KL) divergence has been one of the most common choices, recent studies have proposed Wasserstein distance as an alternative. In this work, we first employ a toy example to illustrate an issue of Wasserstein distance - the value of Wasserstein distance of a fixed-shape posterior depends on the relative position of its main mass within the support and can exhibit false rewards unrelated to information gain, especially with a non-informative prior (e.g., uniform distribution). We then further provide a systematic comparison between these two criteria through a classical source inversion problem in the BED literature, revealing that the KL divergence tends to lead to faster convergence in the absence of model discrepancy, while Wasserstein metrics provide more robust sequential BED results if model discrepancy is non-negligible. These findings clarify the trade-offs between KL divergence and Wasserstein metrics for the utility function and provide guidelines for selecting suitable criteria in practical BED applications.

