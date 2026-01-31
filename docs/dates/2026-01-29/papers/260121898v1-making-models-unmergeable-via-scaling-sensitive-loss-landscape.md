---
layout: default
title: Making Models Unmergeable via Scaling-Sensitive Loss Landscape
---

# Making Models Unmergeable via Scaling-Sensitive Loss Landscape
**arXiv**：[2601.21898v1](https://arxiv.org/abs/2601.21898) · [PDF](https://arxiv.org/pdf/2601.21898.pdf)  
**作者**：Minwoo Jang, Hoyoung Kim, Jabin Koo, Jungseul Ok  

**一句话要点**：提出Trap²框架，通过缩放敏感损失景观使模型不可合并，以解决模型合并中的治理缺口问题。

**关键词**：模型合并保护, 权重缩放, 损失景观, 架构无关防御, 微调安全

## 3 点简述
- 核心问题：模型中心化导致下游用户可未经授权合并权重，绕过安全对齐或许可条款，现有防御方法多为事后且架构特定，保护不一致。
- 方法要点：Trap²为架构无关保护框架，在微调期间通过权重重缩放作为合并过程代理，编码保护到更新中，保持独立使用有效但合并时性能下降。
- 实验或效果：未知具体实验细节，但声称能有效防止未经授权的模型合并，适用于适配器或完整模型发布格式。

## 摘要（原文）

> The rise of model hubs has made it easier to access reusable model components, making model merging a practical tool for combining capabilities. Yet, this modularity also creates a \emph{governance gap}: downstream users can recompose released weights into unauthorized mixtures that bypass safety alignment or licensing terms. Because existing defenses are largely post-hoc and architecture-specific, they provide inconsistent protection across diverse architectures and release formats in practice. To close this gap, we propose \textsc{Trap}$^{2}$, an architecture-agnostic protection framework that encodes protection into the update during fine-tuning, regardless of whether they are released as adapters or full models. Instead of relying on architecture-dependent approaches, \textsc{Trap}$^{2}$ uses weight re-scaling as a simple proxy for the merging process. It keeps released weights effective in standalone use, but degrades them under re-scaling that often arises in merging, undermining unauthorized merging.

