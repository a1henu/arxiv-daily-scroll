---
layout: default
title: Effect of Document Packing on the Latent Multi-Hop Reasoning Capabilities of Large Language Models
---

# Effect of Document Packing on the Latent Multi-Hop Reasoning Capabilities of Large Language Models
**arXiv**：[2512.14427v1](https://arxiv.org/abs/2512.14427) · [PDF](https://arxiv.org/pdf/2512.14427.pdf)  
**作者**：Gabriele Prato, Shagun Sodhani, Alessandro Sordoni, Sarath Chandar  

**一句话要点**：研究文档打包策略对大型语言模型潜在多跳推理能力的影响

**关键词**：文档打包, 多跳推理, 大型语言模型训练, 计算效率优化, 消融研究

## 3 点简述
- 核心问题：标准训练中多文档打包对模型能力的影响未知
- 方法要点：通过不同打包策略实验分析对多跳推理的影响
- 实验或效果：打包可提升性能但增加计算成本，消融研究揭示关键因素

## 摘要（原文）

> The standard practice for training large language models involves packing multiple documents together to optimize computational efficiency. However, the impact of this process on the models' capabilities remains largely unexplored. To address this gap, we investigate how different document-packing strategies influence the latent multi-hop reasoning abilities of LLMs. Our findings indicate that packing can improve model performance compared to training on individual documents, at the expense of more compute. To further understand the underlying mechanisms, we conduct an ablation study, identifying key factors that explain the advantages of packing. Ultimately, our research deepens the understanding of LLM training dynamics and provides practical insights for optimizing model development.

