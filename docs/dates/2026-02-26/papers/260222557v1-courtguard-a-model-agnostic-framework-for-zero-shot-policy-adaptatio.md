---
layout: default
title: CourtGuard: A Model-Agnostic Framework for Zero-Shot Policy Adaptation in LLM Safety
---

# CourtGuard: A Model-Agnostic Framework for Zero-Shot Policy Adaptation in LLM Safety
**arXiv**：[2602.22557v1](https://arxiv.org/abs/2602.22557) · [PDF](https://arxiv.org/pdf/2602.22557.pdf)  
**作者**：Umid Suleymanov, Rufiz Bayramov, Suad Gafarli, Seljan Musayeva, Taghi Mammadov, Aynur Akhundlu, Murat Kantarcioglu  

**一句话要点**：提出CourtGuard框架，通过检索增强多代理辩论实现零样本策略适应，以解决LLM安全机制适应僵化问题。

**关键词**：大语言模型安全, 零样本适应, 检索增强生成, 多代理系统, 对抗性辩论, 政策遵循

## 3 点简述
- 核心问题：现有LLM安全机制依赖静态微调分类器，导致适应新治理规则时需昂贵重训练，缺乏灵活性。
- 方法要点：采用检索增强多代理框架，将安全评估重构为基于外部政策文档的对抗性辩论，实现模型无关的零样本策略适应。
- 实验或效果：在7个安全基准上达到最先进性能，并在维基百科破坏任务中通过替换参考策略实现90%准确率，展示零样本适应能力。

## 摘要（原文）

> Current safety mechanisms for Large Language Models (LLMs) rely heavily on static, fine-tuned classifiers that suffer from adaptation rigidity, the inability to enforce new governance rules without expensive retraining. To address this, we introduce CourtGuard, a retrieval-augmented multi-agent framework that reimagines safety evaluation as Evidentiary Debate. By orchestrating an adversarial debate grounded in external policy documents, CourtGuard achieves state-of-the-art performance across 7 safety benchmarks, outperforming dedicated policy-following baselines without fine-tuning. Beyond standard metrics, we highlight two critical capabilities: (1) Zero-Shot Adaptability, where our framework successfully generalized to an out-of-domain Wikipedia Vandalism task (achieving 90\% accuracy) by swapping the reference policy; and (2) Automated Data Curation and Auditing, where we leveraged CourtGuard to curate and audit nine novel datasets of sophisticated adversarial attacks. Our results demonstrate that decoupling safety logic from model weights offers a robust, interpretable, and adaptable path for meeting current and future regulatory requirements in AI governance.

