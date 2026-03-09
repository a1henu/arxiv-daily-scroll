---
layout: default
title: Self-Auditing Parameter-Efficient Fine-Tuning for Few-Shot 3D Medical Image Segmentation
---

# Self-Auditing Parameter-Efficient Fine-Tuning for Few-Shot 3D Medical Image Segmentation
**arXiv**：[2603.05822v1](https://arxiv.org/abs/2603.05822) · [PDF](https://arxiv.org/pdf/2603.05822.pdf)  
**作者**：Son Thai Ly, Hien V. Nguyen  

**一句话要点**：提出SEA-PEFT以自动化适配器配置，解决少样本3D医学图像分割中的领域偏移问题。

**关键词**：参数高效微调, 3D医学图像分割, 少样本学习, 领域适应, 在线分配, 自动化配置

## 3 点简述
- 核心问题：基础模型适应新临床站点时面临领域偏移和标注稀缺，现有PEFT方法需手动配置或计算成本高。
- 方法要点：SEA-PEFT将适配器配置视为在线分配问题，通过搜索-审计-分配循环动态选择适配器，使用平滑技术和控制器稳定训练。
- 实验或效果：在TotalSegmentator和FLARE'22数据集上，SEA-PEFT在1/5/10-shot设置中比固定拓扑PEFT基线平均Dice提升2.4-2.8点，训练参数<1%。

## 摘要（原文）

> Adapting foundation models to new clinical sites remains challenging in practice. Domain shift and scarce annotations must be handled by experts, yet many clinical groups do not have ready access to skilled AI engineers to tune adapter designs and training recipes. As a result, adaptation cycles can stretch from weeks to months, particularly in few-shot settings. Existing PEFT methods either require manual adapter configuration or automated searches that are computationally infeasible in few-shot 3D settings. We propose SEA-PEFT (SElf-Auditing Parameter-Efficient Fine-Tuning) to automate this process. SEA-PEFT treats adapter configuration as an online allocation problem solved during fine-tuning rather than through manual, fixed-topology choices. SEA-PEFT uses a search-audit-allocate loop that trains active adapters, estimates each adapter's Dice utility by momentarily toggling it off, and then reselects the active set under a parameter budget using a greedy knapsack allocator. Exponential Moving Average and Interquartile Range smoothing, together with a Finite-State Ranking controller, stabilize the loop and improve reliability in high-noise few-shot regimes. On TotalSegmentator and FLARE'22, SEA-PEFT improves mean Dice by 2.4--2.8 points over the strongest fixed-topology PEFT baselines across 1/5/10-shot settings while training <1% of parameters. For reproducibility purposes, we made our code publicly available at https://github.com/tsly123/SEA_PEFT

