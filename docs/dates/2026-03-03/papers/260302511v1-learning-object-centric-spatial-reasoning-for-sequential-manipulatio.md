---
layout: default
title: Learning Object-Centric Spatial Reasoning for Sequential Manipulation in Cluttered Environments
---

# Learning Object-Centric Spatial Reasoning for Sequential Manipulation in Cluttered Environments
**arXiv**：[2603.02511v1](https://arxiv.org/abs/2603.02511) · [PDF](https://arxiv.org/pdf/2603.02511.pdf)  
**作者**：Chrisantus Eze, Ryan C Julian, Christopher Crick  

**一句话要点**：提出Unveiler框架，通过解耦空间推理与动作执行，解决密集杂乱环境中机器人抓取目标物体的挑战。

**关键词**：机器人操作, 空间推理, 解耦架构, Transformer编码器, 密集杂乱环境, 零样本迁移

## 3 点简述
- 核心问题：密集杂乱环境中机器人抓取目标物体时，现有端到端模型数据效率低且模块性不足。
- 方法要点：采用轻量级Transformer空间关系编码器进行顺序障碍物识别，结合旋转不变动作解码器执行移除操作。
- 实验或效果：在模拟中部分遮挡场景成功率97.6%，完全遮挡场景90.0%，并实现零样本迁移到真实场景。

## 摘要（原文）

> Robotic manipulation in cluttered environments presents a critical challenge for automation. Recent large-scale, end-to-end models demonstrate impressive capabilities but often lack the data efficiency and modularity required for retrieving objects in dense clutter. In this work, we argue for a paradigm of specialized, decoupled systems and present Unveiler, a framework that explicitly separates high-level spatial reasoning from low-level action execution. Unveiler's core is a lightweight, transformer-based Spatial Relationship Encoder (SRE) that sequentially identifies the most critical obstacle for removal. This discrete decision is then passed to a rotation-invariant Action Decoder for execution. We demonstrate that this decoupled architecture is not only more computationally efficient in terms of parameter count and inference time, but also significantly outperforms both classic end-to-end policies and modern, large-model-based baselines in retrieving targets from dense clutter. The SRE is trained in two stages: imitation learning from heuristic demonstrations provides sample-efficient initialization, after which PPO fine-tuning enables the policy to discover removal strategies that surpass the heuristic in dense clutter. Our results, achieving up to 97.6\% success in partially occluded and 90.0\% in fully occluded scenarios in simulation, make a case for the power of specialized, object-centric reasoning in complex manipulation tasks. Additionally, we demonstrate that the SRE's spatial reasoning transfers zero-shot to real scenes, and validate the full system on a physical robot requiring only geometric workspace calibration; no learned components are retrained.

