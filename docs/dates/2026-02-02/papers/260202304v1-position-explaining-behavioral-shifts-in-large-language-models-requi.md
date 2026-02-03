---
layout: default
title: Position: Explaining Behavioral Shifts in Large Language Models Requires a Comparative Approach
---

# Position: Explaining Behavioral Shifts in Large Language Models Requires a Comparative Approach
**arXiv**：[2602.02304v1](https://arxiv.org/abs/2602.02304) · [PDF](https://arxiv.org/pdf/2602.02304.pdf)  
**作者**：Martino Ciaperoni, Marzio Di Vece, Luca Pappalardo, Fosca Giannotti, Francesco Giannini  

**一句话要点**：提出比较性可解释AI框架以解释大语言模型的行为偏移

**关键词**：行为偏移, 可解释AI, 大语言模型, 比较分析, 模型干预

## 3 点简述
- 核心问题：大模型行为偏移的解释被忽视，传统XAI方法不适用于跨检查点比较
- 方法要点：引入Δ-XAI框架，强调比较参考模型与干预模型间的内部变化
- 实验或效果：设计Δ-XAI实验管道，关联框架需求，提供具体应用示例

## 摘要（原文）

> Large-scale foundation models exhibit behavioral shifts: intervention-induced behavioral changes that appear after scaling, fine-tuning, reinforcement learning or in-context learning. While investigating these phenomena have recently received attention, explaining their appearance is still overlooked. Classic explainable AI (XAI) methods can surface failures at a single checkpoint of a model, but they are structurally ill-suited to justify what changed internally across different checkpoints and which explanatory claims are warranted about that change. We take the position that behavioral shifts should be explained comparatively: the core target should be the intervention-induced shift between a reference model and an intervened model, rather than any single model in isolation. To this aim we formulate a Comparative XAI ($Δ$-XAI) framework with a set of desiderata to be taken into account when designing proper explaining methods. To highlight how $Δ$-XAI methods work, we introduce a set of possible pipelines, relate them to the desiderata, and provide a concrete $Δ$-XAI experiment.

