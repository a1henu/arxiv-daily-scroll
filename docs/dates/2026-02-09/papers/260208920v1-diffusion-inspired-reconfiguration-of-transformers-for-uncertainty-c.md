---
layout: default
title: Diffusion-Inspired Reconfiguration of Transformers for Uncertainty Calibration
---

# Diffusion-Inspired Reconfiguration of Transformers for Uncertainty Calibration
**arXiv**：[2602.08920v1](https://arxiv.org/abs/2602.08920) · [PDF](https://arxiv.org/pdf/2602.08920.pdf)  
**作者**：Manh Cuong Dao, Quang Hung Pham, Phi Le Nguyen, Thao Nguyen Truong, Bryan Kian Hsiang Low, Trong Nghia Hoang  

**一句话要点**：提出扩散启发的Transformer重构方法，以解决预训练模型在风险敏感应用中的不确定性校准问题。

**关键词**：不确定性校准, Transformer重构, 扩散过程, 概率映射, 风险敏感应用, 预训练模型

## 3 点简述
- 核心问题：预训练Transformer缺乏不确定性在特征变换堆栈中的传播机制，影响风险敏感部署的可靠性。
- 方法要点：将每个特征变换块建模为概率映射，组合成类似扩散过程的概率路径，通过统一转移模型重新编译以实现不确定性传播。
- 实验或效果：在多种视觉和语言基准测试中，该方法在保持预测性能的同时，实现了优于现有不确定性感知Transformer的校准和预测准确性。

## 摘要（原文）

> Uncertainty calibration in pre-trained transformers is critical for their reliable deployment in risk-sensitive applications. Yet, most existing pre-trained transformers do not have a principled mechanism for uncertainty propagation through their feature transformation stack. In this work, we propose a diffusion-inspired reconfiguration of transformers in which each feature transformation block is modeled as a probabilistic mapping. Composing these probabilistic mappings reveals a probability path that mimics the structure of a diffusion process, transporting data mass from the input distribution to the pre-trained feature distribution. This probability path can then be recompiled on a diffusion process with a unified transition model to enable principled propagation of representation uncertainty throughout the pre-trained model's architecture while maintaining its original predictive performance. Empirical results across a variety of vision and language benchmarks demonstrate that our method achieves superior calibration and predictive accuracy compared to existing uncertainty-aware transformers.

