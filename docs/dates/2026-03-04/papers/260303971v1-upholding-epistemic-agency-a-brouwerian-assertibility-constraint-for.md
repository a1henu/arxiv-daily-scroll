---
layout: default
title: Upholding Epistemic Agency: A Brouwerian Assertibility Constraint for Responsible AI
---

# Upholding Epistemic Agency: A Brouwerian Assertibility Constraint for Responsible AI
**arXiv**：[2603.03971v1](https://arxiv.org/abs/2603.03971) · [PDF](https://arxiv.org/pdf/2603.03971.pdf)  
**作者**：Michael Jülich  

**一句话要点**：提出基于Brouwer可断言性约束的负责任AI框架，以在高风险领域保护认知主体性。

**关键词**：负责任AI, 认知主体性, 可断言性约束, 高风险领域, 公开证书, 接口语义

## 3 点简述
- 核心问题：生成式AI将不确定性转化为权威性断言，削弱民主认知主体性。
- 方法要点：引入三状态接口语义（断言、否认、未确定），要求系统提供公开可检视的证书。
- 实验或效果：通过决策层门控和输出契约实现，确保输出基于可挑战的凭证而非仅置信度。

## 摘要（原文）

> Generative AI can convert uncertainty into authoritative-seeming verdicts, displacing the justificatory work on which democratic epistemic agency depends. As a corrective, I propose a Brouwer-inspired assertibility constraint for responsible AI: in high-stakes domains, systems may assert or deny claims only if they can provide a publicly inspectable and contestable certificate of entitlement; otherwise they must return "Undetermined". This constraint yields a three-status interface semantics (Asserted, Denied, Undetermined) that cleanly separates internal entitlement from public standing while connecting them via the certificate as a boundary object. It also produces a time-indexed entitlement profile that is stable under numerical refinement yet revisable as the public record changes. I operationalize the constraint through decision-layer gating of threshold and argmax outputs, using internal witnesses (e.g., sound bounds or separation margins) and an output contract with reason-coded abstentions. A design lemma shows that any total, certificate-sound binary interface already decides the deployed predicate on its declared scope, so "Undetermined" is not a tunable reject option but a mandatory status whenever no forcing witness is available. By making outputs answerable to challengeable warrants rather than confidence alone, the paper aims to preserve epistemic agency where automated speech enters public justification.

