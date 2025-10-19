---
layout: default
title: When Planners Meet Reality: How Learned, Reactive Traffic Agents Shift nuPlan Benchmarks
---

# When Planners Meet Reality: How Learned, Reactive Traffic Agents Shift nuPlan Benchmarks
**arXiv**：[2510.14677v1](https://arxiv.org/abs/2510.14677) · [PDF](https://arxiv.org/pdf/2510.14677.pdf)  
**作者**：Steffen Hagedorn, Luka Donkov, Aron Distelzweig, Alexandru P. Condurache  

**一句话要点**：集成SMART智能体以解决nuPlan基准中规则交通代理的局限性

**关键词**：交通代理模拟, 规划器评估, nuPlan基准, 学习型代理, 闭环仿真

## 3 点简述
- 规则交通代理如IDM行为简单，隐藏规划器缺陷并偏置评估。
- 集成学习型交通代理SMART，模拟更真实交互，评估14个规划器。
- SMART模拟显示规划器性能普遍下降，但在复杂场景中交互能力提升。

## 摘要（原文）

> Planner evaluation in closed-loop simulation often uses rule-based traffic
> agents, whose simplistic and passive behavior can hide planner deficiencies and
> bias rankings. Widely used IDM agents simply follow a lead vehicle and cannot
> react to vehicles in adjacent lanes, hindering tests of complex interaction
> capabilities. We address this issue by integrating the state-of-the-art learned
> traffic agent model SMART into nuPlan. Thus, we are the first to evaluate
> planners under more realistic conditions and quantify how conclusions shift
> when narrowing the sim-to-real gap. Our analysis covers 14 recent planners and
> established baselines and shows that IDM-based simulation overestimates
> planning performance: nearly all scores deteriorate. In contrast, many planners
> interact better than previously assumed and even improve in multi-lane,
> interaction-heavy scenarios like lane changes or turns. Methods trained in
> closed-loop demonstrate the best and most stable driving performance. However,
> when reaching their limits in augmented edge-case scenarios, all learned
> planners degrade abruptly, whereas rule-based planners maintain reasonable
> basic behavior. Based on our results, we suggest SMART-reactive simulation as a
> new standard closed-loop benchmark in nuPlan and release the SMART agents as a
> drop-in alternative to IDM at https://github.com/shgd95/InteractiveClosedLoop.

