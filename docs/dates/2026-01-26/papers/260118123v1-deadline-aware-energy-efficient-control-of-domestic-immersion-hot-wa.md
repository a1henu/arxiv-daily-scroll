---
layout: default
title: Deadline-Aware, Energy-Efficient Control of Domestic Immersion Hot Water Heaters
---

# Deadline-Aware, Energy-Efficient Control of Domestic Immersion Hot Water Heaters
**arXiv**：[2601.18123v1](https://arxiv.org/abs/2601.18123) · [PDF](https://arxiv.org/pdf/2601.18123.pdf)  
**作者**：Muhammad Ibrahim Khan, Bivin Pradeep, James Brusey  

**一句话要点**：提出基于强化学习的截止时间感知控制方法，以优化家用浸入式热水器的能效。

**关键词**：强化学习, 能效优化, 截止时间感知控制, 家用热水器, PPO算法

## 3 点简述
- 核心问题：传统热水器在冬季连续运行，忽略需求窗口和热损失，导致能效低下。
- 方法要点：引入Gymnasium环境建模，比较时间最优bang-bang、零样本MCTS规划和PPO策略。
- 实验或效果：PPO在2小时截止时间下能耗最低，相比基线节省26%至69%能量。

## 摘要（原文）

> Typical domestic immersion water heater systems are often operated continuously during winter, heating quickly rather than efficiently and ignoring predictable demand windows and ambient losses. We study deadline-aware control, where the aim is to reach a target temperature at a specified time while minimising energy consumption. We introduce an efficient Gymnasium environment that models an immersion hot water heater with first-order thermal losses and discrete on and off actions of 0 W and 6000 W applied every 120 seconds. Methods include a time-optimal bang-bang baseline, a zero-shot Monte Carlo Tree Search planner, and a Proximal Policy Optimisation policy. We report total energy consumption in watt-hours under identical physical dynamics. Across sweeps of initial temperature from 10 to 30 degrees Celsius, deadline from 30 to 90 steps, and target temperature from 40 to 80 degrees Celsius, PPO achieves the most energy-efficient performance at a 60-step horizon of 2 hours, using 3.23 kilowatt-hours, compared to 4.37 to 10.45 kilowatt-hours for bang-bang control and 4.18 to 6.46 kilowatt-hours for MCTS. This corresponds to energy savings of 26 percent at 30 steps and 69 percent at 90 steps. In a representative trajectory with a 50 kg water mass, 20 degrees Celsius ambient temperature, and a 60 degrees Celsius target, PPO consumes 54 percent less energy than bang-bang control and 33 percent less than MCTS. These results show that learned deadline-aware control reduces energy consumption under identical physical assumptions, while planners provide partial savings without training and learned policies offer near-zero inference cost once trained.

