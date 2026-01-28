---
layout: default
title: SETA: Statistical Fault Attribution for Compound AI Systems
---

# SETA: Statistical Fault Attribution for Compound AI Systems
**arXiv**：[2601.19337v1](https://arxiv.org/abs/2601.19337) · [PDF](https://arxiv.org/pdf/2601.19337.pdf)  
**作者**：Sayak Chowdhury, Meenakshi D'Souza  

**一句话要点**：提出SETA统计故障归因框架以解决复合AI系统鲁棒性测试难题

**关键词**：复合AI系统, 鲁棒性测试, 故障归因, 模块化框架, 错误传播分析

## 3 点简述
- 核心问题：现有鲁棒性测试技术针对单网络模型，难以扩展至多网络复合系统。
- 方法要点：采用模块化测试框架，支持组件级分析和错误传播推理，架构与模态无关。
- 实验或效果：应用于真实铁路巡检系统，实现超越端到端指标的细粒度鲁棒性分析。

## 摘要（原文）

> Modern AI systems increasingly comprise multiple interconnected neural networks to tackle complex inference tasks. Testing such systems for robustness and safety entails significant challenges. Current state-of-the-art robustness testing techniques, whether black-box or white-box, have been proposed and implemented for single-network models and do not scale well to multi-network pipelines. We propose a modular robustness testing framework that applies a given set of perturbations to test data. Our testing framework supports (1) a component-wise system analysis to isolate errors and (2) reasoning about error propagation across the neural network modules. The testing framework is architecture and modality agnostic and can be applied across domains. We apply the framework to a real-world autonomous rail inspection system composed of multiple deep networks and successfully demonstrate how our approach enables fine-grained robustness analysis beyond conventional end-to-end metrics.

