---
layout: default
title: FUPareto: Bridging the Forgetting-Utility Gap in Federated Unlearning via Pareto Augmented Optimization
---

# FUPareto: Bridging the Forgetting-Utility Gap in Federated Unlearning via Pareto Augmented Optimization
**arXiv**：[2602.01852v1](https://arxiv.org/abs/2602.01852) · [PDF](https://arxiv.org/pdf/2602.01852.pdf)  
**作者**：Zeyan Wang, Zhengmao Liu, Yongxin Cai, Chi Li, Xiaoying Tang, Jingchao Chen, Zibin Pan, Jing Qiu  

**一句话要点**：提出FUPareto框架，通过帕累托增强优化解决联邦遗忘中遗忘与效用的冲突

**关键词**：联邦遗忘, 帕累托优化, 多客户端并发遗忘, 梯度冲突解耦, 最小边界偏移损失

## 3 点简述
- 核心问题：联邦遗忘存在遗忘与效用冲突，多客户端并发遗忘时梯度冲突降低遗忘质量
- 方法要点：引入最小边界偏移损失和帕累托改进步骤，结合零空间投影多梯度下降算法解耦梯度冲突
- 实验或效果：在多种场景下实验显示，FUPareto在遗忘效果和保留效用上优于现有方法

## 摘要（原文）

> Federated Unlearning (FU) aims to efficiently remove the influence of specific client data from a federated model while preserving utility for the remaining clients. However, three key challenges remain: (1) existing unlearning objectives often compromise model utility or increase vulnerability to Membership Inference Attacks (MIA); (2) there is a persistent conflict between forgetting and utility, where further unlearning inevitably harms retained performance; and (3) support for concurrent multi-client unlearning is poor, as gradient conflicts among clients degrade the quality of forgetting. To address these issues, we propose FUPareto, an efficient unlearning framework via Pareto-augmented optimization. We first introduce the Minimum Boundary Shift (MBS) Loss, which enforces unlearning by suppressing the target class logit below the highest non-target class logit; this can improve the unlearning efficiency and mitigate MIA risks. During the unlearning process, FUPareto performs Pareto improvement steps to preserve model utility and executes Pareto expansion to guarantee forgetting. Specifically, during Pareto expansion, the framework integrates a Null-Space Projected Multiple Gradient Descent Algorithm (MGDA) to decouple gradient conflicts. This enables effective, fair, and concurrent unlearning for multiple clients while minimizing utility degradation. Extensive experiments across diverse scenarios demonstrate that FUPareto consistently outperforms state-of-the-art FU methods in both unlearning efficacy and retained utility.

