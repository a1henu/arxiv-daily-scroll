---
layout: default
title: Certificate-Guided Pruning for Stochastic Lipschitz Optimization
---

# Certificate-Guided Pruning for Stochastic Lipschitz Optimization
**arXiv**：[2601.20231v1](https://arxiv.org/abs/2601.20231) · [PDF](https://arxiv.org/pdf/2601.20231.pdf)  
**作者**：Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma  

**一句话要点**：提出证书引导剪枝方法，用于噪声评估下的Lipschitz函数黑盒优化。

**关键词**：黑盒优化, Lipschitz函数, 证书引导剪枝, 样本复杂度, 自适应方法, 信任区域

## 3 点简述
- 研究噪声评估下Lipschitz函数的黑盒优化，现有方法缺乏显式最优性证书。
- 引入CGP方法，通过置信调整Lipschitz包络维护活动集，提供高概率次优性证书。
- 在12个基准测试中，CGP变体匹配或超越基线，并提供基于证书体积的停止准则。

## 摘要（原文）

> We study black-box optimization of Lipschitz functions under noisy evaluations. Existing adaptive discretization methods implicitly avoid suboptimal regions but do not provide explicit certificates of optimality or measurable progress guarantees. We introduce \textbf{Certificate-Guided Pruning (CGP)}, which maintains an explicit \emph{active set} $A_t$ of potentially optimal points via confidence-adjusted Lipschitz envelopes. Any point outside $A_t$ is certifiably suboptimal with high probability, and under a margin condition with near-optimality dimension $α$, we prove $\Vol(A_t)$ shrinks at a controlled rate yielding sample complexity $\tildeO(\varepsilon^{-(2+α)})$. We develop three extensions: CGP-Adaptive learns $L$ online with $O(\log T)$ overhead; CGP-TR scales to $d > 50$ via trust regions with local certificates; and CGP-Hybrid switches to GP refinement when local smoothness is detected. Experiments on 12 benchmarks ($d \in [2, 100]$) show CGP variants match or exceed strong baselines while providing principled stopping criteria via certificate volume.

