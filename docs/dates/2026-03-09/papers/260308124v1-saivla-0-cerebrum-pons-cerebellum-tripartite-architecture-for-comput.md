---
layout: default
title: SaiVLA-0: Cerebrum--Pons--Cerebellum Tripartite Architecture for Compute-Aware Vision-Language-Action
---

# SaiVLA-0: Cerebrum--Pons--Cerebellum Tripartite Architecture for Compute-Aware Vision-Language-Action
**arXiv**：[2603.08124v1](https://arxiv.org/abs/2603.08124) · [PDF](https://arxiv.org/pdf/2603.08124.pdf)  
**作者**：Xiang Shi, Wenlong Huang, Menglin Zou, Xinhai Sun  

**一句话要点**：提出SaiVLA-0三脑架构，通过模块化设计实现计算感知的视觉-语言-动作系统

**关键词**：视觉-语言-动作, 模块化架构, 计算感知, 在线控制, 特征缓存, 机器人学习

## 3 点简述
- 核心问题：传统视觉-语言-动作系统在计算效率和模块化方面存在不足，需要更稳定和可扩展的架构。
- 方法要点：采用大脑-脑桥-小脑三部分架构，大脑提供冻结的多模态先验，脑桥整合实时输入，小脑进行快速并行解码以实现在线控制。
- 实验或效果：初步实验显示，在LIBERO任务中，特征缓存减少训练时间并提高成功率，SaiVLA-0达到99.0%平均成功率。

## 摘要（原文）

> We revisit Vision-Language-Action through a neuroscience-inspired triad. Biologically, the Cerebrum provides stable high-level multimodal priors and remains frozen; the Pons Adapter integrates these cortical features with real-time proprioceptive inputs and compiles intent into execution-ready tokens; and the Cerebellum (ParaCAT) performs fast, parallel categorical decoding for online control, with hysteresis/EMA/temperature/entropy for stability. A fixed-ratio schedule and two-stage feature caching make the system compute-aware and reproducible. Inspired by active, foveated vision, our wrist ROIs are geometrically tied to the end-effector via calibrated projection, providing a movement-stabilized, high-resolution view that is sensitive to fine-grained pose changes and complements the global context of the main view.
>   The design is modular: upgrading the Cerebrum only retrains the Pons; changing robots only trains the Cerebellum; cerebellum-only RL can further refine control without touching high-level semantics. As a concept-and-protocol paper with preliminary evidence, we outline a timing protocol under matched conditions (GPU, resolution, batch) to verify anticipated efficiency gains. We also report preliminary LIBERO evidence showing that split feature caching reduces training time (7.5h to 4.5h) and improves average success (86.5% to 92.5%) under official N1.5 head-only training, and that SaiVLA0 reaches 99.0% mean success.

