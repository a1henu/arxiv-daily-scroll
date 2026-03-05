---
layout: default
title: SimpliHuMoN: Simplifying Human Motion Prediction
---

# SimpliHuMoN: Simplifying Human Motion Prediction
**arXiv**：[2603.04399v1](https://arxiv.org/abs/2603.04399) · [PDF](https://arxiv.org/pdf/2603.04399.pdf)  
**作者**：Aadya Agrawal, Alexander Schwing  

**一句话要点**：提出基于Transformer的简化模型以解决人体运动预测中轨迹与姿态联合预测的难题

**关键词**：人体运动预测, Transformer模型, 自注意力机制, 轨迹预测, 姿态预测, 端到端学习

## 3 点简述
- 核心问题：人体运动预测需联合轨迹预测与姿态预测，现有方法难以在单一模型中兼顾两者，导致在基准测试中表现不佳。
- 方法要点：采用自注意力模块堆叠的Transformer模型，有效捕捉姿态内空间依赖和运动序列间时间关系，实现端到端简化设计。
- 实验或效果：在Human3.6M、AMASS等广泛基准数据集上验证，该模型无需任务特定修改，在姿态、轨迹及联合预测任务中均达到最先进性能。

## 摘要（原文）

> Human motion prediction combines the tasks of trajectory forecasting and human pose prediction. For each of the two tasks, specialized models have been developed. Combining these models for holistic human motion prediction is non-trivial, and recent methods have struggled to compete on established benchmarks for individual tasks. To address this, we propose a simple yet effective transformer-based model for human motion prediction. The model employs a stack of self-attention modules to effectively capture both spatial dependencies within a pose and temporal relationships across a motion sequence. This simple, streamlined, end-to-end model is sufficiently versatile to handle pose-only, trajectory-only, and combined prediction tasks without task-specific modifications. We demonstrate that this approach achieves state-of-the-art results across all tasks through extensive experiments on a wide range of benchmark datasets, including Human3.6M, AMASS, ETH-UCY, and 3DPW.

