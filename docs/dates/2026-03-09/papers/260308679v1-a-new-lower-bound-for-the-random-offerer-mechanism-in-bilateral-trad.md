---
layout: default
title: A New Lower Bound for the Random Offerer Mechanism in Bilateral Trade using AI-Guided Evolutionary Search
---

# A New Lower Bound for the Random Offerer Mechanism in Bilateral Trade using AI-Guided Evolutionary Search
**arXiv**：[2603.08679v1](https://arxiv.org/abs/2603.08679) · [PDF](https://arxiv.org/pdf/2603.08679.pdf)  
**作者**：Yang Cai, Vineet Gupta, Zun Li, Aranyak Mehta  

**一句话要点**：提出AI引导进化搜索框架AlphaEvolve，改进双边贸易中随机报价机制的最坏情况性能下界至2.0749。

**关键词**：双边贸易, 随机报价机制, 近似比下界, AI引导进化搜索, 价值分布探索

## 3 点简述
- 核心问题：双边贸易中随机报价机制相对于最优效率的近似比下界未知，先前假设为2但被反例推翻。
- 方法要点：使用AI引导的进化搜索框架AlphaEvolve探索价值分布空间，寻找新的最坏情况实例。
- 实验或效果：发现新实例将下界提升至2.0749，证明效率差距比已知更宽。

## 摘要（原文）

> The celebrated Myerson--Satterthwaite theorem shows that in bilateral trade, no mechanism can be simultaneously fully efficient, Bayesian incentive compatible (BIC), and budget balanced (BB). This naturally raises the question of how closely the gains from trade (GFT) achievable by a BIC and BB mechanism can approximate the first-best (fully efficient) benchmark. The optimal BIC and BB mechanism is typically complex and highly distribution-dependent, making it difficult to characterize directly. Consequently, much of the literature analyzes simpler mechanisms such as the Random-Offerer (RO) mechanism and establishes constant-factor guarantees relative to the first-best GFT. An important open question concerns the worst-case performance of the RO mechanism relative to first-best (FB) efficiency. While it was originally hypothesized that the approximation ratio $\frac{\text{GFT}_{\text{FB}}}{\text{GFT}_{\text{RO}}}$ is bounded by $2$, recent work provided counterexamples to this conjecture: Cai et al. proved that the ratio can be strictly larger than $2$, and Babaioff et al. exhibited an explicit example with ratio approximately $2.02$.
>   In this work, we employ AlphaEvolve, an AI-guided evolutionary search framework, to explore the space of value distributions. We identify a new worst-case instance that yields an improved lower bound of $\frac{\text{GFT}_{\text{FB}}}{\text{GFT}_{\text{RO}}} \ge \textbf{2.0749}$. This establishes a new lower bound on the worst-case performance of the Random-Offerer mechanism, demonstrating a wider efficiency gap than previously known.

