---
layout: default
title: Privacy-Preserving AI-Enabled Decentralized Learning and Employment Records System
---

# Privacy-Preserving AI-Enabled Decentralized Learning and Employment Records System
**arXiv**：[2601.02720v1](https://arxiv.org/abs/2601.02720) · [PDF](https://arxiv.org/pdf/2601.02720.pdf)  
**作者**：Yuqiao Xu, Mina Namazi, Sahith Reddy Jalapally, Osama Zafar, Youngjin Yoo, Erman Ayday  

**一句话要点**：提出隐私保护AI驱动的去中心化学习与就业记录系统，以解决自动化技能凭证生成和隐私保护问题。

**关键词**：隐私保护AI, 去中心化学习记录系统, 可信执行环境, 自然语言处理, 技能凭证生成, 选择性披露

## 3 点简述
- 现有区块链平台缺乏自动化技能凭证生成和非结构化学习证据整合能力。
- 系统在可信执行环境中使用NLP管道分析记录，生成可验证技能凭证，并实现选择性披露。
- NLP组件评估显示技能映射稳定，安全分析证明凭证不可伪造且敏感信息保密。

## 摘要（原文）

> Learning and Employment Record (LER) systems are emerging as critical infrastructure for securely compiling and sharing educational and work achievements. Existing blockchain-based platforms leverage verifiable credentials but typically lack automated skill-credential generation and the ability to incorporate unstructured evidence of learning. In this paper,a privacy-preserving, AI-enabled decentralized LER system is proposed to address these gaps. Digitally signed transcripts from educational institutions are accepted, and verifiable self-issued skill credentials are derived inside a trusted execution environment (TEE) by a natural language processing pipeline that analyzes formal records (e.g., transcripts, syllabi) and informal artifacts. All verification and job-skill matching are performed inside the enclave with selective disclosure, so raw credentials and private keys remain enclave-confined. Job matching relies solely on attested skill vectors and is invariant to non-skill resume fields, thereby reducing opportunities for screening bias.The NLP component was evaluated on sample learner data; the mapping follows the validated Syllabus-to-O*NET methodology,and a stability test across repeated runs observed <5% variance in top-ranked skills. Formal security statements and proof sketches are provided showing that derived credentials are unforgeable and that sensitive information remains confidential. The proposed system thus supports secure education and employment credentialing, robust transcript verification,and automated, privacy-preserving skill extraction within a decentralized framework.

