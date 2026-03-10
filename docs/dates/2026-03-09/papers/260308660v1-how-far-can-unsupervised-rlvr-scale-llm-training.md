---
layout: default
title: How Far Can Unsupervised RLVR Scale LLM Training?
---

# How Far Can Unsupervised RLVR Scale LLM Training?
**arXiv**：[2603.08660v1](https://arxiv.org/abs/2603.08660) · [PDF](https://arxiv.org/pdf/2603.08660.pdf)  
**作者**：Bingxiang He, Yuxin Zuo, Zeyuan Liu, Shangziqi Zhao, Zixuan Fu, Junlin Yang, Cheng Qian, Kaiyan Zhang, Yuchen Fan, Ganqu Cui, Xiusi Chen, Youbang Sun, Xingtai Lv, Xuekai Zhu, Li Sheng, Ran Li, Huan-ang Gao, Yuchen Zhang, Bowen Zhou, Zhiyuan Liu, Ning Ding  

**一句话要点**：分析无监督强化学习验证奖励在LLM训练中的扩展极限，提出模型崩溃步作为可训练性指标。

**关键词**：无监督强化学习, 大语言模型训练, 奖励验证, 模型崩溃, 计算不对称性

## 3 点简述
- 核心问题：无监督RLVR的扩展潜力与局限，特别是内在奖励方法的收敛机制。
- 方法要点：分类内在与外部奖励，建立理论框架揭示内在方法收敛于模型初始分布锐化。
- 实验或效果：内在奖励呈现先升后降模式，崩溃时机由模型先验决定，外部奖励可能突破限制。

## 摘要（原文）

> Unsupervised reinforcement learning with verifiable rewards (URLVR) offers a pathway to scale LLM training beyond the supervision bottleneck by deriving rewards without ground truth labels. Recent works leverage model intrinsic signals, showing promising early gains, yet their potential and limitations remain unclear. In this work, we revisit URLVR and provide a comprehensive analysis spanning taxonomy, theory and extensive experiments. We first classify URLVR methods into intrinsic versus external based on reward sources, then establish a unified theoretical framework revealing that all intrinsic methods converge toward sharpening the model's initial distribution This sharpening mechanism succeeds when initial confidence aligns with correctness but fails catastrophically when misaligned. Through systematic experiments, we show intrinsic rewards consistently follow a rise-then-fall pattern across methods, with collapse timing determined by model prior rather than engineering choices. Despite these scaling limits, we find intrinsic rewards remain valuable in test-time training on small datasets, and propose Model Collapse Step to measure model prior, serving as a practical indicator for RL trainability. Finally, we explore external reward methods that ground verification in computational asymmetries, showing preliminary evidence they may escape the confidence-correctness ceiling. Our findings chart boundaries for intrinsic URLVR while motivating paths toward scalable alternatives.

