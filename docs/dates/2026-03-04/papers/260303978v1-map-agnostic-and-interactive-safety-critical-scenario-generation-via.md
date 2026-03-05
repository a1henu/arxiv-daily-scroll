---
layout: default
title: Map-Agnostic And Interactive Safety-Critical Scenario Generation via Multi-Objective Tree Search
---

# Map-Agnostic And Interactive Safety-Critical Scenario Generation via Multi-Objective Tree Search
**arXiv**：[2603.03978v1](https://arxiv.org/abs/2603.03978) · [PDF](https://arxiv.org/pdf/2603.03978.pdf)  
**作者**：Wenyun Li, Zejian Deng, Chen Sun  

**一句话要点**：提出基于多目标树搜索的交通流级安全关键场景生成框架，以解决碰撞真实性与多样性不足问题。

**关键词**：安全关键场景生成, 多目标树搜索, 自动驾驶验证, 交通流模拟, 交互式场景

## 3 点简述
- 核心问题：现有方法难以生成真实、多样且具交互逻辑的安全关键场景，用于自动驾驶系统验证。
- 方法要点：采用多目标蒙特卡洛树搜索，将轨迹可行性和自然行为作为优化目标，结合混合置信界搜索策略。
- 实验或效果：在香港高风险区域验证，实现85%碰撞失败率，生成轨迹在可行性和舒适度上表现优异。

## 摘要（原文）

> Generating safety-critical scenarios is essential for validating the robustness of autonomous driving systems, yet existing methods often struggle to produce collisions that are both realistic and diverse while ensuring explicit interaction logic among traffic participants. This paper presents a novel framework for traffic-flow level safety-critical scenario generation via multi-objective Monte Carlo Tree Search (MCTS). We reframe trajectory feasibility and naturalistic behavior as optimization objectives within a unified evaluation function, enabling the discovery of diverse collision events without compromising realism. A hybrid Upper Confidence Bound (UCB) and Lower Confidence Bound (LCB) search strategy is introduced to balance exploratory efficiency with risk-averse decision-making. Furthermore, our method is map-agnostic and supports interactive scenario generation with each vehicle individually powered by SUMO's microscopic traffic models, enabling realistic agent behaviors in arbitrary geographic locations imported from OpenStreetMap. We validate our approach across four high-risk accident zones in Hong Kong's complex urban environments. Experimental results demonstrate that our framework achieves an 85\% collision failure rate while generating trajectories with superior feasibility and comfort metrics. The resulting scenarios exhibit greater complexity, as evidenced by increased vehicle mileage and CO\(_2\) emissions. Our work provides a principled solution for stress testing autonomous vehicles through the generation of realistic yet infrequent corner cases at traffic-flow level.

