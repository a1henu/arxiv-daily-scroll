---
layout: default
title: BPP: Long-Context Robot Imitation Learning by Focusing on Key History Frames
---

# BPP: Long-Context Robot Imitation Learning by Focusing on Key History Frames
**arXiv**：[2602.15010v1](https://arxiv.org/abs/2602.15010) · [PDF](https://arxiv.org/pdf/2602.15010.pdf)  
**作者**：Max Sobol Mark, Jacky Liang, Maria Attarian, Chuyuan Fu, Debidatta Dwibedi, Dhruv Shah, Aviral Kumar  

**一句话要点**：提出Big Picture Policies，通过视觉语言模型检测关键帧以解决机器人模仿学习中的历史依赖与虚假相关性问题。

**关键词**：机器人模仿学习, 长上下文策略, 关键帧检测, 视觉语言模型, 分布偏移缓解, 历史依赖任务

## 3 点简述
- 核心问题：机器人策略仅依赖当前观测，无法处理需历史记忆的任务，且训练中历史覆盖不足导致虚假相关。
- 方法要点：使用视觉语言模型识别任务相关关键帧，将多样轨迹投影到紧凑事件集，减少训练与部署间的分布偏移。
- 实验或效果：在真实世界和仿真任务中评估，BPP相比最佳基线成功率提高70%，验证其有效性。

## 摘要（原文）

> Many robot tasks require attending to the history of past observations. For example, finding an item in a room requires remembering which places have already been searched. However, the best-performing robot policies typically condition only on the current observation, limiting their applicability to such tasks. Naively conditioning on past observations often fails due to spurious correlations: policies latch onto incidental features of training histories that do not generalize to out-of-distribution trajectories upon deployment. We analyze why policies latch onto these spurious correlations and find that this problem stems from limited coverage over the space of possible histories during training, which grows exponentially with horizon. Existing regularization techniques provide inconsistent benefits across tasks, as they do not fundamentally address this coverage problem. Motivated by these findings, we propose Big Picture Policies (BPP), an approach that conditions on a minimal set of meaningful keyframes detected by a vision-language model. By projecting diverse rollouts onto a compact set of task-relevant events, BPP substantially reduces distribution shift between training and deployment, without sacrificing expressivity. We evaluate BPP on four challenging real-world manipulation tasks and three simulation tasks, all requiring history conditioning. BPP achieves 70% higher success rates than the best comparison on real-world evaluations.

