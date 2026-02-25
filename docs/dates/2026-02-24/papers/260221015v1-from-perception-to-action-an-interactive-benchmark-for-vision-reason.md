---
layout: default
title: From Perception to Action: An Interactive Benchmark for Vision Reasoning
---

# From Perception to Action: An Interactive Benchmark for Vision Reasoning
**arXiv**：[2602.21015v1](https://arxiv.org/abs/2602.21015) · [PDF](https://arxiv.org/pdf/2602.21015.pdf)  
**作者**：Yuhao Wu, Maojia Song, Yihuai Lan, Lei Wang, Zhiqiang Hu, Yao Xiao, Heng Zhou, Weihua Zheng, Dylan Raharja, Soujanya Poria, Roy Ka-Wei Lee  

**一句话要点**：提出CHAIN基准以评估模型在物理约束下的交互式视觉推理能力

**关键词**：视觉语言模型, 物理推理, 交互式基准, 长时程规划, 3D视觉

## 3 点简述
- 现有VLM评估集中于结构无关的单轮任务，无法评估物理结构理解
- CHAIN是交互式3D物理驱动基准，涵盖机械拼图和堆叠等任务
- 实验显示顶级模型在长时程规划和动作执行方面仍存在困难

## 摘要（原文）

> Understanding the physical structure is essential for real-world applications such as embodied agents, interactive design, and long-horizon manipulation. Yet, prevailing Vision-Language Model (VLM) evaluations still center on structure-agnostic, single-turn setups (e.g., VQA), which fail to assess agents' ability to reason about how geometry, contact, and support relations jointly constrain what actions are possible in a dynamic environment. To address this gap, we introduce the Causal Hierarchy of Actions and Interactions (CHAIN) benchmark, an interactive 3D, physics-driven testbed designed to evaluate whether models can understand, plan, and execute structured action sequences grounded in physical constraints. CHAIN shifts evaluation from passive perception to active problem solving, spanning tasks such as interlocking mechanical puzzles and 3D stacking and packing. We conduct a comprehensive study of state-of-the-art VLMs and diffusion-based models under unified interactive settings. Our results show that top-performing models still struggle to internalize physical structure and causal constraints, often failing to produce reliable long-horizon plans and cannot robustly translate perceived structure into effective actions. The project is available at https://social-ai-studio.github.io/CHAIN/.

