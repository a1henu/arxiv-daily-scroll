---
layout: default
title: Declarative Scenario-based Testing with RoadLogic
---

# Declarative Scenario-based Testing with RoadLogic
**arXiv**：[2603.09455v1](https://arxiv.org/abs/2603.09455) · [PDF](https://arxiv.org/pdf/2603.09455.pdf)  
**作者**：Ezio Bartocci, Alessio Gambi, Felix Gigler, Cristinel Mateis, Dejan Ničković  

**一句话要点**：提出RoadLogic以桥接声明式场景规范与可执行仿真，支持自动驾驶系统测试。

**关键词**：自动驾驶测试, 场景生成, 答案集编程, 运动规划, 规范监控

## 3 点简述
- 核心问题：现有声明式场景定义缺乏系统方法生成符合规范的具体仿真场景。
- 方法要点：使用答案集编程生成抽象计划，结合运动规划细化轨迹，并基于规范监控验证正确性。
- 实验或效果：在CommonRoad框架中评估，能快速生成现实且满足规范的仿真，捕获行为变体。

## 摘要（原文）

> Scenario-based testing is a key method for cost-effective and safe validation of autonomous vehicles (AVs). Existing approaches rely on imperative scenario definitions, requiring developers to manually enumerate numerous variants to achieve coverage. Declarative languages, such as OpenSCENARIO DSL (OS2), raise the abstraction level but lack systematic methods for instantiating concrete, specification-compliant scenarios as simulations. To our knowledge, currently, no open-source solution provides this capability.
>   We present RoadLogic that bridges declarative OS2 specifications and executable simulations. It uses Answer Set Programming to generate abstract plans satisfying scenario constraints, motion planning to refine the plans into feasible trajectories, and specification-based monitoring to verify correctness.
>   We evaluate RoadLogic on instantiating representative OS2 scenarios as simulations in the CommonRoad framework. Results show that RoadLogic consistently produces realistic, specification-satisfying simulations within minutes and captures diverse behavioral variants through parameter sampling, thus opening the door to systematic scenario-based testing for autonomous driving systems.

