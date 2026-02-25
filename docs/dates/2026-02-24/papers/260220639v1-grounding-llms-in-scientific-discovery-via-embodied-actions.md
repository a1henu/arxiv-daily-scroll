---
layout: default
title: Grounding LLMs in Scientific Discovery via Embodied Actions
---

# Grounding LLMs in Scientific Discovery via Embodied Actions
**arXiv**：[2602.20639v1](https://arxiv.org/abs/2602.20639) · [PDF](https://arxiv.org/pdf/2602.20639.pdf)  
**作者**：Bo Zhang, Jinfeng Zhou, Yuxuan Chen, Jianing Yin, Minlie Huang, Hongning Wang  

**一句话要点**：提出EmbodiedAct框架，通过具身动作将LLMs与科学软件结合，以解决模拟中的感知缺失问题。

**关键词**：大语言模型, 科学发现, 具身动作, 感知-执行循环, 物理模拟, 工程设计

## 3 点简述
- 核心问题：LLMs在科学发现中难以连接理论推理与可验证物理模拟，现有方法缺乏运行时感知。
- 方法要点：将科学软件转化为具身代理，通过紧密的感知-执行循环实现LLMs的具身动作。
- 实验或效果：在MATLAB中实例化，复杂任务上显著超越基线，提升模拟可靠性和建模准确性。

## 摘要（原文）

> Large Language Models (LLMs) have shown significant potential in scientific discovery but struggle to bridge the gap between theoretical reasoning and verifiable physical simulation. Existing solutions operate in a passive "execute-then-response" loop and thus lacks runtime perception, obscuring agents to transient anomalies (e.g., numerical instability or diverging oscillations). To address this limitation, we propose EmbodiedAct, a framework that transforms established scientific software into active embodied agents by grounding LLMs in embodied actions with a tight perception-execution loop. We instantiate EmbodiedAct within MATLAB and evaluate it on complex engineering design and scientific modeling tasks. Extensive experiments show that EmbodiedAct significantly outperforms existing baselines, achieving SOTA performance by ensuring satisfactory reliability and stability in long-horizon simulations and enhanced accuracy in scientific modeling.

