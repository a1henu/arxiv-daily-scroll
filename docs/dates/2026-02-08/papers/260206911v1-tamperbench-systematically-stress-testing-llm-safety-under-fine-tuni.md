---
layout: default
title: TamperBench: Systematically Stress-Testing LLM Safety Under Fine-Tuning and Tampering
---

# TamperBench: Systematically Stress-Testing LLM Safety Under Fine-Tuning and Tampering
**arXiv**：[2602.06911v1](https://arxiv.org/abs/2602.06911) · [PDF](https://arxiv.org/pdf/2602.06911.pdf)  
**作者**：Saad Hossain, Tom Tseng, Punya Syon Pandey, Samanvay Vajpayee, Matthew Kowal, Nayeema Nonta, Samuel Simko, Stephen Casper, Zhijing Jin, Kellin Pelrine, Sirisha Rambhatla  

**一句话要点**：提出TamperBench框架以系统评估大语言模型在微调与篡改下的安全性

**关键词**：大语言模型安全, 篡改抵抗评估, 微调攻击, 对齐阶段防御, 系统化测试框架, 可复现性

## 3 点简述
- 核心问题：缺乏标准方法评估大语言模型对不安全修改的抵抗能力，难以比较模型与防御措施。
- 方法要点：整合权重空间微调攻击和潜在空间表示攻击，支持系统化超参数扫描和端到端可复现性。
- 实验或效果：评估21个开源大语言模型，发现后训练影响抵抗性，越狱调优为最严重攻击，Triplet为领先防御方法。

## 摘要（原文）

> As increasingly capable open-weight large language models (LLMs) are deployed, improving their tamper resistance against unsafe modifications, whether accidental or intentional, becomes critical to minimize risks. However, there is no standard approach to evaluate tamper resistance. Varied data sets, metrics, and tampering configurations make it difficult to compare safety, utility, and robustness across different models and defenses. To this end, we introduce TamperBench, the first unified framework to systematically evaluate the tamper resistance of LLMs. TamperBench (i) curates a repository of state-of-the-art weight-space fine-tuning attacks and latent-space representation attacks; (ii) enables realistic adversarial evaluation through systematic hyperparameter sweeps per attack-model pair; and (iii) provides both safety and utility evaluations. TamperBench requires minimal additional code to specify any fine-tuning configuration, alignment-stage defense method, and metric suite while ensuring end-to-end reproducibility. We use TamperBench to evaluate 21 open-weight LLMs, including defense-augmented variants, across nine tampering threats using standardized safety and capability metrics with hyperparameter sweeps per model-attack pair. This yields novel insights, including effects of post-training on tamper resistance, that jailbreak-tuning is typically the most severe attack, and that Triplet emerges as a leading alignment-stage defense. Code is available at: https://github.com/criticalml-uw/TamperBench

