---
layout: default
title: MMA: Multimodal Memory Agent
---

# MMA: Multimodal Memory Agent
**arXiv**：[2602.16493v1](https://arxiv.org/abs/2602.16493) · [PDF](https://arxiv.org/pdf/2602.16493.pdf)  
**作者**：Yihao Lu, Wanru Cheng, Zeyu Zhang, Hao Tang  

**一句话要点**：提出多模态记忆代理MMA，通过动态可靠性评分解决长时程多模态代理中记忆检索的过自信错误问题。

**关键词**：多模态代理, 记忆检索, 可靠性评分, 视觉偏见, 基准测试, 长时程任务

## 3 点简述
- 核心问题：基于相似性的记忆检索易导致陈旧、低可信或冲突项，引发过自信错误。
- 方法要点：结合来源可信度、时间衰减和冲突感知网络共识，为检索项分配动态可靠性评分，并据此重加权证据或弃权。
- 实验或效果：在FEVER上匹配基线准确率，方差降低35.2%；在MMA-Bench上视觉模式Type-B准确率达41.18%，基线为0.0%。

## 摘要（原文）

> Long-horizon multimodal agents depend on external memory; however, similarity-based retrieval often surfaces stale, low-credibility, or conflicting items, which can trigger overconfident errors. We propose Multimodal Memory Agent (MMA), which assigns each retrieved memory item a dynamic reliability score by combining source credibility, temporal decay, and conflict-aware network consensus, and uses this signal to reweight evidence and abstain when support is insufficient. We also introduce MMA-Bench, a programmatically generated benchmark for belief dynamics with controlled speaker reliability and structured text-vision contradictions. Using this framework, we uncover the "Visual Placebo Effect", revealing how RAG-based agents inherit latent visual biases from foundation models. On FEVER, MMA matches baseline accuracy while reducing variance by 35.2% and improving selective utility; on LoCoMo, a safety-oriented configuration improves actionable accuracy and reduces wrong answers; on MMA-Bench, MMA reaches 41.18% Type-B accuracy in Vision mode, while the baseline collapses to 0.0% under the same protocol. Code: https://github.com/AIGeeksGroup/MMA.

