---
layout: default
title: TensorCommitments: A Lightweight Verifiable Inference for Language Models
---

# TensorCommitments: A Lightweight Verifiable Inference for Language Models
**arXiv**：[2602.12630v1](https://arxiv.org/abs/2602.12630) · [PDF](https://arxiv.org/pdf/2602.12630.pdf)  
**作者**：Oguzhan Baser, Elahe Sadeghi, Eric Wang, David Ribeiro Alves, Sam Kazemian, Hong Kang, Sandeep P. Chinchali, Sriram Vishwanath  

**一句话要点**：提出TensorCommitments以实现轻量级可验证语言模型推理，解决云端LLM推理的信任问题。

**关键词**：可验证推理, 语言模型, 张量承诺, Terkle树, 轻量级验证, 抗攻击性

## 3 点简述
- 核心问题：云端LLM推理存在信任风险，用户需验证推理正确性，现有方法效率低或要求强验证器。
- 方法要点：基于张量原生承诺方案，通过多变量Terkle树绑定推理过程，生成防篡改标签。
- 实验或效果：在LLaMA2上，仅增加0.97%证明时间和0.12%验证时间，抗攻击能力提升达48%。

## 摘要（原文）

> Most large language models (LLMs) run on external clouds: users send a prompt, pay for inference, and must trust that the remote GPU executes the LLM without any adversarial tampering. We critically ask how to achieve verifiable LLM inference, where a prover (the service) must convince a verifier (the client) that an inference was run correctly without rerunning the LLM. Existing cryptographic works are too slow at the LLM scale, while non-cryptographic ones require a strong verifier GPU. We propose TensorCommitments (TCs), a tensor-native proof-of-inference scheme. TC binds the LLM inference to a commitment, an irreversible tag that breaks under tampering, organized in our multivariate Terkle Trees. For LLaMA2, TC adds only 0.97% prover and 0.12% verifier time over inference while improving robustness to tailored LLM attacks by up to 48% over the best prior work requiring a verifier GPU.

