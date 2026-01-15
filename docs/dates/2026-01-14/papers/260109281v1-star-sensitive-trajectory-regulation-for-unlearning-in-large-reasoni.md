---
layout: default
title: STaR: Sensitive Trajectory Regulation for Unlearning in Large Reasoning Models
---

# STaR: Sensitive Trajectory Regulation for Unlearning in Large Reasoning Models
**arXiv**：[2601.09281v1](https://arxiv.org/abs/2601.09281) · [PDF](https://arxiv.org/pdf/2601.09281.pdf)  
**作者**：Jingjing Zhou, Gaoxiang Cong, Li Su, Liang Li  

**一句话要点**：提出STaR框架以解决大型推理模型在推理链中敏感信息遗忘不足的隐私风险

**关键词**：大型推理模型, 隐私保护, 推理链遗忘, 无参数框架, 敏感轨迹抑制, 多粒度评估

## 3 点简述
- 核心问题：大型推理模型生成复杂推理链时，敏感信息嵌入中间步骤，现有遗忘方法仅修改最终答案，导致隐私泄露。
- 方法要点：STaR通过语义检测、安全提示前缀、轨迹抑制和自适应过滤，实现推理过程的无参数遗忘。
- 实验或效果：在R-TOFU基准上，STaR以最小效用损失实现全面稳定遗忘，并引入新评估指标验证隐私保护。

## 摘要（原文）

> Large Reasoning Models (LRMs) have advanced automated multi-step reasoning, but their ability to generate complex Chain-of-Thought (CoT) trajectories introduces severe privacy risks, as sensitive information may be deeply embedded throughout the reasoning process. Existing Large Language Models (LLMs) unlearning approaches that typically focus on modifying only final answers are insufficient for LRMs, as they fail to remove sensitive content from intermediate steps, leading to persistent privacy leakage and degraded security. To address these challenges, we propose Sensitive Trajectory Regulation (STaR), a parameter-free, inference-time unlearning framework that achieves robust privacy protection throughout the reasoning process. Specifically, we first identify sensitive content via semantic-aware detection. Then, we inject global safety constraints through secure prompt prefix. Next, we perform trajectory-aware suppression to dynamically block sensitive content across the entire reasoning chain. Finally, we apply token-level adaptive filtering to prevent both exact and paraphrased sensitive tokens during generation. Furthermore, to overcome the inadequacies of existing evaluation protocols, we introduce two metrics: Multi-Decoding Consistency Assessment (MCS), which measures the consistency of unlearning across diverse decoding strategies, and Multi-Granularity Membership Inference Attack (MIA) Evaluation, which quantifies privacy protection at both answer and reasoning-chain levels. Experiments on the R-TOFU benchmark demonstrate that STaR achieves comprehensive and stable unlearning with minimal utility loss, setting a new standard for privacy-preserving reasoning in LRMs.

