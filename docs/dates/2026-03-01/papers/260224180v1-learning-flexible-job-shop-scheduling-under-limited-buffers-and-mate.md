---
layout: default
title: Learning Flexible Job Shop Scheduling under Limited Buffers and Material Kitting Constraints
---

# Learning Flexible Job Shop Scheduling under Limited Buffers and Material Kitting Constraints
**arXiv**：[2602.24180v1](https://arxiv.org/abs/2602.24180) · [PDF](https://arxiv.org/pdf/2602.24180.pdf)  
**作者**：Shishun Zhang, Juzhan Xu, Yidan Fan, Chenyang Zhu, Ruizhen Hu, Yongjun Wang, Kai Xu  

**一句话要点**：提出基于异构图网络的深度强化学习方法，以解决带有限缓冲区和物料配套约束的柔性作业车间调度问题。

**关键词**：柔性作业车间调度, 深度强化学习, 异构图网络, 有限缓冲区, 物料配套约束, 生产调度优化

## 3 点简述
- 研究柔性作业车间调度问题，引入有限缓冲区和物料配套约束以贴近实际生产场景。
- 采用深度强化学习框架，利用异构图网络建模全局状态，通过消息传递优化调度决策。
- 在合成和真实数据集上验证，方法在完工时间和托盘更换次数上优于传统启发式和先进深度强化学习方法。

## 摘要（原文）

> The Flexible Job Shop Scheduling Problem (FJSP) originates from real production lines, while some practical constraints are often ignored or idealized in current FJSP studies, among which the limited buffer problem has a particular impact on production efficiency. To this end, we study an extended problem that is closer to practical scenarios--the Flexible Job Shop Scheduling Problem with Limited Buffers and Material Kitting. In recent years, deep reinforcement learning (DRL) has demonstrated considerable potential in scheduling tasks. However, its capacity for state modeling remains limited when handling complex dependencies and long-term constraints. To address this, we leverage a heterogeneous graph network within the DRL framework to model the global state. By constructing efficient message passing among machines, operations, and buffers, the network focuses on avoiding decisions that may cause frequent pallet changes during long-sequence scheduling, thereby helping improve buffer utilization and overall decision quality. Experimental results on both synthetic and real production line datasets show that the proposed method outperforms traditional heuristics and advanced DRL methods in terms of makespan and pallet changes, and also achieves a good balance between solution quality and computational cost. Furthermore, a supplementary video is provided to showcase a simulation system that effectively visualizes the progression of the production line.

