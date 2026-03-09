---
layout: default
title: Devil is in Narrow Policy: Unleashing Exploration in Driving VLA Models
---

# Devil is in Narrow Policy: Unleashing Exploration in Driving VLA Models
**arXiv**：[2603.06049v1](https://arxiv.org/abs/2603.06049) · [PDF](https://arxiv.org/pdf/2603.06049.pdf)  
**作者**：Canyu Chen, Yuguang Yang, Zhewen Tan, Yizhi Wang, Ruiyi Zhan, Haiyan Liu, Xuanyao Mao, Jason Bao, Xinyue Tang, Linlin Yang, Bingchuan Sun, Yan Wang, Baochang Zhang  

**一句话要点**：提出Curious-VLA框架以解决自动驾驶VLA模型中探索受限问题

**关键词**：自动驾驶, 视觉语言动作模型, 探索-利用平衡, 模仿学习, 强化学习, 轨迹生成

## 3 点简述
- 核心问题：模仿学习导致探索崩溃，限制强化学习性能提升
- 方法要点：IL阶段采用可行轨迹扩展与归一化表示，RL阶段引入自适应多样性采样与跨度驾驶奖励
- 实验或效果：在Navsim基准上实现SoTA结果，PDMS达90.3，EPDMS达85.4

## 摘要（原文）

> We identify a fundamental Narrow Policy limitation undermining the performance of autonomous VLA models, where driving Imitation Learning (IL) tends to collapse exploration and limit the potential of subsequent Reinforcement Learning (RL) stages, which often saturate prematurely due to insufficient feedback diversity. Thereby, we propose Curious-VLA, a framework that alleviates the exploit-explore dilemma through a two-stage design. During IL, we introduce a Feasible Trajectory Expansion (FTE) strategy to generate multiple physically valid trajectories and a step-wise normalized trajectory representation to adapt this diverse data. In the RL stage, we present Adaptive Diversity-Aware Sampling (ADAS) that prioritizes high-diversity samples and introduce Spanning Driving Reward (SDR) with a focal style weighting to amplify reward's value span for improving sensitivity to driving quality. On the Navsim benchmark, Curious-VLA achieves SoTA results (PDMS 90.3, EPDMS 85.4) and a Best-of-N PDMS of 94.8, demonstrating its effectiveness in unlocking the exploratory potential of VLA models. Code: https://github.com/Mashiroln/curious_vla.git.

