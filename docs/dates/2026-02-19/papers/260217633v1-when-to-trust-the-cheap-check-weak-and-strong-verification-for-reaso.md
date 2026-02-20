---
layout: default
title: When to Trust the Cheap Check: Weak and Strong Verification for Reasoning
---

# When to Trust the Cheap Check: Weak and Strong Verification for Reasoning
**arXiv**：[2602.17633v1](https://arxiv.org/abs/2602.17633) · [PDF](https://arxiv.org/pdf/2602.17633.pdf)  
**作者**：Shayan Kiyani, Sima Noorani, George Pappas, Hamed Hassani  

**一句话要点**：提出弱-强验证策略以优化大语言模型推理中的信任决策

**关键词**：弱验证, 强验证, 信任决策, 在线算法, 错误控制, 大语言模型推理

## 3 点简述
- 核心问题：弱验证（如自一致性）快速但嘈杂，强验证（如人工检查）可靠但昂贵，需平衡信任决策。
- 方法要点：形式化弱-强验证策略，推导最优双阈值结构，并开发在线算法控制错误率。
- 实验或效果：理论分析显示校准和锐度影响弱验证价值，算法无需假设即可控制接受和拒绝错误。

## 摘要（原文）

> Reasoning with LLMs increasingly unfolds inside a broader verification loop. Internally, systems use cheap checks, such as self-consistency or proxy rewards, which we call weak verification. Externally, users inspect outputs and steer the model through feedback until results are trustworthy, which we call strong verification. These signals differ sharply in cost and reliability: strong verification can establish trust but is resource-intensive, while weak verification is fast and scalable but noisy and imperfect. We formalize this tension through weak--strong verification policies, which decide when to accept or reject based on weak verification and when to defer to strong verification. We introduce metrics capturing incorrect acceptance, incorrect rejection, and strong-verification frequency. Over population, we show that optimal policies admit a two-threshold structure and that calibration and sharpness govern the value of weak verifiers. Building on this, we develop an online algorithm that provably controls acceptance and rejection errors without assumptions on the query stream, the language model, or the weak verifier.

