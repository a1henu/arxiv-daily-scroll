---
layout: default
title: Bridging 6G IoT and AI: LLM-Based Efficient Approach for Physical Layer's Optimization Tasks
---

# Bridging 6G IoT and AI: LLM-Based Efficient Approach for Physical Layer's Optimization Tasks
**arXiv**：[2602.06819v1](https://arxiv.org/abs/2602.06819) · [PDF](https://arxiv.org/pdf/2602.06819.pdf)  
**作者**：Ahsan Mehmood, Naveed Ul Hassan, Ghassan M. Kraidy  

**一句话要点**：提出基于提示工程的实时反馈验证框架，用于6G物联网物理层优化任务

**关键词**：6G物联网, 大语言模型, 物理层优化, 提示工程, 实时反馈, 无线通信

## 3 点简述
- 研究大语言模型在6G物联网网络中的作用，解决物理层优化问题
- 提出PE-RTFV框架，利用无线通信系统闭环反馈实现实时优化，无需模型重训练
- 在无线供电物联网测试床上验证，通过语义求解速率-能量区域优化问题，实现接近遗传算法性能

## 摘要（原文）

> This paper investigates the role of large language models (LLMs) in sixth-generation (6G) Internet of Things (IoT) networks and proposes a prompt-engineering-based real-time feedback and verification (PE-RTFV) framework that perform physical-layer's optimization tasks through an iteratively process. By leveraging the naturally available closed-loop feedback inherent in wireless communication systems, PE-RTFV enables real-time physical-layer optimization without requiring model retraining. The proposed framework employs an optimization LLM (O-LLM) to generate task-specific structured prompts, which are provided to an agent LLM (A-LLM) to produce task-specific solutions. Utilizing real-time system feedback, the O-LLM iteratively refines the prompts to guide the A-LLM toward improved solutions in a gradient-descent-like optimization process. We test PE-RTFV approach on wireless-powered IoT testbed case study on user-goal-driven constellation design through semantically solving rate-energy (RE)-region optimization problem which demonstrates that PE-RTFV achieves near-genetic-algorithm performance within only a few iterations, validating its effectiveness for complex physical-layer optimization tasks in resource-constrained IoT networks.

