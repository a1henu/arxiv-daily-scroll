---
layout: default
title: Scaling Embeddings Outperforms Scaling Experts in Language Models
---

# Scaling Embeddings Outperforms Scaling Experts in Language Models
**arXiv**：[2601.21204v1](https://arxiv.org/abs/2601.21204) · [PDF](https://arxiv.org/pdf/2601.21204.pdf)  
**作者**：Hong Liu, Jiaqi Zhang, Chao Wang, Xing Hu, Linkun Lyu, Jiaqi Sun, Xurui Yang, Bo Wang, Fengcun Li, Yulei Qian, Lingtong Si, Yerui Sun, Rumei Li, Peng Pei, Yuchen Xie, Xunliang Cai  

**一句话要点**：提出嵌入缩放作为稀疏扩展新维度，在特定场景下优于专家缩放，并实现推理加速。

**关键词**：嵌入缩放, 稀疏扩展, 专家混合, 推理加速, 语言模型架构

## 3 点简述
- 核心问题：MoE架构面临收益递减和系统瓶颈，需探索稀疏扩展新方法。
- 方法要点：通过嵌入缩放作为正交维度，系统分析关键架构因素如参数预算和模型宽深交互。
- 实验或效果：构建LongCat-Flash-Lite模型，超越参数等效MoE基线，在代理和编码领域表现优异。

## 摘要（原文）

> While Mixture-of-Experts (MoE) architectures have become the standard for sparsity scaling in large language models, they increasingly face diminishing returns and system-level bottlenecks. In this work, we explore embedding scaling as a potent, orthogonal dimension for scaling sparsity. Through a comprehensive analysis and experiments, we identify specific regimes where embedding scaling achieves a superior Pareto frontier compared to expert scaling. We systematically characterize the critical architectural factors governing this efficacy -- ranging from parameter budgeting to the interplay with model width and depth. Moreover, by integrating tailored system optimizations and speculative decoding, we effectively convert this sparsity into tangible inference speedups. Guided by these insights, we introduce LongCat-Flash-Lite, a 68.5B parameter model with ~3B activated trained from scratch. Despite allocating over 30B parameters to embeddings, LongCat-Flash-Lite not only surpasses parameter-equivalent MoE baselines but also exhibits exceptional competitiveness against existing models of comparable scale, particularly in agentic and coding domains.

