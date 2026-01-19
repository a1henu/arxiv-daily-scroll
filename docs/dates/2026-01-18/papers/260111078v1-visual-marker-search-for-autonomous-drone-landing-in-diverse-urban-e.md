---
layout: default
title: Visual Marker Search for Autonomous Drone Landing in Diverse Urban Environments
---

# Visual Marker Search for Autonomous Drone Landing in Diverse Urban Environments
**arXiv**：[2601.11078v1](https://arxiv.org/abs/2601.11078) · [PDF](https://arxiv.org/pdf/2601.11078.pdf)  
**作者**：Jiaohong Yao, Linfeng Liang, Yao Deng, Xi Zheng, Richard Han, Yuankai Qi  

**一句话要点**：提出基于模拟的评估套件，分析无人机在复杂城市环境中视觉标记着陆的鲁棒性。

**关键词**：无人机着陆, 视觉标记, 模拟评估, 城市环境, 强化学习, 传感器性能

## 3 点简述
- 核心问题：现有标记着陆方法在复杂城市环境中的鲁棒性不足，受限于理想化假设。
- 方法要点：在AirSim平台上构建模拟评估套件，系统变化城市布局、光照和天气条件。
- 实验或效果：比较启发式覆盖模式和强化学习代理，评估成功率、路径效率和鲁棒性。

## 摘要（原文）

> Marker-based landing is widely used in drone delivery and return-to-base systems for its simplicity and reliability. However, most approaches assume idealized landing site visibility and sensor performance, limiting robustness in complex urban settings. We present a simulation-based evaluation suite on the AirSim platform with systematically varied urban layouts, lighting, and weather to replicate realistic operational diversity. Using onboard camera sensors (RGB for marker detection and depth for obstacle avoidance), we benchmark two heuristic coverage patterns and a reinforcement learning-based agent, analyzing how exploration strategy and scene complexity affect success rate, path efficiency, and robustness. Results underscore the need to evaluate marker-based autonomous landing under diverse, sensor-relevant conditions to guide the development of reliable aerial navigation systems.

