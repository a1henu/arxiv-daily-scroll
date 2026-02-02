---
layout: default
title: Machine Unlearning in Low-Dimensional Feature Subspace
---

# Machine Unlearning in Low-Dimensional Feature Subspace
**arXiv**：[2601.22456v1](https://arxiv.org/abs/2601.22456) · [PDF](https://arxiv.org/pdf/2601.22456.pdf)  
**作者**：Kun Fang, Qinghua Tao, Junxu Liu, Yaxin Xiao, Qingqing Ye, Jian Sun, Haibo Hu  

**一句话要点**：提出LOFT方法，在低维特征子空间进行机器遗忘以解决隐私泄露和效率低下问题。

**关键词**：机器遗忘, 低维特征子空间, 隐私保护, 高效更新, 投影优化

## 3 点简述
- 核心问题：机器遗忘需移除特定数据影响，但主流方法存在隐私泄露风险和模型更新低效。
- 方法要点：在预训练模型低维特征子空间优化投影矩阵，最大化保留剩余数据信息并减少遗忘数据信息。
- 实验或效果：实验验证LOFT计算开销显著降低，遗忘性能优越，适用于多种模型、数据集和任务。

## 摘要（原文）

> Machine Unlearning (MU) aims at removing the influence of specific data from a pretrained model while preserving performance on the remaining data. In this work, a novel perspective for MU is presented upon low-dimensional feature subspaces, which gives rise to the potentials of separating the remaining and forgetting data herein. This separability motivates our LOFT, a method that proceeds unlearning in a LOw-dimensional FeaTure subspace from the pretrained model skithrough principal projections, which are optimized to maximally capture the information of the remaining data and meanwhile diminish that of the forgetting data. In training, LOFT simply optimizes a small-size projection matrix flexibly plugged into the pretrained model, and only requires one-shot feature fetching from the pretrained backbone instead of repetitively accessing the raw data. Hence, LOFT mitigates two critical issues in mainstream MU methods, i.e., the privacy leakage risk from massive data reload and the inefficiency of updates to the entire pretrained model. Extensive experiments validate the significantly lower computational overhead and superior unlearning performance of LOFT across diverse models, datasets, tasks, and applications. Code is anonymously available at https://anonymous.4open.science/r/4352/.

