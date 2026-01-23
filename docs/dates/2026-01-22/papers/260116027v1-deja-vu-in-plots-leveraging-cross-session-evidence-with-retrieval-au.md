---
layout: default
title: Deja Vu in Plots: Leveraging Cross-Session Evidence with Retrieval-Augmented LLMs for Live Streaming Risk Assessment
---

# Deja Vu in Plots: Leveraging Cross-Session Evidence with Retrieval-Augmented LLMs for Live Streaming Risk Assessment
**arXiv**：[2601.16027v1](https://arxiv.org/abs/2601.16027) · [PDF](https://arxiv.org/pdf/2601.16027.pdf)  
**作者**：Yiran Qiao, Xiang Ao, Jing Chen, Yang Liu, Qiwei Zhong, Qing He  

**一句话要点**：提出CS-VAR以解决直播流中跨会话风险检测问题

**关键词**：直播风险检测, 跨会话分析, 检索增强LLM, 模型蒸馏, 实时部署

## 3 点简述
- 核心问题：直播中恶意行为跨会话累积复发，检测困难
- 方法要点：结合检索增强LLM推理跨会话证据，指导轻量模型训练
- 实验或效果：工业数据集验证性能领先，提供可解释信号支持实时审核

## 摘要（原文）

> The rise of live streaming has transformed online interaction, enabling massive real-time engagement but also exposing platforms to complex risks such as scams and coordinated malicious behaviors. Detecting these risks is challenging because harmful actions often accumulate gradually and recur across seemingly unrelated streams. To address this, we propose CS-VAR (Cross-Session Evidence-Aware Retrieval-Augmented Detector) for live streaming risk assessment. In CS-VAR, a lightweight, domain-specific model performs fast session-level risk inference, guided during training by a Large Language Model (LLM) that reasons over retrieved cross-session behavioral evidence and transfers its local-to-global insights to the small model. This design enables the small model to recognize recurring patterns across streams, perform structured risk assessment, and maintain efficiency for real-time deployment. Extensive offline experiments on large-scale industrial datasets, combined with online validation, demonstrate the state-of-the-art performance of CS-VAR. Furthermore, CS-VAR provides interpretable, localized signals that effectively empower real-world moderation for live streaming.

