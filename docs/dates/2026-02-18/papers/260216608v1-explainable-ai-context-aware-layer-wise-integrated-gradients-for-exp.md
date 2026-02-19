---
layout: default
title: Explainable AI: Context-Aware Layer-Wise Integrated Gradients for Explaining Transformer Models
---

# Explainable AI: Context-Aware Layer-Wise Integrated Gradients for Explaining Transformer Models
**arXiv**：[2602.16608v1](https://arxiv.org/abs/2602.16608) · [PDF](https://arxiv.org/pdf/2602.16608.pdf)  
**作者**：Melkamu Abay Mersha, Jugal Kalita  

**一句话要点**：提出上下文感知层间集成梯度框架以解释Transformer模型决策

**关键词**：可解释人工智能, Transformer模型, 层间归因, 上下文感知, 集成梯度, 注意力机制

## 3 点简述
- Transformer模型解释性不足，现有方法缺乏上下文感知和层间相关性追踪
- CA-LIG框架结合层间集成梯度和类别特定注意力梯度，生成带符号的上下文敏感归因图
- 在多种任务和模型上验证，CA-LIG提供更忠实、语义清晰的解释，优于现有方法

## 摘要（原文）

> Transformer models achieve state-of-the-art performance across domains and tasks, yet their deeply layered representations make their predictions difficult to interpret. Existing explainability methods rely on final-layer attributions, capture either local token-level attributions or global attention patterns without unification, and lack context-awareness of inter-token dependencies and structural components. They also fail to capture how relevance evolves across layers and how structural components shape decision-making. To address these limitations, we proposed the \textbf{Context-Aware Layer-wise Integrated Gradients (CA-LIG) Framework}, a unified hierarchical attribution framework that computes layer-wise Integrated Gradients within each Transformer block and fuses these token-level attributions with class-specific attention gradients. This integration yields signed, context-sensitive attribution maps that capture supportive and opposing evidence while tracing the hierarchical flow of relevance through the Transformer layers. We evaluate the CA-LIG Framework across diverse tasks, domains, and transformer model families, including sentiment analysis and long and multi-class document classification with BERT, hate speech detection in a low-resource language setting with XLM-R and AfroLM, and image classification with Masked Autoencoder vision Transformer model. Across all tasks and architectures, CA-LIG provides more faithful attributions, shows stronger sensitivity to contextual dependencies, and produces clearer, more semantically coherent visualizations than established explainability methods. These results indicate that CA-LIG provides a more comprehensive, context-aware, and reliable explanation of Transformer decision-making, advancing both the practical interpretability and conceptual understanding of deep neural models.

