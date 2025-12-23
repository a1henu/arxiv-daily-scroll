---
layout: default
title: DTCCL: Disengagement-Triggered Contrastive Continual Learning for Autonomous Bus Planners
---

# DTCCL: Disengagement-Triggered Contrastive Continual Learning for Autonomous Bus Planners
**arXiv**：[2512.18988v1](https://arxiv.org/abs/2512.18988) · [PDF](https://arxiv.org/pdf/2512.18988.pdf)  
**作者**：Yanding Yang, Weitao Zhou, Jinhai Wang, Xiaomin Guo, Junze Wen, Xiaolong Liu, Lang Ding, Zheng Fu, Jinyu Miao, Kun Jiang, Diange Yang  

**一句话要点**：提出DTCCL框架，通过对比持续学习解决自动驾驶公交车规划器在交互区域失败的问题。

**关键词**：自动驾驶规划, 对比学习, 持续学习, 数据增强, 云边计算, 公共交通

## 3 点简述
- 核心问题：自动驾驶公交车在固定路线上运行，但规划器在动态城市环境中易在交互区域失败，传统模仿学习难以纠正。
- 方法要点：利用脱钩事件触发云端数据增强，生成正负样本，通过对比学习优化策略表示，实现无监督云边持续更新。
- 实验或效果：在城市公交路线实验中，相比直接重训练，DTCCL提升整体规划性能48.6%，验证了可扩展闭环改进的有效性。

## 摘要（原文）

> Autonomous buses run on fixed routes but must operate in open, dynamic urban environments. Disengagement events on these routes are often geographically concentrated and typically arise from planner failures in highly interactive regions. Such policy-level failures are difficult to correct using conventional imitation learning, which easily overfits to sparse disengagement data. To address this issue, this paper presents a Disengagement-Triggered Contrastive Continual Learning (DTCCL) framework that enables autonomous buses to improve planning policies through real-world operation. Each disengagement triggers cloud-based data augmentation that generates positive and negative samples by perturbing surrounding agents while preserving route context. Contrastive learning refines policy representations to better distinguish safe and unsafe behaviors, and continual updates are applied in a cloud-edge loop without human supervision. Experiments on urban bus routes demonstrate that DTCCL improves overall planning performance by 48.6 percent compared with direct retraining, validating its effectiveness for scalable, closed-loop policy improvement in autonomous public transport.

