---
layout: default
title: Classification Under Local Differential Privacy with Model Reversal and Model Averaging
---

# Classification Under Local Differential Privacy with Model Reversal and Model Averaging
**arXiv**：[2602.05797v1](https://arxiv.org/abs/2602.05797) · [PDF](https://arxiv.org/pdf/2602.05797.pdf)  
**作者**：Caihong Qin, Yang Bai  

**一句话要点**：提出模型反转与模型平均方法，以提升本地差分隐私下的分类性能

**关键词**：本地差分隐私, 分类学习, 模型反转, 模型平均, 数据效用评估, 隐私保护机器学习

## 3 点简述
- 核心问题：本地差分隐私引入噪声导致数据效用显著下降，影响分类准确性。
- 方法要点：通过噪声二进制反馈评估数据效用，利用模型反转修复分类器，并基于效用加权平均多个反转模型。
- 实验或效果：理论分析提供超额风险界，实证在模拟和真实数据集上显示分类准确率大幅提升。

## 摘要（原文）

> Local differential privacy (LDP) has become a central topic in data privacy research, offering strong privacy guarantees by perturbing user data at the source and removing the need for a trusted curator. However, the noise introduced by LDP often significantly reduces data utility. To address this issue, we reinterpret private learning under LDP as a transfer learning problem, where the noisy data serve as the source domain and the unobserved clean data as the target. We propose novel techniques specifically designed for LDP to improve classification performance without compromising privacy: (1) a noised binary feedback-based evaluation mechanism for estimating dataset utility; (2) model reversal, which salvages underperforming classifiers by inverting their decision boundaries; and (3) model averaging, which assigns weights to multiple reversed classifiers based on their estimated utility. We provide theoretical excess risk bounds under LDP and demonstrate how our methods reduce this risk. Empirical results on both simulated and real-world datasets show substantial improvements in classification accuracy.

