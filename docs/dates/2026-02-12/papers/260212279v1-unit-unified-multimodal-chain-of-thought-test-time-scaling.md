---
layout: default
title: UniT: Unified Multimodal Chain-of-Thought Test-time Scaling
---

# UniT: Unified Multimodal Chain-of-Thought Test-time Scaling
**arXiv**：[2602.12279v1](https://arxiv.org/abs/2602.12279) · [PDF](https://arxiv.org/pdf/2602.12279.pdf)  
**作者**：Leon Liangyu Chen, Haoyu Ma, Zhipeng Fan, Ziqi Huang, Animesh Sinha, Xiaoliang Dai, Jialiang Wang, Zecheng He, Jianwei Yang, Chunyuan Li, Junzhe Sun, Chu Wang, Serena Yeung-Levy, Felix Juefei-Xu  

**一句话要点**：提出UniT框架以实现统一多模态模型的链式思维测试时扩展，解决复杂任务迭代推理问题。

**关键词**：多模态统一模型, 测试时扩展, 链式思维推理, 迭代推理, 视觉生成与理解, 代理数据合成

## 3 点简述
- 核心问题：统一多模态模型缺乏迭代推理能力，难以处理复杂空间组合或多对象交互任务。
- 方法要点：结合代理数据合成、统一模型训练和灵活测试时推理，支持验证、子目标分解和内容记忆。
- 实验或效果：训练短推理轨迹可泛化至长推理链，链式思维推理比并行采样更高效，提升分布外视觉推理。

## 摘要（原文）

> Unified models can handle both multimodal understanding and generation within a single architecture, yet they typically operate in a single pass without iteratively refining their outputs. Many multimodal tasks, especially those involving complex spatial compositions, multiple interacting objects, or evolving instructions, require decomposing instructions, verifying intermediate results, and making iterative corrections. While test-time scaling (TTS) has demonstrated that allocating additional inference compute for iterative reasoning substantially improves language model performance, extending this paradigm to unified multimodal models remains an open challenge. We introduce UniT, a framework for multimodal chain-of-thought test-time scaling that enables a single unified model to reason, verify, and refine across multiple rounds. UniT combines agentic data synthesis, unified model training, and flexible test-time inference to elicit cognitive behaviors including verification, subgoal decomposition, and content memory. Our key findings are: (1) unified models trained on short reasoning trajectories generalize to longer inference chains at test time; (2) sequential chain-of-thought reasoning provides a more scalable and compute-efficient TTS strategy than parallel sampling; (3) training on generation and editing trajectories improves out-of-distribution visual reasoning. These results establish multimodal test-time scaling as an effective paradigm for advancing both generation and understanding in unified models.

