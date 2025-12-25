---
layout: default
title: Embodied AI-Enhanced IoMT Edge Computing: UAV Trajectory Optimization and Task Offloading with Mobility Prediction
---

# Embodied AI-Enhanced IoMT Edge Computing: UAV Trajectory Optimization and Task Offloading with Mobility Prediction
**arXiv**：[2512.20902v1](https://arxiv.org/abs/2512.20902) · [PDF](https://arxiv.org/pdf/2512.20902.pdf)  
**作者**：Siqi Mu, Shuo Wen, Yang Lu, Ruihong Jiang, Bo Ai  

**一句话要点**：提出基于Transformer轨迹预测与DRL的UAV轨迹优化与任务卸载方法，以最小化IoMT中WBAN用户加权平均任务完成时间。

**关键词**：无人机轨迹优化, 任务卸载, 移动性预测, 深度强化学习, Transformer模型, 医疗物联网

## 3 点简述
- 研究UAV在IoMT中为WBAN用户提供边缘计算服务时，动态任务卸载与轨迹优化问题，考虑用户任务关键性变化与双移动性。
- 建立具身AI增强框架，包括基于Transformer的用户轨迹预测模型和集成预测的DRL算法，以智能优化UAV飞行与卸载决策。
- 使用真实移动轨迹和仿真验证方法优于现有基准，具体性能提升未知。

## 摘要（原文）

> Due to their inherent flexibility and autonomous operation, unmanned aerial vehicles (UAVs) have been widely used in Internet of Medical Things (IoMT) to provide real-time biomedical edge computing service for wireless body area network (WBAN) users. In this paper, considering the time-varying task criticality characteristics of diverse WBAN users and the dual mobility between WBAN users and UAV, we investigate the dynamic task offloading and UAV flight trajectory optimization problem to minimize the weighted average task completion time of all the WBAN users, under the constraint of UAV energy consumption. To tackle the problem, an embodied AI-enhanced IoMT edge computing framework is established. Specifically, we propose a novel hierarchical multi-scale Transformer-based user trajectory prediction model based on the users' historical trajectory traces captured by the embodied AI agent (i.e., UAV). Afterwards, a prediction-enhanced deep reinforcement learning (DRL) algorithm that integrates predicted users' mobility information is designed for intelligently optimizing UAV flight trajectory and task offloading decisions. Real-word movement traces and simulation results demonstrate the superiority of the proposed methods in comparison with the existing benchmarks.

