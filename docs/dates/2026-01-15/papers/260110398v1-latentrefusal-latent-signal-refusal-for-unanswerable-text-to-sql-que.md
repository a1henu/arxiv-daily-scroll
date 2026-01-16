---
layout: default
title: LatentRefusal: Latent-Signal Refusal for Unanswerable Text-to-SQL Queries
---

# LatentRefusal: Latent-Signal Refusal for Unanswerable Text-to-SQL Queries
**arXiv**：[2601.10398v1](https://arxiv.org/abs/2601.10398) · [PDF](https://arxiv.org/pdf/2601.10398.pdf)  
**作者**：Xuancheng Ren, Shijing Hu, Zhihui Lu, Jiangqi Huang, Qiang Duan  

**一句话要点**：提出LatentRefusal机制，基于隐层激活预测查询可答性，以解决文本到SQL系统中不可答查询的安全拒绝问题。

**关键词**：文本到SQL, 安全拒绝, 隐层激活, 可答性预测, 轻量探测, 查询-模式匹配

## 3 点简述
- 核心问题：LLM文本到SQL系统中，不可答或欠指定查询可能生成错误SQL程序，导致误导结果或安全风险。
- 方法要点：引入Tri-Residual Gated Encoder轻量探测架构，从LLM隐层激活中提取查询-模式不匹配信号，预测可答性。
- 实验或效果：在四个基准测试中，平均F1提升至88.5%，探测开销仅约2毫秒，验证了方法的有效性和高效性。

## 摘要（原文）

> In LLM-based text-to-SQL systems, unanswerable and underspecified user queries may generate not only incorrect text but also executable programs that yield misleading results or violate safety constraints, posing a major barrier to safe deployment. Existing refusal strategies for such queries either rely on output-level instruction following, which is brittle due to model hallucinations, or estimate output uncertainty, which adds complexity and overhead. To address this challenge, we formalize safe refusal in text-to-SQL systems as an answerability-gating problem and propose LatentRefusal, a latent-signal refusal mechanism that predicts query answerability from intermediate hidden activations of a large language model. We introduce the Tri-Residual Gated Encoder, a lightweight probing architecture, to suppress schema noise and amplify sparse, localized cues of question-schema mismatch that indicate unanswerability. Extensive empirical evaluations across diverse ambiguous and unanswerable settings, together with ablation studies and interpretability analyses, demonstrate the effectiveness of the proposed approach and show that LatentRefusal provides an attachable and efficient safety layer for text-to-SQL systems. Across four benchmarks, LatentRefusal improves average F1 to 88.5 percent on both backbones while adding approximately 2 milliseconds of probe overhead.

