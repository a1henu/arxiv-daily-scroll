---
layout: default
title: Rethinking the Efficiency and Effectiveness of Reinforcement Learning for Radiology Report Generation
---

# Rethinking the Efficiency and Effectiveness of Reinforcement Learning for Radiology Report Generation
**arXiv**：[2603.04022v1](https://arxiv.org/abs/2603.04022) · [PDF](https://arxiv.org/pdf/2603.04022.pdf)  
**作者**：Zilin Lu, Ruifeng Yuan, Weiwei Cao, Wanxing Chang, Zhongyu Wei, Sinuo Wang, Yong Xia, Ling Zhang, Jianpeng Zhang  

**一句话要点**：提出诊断多样性采样与诊断令牌加权策略优化，提升放射学报告生成的强化学习效率与临床准确性。

**关键词**：放射学报告生成, 强化学习, 数据效率, 临床准确性, 诊断令牌加权, 医疗AI

## 3 点简述
- 核心问题：强化学习在放射学报告生成中数据效率低、临床关键令牌易被忽略。
- 方法要点：引入诊断多样性采样策略减少样本需求，设计诊断令牌加权策略优化以优先临床内容。
- 实验或效果：在多个数据集上实现SOTA性能，仅用20%样本在MIMIC-CXR达到F1分数0.516。

## 摘要（原文）

> Radiologists highly desire fully automated AI for radiology report generation (R2G), yet existing approaches fall short in clinical utility. Reinforcement learning (RL) holds potential to address these shortcomings, but its adoption in this task remains underexplored. In this paper, we revisit RL in terms of data efficiency and optimization effectiveness for R2G tasks. First, we explore the impact of data quantity and quality on the performance of RL in medical contexts, revealing that data quality plays a more critical role than quantity. To this end, we propose a diagnostic diversity-based data sampling strategy that enables comparable performance with fewer samples. Second, we observe that the majority of tokens in radiology reports are template-like and diagnostically uninformative, whereas the low frequency of clinically critical tokens heightens the risk of being overlooked during optimization. To tackle this, we introduce Diagnostic Token-weighted Policy Optimization (DiTPO), which directly optimizes for clinical accuracy by using a diagnostic F1 score as the reward signal. Unlike standard RL approaches that treat all tokens equally, DiTPO explicitly models the varying importance of different tokens through rule- or gradient-based mechanisms to prioritize clinically relevant content. Extensive experiments on the MIMIC-CXR, IU-Xray, and CheXpert Plus datasets demonstrate that our framework achieves state-of-the-art (SOTA) performance while requiring substantially fewer training samples in RL. Notably, on MIMIC-CXR, our framework attains an F1 score of 0.516 using only 20% of the RL training samples.

