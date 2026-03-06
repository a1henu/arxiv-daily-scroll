---
layout: default
title: Interactive Benchmarks
---

# Interactive Benchmarks
**arXiv**：[2603.04737v1](https://arxiv.org/abs/2603.04737) · [PDF](https://arxiv.org/pdf/2603.04737.pdf)  
**作者**：Baoqing Yue, Zihan Zhu, Yifan Zhang, Jichen Feng, Hufei Yang, Mengdi Wang  

**一句话要点**：提出交互式基准以评估模型在预算约束下的主动信息获取与推理能力

**关键词**：交互式评估, 主动推理, 基准测试, 逻辑证明, 策略游戏, 模型智能

## 3 点简述
- 核心问题：标准基准因饱和、主观性和泛化差而不可靠，需评估模型主动获取信息的能力
- 方法要点：建立统一评估范式，通过交互过程在逻辑数学和策略游戏中测试模型推理
- 实验或效果：结果显示交互基准能稳健评估模型智能，揭示交互场景仍有较大改进空间

## 摘要（原文）

> Standard benchmarks have become increasingly unreliable due to saturation, subjectivity, and poor generalization. We argue that evaluating model's ability to acquire information actively is important to assess model's intelligence. We propose Interactive Benchmarks, a unified evaluation paradigm that assesses model's reasoning ability in an interactive process under budget constraints. We instantiate this framework across two settings: Interactive Proofs, where models interact with a judge to deduce objective truths or answers in logic and mathematics; and Interactive Games, where models reason strategically to maximize long-horizon utilities. Our results show that interactive benchmarks provide a robust and faithful assessment of model intelligence, revealing that there is still substantial room to improve in interactive scenarios. Project page: https://github.com/interactivebench/interactivebench

