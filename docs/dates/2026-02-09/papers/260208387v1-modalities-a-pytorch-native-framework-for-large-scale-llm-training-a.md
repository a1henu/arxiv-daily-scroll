---
layout: default
title: Modalities, a PyTorch-native Framework For Large-scale LLM Training and Research
---

# Modalities, a PyTorch-native Framework For Large-scale LLM Training and Research
**arXiv**：[2602.08387v1](https://arxiv.org/abs/2602.08387) · [PDF](https://arxiv.org/pdf/2602.08387.pdf)  
**作者**：Max Lübbering, Timm Ruland, Richard Rutmann, Felix Stollenwerk, David Fitzek, Michael Fromm, Alexander Weber, Rafet Sifa, Nicolas Flores-Herr, Joachim Köhler, Mehdi Ali  

**一句话要点**：提出Modalities框架以解决大规模LLM训练与研究中系统化消融实验工具不足的问题

**关键词**：大规模语言模型训练, 消融实验框架, PyTorch原生框架, 并行化策略, 模块化设计, 可复现性

## 3 点简述
- 核心问题：现有开源框架在大规模消融实验上工具有限，导致高计算成本下需自定义脚本
- 方法要点：集成先进并行化策略，支持万亿token和十亿参数规模的高效预训练与系统消融
- 实验或效果：采用模块化设计和声明式配置，提升可复现性和可扩展性，优于现有框架

## 摘要（原文）

> Today's LLM (pre-) training and research workflows typically allocate a significant amount of compute to large-scale ablation studies. Despite the substantial compute costs of these ablations, existing open-source frameworks provide limited tooling for these experiments, often forcing researchers to write their own wrappers and scripts. We propose Modalities, an end-to-end PyTorch-native framework that integrates data-driven LLM research with large-scale model training from two angles. Firstly, by integrating state-of-the-art parallelization strategies, it enables both efficient pretraining and systematic ablations at trillion-token and billion-parameter scale. Secondly, Modalities adopts modular design with declarative, self-contained configuration, enabling reproducibility and extensibility levels that are difficult to achieve out-of-the-box with existing LLM training frameworks.

