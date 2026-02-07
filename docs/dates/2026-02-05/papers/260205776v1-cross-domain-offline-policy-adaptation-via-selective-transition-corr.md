---
layout: default
title: Cross-Domain Offline Policy Adaptation via Selective Transition Correction
---

# Cross-Domain Offline Policy Adaptation via Selective Transition Correction
**arXiv**：[2602.05776v1](https://arxiv.org/abs/2602.05776) · [PDF](https://arxiv.org/pdf/2602.05776.pdf)  
**作者**：Mengbei Yan, Jiafei Lyu, Shengjie Sun, Zhongjian Qiao, Jingwen Yang, Zichuan Lin, Deheng Ye, Xiu Li  

**一句话要点**：提出选择性转移校正算法以解决跨域离线强化学习中的动态不匹配问题

**关键词**：跨域强化学习, 离线策略适应, 动态校正, 选择性转移, 逆策略模型, 前向动态模型

## 3 点简述
- 核心问题：跨域离线强化学习中，源域和目标域动态不匹配导致直接合并数据集性能不佳
- 方法要点：利用逆策略模型和奖励模型校正源域转移，并通过前向动态模型选择性保留校正样本
- 实验或效果：在多种动态偏移环境中，STC算法优于现有基线，实现更优性能

## 摘要（原文）

> It remains a critical challenge to adapt policies across domains with mismatched dynamics in reinforcement learning (RL). In this paper, we study cross-domain offline RL, where an offline dataset from another similar source domain can be accessed to enhance policy learning upon a target domain dataset. Directly merging the two datasets may lead to suboptimal performance due to potential dynamics mismatches. Existing approaches typically mitigate this issue through source domain transition filtering or reward modification, which, however, may lead to insufficient exploitation of the valuable source domain data. Instead, we propose to modify the source domain data into the target domain data. To that end, we leverage an inverse policy model and a reward model to correct the actions and rewards of source transitions, explicitly achieving alignment with the target dynamics. Since limited data may result in inaccurate model training, we further employ a forward dynamics model to retain corrected samples that better match the target dynamics than the original transitions. Consequently, we propose the Selective Transition Correction (STC) algorithm, which enables reliable usage of source domain data for policy adaptation. Experiments on various environments with dynamics shifts demonstrate that STC achieves superior performance against existing baselines.

