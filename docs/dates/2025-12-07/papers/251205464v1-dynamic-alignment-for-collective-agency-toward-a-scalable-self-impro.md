---
layout: default
title: Dynamic Alignment for Collective Agency: Toward a Scalable Self-Improving Framework for Open-Ended LLM Alignment
---

# Dynamic Alignment for Collective Agency: Toward a Scalable Self-Improving Framework for Open-Ended LLM Alignment
**arXiv**：[2512.05464v1](https://arxiv.org/abs/2512.05464) · [PDF](https://arxiv.org/pdf/2512.05464.pdf)  
**作者**：Panatchakorn Anantaprayoon, Nataliia Babina, Jad Tarifi, Nima Asgharbeygi  

**一句话要点**：提出动态对齐框架与集体代理价值，以可扩展自改进方法解决大语言模型开放对齐问题

**关键词**：大语言模型对齐, 自改进对齐, 集体代理, 动态对齐框架, 自奖励机制, GRPO学习

## 3 点简述
- 核心问题：传统对齐方法在AGI/ASI发展中可能不足，且基于人类反馈的资源密集难以扩展
- 方法要点：引入集体代理作为开放对齐价值，结合自动数据集生成与自奖励机制实现迭代自对齐
- 实验或效果：实验表明方法成功对齐模型至集体代理，同时保持一般NLP能力

## 摘要（原文）

> Large Language Models (LLMs) are typically aligned with human values using preference data or predefined principles such as helpfulness, honesty, and harmlessness. However, as AI systems progress toward Artificial General Intelligence (AGI) and Artificial Superintelligence (ASI), such value systems may become insufficient. In addition, human feedback-based alignment remains resource-intensive and difficult to scale. While AI-feedback-based self-improving alignment methods have been explored as a scalable alternative, they have largely remained constrained to conventional alignment values. In this work, we explore both a more holistic alignment objective and a scalable, self-improving alignment approach. Aiming to transcend conventional alignment norms, we introduce Collective Agency (CA)-a unified and open-ended alignment value that encourages integrated agentic capabilities. We also propose Dynamic Alignment-an alignment framework that enables an LLM to iteratively align itself. Dynamic Alignment comprises two key components: (1) automated training dataset generation with LLMs, and (2) a self-rewarding mechanism, where the policy model evaluates its own output candidates and assigns rewards for GRPO-based learning. Experimental results demonstrate that our approach successfully aligns the model to CA while preserving general NLP capabilities.

