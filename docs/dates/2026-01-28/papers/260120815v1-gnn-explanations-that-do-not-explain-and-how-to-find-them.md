---
layout: default
title: GNN Explanations that do not Explain and How to find Them
---

# GNN Explanations that do not Explain and How to find Them
**arXiv**：[2601.20815v1](https://arxiv.org/abs/2601.20815) · [PDF](https://arxiv.org/pdf/2601.20815.pdf)  
**作者**：Steve Azzolin, Stefano Teso, Bruno Lepri, Andrea Passerini, Sagar Malhotra  

**一句话要点**：提出新忠实度指标以检测自解释图神经网络中的退化解释问题

**关键词**：自解释图神经网络, 解释忠实度, 退化解释, 图神经网络审计, 敏感属性检测

## 3 点简述
- 识别自解释图神经网络解释可能无关模型推理的退化失败案例
- 揭示退化解释可恶意植入或自然出现，现有忠实度指标常失效
- 引入新忠实度指标，在恶意和自然场景下可靠标记退化解释为不忠实

## 摘要（原文）

> Explanations provided by Self-explainable Graph Neural Networks (SE-GNNs) are fundamental for understanding the model's inner workings and for identifying potential misuse of sensitive attributes. Although recent works have highlighted that these explanations can be suboptimal and potentially misleading, a characterization of their failure cases is unavailable. In this work, we identify a critical failure of SE-GNN explanations: explanations can be unambiguously unrelated to how the SE-GNNs infer labels. We show that, on the one hand, many SE-GNNs can achieve optimal true risk while producing these degenerate explanations, and on the other, most faithfulness metrics can fail to identify these failure modes. Our empirical analysis reveals that degenerate explanations can be maliciously planted (allowing an attacker to hide the use of sensitive attributes) and can also emerge naturally, highlighting the need for reliable auditing. To address this, we introduce a novel faithfulness metric that reliably marks degenerate explanations as unfaithful, in both malicious and natural settings. Our code is available in the supplemental.

