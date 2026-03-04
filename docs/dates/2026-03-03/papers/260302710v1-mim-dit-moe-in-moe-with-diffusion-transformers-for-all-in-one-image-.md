---
layout: default
title: MiM-DiT: MoE in MoE with Diffusion Transformers for All-in-One Image Restoration
---

# MiM-DiT: MoE in MoE with Diffusion Transformers for All-in-One Image Restoration
**arXiv**：[2603.02710v1](https://arxiv.org/abs/2603.02710) · [PDF](https://arxiv.org/pdf/2603.02710.pdf)  
**作者**：Lingshun Kong, Jiawei Zhang, Zhengpeng Duan, Xiaohe Wu, Yueqi Yang, Xiaotao Wang, Dongqing Zou, Lei Lei, Jinshan Pan  

**一句话要点**：提出MiM-DiT框架，集成双层级MoE与扩散模型以解决全场景图像修复难题

**关键词**：图像修复, 混合专家, 扩散模型, 全场景处理, 自适应架构

## 3 点简述
- 核心问题：全场景图像修复需处理多种退化类型，单一模型难以有效应对。
- 方法要点：采用双层级MoE架构，Inter-MoE处理主要退化类型，Intra-MoE调整细粒度变化。
- 实验或效果：在多项任务上优于现有方法，实现高专业化修复。

## 摘要（原文）

> All-in-one image restoration is challenging because different degradation types, such as haze, blur, noise, and low-light, impose diverse requirements on restoration strategies, making it difficult for a single model to handle them effectively. In this paper, we propose a unified image restoration framework that integrates a dual-level Mixture-of-Experts (MoE) architecture with a pretrained diffusion model. The framework operates at two levels: the Inter-MoE layer adaptively combines expert groups to handle major degradation types, while the Intra-MoE layer further selects specialized sub-experts to address fine-grained variations within each type. This design enables the model to achieve coarse-grained adaptation across diverse degradation categories while performing fine-grained modulation for specific intra-class variations, ensuring both high specialization in handling complex, real-world corruptions. Extensive experiments demonstrate that the proposed method performs favorably against the state-of-the-art approaches on multiple image restoration task.

