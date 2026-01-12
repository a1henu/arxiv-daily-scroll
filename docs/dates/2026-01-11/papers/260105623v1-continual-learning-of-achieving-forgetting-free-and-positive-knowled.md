---
layout: default
title: Continual Learning of Achieving Forgetting-free and Positive Knowledge Transfer
---

# Continual Learning of Achieving Forgetting-free and Positive Knowledge Transfer
**arXiv**：[2601.05623v1](https://arxiv.org/abs/2601.05623) · [PDF](https://arxiv.org/pdf/2601.05623.pdf)  
**作者**：Zhi Wang, Zhongbin Wu, Yanni Li, Bing Liu, Guangxi Li, Yuping Wang  

**一句话要点**：提出ETCL方法以实现持续学习中的遗忘消除与正向知识迁移

**关键词**：持续学习, 知识迁移, 灾难性遗忘, 任务相似性检测, 梯度对齐, 正交投影

## 3 点简述
- 核心问题：现有持续学习研究主要关注灾难性遗忘，但理想代理还需实现正向前后向知识迁移。
- 方法要点：ETCL通过任务特定掩码隔离子网络，结合梯度对齐和正交投影优化策略，确保正向迁移。
- 实验或效果：在多种任务序列上显著优于基线，验证了遗忘消除和正向迁移的有效性。

## 摘要（原文）

> Existing research on continual learning (CL) of a sequence of tasks focuses mainly on dealing with catastrophic forgetting (CF) to balance the learning plasticity of new tasks and the memory stability of old tasks. However, an ideal CL agent should not only be able to overcome CF, but also encourage positive forward and backward knowledge transfer (KT), i.e., using the learned knowledge from previous tasks for the new task learning (namely FKT), and improving the previous tasks' performance with the knowledge of the new task (namely BKT). To this end, this paper first models CL as an optimization problem in which each sequential learning task aims to achieve its optimal performance under the constraint that both FKT and BKT should be positive. It then proposes a novel Enhanced Task Continual Learning (ETCL) method, which achieves forgetting-free and positive KT. Furthermore, the bounds that can lead to negative FKT and BKT are estimated theoretically. Based on the bounds, a new strategy for online task similarity detection is also proposed to facilitate positive KT. To overcome CF, ETCL learns a set of task-specific binary masks to isolate a sparse sub-network for each task while preserving the performance of a dense network for the task. At the beginning of a new task learning, ETCL tries to align the new task's gradient with that of the sub-network of the previous most similar task to ensure positive FKT. By using a new bi-objective optimization strategy and an orthogonal gradient projection method, ETCL updates only the weights of previous similar tasks at the classification layer to achieve positive BKT. Extensive evaluations demonstrate that the proposed ETCL markedly outperforms strong baselines on dissimilar, similar, and mixed task sequences.

