---
layout: default
title: Optimal certification of constant-local Hamiltonians
---

# Optimal certification of constant-local Hamiltonians
**arXiv**：[2512.09778v1](https://arxiv.org/abs/2512.09778) · [PDF](https://arxiv.org/pdf/2512.09778.pdf)  
**作者**：Junseo Lee, Myeongjin Shin  

**一句话要点**：提出最优常数局域哈密顿量认证协议，仅需正向实时动力学实现容错验证。

**关键词**：哈密顿量认证, 常数局域哈密顿量, 实时动力学, Heisenberg极限, 量子算法, 容错验证

## 3 点简述
- 研究从哈密顿量动力学实时访问中认证常数局域哈密顿量的问题。
- 引入首个对所有常数局域哈密顿量实现最优性能的容错认证协议，无需逆演化或受控操作。
- 对n量子比特、k局域、无迹哈密顿量，总演化时间为O(c^k/ε)，常数局域时达到Θ(1/ε)的Heisenberg极限。

## 摘要（原文）

> We study the problem of certifying local Hamiltonians from real-time access to their dynamics. Given oracle access to $e^{-itH}$ for an unknown $k$-local Hamiltonian $H$ and a fully specified target Hamiltonian $H_0$, the goal is to decide whether $H$ is exactly equal to $H_0$ or differs from $H_0$ by at least $\varepsilon$ in normalized Frobenius norm, while minimizing the total evolution time. We introduce the first intolerant Hamiltonian certification protocol that achieves optimal performance for all constant-locality Hamiltonians. For general $n$-qubit, $k$-local, traceless Hamiltonians, our procedure uses $O(c^k/\varepsilon)$ total evolution time for a universal constant $c$, and succeeds with high probability. In particular, for $O(1)$-local Hamiltonians, the total evolution time becomes $Θ(1/\varepsilon)$, matching the known $Ω(1/\varepsilon)$ lower bounds and achieving the gold-standard Heisenberg-limit scaling. Prior certification methods either relied on implementing inverse evolution of $H$, required controlled access to $e^{-itH}$, or achieved near-optimal guarantees only in restricted settings such as the Ising case ($k=2$). In contrast, our algorithm requires neither inverse evolution nor controlled operations: it uses only forward real-time dynamics and achieves optimal intolerant certification for all constant-locality Hamiltonians.

