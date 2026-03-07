---
layout: default
title: Knowledge Divergence and the Value of Debate for Scalable Oversight
---

# Knowledge Divergence and the Value of Debate for Scalable Oversight
**arXiv**：[2603.05293v1](https://arxiv.org/abs/2603.05293) · [PDF](https://arxiv.org/pdf/2603.05293.pdf)  
**作者**：Robin Young  

**一句话要点**：提出基于知识分歧几何的辩论价值分析框架，以连接辩论与RLAIF并量化辩论优势。

**关键词**：知识分歧, 辩论监督, RLAIF, 几何分析, 可扩展监督, 主角度

## 3 点简述
- 核心问题：缺乏连接辩论与RLAIF的形式框架，辩论优势条件未知。
- 方法要点：通过模型表示子空间的主角度参数化知识分歧，推导辩论优势的闭式解。
- 实验或效果：分类知识分歧三机制，证明辩论可实现单模型无法达成的结果，但对抗激励可能导致协调失败。

## 摘要（原文）

> AI safety via debate and reinforcement learning from AI feedback (RLAIF) are both proposed methods for scalable oversight of advanced AI systems, yet no formal framework relates them or characterizes when debate offers an advantage. We analyze this by parameterizing debate's value through the geometry of knowledge divergence between debating models. Using principal angles between models' representation subspaces, we prove that the debate advantage admits an exact closed form. When models share identical training corpora, debate reduces to RLAIF-like where a single-agent method recovers the same optimum. When models possess divergent knowledge, debate advantage scales with a phase transition from quadratic regime (debate offers negligible benefit) to linear regime (debate is essential). We classify three regimes of knowledge divergence (shared, one-sided, and compositional) and provide existence results showing that debate can achieve outcomes inaccessible to either model alone, alongside a negative result showing that sufficiently strong adversarial incentives cause coordination failure in the compositional regime, with a sharp threshold separating effective from ineffective debate. We offer the first formal connection between debate and RLAIF, a geometric foundation for understanding when adversarial oversight protocols are justified, and connection to the problem of eliciting latent knowledge across models with complementary information.

