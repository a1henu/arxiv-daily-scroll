---
layout: default
title: $χ_{0}$: Resource-Aware Robust Manipulation via Taming Distributional Inconsistencies
---

# $χ_{0}$: Resource-Aware Robust Manipulation via Taming Distributional Inconsistencies
**arXiv**：[2602.09021v1](https://arxiv.org/abs/2602.09021) · [PDF](https://arxiv.org/pdf/2602.09021.pdf)  
**作者**：Checheng Yu, Chonghao Sima, Gangcheng Jiang, Hai Zhang, Haoguang Mai, Hongyang Li, Huijie Wang, Jin Chen, Kaiyang Wu, Li Chen, Lirui Zhao, Modi Shi, Ping Luo, Qingwen Bu, Shijia Peng, Tianyu Li, Yibo Yuan  

**一句话要点**：提出资源感知框架χ₀以解决机器人操作中分布不一致导致的鲁棒性问题

**关键词**：机器人操作, 分布不一致, 资源效率, 多阶段任务, 鲁棒性框架

## 3 点简述
- 核心问题：机器人操作中，演示分布、策略学习分布与执行分布之间的不一致性导致多阶段任务错误累积。
- 方法要点：通过模型算术、阶段优势估计和训练部署对齐三个技术支柱，高效整合多样分布并稳定学习信号。
- 实验或效果：在双臂机器人衣物操作任务中，以较少数据和计算资源实现高可靠性，成功率比现有方法提升近250%。

## 摘要（原文）

> High-reliability long-horizon robotic manipulation has traditionally relied on large-scale data and compute to understand complex real-world dynamics. However, we identify that the primary bottleneck to real-world robustness is not resource scale alone, but the distributional shift among the human demonstration distribution, the inductive bias learned by the policy, and the test-time execution distribution -- a systematic inconsistency that causes compounding errors in multi-stage tasks. To mitigate these inconsistencies, we propose $χ_{0}$, a resource-efficient framework with effective modules designated to achieve production-level robustness in robotic manipulation. Our approach builds off three technical pillars: (i) Model Arithmetic, a weight-space merging strategy that efficiently soaks up diverse distributions of different demonstrations, varying from object appearance to state variations; (ii) Stage Advantage, a stage-aware advantage estimator that provides stable, dense progress signals, overcoming the numerical instability of prior non-stage approaches; and (iii) Train-Deploy Alignment, which bridges the distribution gap via spatio-temporal augmentation, heuristic DAgger corrections, and temporal chunk-wise smoothing. $χ_{0}$ enables two sets of dual-arm robots to collaboratively orchestrate long-horizon garment manipulation, spanning tasks from flattening, folding, to hanging different clothes. Our method exhibits high-reliability autonomy; we are able to run the system from arbitrary initial state for consecutive 24 hours non-stop. Experiments validate that $χ_{0}$ surpasses the state-of-the-art $π_{0.5}$ in success rate by nearly 250%, with only 20-hour data and 8 A100 GPUs. Code, data and models will be released to facilitate the community.

