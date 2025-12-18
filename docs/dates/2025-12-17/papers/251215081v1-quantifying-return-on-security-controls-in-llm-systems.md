---
layout: default
title: Quantifying Return on Security Controls in LLM Systems
---

# Quantifying Return on Security Controls in LLM Systems
**arXiv**：[2512.15081v1](https://arxiv.org/abs/2512.15081) · [PDF](https://arxiv.org/pdf/2512.15081.pdf)  
**作者**：Richard Helder Moulton, Austin O'Brien, John D. Hastings  

**一句话要点**：提出量化LLM系统安全控制回报的决策框架，评估缓解措施的经济效益。

**关键词**：LLM安全, 风险量化, 蒙特卡洛模拟, 安全控制回报, 对抗攻击

## 3 点简述
- 核心问题：LLM在安全关键工作流中缺乏量化指导，难以评估安全措施的价值。
- 方法要点：结合对抗探测、概率估计和蒙特卡洛模拟，将攻击成功概率转化为财务风险。
- 实验或效果：在RAG服务上测试三种缓解措施，ABAC和NER显著降低风险，NeMo Guardrails效果有限。

## 摘要（原文）

> Although large language models (LLMs) are increasingly used in security-critical workflows, practitioners lack quantitative guidance on which safeguards are worth deploying. This paper introduces a decision-oriented framework and reproducible methodology that together quantify residual risk, convert adversarial probe outcomes into financial risk estimates and return-on-control (RoC) metrics, and enable monetary comparison of layered defenses for LLM-based systems. A retrieval-augmented generation (RAG) service is instantiated using the DeepSeek-R1 model over a corpus containing synthetic personally identifiable information (PII), and subjected to automated attacks with Garak across five vulnerability classes: PII leakage, latent context injection, prompt injection, adversarial attack generation, and divergence. For each (vulnerability, control) pair, attack success probabilities are estimated via Laplace's Rule of Succession and combined with loss triangle distributions, calibrated from public breach-cost data, in 10,000-run Monte Carlo simulations to produce loss exceedance curves and expected losses. Three widely used mitigations, attribute-based access control (ABAC); named entity recognition (NER) redaction using Microsoft Presidio; and NeMo Guardrails, are then compared to a baseline RAG configuration. The baseline system exhibits very high attack success rates (>= 0.98 for PII, latent injection, and prompt injection), yielding a total simulated expected loss of $313k per attack scenario. ABAC collapses success probabilities for PII and prompt-related attacks to near zero and reduces the total expected loss by ~94%, achieving an RoC of 9.83. NER redaction likewise eliminates PII leakage and attains an RoC of 5.97, while NeMo Guardrails provides only marginal benefit (RoC of 0.05).

