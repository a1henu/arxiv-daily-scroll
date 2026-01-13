---
layout: default
title: GRPO with State Mutations: Improving LLM-Based Hardware Test Plan Generation
---

# GRPO with State Mutations: Improving LLM-Based Hardware Test Plan Generation
**arXiv**：[2601.07593v1](https://arxiv.org/abs/2601.07593) · [PDF](https://arxiv.org/pdf/2601.07593.pdf)  
**作者**：Dimple Vijay Kochar, Nathaniel Pinckney, Guan-Ting Liu, Chia-Tung Ho, Chenhui Deng, Haoxing Ren, Brucek Khailany  

**一句话要点**：提出GRPO-SMu训练方法以提升LLM在硬件测试计划生成中的推理能力

**关键词**：硬件测试计划生成, LLM推理能力, GRPO-SMu训练, RTL验证, 强化学习, 树状突变策略

## 3 点简述
- 核心问题：LLM在RTL验证刺激生成中成功率低，仅15.7-21.7%通过黄金设计测试
- 方法要点：结合监督微调与GRPO-SMu强化学习，采用树状分支突变策略增强探索
- 实验或效果：7B参数模型实现33.3%黄金测试通过率，比基线提升17.6%

## 摘要（原文）

> RTL design often relies heavily on ad-hoc testbench creation early in the design cycle. While large language models (LLMs) show promise for RTL code generation, their ability to reason about hardware specifications and generate targeted test plans remains largely unexplored. We present the first systematic study of LLM reasoning capabilities for RTL verification stimuli generation, establishing a two-stage framework that decomposes test plan generation from testbench execution. Our benchmark reveals that state-of-the-art models, including DeepSeek-R1 and Claude-4.0-Sonnet, achieve only 15.7-21.7% success rates on generating stimuli that pass golden RTL designs. To improve LLM generated stimuli, we develop a comprehensive training methodology combining supervised fine-tuning with a novel reinforcement learning approach, GRPO with State Mutation (GRPO-SMu), which enhances exploration by varying input mutations. Our approach leverages a tree-based branching mutation strategy to construct training data comprising equivalent and mutated trees, moving beyond linear mutation approaches to provide rich learning signals. Training on this curated dataset, our 7B parameter model achieves a 33.3% golden test pass rate and a 13.9% mutation detection rate, representing a 17.6% absolute improvement over baseline and outperforming much larger general-purpose models. These results demonstrate that specialized training methodologies can significantly enhance LLM reasoning capabilities for hardware verification tasks, establishing a foundation for automated sub-unit testing in semiconductor design workflows.

