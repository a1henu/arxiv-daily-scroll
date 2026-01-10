---
layout: default
title: CuMA: Aligning LLMs with Sparse Cultural Values via Demographic-Aware Mixture of Adapters
---

# CuMA: Aligning LLMs with Sparse Cultural Values via Demographic-Aware Mixture of Adapters
**arXiv**：[2601.04885v1](https://arxiv.org/abs/2601.04885) · [PDF](https://arxiv.org/pdf/2601.04885.pdf)  
**作者**：Ao Sun, Xiaoyu Wang, Zhe Tan, Yu Li, Jiachen Zhu, Shu Su, Yuheng Jia  

**一句话要点**：提出CuMA框架，通过人口统计感知的适配器混合解决大语言模型文化对齐中的均值崩溃问题。

**关键词**：文化对齐, 适配器混合, 均值崩溃, 人口统计感知, 大语言模型, 梯度解耦

## 3 点简述
- 核心问题：密集模型在拟合冲突文化价值时发生均值崩溃，无法代表多元群体。
- 方法要点：采用条件容量分离，通过人口统计感知路由将冲突梯度解耦到专家子空间。
- 实验或效果：在WorldValuesBench等基准上实现SOTA，有效缓解均值崩溃并保持文化多样性。

## 摘要（原文）

> As Large Language Models (LLMs) serve a global audience, alignment must transition from enforcing universal consensus to respecting cultural pluralism. We demonstrate that dense models, when forced to fit conflicting value distributions, suffer from \textbf{Mean Collapse}, converging to a generic average that fails to represent diverse groups. We attribute this to \textbf{Cultural Sparsity}, where gradient interference prevents dense parameters from spanning distinct cultural modes. To resolve this, we propose \textbf{\textsc{CuMA}} (\textbf{Cu}ltural \textbf{M}ixture of \textbf{A}dapters), a framework that frames alignment as a \textbf{conditional capacity separation} problem. By incorporating demographic-aware routing, \textsc{CuMA} internalizes a \textit{Latent Cultural Topology} to explicitly disentangle conflicting gradients into specialized expert subspaces. Extensive evaluations on WorldValuesBench, Community Alignment, and PRISM demonstrate that \textsc{CuMA} achieves state-of-the-art performance, significantly outperforming both dense baselines and semantic-only MoEs. Crucially, our analysis confirms that \textsc{CuMA} effectively mitigates mean collapse, preserving cultural diversity. Our code is available at https://github.com/Throll/CuMA.

