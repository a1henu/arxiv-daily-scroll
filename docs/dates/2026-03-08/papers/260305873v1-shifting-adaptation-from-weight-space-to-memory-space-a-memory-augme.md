---
layout: default
title: Shifting Adaptation from Weight Space to Memory Space: A Memory-Augmented Agent for Medical Image Segmentation
---

# Shifting Adaptation from Weight Space to Memory Space: A Memory-Augmented Agent for Medical Image Segmentation
**arXiv**：[2603.05873v1](https://arxiv.org/abs/2603.05873) · [PDF](https://arxiv.org/pdf/2603.05873.pdf)  
**作者**：Bowen Chen, Qiaohui Gao, Shaowen Wan, Shanhui Sun, Wei Liu, Xiang Li, Tianming Liu, Lin Zhao  

**一句话要点**：提出MemSeg-Agent，通过记忆空间适应解决医学图像分割的泛化与部署挑战。

**关键词**：医学图像分割, 记忆增强代理, 联邦学习, 测试时适应, 少样本学习, 泛化能力

## 3 点简述
- 核心问题：医学图像分割模型在跨机构、扫描仪或人群时泛化能力差，且联邦学习中微调通信开销大。
- 方法要点：基于固定骨干网络，利用轻量级静态、少样本和测试时工作记忆，通过智能控制器动态组合实现适应。
- 实验或效果：在四个公共数据集上验证，静态记忆匹配或超越强监督基线，测试时记忆进一步提升性能，减少通信开销。

## 摘要（原文）

> Medical image segmentation is fundamental to clinical workflows, yet models trained on a single dataset often fail to generalize across institutions, scanners, or patient populations. While vision foundation models have shown great promise in addressing this challenge, their deployment typically requires task-specific fine-tuning, which introduces substantial communication overhead in federated learning and prevents continuous knowledge evolution during deployment. In this work, we propose a memory-augmented segmentation agent (MemSeg-Agent) that shifts adaptation from weight space to memory space, enabling few-shot learning, federated supervised learning, and test-time adaptation within a unified architecture. MemSeg-Agent conditions a fixed backbone with lightweight static, few-shot, and test-time working memories, which are dynamically composed by an agentic controller. In federated settings, we update compact memory units instead of model parameters, substantially reducing communication overhead. Experiments on four public datasets demonstrate strong performance and robustness to domain shift: Static memory alone matches or surpasses strong supervised baselines with high parameter efficiency, and test-time working memory further improves in-domain and cross-domain performance without fine-tuning. Overall, MemSeg-Agent introduces a new paradigm for scalable and adaptive medical image segmentation in the era of agentic AI.

