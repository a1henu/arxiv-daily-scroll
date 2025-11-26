---
layout: default
title: WPT: World-to-Policy Transfer via Online World Model Distillation
---

# WPT: World-to-Policy Transfer via Online World Model Distillation
**arXiv**：[2511.20095v1](https://arxiv.org/abs/2511.20095) · [PDF](https://arxiv.org/pdf/2511.20095.pdf)  
**作者**：Guangfeng Jiang, Yueru Luo, Jun Liu, Yi Huang, Yiyao Zhu, Zhan Qu, Dave Zhenyu Chen, Bingbing Liu, Xu Yan  

**一句话要点**：提出WPT训练范式，通过在线世界模型蒸馏提升策略性能与推理速度。

**关键词**：世界模型, 策略蒸馏, 在线蒸馏, 奖励模型, 推理加速

## 3 点简述
- 现有世界模型存在运行时耦合或依赖离线奖励，导致推理开销大或优化困难。
- WPT使用可训练奖励模型和策略蒸馏，将世界知识转移到轻量学生策略。
- 实验显示WPT在开环和闭环基准上实现SOTA性能，推理速度提升4.9倍。

## 摘要（原文）

> Recent years have witnessed remarkable progress in world models, which primarily aim to capture the spatio-temporal correlations between an agent's actions and the evolving environment. However, existing approaches often suffer from tight runtime coupling or depend on offline reward signals, resulting in substantial inference overhead or hindering end-to-end optimization. To overcome these limitations, we introduce WPT, a World-to-Policy Transfer training paradigm that enables online distillation under the guidance of an end-to-end world model. Specifically, we develop a trainable reward model that infuses world knowledge into a teacher policy by aligning candidate trajectories with the future dynamics predicted by the world model. Subsequently, we propose policy distillation and world reward distillation to transfer the teacher's reasoning ability into a lightweight student policy, enhancing planning performance while preserving real-time deployability. Extensive experiments on both open-loop and closed-loop benchmarks show that our WPT achieves state-of-the-art performance with a simple policy architecture: it attains a 0.11 collision rate (open-loop) and achieves a 79.23 driving score (closed-loop) surpassing both world-model-based and imitation-learning methods in accuracy and safety. Moreover, the student sustains up to 4.9x faster inference, while retaining most of the gains.

