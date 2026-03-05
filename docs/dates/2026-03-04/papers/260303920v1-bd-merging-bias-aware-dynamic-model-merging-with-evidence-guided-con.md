---
layout: default
title: BD-Merging: Bias-Aware Dynamic Model Merging with Evidence-Guided Contrastive Learning
---

# BD-Merging: Bias-Aware Dynamic Model Merging with Evidence-Guided Contrastive Learning
**arXiv**：[2603.03920v1](https://arxiv.org/abs/2603.03920) · [PDF](https://arxiv.org/pdf/2603.03920.pdf)  
**作者**：Yuhan Xie, Chen Lyu  

**一句话要点**：提出BD-Merging框架，通过证据引导的对比学习解决模型合并中的分布偏移偏差问题

**关键词**：模型合并, 分布偏移, 不确定性建模, 对比学习, 多任务学习, 自适应路由

## 3 点简述
- 核心问题：模型合并方法在测试时分布偏移下可靠性不足，导致预测偏差和泛化性能下降
- 方法要点：引入联合证据头学习不确定性，基于邻接差异分数进行对比学习，训练去偏路由器自适应分配权重
- 实验或效果：在多样化任务上验证，BD-Merging相比现有方法展现出更优的有效性和鲁棒性

## 摘要（原文）

> Model Merging (MM) has emerged as a scalable paradigm for multi-task learning (MTL), enabling multiple task-specific models to be integrated without revisiting the original training data. Despite recent progress, the reliability of MM under test-time distribution shift remains insufficiently understood. Most existing MM methods typically assume that test data are clean and distributionally aligned with both the training and auxiliary sources. However, this assumption rarely holds in practice, often resulting in biased predictions with degraded generalization. To address this issue, we present BD-Merging, a bias-aware unsupervised model merging framework that explicitly models uncertainty to achieve adaptive reliability under distribution shift. First, BD-Merging introduces a joint evidential head that learns uncertainty over a unified label space, capturing cross-task semantic dependencies in MM. Second, building upon this evidential foundation, we propose an Adjacency Discrepancy Score (ADS) that quantifies evidential alignment among neighboring samples. Third, guided by ADS, a discrepancy-aware contrastive learning mechanism refines the merged representation by aligning consistent samples and separating conflicting ones. Combined with general unsupervised learning, this process trains a debiased router that adaptively allocates task-specific or layer-specific weights on a per-sample basis, effectively mitigating the adverse effects of distribution shift. Extensive experiments across diverse tasks demonstrate that BD-Merging achieves superior effectiveness and robustness compared to state-of-the-art MM baselines.

