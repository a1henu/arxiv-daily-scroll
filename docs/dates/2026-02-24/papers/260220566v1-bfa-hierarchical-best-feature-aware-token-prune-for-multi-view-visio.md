---
layout: default
title: BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model
---

# BFA++: Hierarchical Best-Feature-Aware Token Prune for Multi-View Vision Language Action Model
**arXiv**：[2602.20566v1](https://arxiv.org/abs/2602.20566) · [PDF](https://arxiv.org/pdf/2602.20566.pdf)  
**作者**：Haosheng Li, Weixin Mao, Zihan Lan, Hongwei Xiong, Hongan Wang, Chenyang Si, Ziwei Liu, Xiaoming Deng, Hua Chen  

**一句话要点**：提出BFA++分层剪枝框架，以解决多视图视觉语言动作模型实时性挑战

**关键词**：视觉语言动作模型, 令牌剪枝, 多视图处理, 机器人操作, 实时推理, 分层策略

## 3 点简述
- 核心问题：多视图视觉语言动作模型视觉令牌过多，现有剪枝方法忽略视图关系和任务动态性，导致性能下降
- 方法要点：引入分层剪枝策略，通过视图内和视图间重要性预测器动态选择令牌，减少冗余并保留关键视觉线索
- 实验或效果：在RoboTwin基准和真实任务中，BFA++提升成功率约10%，加速1.5-1.8倍，优于现有方法

## 摘要（原文）

> Vision-Language-Action (VLA) models have achieved significant breakthroughs by leveraging Large Vision Language Models (VLMs) to jointly interpret instructions and visual inputs. However, the substantial increase in visual tokens, particularly from multi-view inputs, poses serious challenges to real-time robotic manipulation. Existing acceleration techniques for VLMs, such as token pruning, often result in degraded performance when directly applied to VLA models, as they overlook the relationships between different views and fail to account for the dynamic and task-specific characteristics of robotic operation. To address this, we propose BFA++, a dynamic token pruning framework designed specifically for VLA models. BFA++ introduces a hierarchical pruning strategy guided by two-level importance predictors: an intra-view predictor highlights task-relevant regions within each image to suppress spatial noise, while an inter-view predictor identifies critical camera views throughout different manipulation phases to reduce cross-view redundancy. This design enables efficient token selection while preserving essential visual cues, resulting in improved computational efficiency and higher manipulation success rates. Evaluations on the RoboTwin benchmark and real-world robotic tasks demonstrate that BFA++ consistently outperforms existing methods. BFA++ improves the success rate by about 10% on both the π0 and RDT models, achieving speedup of 1.8X and 1.5X, respectively. Our results highlight that context-sensitive and task-aware token pruning serves as a more effective strategy than full visual processing, enabling faster inference and improved manipulation accuracy in real-world robotic systems.

