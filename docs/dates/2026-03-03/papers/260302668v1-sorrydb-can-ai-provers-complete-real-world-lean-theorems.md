---
layout: default
title: SorryDB: Can AI Provers Complete Real-World Lean Theorems?
---

# SorryDB: Can AI Provers Complete Real-World Lean Theorems?
**arXiv**：[2603.02668v1](https://arxiv.org/abs/2603.02668) · [PDF](https://arxiv.org/pdf/2603.02668.pdf)  
**作者**：Austin Letson, Leopoldo Sarra, Auguste Poiroux, Oliver Dressler, Paul Lezeau, Dhyan Aranha, Frederick Pu, Aaron Hill, Miguel Corredera Hidalgo, Julian Berman, George Tsoukalas, Lenny Taelman  

**一句话要点**：提出SorryDB动态基准以评估AI证明器在真实Lean定理任务中的能力

**关键词**：形式化数学, 动态基准, AI证明器, Lean定理, 测试集污染, 社区对齐

## 3 点简述
- 核心问题：现有静态基准多基于竞赛问题，无法反映真实数学社区需求，且易受测试集污染影响
- 方法要点：构建动态更新的基准，从GitHub 78个真实形式化项目中提取开放Lean任务，确保任务新颖性和依赖性
- 实验或效果：评估多种方法（如大语言模型、代理方法、符号证明器），发现当前方法互补，代理方法表现最佳但非绝对优势

## 摘要（原文）

> We present SorryDB, a dynamically-updating benchmark of open Lean tasks drawn from 78 real world formalization projects on GitHub. Unlike existing static benchmarks, often composed of competition problems, hillclimbing the SorryDB benchmark will yield tools that are aligned to the community needs, more usable by mathematicians, and more capable of understanding complex dependencies. Moreover, by providing a continuously updated stream of tasks, SorryDB mitigates test-set contamination and offers a robust metric for an agent's ability to contribute to novel formal mathematics projects. We evaluate a collection of approaches, including generalist large language models, agentic approaches, and specialized symbolic provers, over a selected snapshot of 1000 tasks from SorryDB. We show that current approaches are complementary: even though an agentic approach based on Gemini Flash is the most performant, it is not strictly better than other off-the-shelf large-language models, specialized provers, or even a curated list of Lean tactics.

