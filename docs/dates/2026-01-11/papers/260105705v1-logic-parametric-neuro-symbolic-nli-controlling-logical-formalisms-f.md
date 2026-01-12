---
layout: default
title: Logic-Parametric Neuro-Symbolic NLI: Controlling Logical Formalisms for Verifiable LLM Reasoning
---

# Logic-Parametric Neuro-Symbolic NLI: Controlling Logical Formalisms for Verifiable LLM Reasoning
**arXiv**：[2601.05705v1](https://arxiv.org/abs/2601.05705) · [PDF](https://arxiv.org/pdf/2601.05705.pdf)  
**作者**：Ali Farjami, Luca Redondi, Marco Valentino  

**一句话要点**：提出逻辑参数化神经符号NLI框架，通过控制逻辑形式主义实现可验证的LLM推理

**关键词**：神经符号推理, 逻辑参数化, 自然语言推理, 可验证推理, 高阶逻辑, 领域适应性

## 3 点简述
- 现有方法依赖固定逻辑形式主义，限制了神经符号NLI的鲁棒性和适应性
- 采用LogiKEy方法将经典和非经典逻辑嵌入高阶逻辑，实现逻辑作为可控组件的系统比较
- 实验表明逻辑内部策略能提升性能并生成更高效的混合证明，逻辑有效性具有领域依赖性

## 摘要（原文）

> Large language models (LLMs) and theorem provers (TPs) can be effectively combined for verifiable natural language inference (NLI). However, existing approaches rely on a fixed logical formalism, a feature that limits robustness and adaptability. We propose a logic-parametric framework for neuro-symbolic NLI that treats the underlying logic not as a static background, but as a controllable component. Using the LogiKEy methodology, we embed a range of classical and non-classical formalisms into higher-order logic (HOL), enabling a systematic comparison of inference quality, explanation refinement, and proof behavior. We focus on normative reasoning, where the choice of logic has significant implications. In particular, we compare logic-external approaches, where normative requirements are encoded via axioms, with logic-internal approaches, where normative patterns emerge from the logic's built-in structure. Extensive experiments demonstrate that logic-internal strategies can consistently improve performance and produce more efficient hybrid proofs for NLI. In addition, we show that the effectiveness of a logic is domain-dependent, with first-order logic favouring commonsense reasoning, while deontic and modal logics excel in ethical domains. Our results highlight the value of making logic a first-class, parametric element in neuro-symbolic architectures for more robust, modular, and adaptable reasoning.

