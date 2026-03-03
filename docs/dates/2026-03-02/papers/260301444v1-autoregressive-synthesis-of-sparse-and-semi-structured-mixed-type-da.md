---
layout: default
title: Autoregressive Synthesis of Sparse and Semi-Structured Mixed-Type Data
---

# Autoregressive Synthesis of Sparse and Semi-Structured Mixed-Type Data
**arXiv**：[2603.01444v1](https://arxiv.org/abs/2603.01444) · [PDF](https://arxiv.org/pdf/2603.01444.pdf)  
**作者**：Thomas Rückstieß, Robin Vujanic  

**一句话要点**：提出Origami自回归Transformer架构，以原生生成稀疏半结构化混合类型数据

**关键词**：稀疏数据合成, 半结构化数据, 自回归Transformer, 数据令牌化, 隐私保护合成

## 3 点简述
- 核心问题：现有合成方法假设密集固定模式表格数据，不适用于稀疏半结构化数据如JSON，需扁平化处理但扩展性差。
- 方法要点：Origami将数据记录（包括嵌套对象和变长数组）标记化为键、值和结构令牌序列，无需扁平化或插补。
- 实验或效果：在保真度、实用性和检测指标上优于GAN、VAE、扩散和自回归基线，隐私得分高，在稀疏度达38%的数据集上保持高保真合成。

## 摘要（原文）

> Synthetic data generation is a critical capability for data sharing, privacy compliance, system benchmarking and test data provisioning. Existing methods assume dense, fixed-schema tabular data, yet this assumption is increasingly at odds with modern data systems - from document databases, REST APIs to data lakes - which store and exchange data in sparse, semi-structured formats like JSON. Applying existing tabular methods to such data requires flattening of nested data into wide, sparse tables which scales poorly. We present Origami, an autoregressive transformer-based architecture that tokenizes data records, including nested objects and variable length arrays, into sequences of key, value and structural tokens. This representation natively handles sparsity, mixed types and hierarchical structure without flattening or imputation. Origami outperforms baselines spanning GAN, VAE, diffusion and autoregressive architectures on fidelity, utility and detection metrics across nearly all settings, while maintaining high privacy scores. On semi-structured datasets with up to 38% sparsity, baseline synthesizers either fail to scale or degrade substantially, while Origami maintains high-fidelity synthesis that is harder to distinguish from real data. To the best of our knowledge, Origami is the first architecture capable of natively modeling and generating semi-structured data end-to-end.

