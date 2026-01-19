---
layout: default
title: Extractive summarization on a CMOS Ising machine
---

# Extractive summarization on a CMOS Ising machine
**arXiv**：[2601.11491v1](https://arxiv.org/abs/2601.11491) · [PDF](https://arxiv.org/pdf/2601.11491.pdf)  
**作者**：Ziqing Zeng, Abhimanyu Kumar, Chris H. Kim, Ulya R. Karpuzcu, Sachin S. Sapatnekar  

**一句话要点**：提出基于CMOS Ising机器的抽取式摘要方法，以在资源受限环境中实现低功耗实时推理。

**关键词**：抽取式摘要, CMOS Ising机器, 低功耗硬件, 实时推理, 整数耦合优化, 边缘计算

## 3 点简述
- 核心问题：传统抽取式摘要系统依赖高能耗CPU/GPU，不适合资源受限环境。
- 方法要点：开发硬件感知Ising公式和分解策略，在CMOS Ising机器上实现整数耦合的摘要生成。
- 实验或效果：在CNN/DailyMail数据集上，实现3-4.5倍加速和能耗降低2-3个数量级，摘要质量保持竞争力。

## 摘要（原文）

> Extractive summarization (ES) aims to generate a concise summary by selecting a subset of sentences from a document while maximizing relevance and minimizing redundancy. Although modern ES systems achieve high accuracy using powerful neural models, their deployment typically relies on CPU or GPU infrastructures that are energy-intensive and poorly suited for real-time inference in resource-constrained environments. In this work, we explore the feasibility of implementing McDonald-style extractive summarization on a low-power CMOS coupled oscillator-based Ising machine (COBI) that supports integer-valued, all-to-all spin couplings. We first propose a hardware-aware Ising formulation that reduces the scale imbalance between local fields and coupling terms, thereby improving robustness to coefficient quantization: this method can be applied to any problem formulation that requires k of n variables to be chosen. We then develop a complete ES pipeline including (i) stochastic rounding and iterative refinement to compensate for precision loss, and (ii) a decomposition strategy that partitions a large ES problem into smaller Ising subproblems that can be efficiently solved on COBI and later combined. Experimental results on the CNN/DailyMail dataset show that our pipeline can produce high-quality summaries using only integer-coupled Ising hardware with limited precision. COBI achieves 3-4.5x runtime speedups compared to a brute-force method, which is comparable to software Tabu search, and two to three orders of magnitude reductions in energy, while maintaining competitive summary quality. These results highlight the potential of deploying CMOS Ising solvers for real-time, low-energy text summarization on edge devices.

