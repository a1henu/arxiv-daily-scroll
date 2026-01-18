---
layout: default
title: Beyond Single Prompts: Synergistic Fusion and Arrangement for VICL
---

# Beyond Single Prompts: Synergistic Fusion and Arrangement for VICL
**arXiv**：[2601.10117v1](https://arxiv.org/abs/2601.10117) · [PDF](https://arxiv.org/pdf/2601.10117.pdf)  
**作者**：Wenwen Liao, Jianbo Yu, Yuansong Wang, Shifu Yan, Xiaofeng Yang  

**一句话要点**：提出融合与排列协同的端到端VICL框架，以解决多提示互补性和结构化信息利用不足的问题。

**关键词**：视觉上下文学习, 提示融合, 排列解耦, 双向微调, 跨任务泛化

## 3 点简述
- 核心问题：现有VICL方法仅选择最相似提示，忽略其他高质量提示的互补线索，且未利用不同提示排列的结构化信息。
- 方法要点：通过自适应融合模块聚合多提示关键模式，并引入排列特定轻量MLP解耦布局先验，结合双向微调机制增强协作。
- 实验或效果：在分割、检测和着色任务上展示优越结果和强跨任务泛化能力。

## 摘要（原文）

> Vision In-Context Learning (VICL) enables inpainting models to quickly adapt to new visual tasks from only a few prompts. However, existing methods suffer from two key issues: (1) selecting only the most similar prompt discards complementary cues from other high-quality prompts; and (2) failing to exploit the structured information implied by different prompt arrangements.
>   We propose an end-to-end VICL framework to overcome these limitations. Firstly, an adaptive Fusion Module aggregates critical patterns and annotations from multiple prompts to form more precise contextual prompts. Secondly, we introduce arrangement-specific lightweight MLPs to decouple layout priors from the core model, while minimally affecting the overall model. In addition, an bidirectional fine-tuning mechanism swaps the roles of query and prompt, encouraging the model to reconstruct the original prompt from fused context and thus enhancing collaboration between the fusion module and the inpainting model. Experiments on foreground segmentation, single-object detection, and image colorization demonstrate superior results and strong cross-task generalization of our method.

