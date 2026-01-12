---
layout: default
title: ReasonAny: Incorporating Reasoning Capability to Any Model via Simple and Effective Model Merging
---

# ReasonAny: Incorporating Reasoning Capability to Any Model via Simple and Effective Model Merging
**arXiv**：[2601.05560v1](https://arxiv.org/abs/2601.05560) · [PDF](https://arxiv.org/pdf/2601.05560.pdf)  
**作者**：Junyao Yang, Chen Qian, Dongrui Liu, Wen Shen, Yong Liu, Jing Shao  

**一句话要点**：提出ReasonAny框架，通过对比梯度识别解决模型合并中的推理-领域性能崩溃问题

**关键词**：模型合并, 推理能力增强, 梯度敏感性分析, 领域适应, 训练免费方法

## 3 点简述
- 核心问题：现有模型合并方法在赋予领域模型推理能力时，常导致推理深度减弱和领域性能下降
- 方法要点：基于推理能力存在于低梯度敏感参数区域的发现，设计对比梯度识别机制进行模型合并
- 实验或效果：在安全、生物医学和金融领域验证，ReasonAny显著优于基线，保持稳健推理性能

## 摘要（原文）

> Large Reasoning Models (LRMs) with long chain-of-thought reasoning have recently achieved remarkable success. Yet, equipping domain-specialized models with such reasoning capabilities, referred to as "Reasoning + X", remains a significant challenge. While model merging offers a promising training-free solution, existing methods often suffer from a destructive performance collapse: existing methods tend to both weaken reasoning depth and compromise domain-specific utility. Interestingly, we identify a counter-intuitive phenomenon underlying this failure: reasoning ability predominantly resides in parameter regions with low gradient sensitivity, contrary to the common assumption that domain capabilities correspond to high-magnitude parameters. Motivated by this insight, we propose ReasonAny, a novel merging framework that resolves the reasoning-domain performance collapse through Contrastive Gradient Identification. Experiments across safety, biomedicine, and finance domains show that ReasonAny effectively synthesizes "Reasoning + X" capabilities, significantly outperforming state-of-the-art baselines while retaining robust reasoning performance.

