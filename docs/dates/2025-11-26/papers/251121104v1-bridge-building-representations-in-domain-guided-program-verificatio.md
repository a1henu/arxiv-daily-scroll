---
layout: default
title: BRIDGE: Building Representations In Domain Guided Program Verification
---

# BRIDGE: Building Representations In Domain Guided Program Verification
**arXiv**：[2511.21104v1](https://arxiv.org/abs/2511.21104) · [PDF](https://arxiv.org/pdf/2511.21104.pdf)  
**作者**：Robert Joseph George, Carson Eisenach, Udaya Ghai, Dominique Perrault-Joncas, Anima Anandkumar, Dean Foster  

**一句话要点**：提出BRIDGE结构化提示方法以提升可扩展的验证程序生成

**关键词**：程序验证, 结构化提示, 大语言模型, 代码生成, 规范驱动推理, 证明导向推理

## 3 点简述
- 核心问题：大语言模型在程序验证中难以扩展，需同时处理代码、规范和证明
- 方法要点：将验证分解为代码、规范和证明三个领域，引导不同推理行为作为中间表示
- 实验或效果：在Lean4中代码正确性提升近1.5倍，推理效率提高2倍，Python编码通过率提升17.5%

## 摘要（原文）

> Large language models (LLMs) have achieved impressive results in code generation, yet struggle with program verification, especially in interactive proof frameworks such as Lean4. A central challenge is scalability: verified synthesis requires not just code, but also precise specifications and correctness proofs, and existing approaches rarely span all three domains. We present BRIDGE, the first systematic study of structured prompting for scalable verified program generation. BRIDGE decomposes verification into three interconnected domains: Code (executable implementations), Specifications (formal intent statements), and Proofs (constructive correctness arguments). Our key idea is to elicit distinct reasoning behaviors functional, specification-driven, and proof-oriented as intermediate representations that preserve semantic structure and connect these domains. Through systematic ablations, we show that this approach substantially improves both accuracy and efficiency beyond standard error feedback methods. For example, functional reasoning improves correctness of code in formal languages (Lean4) by nearly 1.5x (pass@5) over direct baselines. In inference-time compute, functional reasoning is also 2x more efficient, achieving higher pass rates with fewer generations and lower total sampling budgets. Similarly, we find that specification-driven prompting boosts Python coding pass rates by up to 17.5%. These findings suggest that structured domain alignment is a promising direction for advancing verified synthesis. BRIDGE establishes a foundation for training via expert iteration or RLVR, enabling models to internalize these reasoning strategies across code, specifications, and proofs.

