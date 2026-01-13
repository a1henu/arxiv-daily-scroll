---
layout: default
title: Towards Automating Blockchain Consensus Verification with IsabeLLM
---

# Towards Automating Blockchain Consensus Verification with IsabeLLM
**arXiv**：[2601.07654v1](https://arxiv.org/abs/2601.07654) · [PDF](https://arxiv.org/pdf/2601.07654.pdf)  
**作者**：Elliot Jones, William Knottenbelt  

**一句话要点**：提出IsabeLLM工具，集成Isabelle与大型语言模型以自动化区块链共识协议的形式化验证。

**关键词**：区块链共识验证, 形式化验证, Isabelle证明助手, 大型语言模型, 自动化证明

## 3 点简述
- 核心问题：区块链共识协议的形式化验证需高专业度与努力，常被开发过程忽略。
- 方法要点：IsabeLLM结合Isabelle证明助手与大型语言模型，辅助并自动化证明生成。
- 实验或效果：使用DeepSeek R1 API，成功为比特币工作量证明协议的非平凡引理生成正确证明。

## 摘要（原文）

> Consensus protocols are crucial for a blockchain system as they are what allow agreement between the system's nodes in a potentially adversarial environment. For this reason, it is paramount to ensure their correct design and implementation to prevent such adversaries from carrying out malicious behaviour. Formal verification allows us to ensure the correctness of such protocols, but requires high levels of effort and expertise to carry out and thus is often omitted in the development process. In this paper, we present IsabeLLM, a tool that integrates the proof assistant Isabelle with a Large Language Model to assist and automate proofs. We demonstrate the effectiveness of IsabeLLM by using it to develop a novel model of Bitcoin's Proof of Work consensus protocol and verify its correctness. We use the DeepSeek R1 API for this demonstration and found that we were able to generate correct proofs for each of the non-trivial lemmas present in the verification.

