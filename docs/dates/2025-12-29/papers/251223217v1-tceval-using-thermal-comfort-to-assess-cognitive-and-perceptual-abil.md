---
layout: default
title: TCEval: Using Thermal Comfort to Assess Cognitive and Perceptual Abilities of AI
---

# TCEval: Using Thermal Comfort to Assess Cognitive and Perceptual Abilities of AI
**arXiv**：[2512.23217v1](https://arxiv.org/abs/2512.23217) · [PDF](https://arxiv.org/pdf/2512.23217.pdf)  
**作者**：Jingming Li  

**一句话要点**：提出TCEval框架，利用热舒适场景评估AI的认知与感知能力

**关键词**：热舒适评估, 认知能力测试, 跨模态推理, LLM代理, 生态效度

## 3 点简述
- 核心问题：现有LLM基准缺乏评估真实世界认知能力的任务特定测试
- 方法要点：通过热舒适场景初始化LLM代理，评估跨模态推理、因果关联和自适应决策
- 实验或效果：实验显示LLM在热舒适分类中表现接近随机，但跨模态推理有基础能力

## 摘要（原文）

> A critical gap exists in LLM task-specific benchmarks. Thermal comfort, a sophisticated interplay of environmental factors and personal perceptions involving sensory integration and adaptive decision-making, serves as an ideal paradigm for evaluating real-world cognitive capabilities of AI systems. To address this, we propose TCEval, the first evaluation framework that assesses three core cognitive capacities of AI, cross-modal reasoning, causal association, and adaptive decision-making, by leveraging thermal comfort scenarios and large language model (LLM) agents. The methodology involves initializing LLM agents with virtual personality attributes, guiding them to generate clothing insulation selections and thermal comfort feedback, and validating outputs against the ASHRAE Global Database and Chinese Thermal Comfort Database. Experiments on four LLMs show that while agent feedback has limited exact alignment with humans, directional consistency improves significantly with a 1 PMV tolerance. Statistical tests reveal that LLM-generated PMV distributions diverge markedly from human data, and agents perform near-randomly in discrete thermal comfort classification. These results confirm the feasibility of TCEval as an ecologically valid Cognitive Turing Test for AI, demonstrating that current LLMs possess foundational cross-modal reasoning ability but lack precise causal understanding of the nonlinear relationships between variables in thermal comfort. TCEval complements traditional benchmarks, shifting AI evaluation focus from abstract task proficiency to embodied, context-aware perception and decision-making, offering valuable insights for advancing AI in human-centric applications like smart buildings.

