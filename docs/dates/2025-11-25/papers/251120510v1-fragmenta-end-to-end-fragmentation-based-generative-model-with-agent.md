---
layout: default
title: FRAGMENTA: End-to-end Fragmentation-based Generative Model with Agentic Tuning for Drug Lead Optimization
---

# FRAGMENTA: End-to-end Fragmentation-based Generative Model with Agentic Tuning for Drug Lead Optimization
**arXiv**：[2511.20510v1](https://arxiv.org/abs/2511.20510) · [PDF](https://arxiv.org/pdf/2511.20510.pdf)  
**作者**：Yuto Suzuki, Paul Awolade, Daniel V. LaBarbera, Farnoush Banaei-Kashani  

**一句话要点**：提出FRAGMENTA框架以解决药物先导优化中数据稀缺和模型调优问题

**关键词**：分子生成, 碎片化模型, Q学习优化, 代理AI系统, 药物先导优化, 专家反馈学习

## 3 点简述
- 核心问题：分子生成数据稀缺，现有碎片化方法限制多样性和专家调优缓慢
- 方法要点：使用动态Q学习联合优化碎片化和生成，结合代理AI系统通过对话反馈学习专家知识
- 实验或效果：在癌症药物发现中，代理系统识别更多高分分子，优于传统调优

## 摘要（原文）

> Molecule generation using generative AI is vital for drug discovery, yet class-specific datasets often contain fewer than 100 training examples. While fragment-based models handle limited data better than atom-based approaches, existing heuristic fragmentation limits diversity and misses key fragments. Additionally, model tuning typically requires slow, indirect collaboration between medicinal chemists and AI engineers. We introduce FRAGMENTA, an end-to-end framework for drug lead optimization comprising: 1) a novel generative model that reframes fragmentation as a "vocabulary selection" problem, using dynamic Q-learning to jointly optimize fragmentation and generation; and 2) an agentic AI system that refines objectives via conversational feedback from domain experts. This system removes the AI engineer from the loop and progressively learns domain knowledge to eventually automate tuning. In real-world cancer drug discovery experiments, FRAGMENTA's Human-Agent configuration identified nearly twice as many high-scoring molecules as baselines. Furthermore, the fully autonomous Agent-Agent system outperformed traditional Human-Human tuning, demonstrating the efficacy of agentic tuning in capturing expert intent.

