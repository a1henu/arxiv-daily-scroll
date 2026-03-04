---
layout: default
title: Less Noise, Same Certificate: Retain Sensitivity for Unlearning
---

# Less Noise, Same Certificate: Retain Sensitivity for Unlearning
**arXiv**：[2603.03172v1](https://arxiv.org/abs/2603.03172) · [PDF](https://arxiv.org/pdf/2603.03172.pdf)  
**作者**：Carolin Heinzler, Kasra Malihi, Amartya Sanyal  

**一句话要点**：提出保留敏感性以减少认证遗忘中的噪声，保持相同证书

**关键词**：认证遗忘, 差分隐私, 保留敏感性, 噪声减少, 机器学习安全, 模型效用

## 3 点简述
- 核心问题：现有认证遗忘方法基于差分隐私全局敏感性添加噪声，可能过于保守。
- 方法要点：定义保留敏感性，基于保留数据固定时的最坏输出变化，减少噪声。
- 实验或效果：理论验证和实证评估在最小生成树、PCA和ERM等问题中降低噪声并提升效用。

## 摘要（原文）

> Certified machine unlearning aims to provably remove the influence of a deletion set $U$ from a model trained on a dataset $S$, by producing an unlearned output that is statistically indistinguishable from retraining on the retain set $R:=S\setminus U$. Many existing certified unlearning methods adapt techniques from Differential Privacy (DP) and add noise calibrated to global sensitivity, i.e., the worst-case output change over all adjacent datasets. We show that this DP-style calibration is often overly conservative for unlearning, based on a key observation: certified unlearning, by definition, does not require protecting the privacy of the retained data $R$. Motivated by this distinction, we define retain sensitivity as the worst-case output change over deletions $U$ while keeping $R$ fixed. While insufficient for DP, retain sensitivity is exactly sufficient for unlearning, allowing for the same certificates with less noise. We validate these reductions in noise theoretically and empirically across several problems, including the weight of minimum spanning trees, PCA, and ERM. Finally, we refine the analysis of two widely used certified unlearning algorithms through the lens of retain sensitivity, leveraging the regularity induced by $R$ to further reduce noise and improve utility.

