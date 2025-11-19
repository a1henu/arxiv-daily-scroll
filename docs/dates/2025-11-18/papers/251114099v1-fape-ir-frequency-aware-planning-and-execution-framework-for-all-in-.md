---
layout: default
title: FAPE-IR: Frequency-Aware Planning and Execution Framework for All-in-One Image Restoration
---

# FAPE-IR: Frequency-Aware Planning and Execution Framework for All-in-One Image Restoration
**arXiv**：[2511.14099v1](https://arxiv.org/abs/2511.14099) · [PDF](https://arxiv.org/pdf/2511.14099.pdf)  
**作者**：Jingren Liu, Shuning Xu, Qirui Yang, Yun Wang, Xiangyu Chen, Zhong Ji  

**一句话要点**：提出FAPE-IR框架，通过频率感知规划与执行解决多退化图像恢复问题

**关键词**：图像恢复, 频率感知, 多模态大语言模型, 混合专家, 扩散模型, 零样本泛化

## 3 点简述
- 现有方法依赖任务特定设计，难以适应真实世界多种退化场景
- 使用冻结MLLM生成频率感知计划，指导LoRA-MoE模块动态选择专家
- 实验显示在七项任务中达到SOTA，并具有零样本泛化能力

## 摘要（原文）

> All-in-One Image Restoration (AIO-IR) aims to develop a unified model that can handle multiple degradations under complex conditions. However, existing methods often rely on task-specific designs or latent routing strategies, making it hard to adapt to real-world scenarios with various degradations. We propose FAPE-IR, a Frequency-Aware Planning and Execution framework for image restoration. It uses a frozen Multimodal Large Language Model (MLLM) as a planner to analyze degraded images and generate concise, frequency-aware restoration plans. These plans guide a LoRA-based Mixture-of-Experts (LoRA-MoE) module within a diffusion-based executor, which dynamically selects high- or low-frequency experts, complemented by frequency features of the input image. To further improve restoration quality and reduce artifacts, we introduce adversarial training and a frequency regularization loss. By coupling semantic planning with frequency-based restoration, FAPE-IR offers a unified and interpretable solution for all-in-one image restoration. Extensive experiments show that FAPE-IR achieves state-of-the-art performance across seven restoration tasks and exhibits strong zero-shot generalization under mixed degradations.

