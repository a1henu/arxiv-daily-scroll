---
layout: default
title: Red-Teaming Claude Opus and ChatGPT-based Security Advisors for Trusted Execution Environments
---

# Red-Teaming Claude Opus and ChatGPT-based Security Advisors for Trusted Execution Environments
**arXiv**：[2602.19450v1](https://arxiv.org/abs/2602.19450) · [PDF](https://arxiv.org/pdf/2602.19450.pdf)  
**作者**：Kunal Mukherjee  

**一句话要点**：提出TEE-RedBench评估方法，以红队测试LLM助手在可信执行环境安全咨询中的风险

**关键词**：可信执行环境, 红队测试, 大型语言模型, 安全咨询, 威胁建模, 评估方法

## 3 点简述
- 核心问题：LLM助手在TEE安全咨询中可能产生幻觉、过度保证或对抗提示下不安全行为，带来社会技术风险
- 方法要点：开发TEE-RedBench方法，包括威胁模型、结构化提示套件和标注准则，评估技术正确性、接地性等维度
- 实验或效果：测试ChatGPT-5.2和Claude Opus-4.6，发现失败可跨模型转移达12.02%，提出LLM-in-the-loop管道减少失败80.62%

## 摘要（原文）

> Trusted Execution Environments (TEEs) (e.g., Intel SGX and ArmTrustZone) aim to protect sensitive computation from a compromised operating system, yet real deployments remain vulnerable to microarchitectural leakage, side-channel attacks, and fault injection. In parallel, security teams increasingly rely on Large Language Model (LLM) assistants as security advisors for TEE architecture review, mitigation planning, and vulnerability triage. This creates a socio-technical risk surface: assistants may hallucinate TEE mechanisms, overclaim guarantees (e.g., what attestation does and does not establish), or behave unsafely under adversarial prompting.
>   We present a red-teaming study of two prevalently deployed LLM assistants in the role of TEE security advisors: ChatGPT-5.2 and Claude Opus-4.6, focusing on the inherent limitations and transferability of prompt-induced failures across LLMs. We introduce TEE-RedBench, a TEE-grounded evaluation methodology comprising (i) a TEE-specific threat model for LLM-mediated security work, (ii) a structured prompt suite spanning SGX and TrustZone architecture, attestation and key management, threat modeling, and non-operational mitigation guidance, along with policy-bound misuse probes, and (iii) an annotation rubric that jointly measures technical correctness, groundedness, uncertainty calibration, refusal quality, and safe helpfulness. We find that some failures are not purely idiosyncratic, transferring up to 12.02% across LLM assistants, and we connect these outcomes to secure architecture by outlining an "LLM-in-the-loop" evaluation pipeline: policy gating, retrieval grounding, structured templates, and lightweight verification checks that, when combined, reduce failures by 80.62%.

