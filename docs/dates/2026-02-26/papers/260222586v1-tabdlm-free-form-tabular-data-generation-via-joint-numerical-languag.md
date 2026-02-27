---
layout: default
title: TabDLM: Free-Form Tabular Data Generation via Joint Numerical-Language Diffusion
---

# TabDLM: Free-Form Tabular Data Generation via Joint Numerical-Language Diffusion
**arXiv**：[2602.22586v1](https://arxiv.org/abs/2602.22586) · [PDF](https://arxiv.org/pdf/2602.22586.pdf)  
**作者**：Donghong Cai, Jiarui Feng, Yanbo Wang, Da Zheng, Yixin Chen, Muhan Zhang  

**一句话要点**：提出TabDLM，通过联合数值-语言扩散模型生成自由格式表格数据

**关键词**：表格数据生成, 扩散模型, 多模态建模, 掩码扩散语言模型, 数值-语言联合建模

## 3 点简述
- 核心问题：现有方法难以联合建模表格中的数值、分类和自由文本字段，导致文本质量差或数值失真。
- 方法要点：基于掩码扩散语言模型，用掩码扩散处理文本和分类特征，连续扩散处理数值特征，通过双向注意力捕获跨模态交互。
- 实验或效果：在多样化基准测试中，TabDLM相比基于扩散和LLM的基线方法表现出有效性。

## 摘要（原文）

> Synthetic tabular data generation has attracted growing attention due to its importance for data augmentation, foundation models, and privacy. However, real-world tabular datasets increasingly contain free-form text fields (e.g., reviews or clinical notes) alongside structured numerical and categorical attributes. Generating such heterogeneous tables with joint modeling of different modalities remains challenging. Existing approaches broadly fall into two categories: diffusion-based methods and LLM-based methods. Diffusion models can capture complex dependencies over numerical and categorical features in continuous or discrete spaces, but extending them to open-ended text is nontrivial and often leads to degraded text quality. In contrast, LLM-based generators naturally produce fluent text, yet their discrete tokenization can distort precise or wide-range numerical values, hindering accurate modeling of both numbers and language. In this work, we propose TabDLM, a unified framework for free-form tabular data generation via a joint numerical--language diffusion model built on masked diffusion language models (MDLMs). TabDLM models textual and categorical features through masked diffusion, while modeling numerical features with a continuous diffusion process through learned specialized numeric tokens embedding; bidirectional attention then captures cross-modality interactions within a single model. Extensive experiments on diverse benchmarks demonstrate the effectiveness of TabDLM compared to strong diffusion- and LLM-based baselines.

