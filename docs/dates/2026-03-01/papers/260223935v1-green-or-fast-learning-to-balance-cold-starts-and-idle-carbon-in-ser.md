---
layout: default
title: Green or Fast? Learning to Balance Cold Starts and Idle Carbon in Serverless Computing
---

# Green or Fast? Learning to Balance Cold Starts and Idle Carbon in Serverless Computing
**arXiv**：[2602.23935v1](https://arxiv.org/abs/2602.23935) · [PDF](https://arxiv.org/pdf/2602.23935.pdf)  
**作者**：Bowen Sun, Christos D. Antonopoulos, Evgenia Smirni, Bin Ren, Nikolaos Bellas, Spyros Lalis  

**一句话要点**：提出LACE-RL框架以平衡无服务器计算中的冷启动延迟与空闲碳排放

**关键词**：无服务器计算, 冷启动优化, 碳排放管理, 深度强化学习, 资源调度

## 3 点简述
- 核心问题：无服务器计算中，保持实例以减少冷启动与回收资源以降低碳排放存在动态平衡难题
- 方法要点：采用深度强化学习动态调整保持时间，联合建模冷启动概率、延迟成本和实时碳强度
- 实验或效果：在华为云轨迹上，相比静态策略，冷启动减少51.69%，空闲碳排放降低77.08%

## 摘要（原文）

> Serverless computing simplifies cloud deployment but introduces new challenges in managing service latency and carbon emissions. Reducing cold-start latency requires retaining warm function instances, while minimizing carbon emissions favors reclaiming idle resources. This balance is further complicated by time-varying grid carbon intensity and varying workload patterns, under which static keep-alive policies are inefficient. We present LACE-RL, a latency-aware and carbon-efficient management framework that formulates serverless pod retention as a sequential decision problem. LACE-RL uses deep reinforcement learning to dynamically tune keep-alive durations, jointly modeling cold-start probability, function-specific latency costs, and real-time carbon intensity. Using the Huawei Public Cloud Trace, we show that LACE-RL reduces cold starts by 51.69% and idle keep-alive carbon emissions by 77.08% compared to Huawei's static policy, while achieving better latency-carbon trade-offs than state-of-the-art heuristic and single-objective baselines, approaching Oracle performance.

