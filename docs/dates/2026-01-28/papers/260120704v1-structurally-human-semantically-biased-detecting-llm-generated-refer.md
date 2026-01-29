---
layout: default
title: Structurally Human, Semantically Biased: Detecting LLM-Generated References with Embeddings and GNNs
---

# Structurally Human, Semantically Biased: Detecting LLM-Generated References with Embeddings and GNNs
**arXiv**：[2601.20704v1](https://arxiv.org/abs/2601.20704) · [PDF](https://arxiv.org/pdf/2601.20704.pdf)  
**作者**：Melika Mobini, Vincent Holst, Floriano Tori, Andres Algaba, Vincent Ginis  

**一句话要点**：提出基于嵌入和图神经网络的检测方法，以区分LLM生成与人类撰写的参考文献列表。

**关键词**：LLM生成检测, 引用图分析, 语义嵌入, 图神经网络, 参考文献偏差

## 3 点简述
- 核心问题：LLM生成的参考文献列表是否与人类撰写的可区分，关注结构模仿与语义偏差。
- 方法要点：构建配对引用图，结合结构特征与标题/摘要嵌入，使用随机森林和图神经网络进行分类。
- 实验或效果：嵌入特征显著提升检测准确率至93%，结构特征效果有限，验证了方法的鲁棒性。

## 摘要（原文）

> Large language models are increasingly used to curate bibliographies, raising the question: are their reference lists distinguishable from human ones? We build paired citation graphs, ground truth and GPT-4o-generated (from parametric knowledge), for 10,000 focal papers ($\approx$ 275k references) from SciSciNet, and added a field-matched random baseline that preserves out-degree and field distributions while breaking latent structure. We compare (i) structure-only node features (degree/closeness/eigenvector centrality, clustering, edge count) with (ii) 3072-D title/abstract embeddings, using an RF on graph-level aggregates and Graph Neural Networks with node features. Structure alone barely separates GPT from ground truth (RF accuracy $\approx$ 0.60) despite cleanly rejecting the random baseline ($\approx$ 0.89--0.92). By contrast, embeddings sharply increase separability: RF on aggregated embeddings reaches $\approx$ 0.83, and GNNs with embedding node features achieve 93\% test accuracy on GPT vs.\ ground truth. We show the robustness of our findings by replicating the pipeline with Claude Sonnet 4.5 and with multiple embedding models (OpenAI and SPECTER), with RF separability for ground truth vs.\ Claude $\approx 0.77$ and clean rejection of the random baseline. Thus, LLM bibliographies, generated purely from parametric knowledge, closely mimic human citation topology, but leave detectable semantic fingerprints; detection and debiasing should target content signals rather than global graph structure.

