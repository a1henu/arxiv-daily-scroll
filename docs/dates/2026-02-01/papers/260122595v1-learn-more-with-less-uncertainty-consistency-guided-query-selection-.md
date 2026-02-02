---
layout: default
title: Learn More with Less: Uncertainty Consistency Guided Query Selection for RLVR
---

# Learn More with Less: Uncertainty Consistency Guided Query Selection for RLVR
**arXiv**：[2601.22595v1](https://arxiv.org/abs/2601.22595) · [PDF](https://arxiv.org/pdf/2601.22595.pdf)  
**作者**：Hao Yi, Yulan Hu, Xin Li, Sheng Ouyang, Lizhong Ding, Yong Liu  

**一句话要点**：提出不确定性一致性指标以在RLVR中通过主动学习减少查询成本

**关键词**：强化学习可验证奖励, 主动学习, 不确定性估计, 数学推理, 查询选择, 成本优化

## 3 点简述
- 核心问题：RLVR算法需大量查询，标注成本高，现有主动学习策略因忽略客观不确定性而效果不佳
- 方法要点：引入不确定性一致性度量，离线用点双列相关系数，在线用归一化优势与主观不确定性计算新变体
- 实验或效果：方法优于随机和经典基线，仅用30%数据达到全数据集性能，有效降低推理任务成本

## 摘要（原文）

> Large Language Models (LLMs) have recently improved mathematical reasoning through Reinforcement Learning with Verifiable Reward (RLVR). However, existing RLVR algorithms require large query budgets, making annotation costly. We investigate whether fewer but more informative queries can yield similar or superior performance, introducing active learning (AL) into RLVR. We identify that classic AL sampling strategies fail to outperform random selection in this setting, due to ignoring objective uncertainty when only selecting by subjective uncertainty. This work proposes an uncertainty consistency metric to evaluate how well subjective uncertainty aligns with objective uncertainty. In the offline setting, this alignment is measured using the Point-Biserial Correlation Coefficient (PBC). For online training, because of limited sampling and dynamically shifting output distributions, PBC estimation is difficult. Therefore, we introduce a new online variant, computed from normalized advantage and subjective uncertainty. Theoretically, we prove that the online variant is strictly negatively correlated with offline PBC and supports better sample selection. Experiments show our method consistently outperforms random and classic AL baselines, achieving full-dataset performance while training on only 30% of the data, effectively reducing the cost of RLVR for reasoning tasks.

