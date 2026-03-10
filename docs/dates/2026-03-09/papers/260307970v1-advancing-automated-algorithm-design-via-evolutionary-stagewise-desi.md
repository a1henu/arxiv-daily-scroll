---
layout: default
title: Advancing Automated Algorithm Design via Evolutionary Stagewise Design with LLMs
---

# Advancing Automated Algorithm Design via Evolutionary Stagewise Design with LLMs
**arXiv**：[2603.07970v1](https://arxiv.org/abs/2603.07970) · [PDF](https://arxiv.org/pdf/2603.07970.pdf)  
**作者**：Chen Lu, Ke Xue, Chengrui Gao, Yunqi Shi, Siyuan Xu, Mingxuan Yuan, Chao Qian, Zhi-Hua Zhou  

**一句话要点**：提出进化阶段化算法设计以解决工业场景中LLM自动化算法设计的幻觉问题

**关键词**：自动化算法设计, 进化计算, 大语言模型, 芯片布局优化, 贝叶斯优化, 多代理系统

## 3 点简述
- 核心问题：LLM自动化算法设计因黑盒建模忽视问题内在机制，导致幻觉设计。
- 方法要点：将算法设计分解为可管理阶段，结合实时反馈和多代理系统迭代优化。
- 实验效果：在芯片布局和黑盒优化任务中超越专家设计和现有方法，实现历史最佳性能。

## 摘要（原文）

> With the rapid advancement of human science and technology, problems in industrial scenarios are becoming increasingly challenging, bringing significant challenges to traditional algorithm design. Automated algorithm design with LLMs emerges as a promising solution, but the currently adopted black-box modeling deprives LLMs of any awareness of the intrinsic mechanism of the target problem, leading to hallucinated designs. In this paper, we introduce Evolutionary Stagewise Algorithm Design (EvoStage), a novel evolutionary paradigm that bridges the gap between the rigorous demands of industrial-scale algorithm design and the LLM-based algorithm design methods. Drawing inspiration from CoT, EvoStage decomposes the algorithm design process into sequential, manageable stages and integrates real-time intermediate feedback to iteratively refine algorithm design directions. To further reduce the algorithm design space and avoid falling into local optima, we introduce a multi-agent system and a "global-local perspective" mechanism. We apply EvoStage to the design of two types of common optimizers: designing parameter configuration schedules of the Adam optimizer for chip placement, and designing acquisition functions of Bayesian optimization for black-box optimization. Experimental results across open-source benchmarks demonstrate that EvoStage outperforms human-expert designs and existing LLM-based methods within only a couple of evolution steps, even achieving the historically state-of-the-art half-perimeter wire-length results on every tested chip case. Furthermore, when deployed on a commercial-grade 3D chip placement tool, EvoStage significantly surpasses the original performance metrics, achieving record-breaking efficiency. We hope EvoStage can significantly advance automated algorithm design in the real world, helping elevate human productivity.

