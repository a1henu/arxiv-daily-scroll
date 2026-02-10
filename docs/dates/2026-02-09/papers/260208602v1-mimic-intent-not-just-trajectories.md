---
layout: default
title: Mimic Intent, Not Just Trajectories
---

# Mimic Intent, Not Just Trajectories
**arXiv**：[2602.08602v1](https://arxiv.org/abs/2602.08602) · [PDF](https://arxiv.org/pdf/2602.08602.pdf)  
**作者**：Renming Huang, Chendong Zeng, Wenjing Tang, Jingtian Cai, Cewu Lu, Panpan Cai  

**一句话要点**：提出MINT方法，通过解耦意图与执行细节，提升模仿学习在灵巧操作中的适应性与技能迁移能力。

**关键词**：模仿学习, 意图解耦, 多尺度分词, 技能迁移, 灵巧操作, 自回归生成

## 3 点简述
- 核心问题：现有模仿学习方法如VLA模型在环境变化适应和技能迁移方面表现不佳，源于仅模仿原始轨迹而未理解底层意图。
- 方法要点：采用多尺度频域分词技术，将动作块表示分解为意图令牌和执行令牌，实现意图与执行的解耦，并通过自回归生成进行渐进推理。
- 实验或效果：在多个操作基准测试和真实机器人上展示出最优成功率、高效推理、鲁棒泛化及有效的一击迁移能力。

## 摘要（原文）

> While imitation learning (IL) has achieved impressive success in dexterous manipulation through generative modeling and pretraining, state-of-the-art approaches like Vision-Language-Action (VLA) models still struggle with adaptation to environmental changes and skill transfer. We argue this stems from mimicking raw trajectories without understanding the underlying intent. To address this, we propose explicitly disentangling behavior intent from execution details in end-2-end IL: \textit{``Mimic Intent, Not just Trajectories'' (MINT)}. We achieve this via \textit{multi-scale frequency-space tokenization}, which enforces a spectral decomposition of action chunk representation. We learn action tokens with a multi-scale coarse-to-fine structure, and force the coarsest token to capture low-frequency global structure and finer tokens to encode high-frequency details. This yields an abstract \textit{Intent token} that facilitates planning and transfer, and multi-scale \textit{Execution tokens} that enable precise adaptation to environmental dynamics. Building on this hierarchy, our policy generates trajectories through \textit{next-scale autoregression}, performing progressive \textit{intent-to-execution reasoning}, thus boosting learning efficiency and generalization. Crucially, this disentanglement enables \textit{one-shot transfer} of skills, by simply injecting the Intent token from a demonstration into the autoregressive generation process. Experiments on several manipulation benchmarks and on a real robot demonstrate state-of-the-art success rates, superior inference efficiency, robust generalization against disturbances, and effective one-shot transfer.

