---
layout: default
title: MECAD: A multi-expert architecture for continual anomaly detection
---

# MECAD: A multi-expert architecture for continual anomaly detection
**arXiv**：[2512.15323v1](https://arxiv.org/abs/2512.15323) · [PDF](https://arxiv.org/pdf/2512.15323.pdf)  
**作者**：Malihe Dahmardeh, Francesco Setti  

**一句话要点**：提出MECAD多专家架构以解决工业环境中持续异常检测的知识退化问题

**关键词**：持续异常检测, 多专家架构, 增量学习, 知识保留, 工业应用, MVTec AD数据集

## 3 点简述
- 核心问题：持续异常检测中，新类别学习易导致旧类别知识退化，影响模型稳定性。
- 方法要点：基于特征相似性动态分配专家给对象类别，结合优化核心集选择和重放缓冲区机制实现增量学习。
- 实验或效果：在MVTec AD数据集上，5专家配置平均AUROC达0.8259，显著减少知识退化，平衡计算效率与适应性。

## 摘要（原文）

> In this paper we propose MECAD, a novel approach for continual anomaly detection using a multi-expert architecture. Our system dynamically assigns experts to object classes based on feature similarity and employs efficient memory management to preserve the knowledge of previously seen classes. By leveraging an optimized coreset selection and a specialized replay buffer mechanism, we enable incremental learning without requiring full model retraining. Our experimental evaluation on the MVTec AD dataset demonstrates that the optimal 5-expert configuration achieves an average AUROC of 0.8259 across 15 diverse object categories while significantly reducing knowledge degradation compared to single-expert approaches. This framework balances computational efficiency, specialized knowledge retention, and adaptability, making it well-suited for industrial environments with evolving product types.

