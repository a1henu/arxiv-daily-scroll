---
layout: default
title: Contextual Safety Reasoning and Grounding for Open-World Robots
---

# Contextual Safety Reasoning and Grounding for Open-World Robots
**arXiv**：[2602.19983v1](https://arxiv.org/abs/2602.19983) · [PDF](https://arxiv.org/pdf/2602.19983.pdf)  
**作者**：Zachary Ravichadran, David Snyder, Alexander Robey, Hamed Hassani, Vijay Kumar, George J. Pappas  

**一句话要点**：提出CORE框架，通过视觉语言模型实现开放世界机器人的上下文安全推理与落地

**关键词**：开放世界机器人, 上下文安全推理, 视觉语言模型, 控制屏障函数, 概率安全保证

## 3 点简述
- 核心问题：传统安全方法在开放世界环境中无法处理上下文变化，依赖先验知识。
- 方法要点：使用VLM从视觉观察在线推理上下文安全规则，并通过控制屏障函数落地执行。
- 实验或效果：在未见环境中实现上下文适当行为，提供概率安全保证，优于现有语义安全方法。

## 摘要（原文）

> Robots are increasingly operating in open-world environments where safe behavior depends on context: the same hallway may require different navigation strategies when crowded versus empty, or during an emergency versus normal operations. Traditional safety approaches enforce fixed constraints in user-specified contexts, limiting their ability to handle the open-ended contextual variability of real-world deployment. We address this gap via CORE, a safety framework that enables online contextual reasoning, grounding, and enforcement without prior knowledge of the environment (e.g., maps or safety specifications). CORE uses a vision-language model (VLM) to continuously reason about context-dependent safety rules directly from visual observations, grounds these rules in the physical environment, and enforces the resulting spatially-defined safe sets via control barrier functions. We provide probabilistic safety guarantees for CORE that account for perceptual uncertainty, and we demonstrate through simulation and real-world experiments that CORE enforces contextually appropriate behavior in unseen environments, significantly outperforming prior semantic safety methods that lack online contextual reasoning. Ablation studies validate our theoretical guarantees and underscore the importance of both VLM-based reasoning and spatial grounding for enforcing contextual safety in novel settings. We provide additional resources at https://zacravichandran.github.io/CORE.

