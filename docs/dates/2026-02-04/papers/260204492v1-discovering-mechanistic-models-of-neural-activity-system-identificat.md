---
layout: default
title: Discovering Mechanistic Models of Neural Activity: System Identification in an in Silico Zebrafish
---

# Discovering Mechanistic Models of Neural Activity: System Identification in an in Silico Zebrafish
**arXiv**：[2602.04492v1](https://arxiv.org/abs/2602.04492) · [PDF](https://arxiv.org/pdf/2602.04492.pdf)  
**作者**：Jan-Matthis Lueckmann, Viren Jain, Michał Januszewski  

**一句话要点**：提出基于LLM树搜索的模型发现方法，在斑马鱼神经模拟中验证系统识别性能。

**关键词**：神经回路建模, 系统识别, LLM树搜索, 斑马鱼模拟, 结构先验, 泛化性能

## 3 点简述
- 核心问题：神经回路机制模型验证缺乏真实基准，限制模型发现。
- 方法要点：利用斑马鱼神经机械模拟作为透明基准，结合LLM树搜索自主发现预测模型。
- 实验或效果：模型显著优于基线，结构先验对泛化和可解释性至关重要。

## 摘要（原文）

> Constructing mechanistic models of neural circuits is a fundamental goal of neuroscience, yet verifying such models is limited by the lack of ground truth. To rigorously test model discovery, we establish an in silico testbed using neuromechanical simulations of a larval zebrafish as a transparent ground truth. We find that LLM-based tree search autonomously discovers predictive models that significantly outperform established forecasting baselines. Conditioning on sensory drive is necessary but not sufficient for faithful system identification, as models exploit statistical shortcuts. Structural priors prove essential for enabling robust out-of-distribution generalization and recovery of interpretable mechanistic models. Our insights provide guidance for modeling real-world neural recordings and offer a broader template for AI-driven scientific discovery.

