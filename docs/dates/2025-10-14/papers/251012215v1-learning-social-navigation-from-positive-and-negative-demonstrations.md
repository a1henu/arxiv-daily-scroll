---
layout: default
title: Learning Social Navigation from Positive and Negative Demonstrations and Rule-Based Specifications
---

# Learning Social Navigation from Positive and Negative Demonstrations and Rule-Based Specifications
**arXiv**：[2510.12215v1](https://arxiv.org/abs/2510.12215) · [PDF](https://arxiv.org/pdf/2510.12215.pdf)  
**作者**：Chanwoo Kim, Jihwan Yoon, Hyeonseong Kim, Taemoon Jeong, Changwoo Yoo, Seungbeen Lee, Soohwan Byeon, Hoon Chung, Matthew Pan, Jean Oh, Kyungjae Lee, Sungjoon Choi  

**一句话要点**：提出结合数据驱动奖励与规则目标的框架，以提升移动机器人在动态人类环境中的导航性能。

**关键词**：社会导航, 奖励学习, 规则集成, 策略蒸馏, 动态环境, 实时控制

## 3 点简述
- 核心问题：移动机器人在动态人类环境中需平衡适应性与安全性。
- 方法要点：从正负演示学习奖励，结合规则目标，蒸馏为实时策略。
- 实验效果：在仿真和真实世界测试中，成功率和时间效率优于基线。

## 摘要（原文）

> Mobile robot navigation in dynamic human environments requires policies that
> balance adaptability to diverse behaviors with compliance to safety
> constraints. We hypothesize that integrating data-driven rewards with
> rule-based objectives enables navigation policies to achieve a more effective
> balance of adaptability and safety. To this end, we develop a framework that
> learns a density-based reward from positive and negative demonstrations and
> augments it with rule-based objectives for obstacle avoidance and goal
> reaching. A sampling-based lookahead controller produces supervisory actions
> that are both safe and adaptive, which are subsequently distilled into a
> compact student policy suitable for real-time operation with uncertainty
> estimates. Experiments in synthetic and elevator co-boarding simulations show
> consistent gains in success rate and time efficiency over baselines, and
> real-world demonstrations with human participants confirm the practicality of
> deployment. A video illustrating this work can be found on our project page
> https://chanwookim971024.github.io/PioneeR/.

