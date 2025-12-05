---
layout: default
title: MARL Warehouse Robots
---

# MARL Warehouse Robots
**arXiv**：[2512.04463v1](https://arxiv.org/abs/2512.04463) · [PDF](https://arxiv.org/pdf/2512.04463.pdf)  
**作者**：Price Allman, Lian Thang, Dre Simmons, Salmon Riaz  

**一句话要点**：比较QMIX与IPPO在仓库机器人协同任务中的性能，展示QMIX通过价值分解显著优于独立学习。

**关键词**：多智能体强化学习, 仓库机器人, 价值分解, 稀疏奖励, Unity仿真, 算法比较

## 3 点简述
- 研究多智能体强化学习在仓库机器人协同搬运中的应用，聚焦QMIX和IPPO算法对比。
- 实验表明QMIX在稀疏奖励环境下通过价值分解实现更高回报，但需大量超参数调优。
- 在Unity ML-Agents中成功部署，小规模机器人（2-4台）能稳定交付包裹，但扩展性面临挑战。

## 摘要（原文）

> We present a comparative study of multi-agent reinforcement learning (MARL) algorithms for cooperative warehouse robotics. We evaluate QMIX and IPPO on the Robotic Warehouse (RWARE) environment and a custom Unity 3D simulation. Our experiments reveal that QMIX's value decomposition significantly outperforms independent learning approaches (achieving 3.25 mean return vs. 0.38 for advanced IPPO), but requires extensive hyperparameter tuning -- particularly extended epsilon annealing (5M+ steps) for sparse reward discovery. We demonstrate successful deployment in Unity ML-Agents, achieving consistent package delivery after 1M training steps. While MARL shows promise for small-scale deployments (2-4 robots), significant scaling challenges remain. Code and analyses: https://pallman14.github.io/MARL-QMIX-Warehouse-Robots/

