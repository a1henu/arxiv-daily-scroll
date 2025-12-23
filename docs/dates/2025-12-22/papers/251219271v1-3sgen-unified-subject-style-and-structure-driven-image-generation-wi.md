---
layout: default
title: 3SGen: Unified Subject, Style, and Structure-Driven Image Generation with Adaptive Task-specific Memory
---

# 3SGen: Unified Subject, Style, and Structure-Driven Image Generation with Adaptive Task-specific Memory
**arXiv**：[2512.19271v1](https://arxiv.org/abs/2512.19271) · [PDF](https://arxiv.org/pdf/2512.19271.pdf)  
**作者**：Xinyang Song, Libin Wang, Weining Wang, Zhiwei Li, Jianxin Sun, Dandan Zheng, Jingdong Chen, Qi Li, Zhenan Sun  

**一句话要点**：提出3SGen框架以统一解决图像生成中主题、风格和结构驱动的条件控制问题

**关键词**：图像生成, 条件控制, 自适应记忆, 多模态学习, 基准评估

## 3 点简述
- 核心问题：现有方法孤立处理主题、风格和结构条件，导致特征纠缠和任务可迁移性有限
- 方法要点：采用自适应任务特定记忆模块动态解耦、存储和检索条件先验，结合MLLM和VAE分支
- 实验或效果：在3SGen-Bench等基准上展示跨任务保真度和可控性的优越性能

## 摘要（原文）

> Recent image generation approaches often address subject, style, and structure-driven conditioning in isolation, leading to feature entanglement and limited task transferability. In this paper, we introduce 3SGen, a task-aware unified framework that performs all three conditioning modes within a single model. 3SGen employs an MLLM equipped with learnable semantic queries to align text-image semantics, complemented by a VAE branch that preserves fine-grained visual details. At its core, an Adaptive Task-specific Memory (ATM) module dynamically disentangles, stores, and retrieves condition-specific priors, such as identity for subjects, textures for styles, and spatial layouts for structures, via a lightweight gating mechanism along with several scalable memory items. This design mitigates inter-task interference and naturally scales to compositional inputs. In addition, we propose 3SGen-Bench, a unified image-driven generation benchmark with standardized metrics for evaluating cross-task fidelity and controllability. Extensive experiments on our proposed 3SGen-Bench and other public benchmarks demonstrate our superior performance across diverse image-driven generation tasks.

