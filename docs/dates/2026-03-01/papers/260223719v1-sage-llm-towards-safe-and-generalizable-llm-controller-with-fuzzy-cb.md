---
layout: default
title: SAGE-LLM: Towards Safe and Generalizable LLM Controller with Fuzzy-CBF Verification and Graph-Structured Knowledge Retrieval for UAV Decision
---

# SAGE-LLM: Towards Safe and Generalizable LLM Controller with Fuzzy-CBF Verification and Graph-Structured Knowledge Retrieval for UAV Decision
**arXiv**：[2602.23719v1](https://arxiv.org/abs/2602.23719) · [PDF](https://arxiv.org/pdf/2602.23719.pdf)  
**作者**：Wenzhe Zhao, Yang Zhao, Ganchao Liu, Zhiyu Jiang, Dandan Ma, Zihao Li, Xuelong Li  

**一句话要点**：提出SAGE-LLM框架，通过模糊CBF验证和图知识检索增强LLM在无人机决策中的安全性与泛化能力。

**关键词**：无人机决策, 大语言模型, 控制屏障函数, 知识检索, 安全验证, 泛化能力

## 3 点简述
- 核心问题：LLM在无人机决策中缺乏领域控制知识和形式化安全保证，限制其直接应用。
- 方法要点：采用双层决策架构，结合模糊CBF验证和星层次图检索系统，实现安全规划与精确控制。
- 实验或效果：在未知障碍和突发威胁的追逃场景中验证，无需在线训练即可显著提升安全性和泛化性能。

## 摘要（原文）

> In UAV dynamic decision, complex and variable hazardous factors pose severe challenges to the generalization capability of algorithms. Despite offering semantic understanding and scene generalization, Large Language Models (LLM) lack domain-specific UAV control knowledge and formal safety assurances, restricting their direct applicability. To bridge this gap, this paper proposes a train-free two-layer decision architecture based on LLMs, integrating high-level safety planning with low-level precise control. The framework introduces three key contributions: 1) A fuzzy Control Barrier Function verification mechanism for semantically-augmented actions, providing provable safety certification for LLM outputs. 2) A star-hierarchical graph-based retrieval-augmented generation system, enabling efficient, elastic, and interpretable scene adaptation. 3) Systematic experimental validation in pursuit-evasion scenarios with unknown obstacles and emergent threats, demonstrating that our SAGE-LLM maintains performance while significantly enhancing safety and generalization without online training. The proposed framework demonstrates strong extensibility, suggesting its potential for generalization to broader embodied intelligence systems and safety-critical control domains.

