---
layout: default
title: Neuronal Attention Circuit (NAC) for Representation Learning
---

# Neuronal Attention Circuit (NAC) for Representation Learning
**arXiv**：[2512.10282v1](https://arxiv.org/abs/2512.10282) · [PDF](https://arxiv.org/pdf/2512.10282.pdf)  
**作者**：Waleed Razzaq, Izis Kankaraway, Yun-Bo Zhao  

**一句话要点**：提出Neuronal Attention Circuit以解决连续时间建模中注意力离散性的限制

**关键词**：连续时间注意力, 稀疏门控, ODE建模, 表示学习, 生物启发机制

## 3 点简述
- 注意力机制提升表示学习，但离散性阻碍连续时间建模。
- NAC将注意力对数计算重构为线性一阶ODE，采用稀疏门控和网络实现高效自适应动态。
- 在多个领域实验中，NAC在准确性上匹配或优于基线，并在运行时和内存效率上处于中间位置。

## 摘要（原文）

> Attention improves representation learning over RNNs, but its discrete nature limits continuous-time (CT) modeling. We introduce Neuronal Attention Circuit (NAC), a novel, biologically plausible CT-Attention mechanism that reformulates attention logits computation as the solution to a linear first-order ODE with nonlinear interlinked gates derived from repurposing \textit{C. elegans} Neuronal Circuit Policies (NCPs) wiring mechanism. NAC replaces dense projections with sparse sensory gates for key-query projections and a sparse backbone network with two heads for computing \textit{content-target} and \textit{learnable time-constant} gates, enabling efficient adaptive dynamics. NAC supports three attention logit computation modes: (i) explicit Euler integration, (ii) exact closed-form solution, and (iii) steady-state approximation. To improve memory intensity, we implemented a sparse Top-\emph{K} pairwise concatenation scheme that selectively curates key-query interactions. We provide rigorous theoretical guarantees, including state stability, bounded approximation errors, and universal approximation. Empirically, we implemented NAC in diverse domains, including irregular time-series classification, lane-keeping for autonomous vehicles, and industrial prognostics. We observed that NAC matches or outperforms competing baselines in accuracy and occupies an intermediate position in runtime and memory efficiency compared with several CT baselines.

