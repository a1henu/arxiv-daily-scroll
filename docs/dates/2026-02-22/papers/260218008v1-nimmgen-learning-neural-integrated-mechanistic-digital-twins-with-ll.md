---
layout: default
title: NIMMGen: Learning Neural-Integrated Mechanistic Digital Twins with LLMs
---

# NIMMGen: Learning Neural-Integrated Mechanistic Digital Twins with LLMs
**arXiv**：[2602.18008v1](https://arxiv.org/abs/2602.18008) · [PDF](https://arxiv.org/pdf/2602.18008.pdf)  
**作者**：Zihan Guan, Rituparna Datta, Mengxuan Hu, Shunshun Liu, Aiying Zhang, Prasanna Balachandran, Sheng Li, Anil Vullikanti  

**一句话要点**：提出NIMMGen框架以增强LLM生成机理模型在现实场景下的可靠性与有效性

**关键词**：机理建模, 大语言模型, 代理框架, 迭代精炼, 反事实模拟

## 3 点简述
- 核心问题：现有LLM生成机理模型在部分观测和多样化任务下可靠性未知，存在模型有效性和代码正确性挑战
- 方法要点：设计NIMMGen代理框架，通过迭代精炼提升代码正确性和实际有效性，集成神经与机理建模
- 实验或效果：在三个多样化科学领域数据集上验证性能，学习模型支持反事实干预模拟

## 摘要（原文）

> Mechanistic models encode scientific knowledge about dynamical systems and are widely used in downstream scientific and policy applications. Recent work has explored LLM-based agentic frameworks to automatically construct mechanistic models from data; however, existing problem settings substantially oversimplify real-world conditions, leaving it unclear whether LLM-generated mechanistic models are reliable in practice. To address this gap, we introduce the Neural-Integrated Mechanistic Modeling (NIMM) evaluation framework, which evaluates LLM-generated mechanistic models under realistic settings with partial observations and diversified task objectives. Our evaluation reveals fundamental challenges in current baselines, ranging from model effectiveness to code-level correctness. Motivated by these findings, we design NIMMgen, an agentic framework for neural-integrated mechanistic modeling that enhances code correctness and practical validity through iterative refinement. Experiments across three datasets from diversified scientific domains demonstrate its strong performance. We also show that the learned mechanistic models support counterfactual intervention simulation.

