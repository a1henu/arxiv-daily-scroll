---
layout: default
title: Quantum Circuit Pre-Synthesis: Learning Local Edits to Reduce $T$-count
---

# Quantum Circuit Pre-Synthesis: Learning Local Edits to Reduce $T$-count
**arXiv**：[2601.19738v1](https://arxiv.org/abs/2601.19738) · [PDF](https://arxiv.org/pdf/2601.19738.pdf)  
**作者**：Daniele Lizzio Bosco, Lukasz Cincio, Giuseppe Serra, M. Cerezo  

**一句话要点**：提出Q-PreSyn策略，通过强化学习优化量子电路预合成以减少T门数量

**关键词**：量子电路合成, T门优化, 强化学习, 局部编辑, 容错量子计算, 电路表示

## 3 点简述
- 核心问题：局部合成方法在编译量子电路时导致T门数量或电路深度次优，性能受电路表示影响
- 方法要点：使用强化学习代理识别局部编辑序列，优化电路表示以降低合成后的T门数量
- 实验或效果：在最多25量子比特的电路上，应用Q-PreSyn后T门数量减少高达20%，无额外近似误差

## 摘要（原文）

> Compiling quantum circuits into Clifford+$T$ gates is a central task for fault-tolerant quantum computing using stabilizer codes. In the near term, $T$ gates will dominate the cost of fault tolerant implementations, and any reduction in the number of such expensive gates could mean the difference between being able to run a circuit or not. While exact synthesis is exponentially hard in the number of qubits, local synthesis approaches are commonly used to compile large circuits by decomposing them into substructures. However, composing local methods leads to suboptimal compilations in key metrics such as $T$-count or circuit depth, and their performance strongly depends on circuit representation. In this work, we address this challenge by proposing \textsc{Q-PreSyn}, a strategy that, given a set of local edits preserving circuit equivalence, uses a RL agent to identify effective sequences of such actions and thereby obtain circuit representations that yield a reduced $T$-count upon synthesis. Experimental results of our proposed strategy, applied on top of well-known synthesis algorithms, show up to a $20\%$ reduction in $T$-count on circuits with up to 25 qubits, without introducing any additional approximation error prior to synthesis.

