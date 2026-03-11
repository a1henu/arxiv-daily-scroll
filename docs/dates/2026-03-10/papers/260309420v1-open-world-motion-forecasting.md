---
layout: default
title: Open-World Motion Forecasting
---

# Open-World Motion Forecasting
**arXiv**：[2603.09420v1](https://arxiv.org/abs/2603.09420) · [PDF](https://arxiv.org/pdf/2603.09420.pdf)  
**作者**：Nicolas Schischka, Nikhil Gosala, B Ravi Kiran, Senthil Yogamani, Abhinav Valada  

**一句话要点**：提出开放世界运动预测框架，通过类增量学习解决感知不完美和对象分类演化的挑战。

**关键词**：运动预测, 开放世界学习, 类增量学习, 灾难性遗忘缓解, 端到端自动驾驶, 伪标签策略

## 3 点简述
- 核心问题：现有方法在封闭世界假设下，难以处理感知不完美和对象分类随时间演化的现实场景。
- 方法要点：采用端到端类增量框架，结合伪标签策略和基于查询特征方差的回放采样，以缓解灾难性遗忘。
- 实验或效果：在nuScenes和Argoverse 2数据集上验证，能抵抗遗忘并适应新类，支持零样本迁移和端到端规划。

## 摘要（原文）

> Motion forecasting aims to predict the future trajectories of dynamic agents in the scene, enabling autonomous vehicles to effectively reason about scene evolution. Existing approaches operate under the closed-world regime and assume fixed object taxonomy as well as access to high-quality perception. Therefore, they struggle in real-world settings where perception is imperfect and object taxonomy evolves over time. In this work, we bridge this fundamental gap by introducing open-world motion forecasting, a novel setting in which new object classes are sequentially introduced over time and future object trajectories are estimated directly from camera images. We tackle this setting by proposing the first end-to-end class-incremental motion forecasting framework to mitigate catastrophic forgetting while simultaneously learning to forecast newly introduced classes. When a new class is introduced, our framework employs a pseudo-labeling strategy to first generate motion forecasting pseudo-labels for all known classes which are then processed by a vision-language model to filter inconsistent and over-confident predictions. Parallelly, our approach further mitigates catastrophic forgetting by using a novel replay sampling strategy that leverages query feature variance to sample previous sequences with informative motion patterns. Extensive evaluation on the nuScenes and Argoverse 2 datasets demonstrates that our approach successfully resists catastrophic forgetting and maintains performance on previously learned classes while improving adaptation to novel ones. Further, we demonstrate that our approach supports zero-shot transfer to real-world driving and naturally extends to end-to-end class-incremental planning, enabling continual adaptation of the full autonomous driving system. We provide the code at https://omen.cs.uni-freiburg.de .

