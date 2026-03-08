---
layout: default
title: TimeWarp: Evaluating Web Agents by Revisiting the Past
---

# TimeWarp: Evaluating Web Agents by Revisiting the Past
**arXiv**：[2603.04949v1](https://arxiv.org/abs/2603.04949) · [PDF](https://arxiv.org/pdf/2603.04949.pdf)  
**作者**：Md Farhan Ishmam, Kenneth Marino  

**一句话要点**：提出TimeWarp基准和TimeTraj算法以提升Web代理在网页变化中的鲁棒性

**关键词**：Web代理评估, 网页演化模拟, 计划蒸馏, 行为克隆, 鲁棒性提升, 容器化环境

## 3 点简述
- 核心问题：当前Web代理在网页UI、设计和布局变化时性能下降，现有基准无法评估泛化能力。
- 方法要点：引入TimeWarp基准模拟网页演化，提出TimeTraj算法通过计划蒸馏跨多版本收集轨迹。
- 实验或效果：实验显示代理对变化敏感，TimeTraj显著提升性能，如Qwen-3 4B从20.4%提升至37.7%。

## 摘要（原文）

> The improvement of web agents on current benchmarks raises the question: Do today's agents perform just as well when the web changes? We introduce TimeWarp, a benchmark that emulates the evolving web using containerized environments that vary in UI, design, and layout. TimeWarp consists of three web environments, each with six UI versions spanning different eras of the internet, paired with a set of complex, realistic tasks requiring different forms of web navigation. Our experiments reveal web agents' vulnerability to changes and the limitations of behavior cloning (BC) on single-version trajectories. To address this, we propose TimeTraj, a simple yet effective algorithm that uses plan distillation to collect trajectories across multiple versions. By training agents on teacher rollouts using our BC-variant, we achieve substantial performance gains: $20.4\%\rightarrow37.7\%$ for Qwen-3 4B and $0\%\rightarrow27.0\%$ for Llama-3.1 8B models. We hope our work helps researchers study generalization across web designs and unlock a new paradigm for collecting plans rather than trajectories, thereby improving the robustness of web agents.

