---
layout: default
title: Democratising Clinical AI through Dataset Condensation for Classical Clinical Models
---

# Democratising Clinical AI through Dataset Condensation for Classical Clinical Models
**arXiv**：[2603.09356v1](https://arxiv.org/abs/2603.09356) · [PDF](https://arxiv.org/pdf/2603.09356.pdf)  
**作者**：Anshul Thakur, Soheila Molaei, Pafue Christy Nganjimi, Joshua Fieggen, Andrew A. S. Soltan, Danielle Belgrave, Lei Clifton, David A. Clifton  

**一句话要点**：提出基于零阶优化的数据集压缩方法，以支持非可微临床模型的数据民主化与隐私保护。

**关键词**：数据集压缩, 临床模型, 差分隐私, 零阶优化, 数据民主化, 非可微模型

## 3 点简述
- 核心问题：现有数据集压缩方法依赖可微神经网络，不兼容决策树等广泛使用的非可微临床模型。
- 方法要点：采用差分隐私的零阶优化框架，仅通过函数评估扩展数据集压缩至非可微模型。
- 实验或效果：在六个数据集上验证，压缩数据集能保持模型效用并提供有效差分隐私保证。

## 摘要（原文）

> Dataset condensation (DC) learns a compact synthetic dataset that enables models to match the performance of full-data training, prioritising utility over distributional fidelity. While typically explored for computational efficiency, DC also holds promise for healthcare data democratisation, especially when paired with differential privacy, allowing synthetic data to serve as a safe alternative to real records. However, existing DC methods rely on differentiable neural networks, limiting their compatibility with widely used clinical models such as decision trees and Cox regression. We address this gap using a differentially private, zero-order optimisation framework that extends DC to non-differentiable models using only function evaluations. Empirical results across six datasets, including both classification and survival tasks, show that the proposed method produces condensed datasets that preserve model utility while providing effective differential privacy guarantees - enabling model-agnostic data sharing for clinical prediction tasks without exposing sensitive patient information.

