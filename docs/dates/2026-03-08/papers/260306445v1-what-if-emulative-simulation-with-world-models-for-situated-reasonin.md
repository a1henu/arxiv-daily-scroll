---
layout: default
title: What if? Emulative Simulation with World Models for Situated Reasoning
---

# What if? Emulative Simulation with World Models for Situated Reasoning
**arXiv**：[2603.06445v1](https://arxiv.org/abs/2603.06445) · [PDF](https://arxiv.org/pdf/2603.06445.pdf)  
**作者**：Ruiping Liu, Yufan Chen, Yuheng Zhang, Junwei Zheng, Kunyu Peng, Chengzhi Wu, Chenguang Huang, Di Wen, Jiaming Zhang, Kailun Yang, Rainer Stiefelhagen  

**一句话要点**：提出WanderDream数据集以支持无主动探索的情境推理，通过世界模型进行模拟探索

**关键词**：情境推理, 世界模型, 模拟探索, 全景视频数据集, 空间问答

## 3 点简述
- 核心问题：在物理限制或安全顾虑下，如何基于有限观察进行情境推理，回答空间假设问题
- 方法要点：构建大规模数据集WanderDream，包含全景视频和问答对，用于模拟心理探索轨迹
- 实验或效果：世界模型在数据集上表现优异，模拟探索显著提升推理能力，数据可迁移至真实场景

## 摘要（原文）

> Situated reasoning often relies on active exploration, yet in many real-world scenarios such exploration is infeasible due to physical constraints of robots or safety concerns of visually impaired users. Given only a limited observation, can an agent mentally simulate a future trajectory toward a target situation and answer spatial what-if questions? We introduce WanderDream, the first large-scale dataset designed for the emulative simulation of mental exploration, enabling models to reason without active exploration. WanderDream-Gen comprises 15.8K panoramic videos across 1,088 real scenes from HM3D, ScanNet++, and real-world captures, depicting imagined trajectories from current viewpoints to target situations. WanderDream-QA contains 158K question-answer pairs, covering starting states, paths, and end states along each trajectory to comprehensively evaluate exploration-based reasoning. Extensive experiments with world models and MLLMs demonstrate (1) that mental exploration is essential for situated reasoning, (2) that world models achieve compelling performance on WanderDream-Gen, (3) that imagination substantially facilitates reasoning on WanderDream-QA, and (4) that WanderDream data exhibit remarkable transferability to real-world scenarios. The source code and all data will be released.

