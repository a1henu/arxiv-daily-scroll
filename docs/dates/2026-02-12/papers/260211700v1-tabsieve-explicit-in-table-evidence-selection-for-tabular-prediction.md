---
layout: default
title: TabSieve: Explicit In-Table Evidence Selection for Tabular Prediction
---

# TabSieve: Explicit In-Table Evidence Selection for Tabular Prediction
**arXiv**：[2602.11700v1](https://arxiv.org/abs/2602.11700) · [PDF](https://arxiv.org/pdf/2602.11700.pdf)  
**作者**：Yongyao Wang, Ziqi Miao, Lu Yang, Haonan Jia, Wenting Yan, Chen Qian, Lijun Li  

**一句话要点**：提出TabSieve框架，通过显式证据选择提升表格预测性能。

**关键词**：表格预测, 证据选择, 强化学习, 少样本学习, 合成数据

## 3 点简述
- 问题：表格预测中现有模型常忽略相关行或受噪声影响，导致性能不稳定。
- 方法：采用先选择后预测框架，结合合成数据和强化学习优化证据选择与预测。
- 效果：在分类和回归任务上平均提升2.92%和4.45%，增强对噪声的鲁棒性。

## 摘要（原文）

> Tabular prediction can benefit from in-table rows as few-shot evidence, yet existing tabular models typically perform instance-wise inference and LLM-based prompting is often brittle. Models do not consistently leverage relevant rows, and noisy context can degrade performance. To address this challenge, we propose TabSieve, a select-then-predict framework that makes evidence usage explicit and auditable. Given a table and a query row, TabSieve first selects a small set of informative rows as evidence and then predicts the missing target conditioned on the selected evidence. To enable this capability, we construct TabSieve-SFT-40K by synthesizing high-quality reasoning trajectories from 331 real tables using a strong teacher model with strict filtering. Furthermore, we introduce TAB-GRPO, a reinforcement learning recipe that jointly optimizes evidence selection and prediction correctness with separate rewards, and stabilizes mixed regression and classification training via dynamic task-advantage balancing. Experiments on a held-out benchmark of 75 classification and 52 regression tables show that TabSieve consistently improves performance across shot budgets, with average gains of 2.92% on classification and 4.45% on regression over the second-best baseline. Further analysis indicates that TabSieve concentrates more attention on the selected evidence, which improves robustness to noisy context.

