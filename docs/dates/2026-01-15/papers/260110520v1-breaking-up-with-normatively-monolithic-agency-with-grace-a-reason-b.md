---
layout: default
title: Breaking Up with Normatively Monolithic Agency with GRACE: A Reason-Based Neuro-Symbolic Architecture for Safe and Ethical AI Alignment
---

# Breaking Up with Normatively Monolithic Agency with GRACE: A Reason-Based Neuro-Symbolic Architecture for Safe and Ethical AI Alignment
**arXiv**：[2601.10520v1](https://arxiv.org/abs/2601.10520) · [PDF](https://arxiv.org/pdf/2601.10520.pdf)  
**作者**：Felix Jahn, Yannic Muskalla, Lisa Dargasz, Patrick Schramowski, Kevin Baum  

**一句话要点**：提出GRACE神经符号架构，通过解耦规范推理与决策制定，确保AI代理的安全与伦理对齐。

**关键词**：神经符号架构, 伦理对齐, 可解释AI, 规范推理, 安全AI

## 3 点简述
- 核心问题：AI代理自主性增强，需确保决策不仅有效，还符合规范伦理。
- 方法要点：GRACE架构包含道德模块、决策模块和守卫，基于理由形式化实现可解释性。
- 实验或效果：以LLM治疗助手为例，展示如何使利益相关者理解、质疑和改进代理行为。

## 摘要（原文）

> As AI agents become increasingly autonomous, widely deployed in consequential contexts, and efficacious in bringing about real-world impacts, ensuring that their decisions are not only instrumentally effective but also normatively aligned has become critical. We introduce a neuro-symbolic reason-based containment architecture, Governor for Reason-Aligned ContainmEnt (GRACE), that decouples normative reasoning from instrumental decision-making and can contain AI agents of virtually any design. GRACE restructures decision-making into three modules: a Moral Module (MM) that determines permissible macro actions via deontic logic-based reasoning; a Decision-Making Module (DMM) that encapsulates the target agent while selecting instrumentally optimal primitive actions in accordance with derived macro actions; and a Guard that monitors and enforces moral compliance. The MM uses a reason-based formalism providing a semantic foundation for deontic logic, enabling interpretability, contestability, and justifiability. Its symbolic representation enriches the DMM's informational context and supports formal verification and statistical guarantees of alignment enforced by the Guard. We demonstrate GRACE on an example of a LLM therapy assistant, showing how it enables stakeholders to understand, contest, and refine agent behavior.

