---
layout: default
title: Learning Dexterous Manipulation Skills from Imperfect Simulations
---

# Learning Dexterous Manipulation Skills from Imperfect Simulations
**arXiv**：[2512.02011v1](https://arxiv.org/abs/2512.02011) · [PDF](https://arxiv.org/pdf/2512.02011.pdf)  
**作者**：Elvis Hsieh, Wen-Han Hsieh, Yen-Jen Wang, Toru Lin, Jitendra Malik, Koushil Sreenath, Haozhi Qi  

**一句话要点**：提出DexScrew框架，通过三阶段方法解决灵巧操作中模拟不完美问题，应用于螺母螺栓紧固和螺丝刀操作。

**关键词**：灵巧操作, 模拟到真实迁移, 强化学习, 触觉感知, 行为克隆, 多指手操作

## 3 点简述
- 核心问题：模拟复杂接触动力学和多感官信号（如触觉反馈）困难，限制灵巧操作的强化学习与模拟到真实迁移进展。
- 方法要点：三阶段框架：在简化模拟中训练策略，通过遥操作收集真实演示，结合触觉感知训练行为克隆策略。
- 实验或效果：相比直接模拟到真实迁移，任务进展比高，对未见物体形状和外部扰动具有鲁棒性能。

## 摘要（原文）

> Reinforcement learning and sim-to-real transfer have made significant progress in dexterous manipulation. However, progress remains limited by the difficulty of simulating complex contact dynamics and multisensory signals, especially tactile feedback. In this work, we propose \ours, a sim-to-real framework that addresses these limitations and demonstrates its effectiveness on nut-bolt fastening and screwdriving with multi-fingered hands. The framework has three stages. First, we train reinforcement learning policies in simulation using simplified object models that lead to the emergence of correct finger gaits. We then use the learned policy as a skill primitive within a teleoperation system to collect real-world demonstrations that contain tactile and proprioceptive information. Finally, we train a behavior cloning policy that incorporates tactile sensing and show that it generalizes to nuts and screwdrivers with diverse geometries. Experiments across both tasks show high task progress ratios compared to direct sim-to-real transfer and robust performance even on unseen object shapes and under external perturbations. Videos and code are available on https://dexscrew.github.io.

