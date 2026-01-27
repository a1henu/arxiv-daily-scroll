---
layout: default
title: FaLW: A Forgetting-aware Loss Reweighting for Long-tailed Unlearning
---

# FaLW: A Forgetting-aware Loss Reweighting for Long-tailed Unlearning
**arXiv**：[2601.18650v1](https://arxiv.org/abs/2601.18650) · [PDF](https://arxiv.org/pdf/2601.18650.pdf)  
**作者**：Liheng Yu, Zhe Zhao, Yuxuan Wang, Pengkun Wang, Binwu Wang, Yang Wang  

**一句话要点**：提出FaLW以解决长尾分布下机器遗忘的偏差问题

**关键词**：机器遗忘, 长尾分布, 损失重加权, 数据隐私, 动态调整

## 3 点简述
- 核心问题：现有遗忘方法在长尾分布遗忘集上存在异质性和偏斜性偏差
- 方法要点：基于样本预测概率与同类未见数据分布比较，动态重加权损失
- 实验或效果：实验显示FaLW在长尾场景下性能优越，代码已开源

## 摘要（原文）

> Machine unlearning, which aims to efficiently remove the influence of specific data from trained models, is crucial for upholding data privacy regulations like the ``right to be forgotten". However, existing research predominantly evaluates unlearning methods on relatively balanced forget sets. This overlooks a common real-world scenario where data to be forgotten, such as a user's activity records, follows a long-tailed distribution. Our work is the first to investigate this critical research gap. We find that in such long-tailed settings, existing methods suffer from two key issues: \textit{Heterogeneous Unlearning Deviation} and \textit{Skewed Unlearning Deviation}. To address these challenges, we propose FaLW, a plug-and-play, instance-wise dynamic loss reweighting method. FaLW innovatively assesses the unlearning state of each sample by comparing its predictive probability to the distribution of unseen data from the same class. Based on this, it uses a forgetting-aware reweighting scheme, modulated by a balancing factor, to adaptively adjust the unlearning intensity for each sample. Extensive experiments demonstrate that FaLW achieves superior performance. Code is available at \textbf{Supplementary Material}.

