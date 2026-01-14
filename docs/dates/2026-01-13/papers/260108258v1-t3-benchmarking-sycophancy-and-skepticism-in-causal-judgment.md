---
layout: default
title: T3: Benchmarking Sycophancy and Skepticism in Causal Judgment
---

# T3: Benchmarking Sycophancy and Skepticism in Causal Judgment
**arXiv**：[2601.08258v1](https://arxiv.org/abs/2601.08258) · [PDF](https://arxiv.org/pdf/2601.08258.pdf)  
**作者**：Edward Y. Chang  

**一句话要点**：提出T3基准以评估大语言模型在因果判断中的可信思考能力

**关键词**：因果判断基准, 大语言模型评估, 可信思考诊断, 因果阶梯, 性能分解, 结构化验证

## 3 点简述
- 核心问题：评估大语言模型在因果阶梯上的判断能力，诊断如怀疑陷阱和缩放悖论等病理
- 方法要点：基于454个专家策划的小故事，分解性能为效用、安全性和明智拒绝
- 实验或效果：应用于前沿模型，发现GPT-5.2在模糊反事实上表现差，验证结构化验证协议可恢复判断

## 摘要（原文）

> We introduce T3 (Testing Trustworthy Thinking), a diagnostic benchmark designed to rigorously evaluate LLM causal judgment across Pearl's Ladder of Causality. Comprising 454 expert-curated vignettes, T3 prioritizes high-resolution failure analysis, decomposing performance into Utility (sensitivity), Safety (specificity), and Wise Refusal on underdetermined cases. By applying T3 to frontier models, we diagnose two distinct pathologies: a "Skepticism Trap" at L1 (where safety-tuned models like Claude Haiku reject 60% of valid links) and a non-monotonic Scaling Paradox at L3. In the latter, the larger GPT-5.2 underperforms GPT-4-Turbo by 55 points on ambiguous counterfactuals, driven by a collapse into paralysis (excessive hedging) rather than hallucination. Finally, we use the benchmark to validate a process-verified protocol (RCA), showing that T3 successfully captures the restoration of decisive causal judgment under structured verification.

