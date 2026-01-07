---
layout: default
title: Bridging Mechanistic Interpretability and Prompt Engineering with Gradient Ascent for Interpretable Persona Control
---

# Bridging Mechanistic Interpretability and Prompt Engineering with Gradient Ascent for Interpretable Persona Control
**arXiv**：[2601.02896v1](https://arxiv.org/abs/2601.02896) · [PDF](https://arxiv.org/pdf/2601.02896.pdf)  
**作者**：Harshvardhan Saini, Yiming Tang, Dianbo Liu  

**一句话要点**：提出基于梯度上升的框架以解决大语言模型行为角色可控性与可解释性问题

**关键词**：大语言模型, 行为控制, 梯度上升, 提示工程, 可解释性, AI安全

## 3 点简述
- 核心问题：控制大语言模型中的涌现行为角色（如奉承、幻觉）是AI安全的关键挑战，现有方法在可扩展性和可解释性上存在局限。
- 方法要点：提出RESGA和SAEGA方法，通过梯度上升优化随机初始化提示，结合流畅梯度上升控制提示流畅度，实现与目标角色方向的对齐。
- 实验或效果：在Llama 3.1、Qwen 2.5和Gemma 3模型上验证，针对奉承、幻觉和短视奖励角色，自动发现提示显著提升性能（如奉承从49.90%改善至79.24%）。

## 摘要（原文）

> Controlling emergent behavioral personas (e.g., sycophancy, hallucination) in Large Language Models (LLMs) is critical for AI safety, yet remains a persistent challenge. Existing solutions face a dilemma: manual prompt engineering is intuitive but unscalable and imprecise, while automatic optimization methods are effective but operate as "black boxes" with no interpretable connection to model internals. We propose a novel framework that adapts gradient ascent to LLMs, enabling targeted prompt discovery. In specific, we propose two methods, RESGA and SAEGA, that both optimize randomly initialized prompts to achieve better aligned representation with an identified persona direction. We introduce fluent gradient ascent to control the fluency of discovered persona steering prompts. We demonstrate RESGA and SAEGA's effectiveness across Llama 3.1, Qwen 2.5, and Gemma 3 for steering three different personas,sycophancy, hallucination, and myopic reward. Crucially, on sycophancy, our automatically discovered prompts achieve significant improvement (49.90% compared with 79.24%). By grounding prompt discovery in mechanistically meaningful features, our method offers a new paradigm for controllable and interpretable behavior modification.

