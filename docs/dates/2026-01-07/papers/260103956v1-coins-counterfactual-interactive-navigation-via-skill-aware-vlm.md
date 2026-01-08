---
layout: default
title: CoINS: Counterfactual Interactive Navigation via Skill-Aware VLM
---

# CoINS: Counterfactual Interactive Navigation via Skill-Aware VLM
**arXiv**：[2601.03956v1](https://arxiv.org/abs/2601.03956) · [PDF](https://arxiv.org/pdf/2601.03956.pdf)  
**作者**：Kangjie Zhou, Zhejia Wen, Zhiyong Zhuo, Zike Yan, Pengying Wu, Ieng Hou U, Shuaiyang Li, Han Gao, Kang Ding, Wenhan Cao, Wei Pan, Chang Liu  

**一句话要点**：提出CoINS框架以解决机器人交互导航中VLM缺乏物理技能理解的问题

**关键词**：交互导航, 视觉语言模型, 反事实推理, 技能库, 强化学习, 机器人规划

## 3 点简述
- 核心问题：现有VLM导航器仅能被动避障，无法在杂乱环境中主动交互以清理路径
- 方法要点：通过技能感知VLM进行反事实推理，结合强化学习技能库执行高层计划
- 实验或效果：在模拟和真实实验中，CoINS整体成功率提升17%，复杂场景改进超80%

## 摘要（原文）

> Recent Vision-Language Models (VLMs) have demonstrated significant potential in robotic planning. However, they typically function as semantic reasoners, lacking an intrinsic understanding of the specific robot's physical capabilities. This limitation is particularly critical in interactive navigation, where robots must actively modify cluttered environments to create traversable paths. Existing VLM-based navigators are predominantly confined to passive obstacle avoidance, failing to reason about when and how to interact with objects to clear blocked paths. To bridge this gap, we propose Counterfactual Interactive Navigation via Skill-aware VLM (CoINS), a hierarchical framework that integrates skill-aware reasoning and robust low-level execution. Specifically, we fine-tune a VLM, named InterNav-VLM, which incorporates skill affordance and concrete constraint parameters into the input context and grounds them into a metric-scale environmental representation. By internalizing the logic of counterfactual reasoning through fine-tuning on the proposed InterNav dataset, the model learns to implicitly evaluate the causal effects of object removal on navigation connectivity, thereby determining interaction necessity and target selection. To execute the generated high-level plans, we develop a comprehensive skill library through reinforcement learning, specifically introducing traversability-oriented strategies to manipulate diverse objects for path clearance. A systematic benchmark in Isaac Sim is proposed to evaluate both the reasoning and execution aspects of interactive navigation. Extensive simulations and real-world experiments demonstrate that CoINS significantly outperforms representative baselines, achieving a 17\% higher overall success rate and over 80\% improvement in complex long-horizon scenarios compared to the best-performing baseline

