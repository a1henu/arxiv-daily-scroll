---
layout: default
title: M$^3$Searcher: Modular Multimodal Information Seeking Agency with Retrieval-Oriented Reasoning
---

# M$^3$Searcher: Modular Multimodal Information Seeking Agency with Retrieval-Oriented Reasoning
**arXiv**：[2601.09278v1](https://arxiv.org/abs/2601.09278) · [PDF](https://arxiv.org/pdf/2601.09278.pdf)  
**作者**：Xiaohan Yu, Chao Feng, Lang Mei, Chong Chen  

**一句话要点**：提出M³Searcher模块化多模态信息搜索代理，以解决多模态工具使用中的专业化-泛化权衡和数据稀缺问题。

**关键词**：多模态信息搜索, 模块化代理, 检索导向推理, 多目标奖励优化, 多跳数据集

## 3 点简述
- 核心问题：现有自主信息搜索代理局限于文本模态，面临多模态工具使用的专业化-泛化权衡和训练数据稀缺挑战。
- 方法要点：通过模块化设计分离信息获取与答案推导，采用检索导向的多目标奖励优化，并开发MMSearchVQA数据集支持训练。
- 实验或效果：实验显示M³Searcher优于现有方法，在复杂多模态任务中表现出强迁移适应性和有效推理能力。

## 摘要（原文）

> Recent advances in DeepResearch-style agents have demonstrated strong capabilities in autonomous information acquisition and synthesize from real-world web environments. However, existing approaches remain fundamentally limited to text modality. Extending autonomous information-seeking agents to multimodal settings introduces critical challenges: the specialization-generalization trade-off that emerges when training models for multimodal tool-use at scale, and the severe scarcity of training data capturing complex, multi-step multimodal search trajectories. To address these challenges, we propose M$^3$Searcher, a modular multimodal information-seeking agent that explicitly decouples information acquisition from answer derivation. M$^3$Searcher is optimized with a retrieval-oriented multi-objective reward that jointly encourages factual accuracy, reasoning soundness, and retrieval fidelity. In addition, we develop MMSearchVQA, a multimodal multi-hop dataset to support retrieval centric RL training. Experimental results demonstrate that M$^3$Searcher outperforms existing approaches, exhibits strong transfer adaptability and effective reasoning in complex multimodal tasks.

