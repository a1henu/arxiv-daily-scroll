---
layout: default
title: Solving an Open Problem in Theoretical Physics using AI-Assisted Discovery
---

# Solving an Open Problem in Theoretical Physics using AI-Assisted Discovery
**arXiv**：[2603.04735v1](https://arxiv.org/abs/2603.04735) · [PDF](https://arxiv.org/pdf/2603.04735.pdf)  
**作者**：Michael P. Brenner, Vincent Cohen-Addad, David Woodruff  

**一句话要点**：提出神经符号系统结合树搜索与数值反馈，解决宇宙弦引力辐射功率谱的开放问题

**关键词**：神经符号系统, 树搜索, 引力辐射, 宇宙弦, 解析解, AI辅助发现

## 3 点简述
- 核心问题：推导宇宙弦引力辐射功率谱的精确解析解，改进先前AI仅得渐近解
- 方法要点：结合Gemini大语言模型与树搜索框架，利用自动数值反馈指导模型
- 实验或效果：系统识别6种解析方法，获得大N渐近结果，与数值计算一致并连接量子场论

## 摘要（原文）

> This paper demonstrates that artificial intelligence can accelerate mathematical discovery by autonomously solving an open problem in theoretical physics. We present a neuro-symbolic system, combining the Gemini Deep Think large language model with a systematic Tree Search (TS) framework and automated numerical feedback, that successfully derived novel, exact analytical solutions for the power spectrum of gravitational radiation emitted by cosmic strings. Specifically, the agent evaluated the core integral $I(N,α)$ for arbitrary loop geometries, directly improving upon recent AI-assisted attempts \cite{BCE+25} that only yielded partial asymptotic solutions. To substantiate our methodological claims regarding AI-accelerated discovery and to ensure transparency, we detail system prompts, search constraints, and intermittent feedback loops that guided the model. The agent identified a suite of 6 different analytical methods, the most elegant of which expands the kernel in Gegenbauer polynomials $C_l^{(3/2)}$ to naturally absorb the integrand's singularities. The methods lead to an asymptotic result for $I(N,α)$ at large $N$ that both agrees with numerical results and also connects to the continuous Feynman parameterization of Quantum Field Theory. We detail both the algorithmic methodology that enabled this discovery and the resulting mathematical derivations.

