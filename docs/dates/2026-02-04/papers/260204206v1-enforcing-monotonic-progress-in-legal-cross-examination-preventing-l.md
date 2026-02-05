---
layout: default
title: Enforcing Monotonic Progress in Legal Cross-Examination: Preventing Long-Horizon Stagnation in LLM-Based Inquiry
---

# Enforcing Monotonic Progress in Legal Cross-Examination: Preventing Long-Horizon Stagnation in LLM-Based Inquiry
**arXiv**：[2602.04206v1](https://arxiv.org/abs/2602.04206) · [PDF](https://arxiv.org/pdf/2602.04206.pdf)  
**作者**：Hsien-Jyh Liao  

**一句话要点**：提出Soft-FSM架构，通过外部状态控制器在基于LLM的法律交叉询问中强制单调进展，解决程序停滞问题。

**关键词**：法律交叉询问, 长时程任务, 程序停滞, 神经符号架构, 外部状态控制, 单调进展

## 3 点简述
- 核心问题：LLM在长时程任务中易出现程序停滞，无法确保在约束下可靠推进。
- 方法要点：采用神经符号架构，利用外部确定性状态控制器基于关键信息单元强制单调进展。
- 实验或效果：在台湾刑事凶杀案实验中，基线方法完成度低于40%，Soft-FSM达97%以上且冗余近零。

## 摘要（原文）

> Large language models (LLMs) exhibit impressive linguistic fluency but struggle to reliably complete long-horizon tasks under explicit procedural constraints. In legal cross-examination, purely proba-bilistic generation often maintains behavioral coherence while failing to ensure procedural advancement. We characterize this failure as procedural stagnation and propose Soft-FSM, a neuro-symbolic architecture that enforces monotonic progress over accumulated Key Information Units (KIUs) via an external deterministic state controller. Experiments on three real-world Taiwanese criminal homicide cases show that baseline methods collapse below 40% completeness, while Soft-FSM consistently achieves over 97% with near-zero redundancy. These results suggest that, in such domains, reliable task completion cannot be guaranteed by emergent LLM behavior alone, and can be reliably enforced through explicit and verifiable external state control.

