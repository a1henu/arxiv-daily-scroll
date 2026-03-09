---
layout: default
title: Unified Learning of Temporal Task Structure and Action Timing for Bimanual Robot Manipulation
---

# Unified Learning of Temporal Task Structure and Action Timing for Bimanual Robot Manipulation
**arXiv**：[2603.06538v1](https://arxiv.org/abs/2603.06538) · [PDF](https://arxiv.org/pdf/2603.06538.pdf)  
**作者**：Christian Dreher, Patrick Dormanns, Andre Meixner, Tamim Asfour  

**一句话要点**：提出统一学习符号与子符号时间约束的方法，以生成双手机器人操作的可执行参数化计划。

**关键词**：双手机器人操作, 时间任务结构, 符号与子符号学习, 高斯混合模型, DPLL算法, 参数化计划生成

## 3 点简述
- 核心问题：现有方法分离高层任务规划与低层运动同步，导致双手机器人操作中时间结构学习不足。
- 方法要点：基于高斯混合模型表示子符号时间关系，使用DPLL算法分配Allen关系以识别任务模式，结合优化规划生成参数化计划。
- 实验或效果：在多个数据集上评估，生成计划比基准更接近人类演示，验证了方法的有效性。

## 摘要（原文）

> Temporal task structure is fundamental for bimanual manipulation: a robot must not only know that one action precedes or overlaps another, but also when each action should occur and how long it should take. While symbolic temporal relations enable high-level reasoning about task structure and alternative execution sequences, concrete timing parameters are equally essential for coordinating two hands at the execution level. Existing approaches address these two levels in isolation, leaving a gap between high-level task planning and low-level movement synchronization. This work presents an approach for learning both symbolic and subsymbolic temporal task constraints from human demonstrations and deriving executable, temporally parametrized plans for bimanual manipulation. Our contributions are (i) a 3-dimensional representation of timings between two actions with methods based on multivariate Gaussian Mixture Models to represent temporal relationships between actions on a subsymbolic level, (ii) a method based on the Davis-Putnam-Logemann-Loveland (DPLL) algorithm that finds and ranks all contradiction-free assignments of Allen relations to action pairs, representing different modes of a task, and (iii) an optimization-based planning system that combines the identified symbolic and subsymbolic temporal task constraints to derive temporally parametrized plans for robot execution. We evaluate our approach on several datasets, demonstrating that our method generates temporally parametrized plans closer to human demonstrations than the most characteristic demonstration baseline.

