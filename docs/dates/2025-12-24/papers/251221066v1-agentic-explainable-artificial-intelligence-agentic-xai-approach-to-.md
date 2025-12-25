---
layout: default
title: Agentic Explainable Artificial Intelligence (Agentic XAI) Approach To Explore Better Explanation
---

# Agentic Explainable Artificial Intelligence (Agentic XAI) Approach To Explore Better Explanation
**arXiv**：[2512.21066v1](https://arxiv.org/abs/2512.21066) · [PDF](https://arxiv.org/pdf/2512.21066.pdf)  
**作者**：Tomoaki Yamaguchi, Yutong Zhou, Masahiro Ryo, Keisuke Katsura  

**一句话要点**：提出基于SHAP和多模态LLM迭代优化的Agentic XAI框架，以提升农业推荐系统的解释质量。

**关键词**：可解释人工智能, 大语言模型, 迭代优化, 农业推荐系统, SHAP, 偏差-方差权衡

## 3 点简述
- 核心问题：XAI解释难以向非专业人士传达，影响AI预测的信任度。
- 方法要点：结合SHAP可解释性与多模态LLM作为自主代理进行迭代优化。
- 实验或效果：在11轮迭代中，解释质量提升30-33%，但过度优化导致质量下降，需早期停止策略。

## 摘要（原文）

> Explainable artificial intelligence (XAI) enables data-driven understanding of factor associations with response variables, yet communicating XAI outputs to laypersons remains challenging, hindering trust in AI-based predictions. Large language models (LLMs) have emerged as promising tools for translating technical explanations into accessible narratives, yet the integration of agentic AI, where LLMs operate as autonomous agents through iterative refinement, with XAI remains unexplored. This study proposes an agentic XAI framework combining SHAP-based explainability with multimodal LLM-driven iterative refinement to generate progressively enhanced explanations. As a use case, we tested this framework as an agricultural recommendation system using rice yield data from 26 fields in Japan. The Agentic XAI initially provided a SHAP result and explored how to improve the explanation through additional analysis iteratively across 11 refinement rounds (Rounds 0-10). Explanations were evaluated by human experts (crop scientists) (n=12) and LLMs (n=14) against seven metrics: Specificity, Clarity, Conciseness, Practicality, Contextual Relevance, Cost Consideration, and Crop Science Credibility. Both evaluator groups confirmed that the framework successfully enhanced recommendation quality with an average score increase of 30-33% from Round 0, peaking at Rounds 3-4. However, excessive refinement showed a substantial drop in recommendation quality, indicating a bias-variance trade-off where early rounds lacked explanation depth (bias) while excessive iteration introduced verbosity and ungrounded abstraction (variance), as revealed by metric-specific analysis. These findings suggest that strategic early stopping (regularization) is needed for optimizing practical utility, challenging assumptions about monotonic improvement and providing evidence-based design principles for agentic XAI systems.

