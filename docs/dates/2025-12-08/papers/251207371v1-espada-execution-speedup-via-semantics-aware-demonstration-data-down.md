---
layout: default
title: ESPADA: Execution Speedup via Semantics Aware Demonstration Data Downsampling for Imitation Learning
---

# ESPADA: Execution Speedup via Semantics Aware Demonstration Data Downsampling for Imitation Learning
**arXiv**：[2512.07371v1](https://arxiv.org/abs/2512.07371) · [PDF](https://arxiv.org/pdf/2512.07371.pdf)  
**作者**：Byungju Kim, Jinu Pahk, Chungwoo Lee, Jaejoon Kim, Jangha Lee, Theo Taeyeong Kim, Kyuhwan Shim, Jun Ki Lee, Byoung-Tak Zhang  

**一句话要点**：提出ESPADA框架，通过语义感知演示数据下采样加速模仿学习中的机器人控制。

**关键词**：模仿学习, 行为克隆, 数据下采样, 语义分割, 机器人控制, 动态时间规整

## 3 点简述
- 行为克隆策略继承人类演示的缓慢节奏，限制实际部署。
- ESPADA利用VLM-LLM管道和3D夹爪-物体关系进行语义分割，仅在非关键段进行激进下采样。
- 在模拟和真实实验中，ESPADA实现约2倍加速，同时保持成功率。

## 摘要（原文）

> Behavior-cloning based visuomotor policies enable precise manipulation but often inherit the slow, cautious tempo of human demonstrations, limiting practical deployment. However, prior studies on acceleration methods mainly rely on statistical or heuristic cues that ignore task semantics and can fail across diverse manipulation settings. We present ESPADA, a semantic and spatially aware framework that segments demonstrations using a VLM-LLM pipeline with 3D gripper-object relations, enabling aggressive downsampling only in non-critical segments while preserving precision-critical phases, without requiring extra data or architectural modifications, or any form of retraining. To scale from a single annotated episode to the full dataset, ESPADA propagates segment labels via Dynamic Time Warping (DTW) on dynamics-only features. Across both simulation and real-world experiments with ACT and DP baselines, ESPADA achieves approximately a 2x speed-up while maintaining success rates, narrowing the gap between human demonstrations and efficient robot control.

