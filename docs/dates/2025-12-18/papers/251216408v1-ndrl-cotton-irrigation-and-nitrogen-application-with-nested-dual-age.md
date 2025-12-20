---
layout: default
title: NDRL: Cotton Irrigation and Nitrogen Application with Nested Dual-Agent Reinforcement Learning
---

# NDRL: Cotton Irrigation and Nitrogen Application with Nested Dual-Agent Reinforcement Learning
**arXiv**：[2512.16408v1](https://arxiv.org/abs/2512.16408) · [PDF](https://arxiv.org/pdf/2512.16408.pdf)  
**作者**：Ruifeng Xu, Liang He  

**一句话要点**：提出嵌套双智能体强化学习以优化棉花灌溉与施氮，提升产量与资源效率。

**关键词**：强化学习, 农业资源管理, 棉花灌溉, 氮肥施用, 决策支持系统, 胁迫量化

## 3 点简述
- 核心问题：现有方法优化水氮组合复杂、产量低，且难以量化胁迫信号导致调控不精准。
- 方法要点：采用父智能体宏观决策与子智能体动态优化，结合量化胁迫因子和混合概率分布。
- 实验或效果：基于DSSAT模拟，相比基线，模拟产量提升约4.7%，灌溉水与氮肥生产力提高。

## 摘要（原文）

> Effective irrigation and nitrogen fertilization have a significant impact on crop yield. However, existing research faces two limitations: (1) the high complexity of optimizing water-nitrogen combinations during crop growth and poor yield optimization results; and (2) the difficulty in quantifying mild stress signals and the delayed feedback, which results in less precise dynamic regulation of water and nitrogen and lower resource utilization efficiency. To address these issues, we propose a Nested Dual-Agent Reinforcement Learning (NDRL) method. The parent agent in NDRL identifies promising macroscopic irrigation and fertilization actions based on projected cumulative yield benefits, reducing ineffective explorationwhile maintaining alignment between objectives and yield. The child agent's reward function incorporates quantified Water Stress Factor (WSF) and Nitrogen Stress Factor (NSF), and uses a mixed probability distribution to dynamically optimize daily strategies, thereby enhancing both yield and resource efficiency. We used field experiment data from 2023 and 2024 to calibrate and validate the Decision Support System for Agrotechnology Transfer (DSSAT) to simulate real-world conditions and interact with NDRL. Experimental results demonstrate that, compared to the best baseline, the simulated yield increased by 4.7% in both 2023 and 2024, the irrigation water productivity increased by 5.6% and 5.1% respectively, and the nitrogen partial factor productivity increased by 6.3% and 1.0% respectively. Our method advances the development of cotton irrigation and nitrogen fertilization, providing new ideas for addressing the complexity and precision issues in agricultural resource management and for sustainable agricultural development.

