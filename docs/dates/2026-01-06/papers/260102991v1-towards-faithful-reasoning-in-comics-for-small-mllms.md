---
layout: default
title: Towards Faithful Reasoning in Comics for Small MLLMs
---

# Towards Faithful Reasoning in Comics for Small MLLMs
**arXiv**：[2601.02991v1](https://arxiv.org/abs/2601.02991) · [PDF](https://arxiv.org/pdf/2601.02991.pdf)  
**作者**：Chengcheng Feng, Haojie Yin, Yucheng Jin, Kaizhu Huang  

**一句话要点**：提出漫画推理框架以提升小规模多模态大语言模型在漫画视觉问答中的忠实推理能力

**关键词**：漫画视觉问答, 思维链提示, 强化微调, 小规模多模态大语言模型, 幽默理解, 抽象视觉推理

## 3 点简述
- 核心问题：标准思维链提示在漫画视觉问答中导致状态纠缠、虚假转移和探索低效，尤其影响小模型性能。
- 方法要点：结合模块化思维链生成、基于GRPO的强化微调和结构化奖励，设计漫画推理框架。
- 实验或效果：在五个基准测试中，3B模型超越现有方法，插件实验平均提升12.1%。

## 摘要（原文）

> Comic-based visual question answering (CVQA) poses distinct challenges to multimodal large language models (MLLMs) due to its reliance on symbolic abstraction, narrative logic, and humor, which differ from conventional VQA tasks. Although Chain-of-Thought (CoT) prompting is widely used to enhance MLLM reasoning, surprisingly, its direct application to CVQA often degrades performance, especially in small-scale models. Our theoretical and empirical analyses reveal that standard CoT in CVQA suffers from state entanglement, spurious transitions, and exploration inefficiency, with small models particularly vulnerable in resource-constrained settings. To address these issues, we propose a novel comic reasoning framework, designed to produce more faithful and transferable reasoning chains in small MLLMs. Specifically, our framework combines modular CoT generation with GRPO-based reinforcement fine-tuning and a novel structured reward. Beyond comic VQA, we further evaluate our approach on a broader class of humor-centric and abstract visual reasoning tasks, including meme understanding and editorial cartoon interpretation. Across five challenging benchmarks, our 3B model outperforms state-of-the-art methods, and plug-in experiments yield an additional average improvement of $\mathbf{12.1\%}$ across different MLLMs.

