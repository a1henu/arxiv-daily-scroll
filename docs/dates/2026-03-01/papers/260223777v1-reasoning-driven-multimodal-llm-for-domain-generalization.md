---
layout: default
title: Reasoning-Driven Multimodal LLM for Domain Generalization
---

# Reasoning-Driven Multimodal LLM for Domain Generalization
**arXiv**：[2602.23777v1](https://arxiv.org/abs/2602.23777) · [PDF](https://arxiv.org/pdf/2602.23777.pdf)  
**作者**：Zhipeng Xu, Zilong Wang, Xinyang Jiang, Dongsheng Li, De Cheng, Nannan Wang  

**一句话要点**：提出RD-MLDG框架，利用多模态大语言模型的推理能力解决领域泛化问题。

**关键词**：领域泛化, 多模态大语言模型, 推理链, 跨域鲁棒性, 自对齐正则化

## 3 点简述
- 核心问题：领域泛化中视觉特征不变性方法有限，需探索推理链以提升跨域鲁棒性。
- 方法要点：结合MTCT和SARR组件，通过多任务交叉训练和自对齐推理正则化优化推理监督。
- 实验或效果：在DomainBed数据集上实现最先进性能，验证推理作为补充信号的有效性。

## 摘要（原文）

> This paper addresses the domain generalization (DG) problem in deep learning. While most DG methods focus on enforcing visual feature invariance, we leverage the reasoning capability of multimodal large language models (MLLMs) and explore the potential of constructing reasoning chains that derives image categories to achieve more robust predictions under domain shift. To this end, we systematically study the role of reasoning in DG using DomainBed-Reasoning, a newly constructed extension of DomainBed dataset, in which each sample is paired with class-relevant reasoning chains. Our analysis reveals two key challenges: (i) fine-tuning MLLMs with reasoning chains for classification is more challenging than direct label supervision, since the model must optimize complex reasoning sequences before label prediction; and (ii) mismatches in reasoning patterns between supervision signals and fine-tuned MLLMs lead to a trade-off between semantic richness (informative but harder to optimize) and optimization efficiency (easier to optimize but less informative). To address these issues, we propose RD-MLDG (Reasoning-Driven Multimodal LLM for Domain Generalization), a framework with two components: (i) MTCT (Multi-Task Cross-Training), which introduces an additional direct classification pathway to guide reasoning supervision; and (ii) SARR (Self-Aligned Reasoning Regularization), which preserves the semantic richness of reasoning chains while mitigating reasoning-pattern mismatches via iterative self-labeling. Experiments on standard DomainBed datasets (PACS, VLCS, OfficeHome, TerraInc) demonstrate that RD-MLDG achieves state-of-the-art performances, highlighting reasoning as a promising complementary signal for robust out-of-domain generalization.

