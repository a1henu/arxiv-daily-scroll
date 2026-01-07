---
layout: default
title: Grad-ELLM: Gradient-based Explanations for Decoder-only LLMs
---

# Grad-ELLM: Gradient-based Explanations for Decoder-only LLMs
**arXiv**：[2601.03089v1](https://arxiv.org/abs/2601.03089) · [PDF](https://arxiv.org/pdf/2601.03089.pdf)  
**作者**：Xin Huang, Antoni B. Chan  

**一句话要点**：提出Grad-ELLM以解决解码器专用LLM的梯度解释问题，提升归因忠实度。

**关键词**：梯度归因, 解码器专用LLM, 注意力机制, 忠实度评估, Transformer解释

## 3 点简述
- 核心问题：现有输入归因方法对Transformer架构不专注，导致LLM解释忠实度有限。
- 方法要点：基于梯度聚合注意力层通道重要性和注意力图空间重要性，生成热图无需修改架构。
- 实验或效果：在情感分类、问答和开放生成任务中，Grad-ELLM比其他方法表现更忠实。

## 摘要（原文）

> Large Language Models (LLMs) have demonstrated remarkable capabilities across diverse tasks, yet their black-box nature raises concerns about transparency and faithfulness. Input attribution methods aim to highlight each input token's contributions to the model's output, but existing approaches are typically model-agnostic, and do not focus on transformer-specific architectures, leading to limited faithfulness. To address this, we propose Grad-ELLM, a gradient-based attribution method for decoder-only transformer-based LLMs. By aggregating channel importance from gradients of the output logit with respect to attention layers and spatial importance from attention maps, Grad-ELLM generates heatmaps at each generation step without requiring architectural modifications. Additionally, we introduce two faithfulneses metrics $π$-Soft-NC and $π$-Soft-NS, which are modifications of Soft-NC/NS that provide fairer comparisons by controlling the amount of information kept when perturbing the text. We evaluate Grad-ELLM on sentiment classification, question answering, and open-generation tasks using different models. Experiment results show that Grad-ELLM consistently achieves superior faithfulness than other attribution methods.

