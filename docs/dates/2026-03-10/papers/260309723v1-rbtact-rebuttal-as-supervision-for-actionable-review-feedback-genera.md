---
layout: default
title: RbtAct: Rebuttal as Supervision for Actionable Review Feedback Generation
---

# RbtAct: Rebuttal as Supervision for Actionable Review Feedback Generation
**arXiv**：[2603.09723v1](https://arxiv.org/abs/2603.09723) · [PDF](https://arxiv.org/pdf/2603.09723.pdf)  
**作者**：Sihong Wu, Yiling Ma, Yilun Zhao, Tiansheng Hu, Owen Jiang, Manasi Patwardhan, Arman Cohan  

**一句话要点**：提出RbtAct方法，利用反驳作为监督信号，优化AI生成同行评审反馈的可操作性

**关键词**：同行评审反馈生成, 可操作性优化, 反驳监督学习, 视角条件生成, Llama模型微调

## 3 点简述
- 核心问题：AI生成的同行评审反馈常缺乏可操作性，无法提供具体指导。
- 方法要点：利用反驳作为隐式监督，训练模型生成基于视角的聚焦评论。
- 实验或效果：通过人类专家和LLM评估，在可操作性和特异性上优于基线模型。

## 摘要（原文）

> Large language models (LLMs) are increasingly used across the scientific workflow, including to draft peer-review reports. However, many AI-generated reviews are superficial and insufficiently actionable, leaving authors without concrete, implementable guidance and motivating the gap this work addresses. We propose RbtAct, which targets actionable review feedback generation and places existing peer review rebuttal at the center of learning. Rebuttals show which reviewer comments led to concrete revisions or specific plans, and which were only defended. Building on this insight, we leverage rebuttal as implicit supervision to directly optimize a feedback generator for actionability. To support this objective, we propose a new task called perspective-conditioned segment-level review feedback generation, in which the model is required to produce a single focused comment based on the complete paper and a specified perspective such as experiments and writing. We also build a large dataset named RMR-75K that maps review segments to the rebuttal segments that address them, with perspective labels and impact categories that order author uptake. We then train the Llama-3.1-8B-Instruct model with supervised fine-tuning on review segments followed by preference optimization using rebuttal derived pairs. Experiments with human experts and LLM-as-a-judge show consistent gains in actionability and specificity over strong baselines while maintaining grounding and relevance.

