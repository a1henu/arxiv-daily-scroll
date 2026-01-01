---
layout: default
title: ResponseRank: Data-Efficient Reward Modeling through Preference Strength Learning
---

# ResponseRank: Data-Efficient Reward Modeling through Preference Strength Learning
**arXiv**：[2512.25023v1](https://arxiv.org/abs/2512.25023) · [PDF](https://arxiv.org/pdf/2512.25023.pdf)  
**作者**：Timo Kaufmann, Yannick Metz, Daniel Keim, Eyke Hüllermeier  

**一句话要点**：提出ResponseRank方法，通过局部相对强度信号学习偏好强度，以解决从人类反馈中强化学习的数据效率问题。

**关键词**：偏好强度学习, 数据高效奖励建模, 人类反馈强化学习, 局部相对信号, 鲁棒学习, 样本效率

## 3 点简述
- 核心问题：二元选择仅传达偏好方向，缺乏强度信息，影响决策和模型泛化。
- 方法要点：利用代理信号（如响应时间）的相对差异，在局部层内排序响应，稳健学习偏好强度。
- 实验或效果：在合成偏好学习、语言建模和RL控制任务中验证了样本效率和鲁棒性提升。

## 摘要（原文）

> Binary choices, as often used for reinforcement learning from human feedback (RLHF), convey only the direction of a preference. A person may choose apples over oranges and bananas over grapes, but which preference is stronger? Strength is crucial for decision-making under uncertainty and generalization of preference models, but hard to measure reliably. Metadata such as response times and inter-annotator agreement can serve as proxies for strength, but are often noisy and confounded. We propose ResponseRank to address the challenge of learning from noisy strength signals. Our method uses relative differences in proxy signals to rank responses to pairwise comparisons by their inferred preference strength. To control for systemic variation, we compare signals only locally within carefully constructed strata. This enables robust learning of utility differences consistent with strength-derived rankings while making minimal assumptions about the strength signal. Our contributions are threefold: (1) ResponseRank, a novel method that robustly learns preference strength by leveraging locally valid relative strength signals; (2) empirical evidence of improved sample efficiency and robustness across diverse tasks: synthetic preference learning (with simulated response times), language modeling (with annotator agreement), and RL control tasks (with simulated episode returns); and (3) the Pearson Distance Correlation (PDC), a novel metric that isolates cardinal utility learning from ordinal accuracy.

