---
layout: default
title: CFLight: Enhancing Safety with Traffic Signal Control through Counterfactual Learning
---

# CFLight: Enhancing Safety with Traffic Signal Control through Counterfactual Learning
**arXiv**：[2512.09368v1](https://arxiv.org/abs/2512.09368) · [PDF](https://arxiv.org/pdf/2512.09368.pdf)  
**作者**：Mingyuan Li, Chunyu Liu, Zhuojun Li, Xiao Liu, Guangsheng Yu, Bo Du, Jun Shen, Qiang Wu  

**一句话要点**：提出CFLight框架，通过反事实学习增强交通信号控制的安全性

**关键词**：交通信号控制, 反事实学习, 强化学习, 安全优化, 因果分析, 碰撞减少

## 3 点简述
- 核心问题：强化学习在交通信号控制中常优先效率而忽视安全，且缺乏可解释性。
- 方法要点：引入反事实学习模块，回溯不安全事件并预测替代行动结果，以平衡安全与效率。
- 实验或效果：在真实和合成数据集上，CFLight减少碰撞并提升整体交通性能，优于传统方法。

## 摘要（原文）

> Traffic accidents result in millions of injuries and fatalities globally, with a significant number occurring at intersections each year. Traffic Signal Control (TSC) is an effective strategy for enhancing safety at these urban junctures. Despite the growing popularity of Reinforcement Learning (RL) methods in optimizing TSC, these methods often prioritize driving efficiency over safety, thus failing to address the critical balance between these two aspects. Additionally, these methods usually need more interpretability. CounterFactual (CF) learning is a promising approach for various causal analysis fields. In this study, we introduce a novel framework to improve RL for safety aspects in TSC. This framework introduces a novel method based on CF learning to address the question: ``What if, when an unsafe event occurs, we backtrack to perform alternative actions, and will this unsafe event still occur in the subsequent period?'' To answer this question, we propose a new structure causal model to predict the result after executing different actions, and we propose a new CF module that integrates with additional ``X'' modules to promote safe RL practices. Our new algorithm, CFLight, which is derived from this framework, effectively tackles challenging safety events and significantly improves safety at intersections through a near-zero collision control strategy. Through extensive numerical experiments on both real-world and synthetic datasets, we demonstrate that CFLight reduces collisions and improves overall traffic performance compared to conventional RL methods and the recent safe RL model. Moreover, our method represents a generalized and safe framework for RL methods, opening possibilities for applications in other domains. The data and code are available in the github https://github.com/MJLee00/CFLight-Enhancing-Safety-with-Traffic-Signal-Control-through-Counterfactual-Learning.

