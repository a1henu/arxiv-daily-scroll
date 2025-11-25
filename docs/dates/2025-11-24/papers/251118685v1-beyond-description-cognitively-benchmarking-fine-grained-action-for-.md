---
layout: default
title: Beyond Description: Cognitively Benchmarking Fine-Grained Action for Embodied Agents
---

# Beyond Description: Cognitively Benchmarking Fine-Grained Action for Embodied Agents
**arXiv**：[2511.18685v1](https://arxiv.org/abs/2511.18685) · [PDF](https://arxiv.org/pdf/2511.18685.pdf)  
**作者**：Dayong Liu, Chao Xu, Weihong Chen, Suyu Zhang, Juncheng Wang, Jiankang Deng, Baigui Sun, Yang Liu  

**一句话要点**：提出CFG-Bench基准以评估具身代理的细粒度动作认知能力

**关键词**：具身代理, 细粒度动作, 多模态基准, 认知能力评估, 监督微调

## 3 点简述
- 现有基准忽视细粒度动作智能，聚焦高层规划或空间推理
- 构建多模态问答对，评估物理交互、时序因果、意图理解和评价判断
- 实验显示MLLMs在细粒度动作生成和高阶推理方面存在显著局限

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) show promising results as decision-making engines for embodied agents operating in complex, physical environments. However, existing benchmarks often prioritize high-level planning or spatial reasoning, leaving the fine-grained action intelligence required for embodied physical interaction underexplored. To address this gap, we introduce CFG-Bench, a new benchmark designed to systematically evaluate this crucial capability. CFG-Bench consists of 1,368 curated videos paired with 19,562 three-modalities question-answer pairs targeting four cognitive abilities: 1) Physical Interaction, 2) Temporal-Causal Relation, 3) Intentional Understanding, and 4) Evaluative Judgment. Together, these dimensions provide a systematic framework for assessing a model's ability to translate visual observations into actionable knowledge, moving beyond mere surface-level recognition. Our comprehensive evaluation on CFG-Bench reveals that leading MLLMs struggle to produce detailed instructions for physical interactions and exhibit profound limitations in the higher-order reasoning of intention and evaluation. Moreover, supervised fine-tuning (SFT) on our data demonstrates that teaching an MLLMs to articulate fine-grained actions directly translates to significant performance gains on established embodied benchmarks. Our analysis highlights these limitations and offers insights for developing more capable and grounded embodied agents.

