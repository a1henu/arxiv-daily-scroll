---
layout: default
title: Classification Under Local Differential Privacy with Model Reversal and Model Averaging
---

# Classification Under Local Differential Privacy with Model Reversal and Model Averaging
**arXiv**：[2602.05797v1](https://arxiv.org/abs/2602.05797) · [PDF](https://arxiv.org/pdf/2602.05797.pdf)  
**作者**：Caihong Qin, Yang Bai  

**一句话要点**：提出模型反转与模型平均方法，以提升本地差分隐私下的分类性能

**关键词**：本地差分隐私, 分类任务, 模型反转, 模型平均, 迁移学习, 隐私保护

## 3 点简述
- 本地差分隐私引入噪声降低数据效用，视为源域到目标域的迁移学习问题
- 引入噪声二进制反馈评估、模型反转和基于效用的模型平均技术
- 理论分析风险界限，实验在模拟和真实数据集上展示分类准确率显著提升

## 摘要（原文）

> Local differential privacy (LDP) has become a central topic in data privacy research, offering strong privacy guarantees by perturbing user data at the source and removing the need for a trusted curator. However, the noise introduced by LDP often significantly reduces data utility. To address this issue, we reinterpret private learning under LDP as a transfer learning problem, where the noisy data serve as the source domain and the unobserved clean data as the target. We propose novel techniques specifically designed for LDP to improve classification performance without compromising privacy: (1) a noised binary feedback-based evaluation mechanism for estimating dataset utility; (2) model reversal, which salvages underperforming classifiers by inverting their decision boundaries; and (3) model averaging, which assigns weights to multiple reversed classifiers based on their estimated utility. We provide theoretical excess risk bounds under LDP and demonstrate how our methods reduce this risk. Empirical results on both simulated and real-world datasets show substantial improvements in classification accuracy.

