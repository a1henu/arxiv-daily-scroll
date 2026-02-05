---
layout: default
title: Cascading Robustness Verification: Toward Efficient Model-Agnostic Certification
---

# Cascading Robustness Verification: Toward Efficient Model-Agnostic Certification
**arXiv**：[2602.04236v1](https://arxiv.org/abs/2602.04236) · [PDF](https://arxiv.org/pdf/2602.04236.pdf)  
**作者**：Mohammadreza Maleki, Rushendra Sidibomma, Arman Adibi, Reza Samavi  

**一句话要点**：提出级联鲁棒性验证框架，以高效模型无关方式增强神经网络对抗样本的认证可靠性。

**关键词**：鲁棒性验证, 对抗样本, 模型无关认证, 级联框架, 计算效率优化

## 3 点简述
- 核心问题：单一不完整验证器可能低估鲁棒性，因近似松散或与训练方法不匹配。
- 方法要点：级联应用多个验证器，从低成本开始，一旦认证即停止，平衡紧致性与计算成本。
- 实验或效果：理论分析显示验证精度不低于基准，实证中认证输入数相当，运行效率提升高达约90%。

## 摘要（原文）

> Certifying neural network robustness against adversarial examples is challenging, as formal guarantees often require solving non-convex problems. Hence, incomplete verifiers are widely used because they scale efficiently and substantially reduce the cost of robustness verification compared to complete methods. However, relying on a single verifier can underestimate robustness because of loose approximations or misalignment with training methods. In this work, we propose Cascading Robustness Verification (CRV), which goes beyond an engineering improvement by exposing fundamental limitations of existing robustness metric and introducing a framework that enhances both reliability and efficiency. CRV is a model-agnostic verifier, meaning that its robustness guarantees are independent of the model's training process. The key insight behind the CRV framework is that, when using multiple verification methods, an input is certifiably robust if at least one method certifies it as robust. Rather than relying solely on a single verifier with a fixed constraint set, CRV progressively applies multiple verifiers to balance the tightness of the bound and computational cost. Starting with the least expensive method, CRV halts as soon as an input is certified as robust; otherwise, it proceeds to more expensive methods. For computationally expensive methods, we introduce a Stepwise Relaxation Algorithm (SR) that incrementally adds constraints and checks for certification at each step, thereby avoiding unnecessary computation. Our theoretical analysis demonstrates that CRV achieves equal or higher verified accuracy compared to powerful but computationally expensive incomplete verifiers in the cascade, while significantly reducing verification overhead. Empirical results confirm that CRV certifies at least as many inputs as benchmark approaches, while improving runtime efficiency by up to ~90%.

