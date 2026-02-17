---
layout: default
title: MAC-AMP: A Closed-Loop Multi-Agent Collaboration System for Multi-Objective Antimicrobial Peptide Design
---

# MAC-AMP: A Closed-Loop Multi-Agent Collaboration System for Multi-Objective Antimicrobial Peptide Design
**arXiv**：[2602.14926v1](https://arxiv.org/abs/2602.14926) · [PDF](https://arxiv.org/pdf/2602.14926.pdf)  
**作者**：Gen Zhou, Sugitha Janarthanan, Lianghong Chen, Pingzhao Hu  

**一句话要点**：提出MAC-AMP闭环多智能体协作系统，以解决多目标抗菌肽设计中的平衡与解释性问题。

**关键词**：抗菌肽设计, 多智能体协作, 多目标优化, 闭环系统, 大语言模型, 自适应强化学习

## 3 点简述
- 核心问题：现有AI模型难以平衡抗菌肽的活性、毒性和新颖性，且评分方法不透明。
- 方法要点：基于大语言模型的多智能体协作，采用闭环模拟同行评审-自适应强化学习框架。
- 实验或效果：在抗菌活性、肽似性、毒性合规和结构可靠性方面优于其他生成模型。

## 摘要（原文）

> To address the global health threat of antimicrobial resistance, antimicrobial peptides (AMP) are being explored for their potent and promising ability to fight resistant pathogens. While artificial intelligence (AI) is being employed to advance AMP discovery and design, most AMP design models struggle to balance key goals like activity, toxicity, and novelty, using rigid or unclear scoring methods that make results hard to interpret and optimize. As the capabilities of Large Language Models (LLM) advance and evolve swiftly, we turn to AI multi-agent collaboration based on such models (multi-agent LLMs), which show rapidly rising potential in complex scientific design scenarios. Based on this, we introduce MAC-AMP, a closed-loop multi-agent collaboration (MAC) system for multi-objective AMP design. The system implements a fully autonomous simulated peer review-adaptive reinforcement learning framework that requires only a task description and example dataset to design novel AMPs. The novelty of our work lies in introducing a closed-loop multi-agent system for AMP design, with cross-domain transferability, that supports multi-objective optimization while remaining explainable rather than a 'black box'. Experiments show that MAC-AMP outperforms other AMP generative models by effectively optimizing AMP generation for multiple key molecular properties, demonstrating exceptional results in antibacterial activity, AMP likeliness, toxicity compliance, and structural reliability.

