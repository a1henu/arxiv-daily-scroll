---
layout: default
title: MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Model for Embodied Task Planning
---

# MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Model for Embodied Task Planning
**arXiv**：[2512.16909v1](https://arxiv.org/abs/2512.16909) · [PDF](https://arxiv.org/pdf/2512.16909.pdf)  
**作者**：Yuanchen Ju, Yongyuan Liang, Yen-Jen Wang, Nandiraju Gireesh, Yuanliang Ju, Seungjae Lee, Qiao Gu, Elvis Hsieh, Furong Huang, Koushil Sreenath  

**一句话要点**：提出MomaGraph统一场景图表示，集成空间功能关系与部件交互，用于具身任务规划。

**关键词**：具身任务规划, 场景图表示, 视觉语言模型, 强化学习, 家庭环境数据集, 零样本规划

## 3 点简述
- 核心问题：现有场景图分离空间功能关系，忽略对象状态、时间更新和任务相关信息。
- 方法要点：引入MomaGraph统一表示，并贡献数据集MomaGraph-Scenes和评估套件MomaGraph-Bench。
- 实验或效果：训练模型MomaGraph-R1，在基准测试中达到71.6%准确率，优于基线并泛化到真实机器人实验。

## 摘要（原文）

> Mobile manipulators in households must both navigate and manipulate. This requires a compact, semantically rich scene representation that captures where objects are, how they function, and which parts are actionable. Scene graphs are a natural choice, yet prior work often separates spatial and functional relations, treats scenes as static snapshots without object states or temporal updates, and overlooks information most relevant for accomplishing the current task. To address these limitations, we introduce MomaGraph, a unified scene representation for embodied agents that integrates spatial-functional relationships and part-level interactive elements. However, advancing such a representation requires both suitable data and rigorous evaluation, which have been largely missing. We thus contribute MomaGraph-Scenes, the first large-scale dataset of richly annotated, task-driven scene graphs in household environments, along with MomaGraph-Bench, a systematic evaluation suite spanning six reasoning capabilities from high-level planning to fine-grained scene understanding. Built upon this foundation, we further develop MomaGraph-R1, a 7B vision-language model trained with reinforcement learning on MomaGraph-Scenes. MomaGraph-R1 predicts task-oriented scene graphs and serves as a zero-shot task planner under a Graph-then-Plan framework. Extensive experiments demonstrate that our model achieves state-of-the-art results among open-source models, reaching 71.6% accuracy on the benchmark (+11.4% over the best baseline), while generalizing across public benchmarks and transferring effectively to real-robot experiments.

