---
layout: default
title: Learning to Forget Attention: Memory Consolidation for Adaptive Compute Reduction
---

# Learning to Forget Attention: Memory Consolidation for Adaptive Compute Reduction
**arXiv**：[2602.12204v1](https://arxiv.org/abs/2602.12204) · [PDF](https://arxiv.org/pdf/2602.12204.pdf)  
**作者**：Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma  

**一句话要点**：提出基于记忆巩固的自适应注意力路由机制，以减少重复模式下的计算冗余。

**关键词**：自适应注意力, 记忆巩固, 计算效率, 状态空间模型, 稀疏注意力, 生物启发学习

## 3 点简述
- 核心问题：现有注意力机制在重复模式中持续冗余，未随训练减少计算需求。
- 方法要点：引入生物启发的记忆巩固机制，将情景检索逐步蒸馏为参数化语义记忆。
- 实验或效果：在SRCD基准上实现100%检索精度，注意力计算减少37.8倍，匹配人类记忆过渡曲线。

## 摘要（原文）

> Hybrid architectures combining state-space models with attention have achieved strong efficiency-quality tradeoffs, yet existing approaches either apply attention uniformly or learn static sparse patterns. This misses a key opportunity: \emph{attention demand should decrease over time as recurring patterns become familiar}. We present a surprising finding from analyzing GPT-2 models: \textbf{88\%} of attention operations retrieve information already predictable from the model's hidden state, and this redundancy does \emph{not} decrease during training. Motivated by this observation, we introduce \textbf{\ours{}} (\textbf{C}onsolidation-based \textbf{R}outing for \textbf{A}daptive \textbf{M}emory), a biologically inspired memory consolidation mechanism that gradually distills episodic retrievals into parametric semantic memory. Unlike prior sparse attention methods, \ours{} exhibits \emph{decreasing attention utilization} over training, achieving a \textbf{37.8$\times$} reduction through a sharp phase transition at approximately 3K steps. We prove that this capability is \emph{impossible} without consolidation: any static routing scheme requires $Ω(f \cdot n)$ attention for tasks with recurring patterns of frequency $f$. On our proposed SRCD benchmark, \ours{} achieves \textbf{100\% retrieval accuracy} at 1.6\% attention compute (vs.\ 68\% for baselines), and consolidated patterns transfer to unseen tasks with \textbf{48--52\%} attention reduction without retraining. Remarkably, the learned consolidation dynamics quantitatively match human episodic-to-semantic memory transition curves from cognitive psychology ($γ= 0.43$ vs.\ $γ_{\text{human}} \approx 0.4$--$0.5$). Code and benchmarks are available at [anonymized].

