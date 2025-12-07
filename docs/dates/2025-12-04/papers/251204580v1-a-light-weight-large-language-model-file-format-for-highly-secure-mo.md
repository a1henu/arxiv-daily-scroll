---
layout: default
title: A Light-Weight Large Language Model File Format for Highly-Secure Model Distribution
---

# A Light-Weight Large Language Model File Format for Highly-Secure Model Distribution
**arXiv**：[2512.04580v1](https://arxiv.org/abs/2512.04580) · [PDF](https://arxiv.org/pdf/2512.04580.pdf)  
**作者**：Huifeng Zhu, Shijie Li, Qinfeng Li, Yier Jin  

**一句话要点**：提出CryptoTensors格式以解决大语言模型在部署和分发中的安全保密问题

**关键词**：大语言模型安全, 模型分发格式, 张量加密, 访问控制, 轻量级部署

## 3 点简述
- 核心问题：现有模型格式缺乏对机密性、访问控制或可信硬件集成的内置支持，导致模型权重保护不足
- 方法要点：基于Safetensors扩展，引入张量级加密和嵌入式访问控制策略，支持透明解密和自动密钥管理
- 实验或效果：实现概念验证库，在序列化和运行时场景中基准测试，验证与Hugging Face Transformers和vLLM等框架的兼容性

## 摘要（原文）

> To enhance the performance of large language models (LLMs) in various domain-specific applications, sensitive data such as healthcare, law, and finance are being used to privately customize or fine-tune these models. Such privately adapted LLMs are regarded as either personal privacy assets or corporate intellectual property. Therefore, protecting model weights and maintaining strict confidentiality during deployment and distribution have become critically important. However, existing model formats and deployment frameworks provide little to no built-in support for confidentiality, access control, or secure integration with trusted hardware. Current methods for securing model deployment either rely on computationally expensive cryptographic techniques or tightly controlled private infrastructure. Although these approaches can be effective in specific scenarios, they are difficult and costly for widespread deployment.
>   In this paper, we introduce CryptoTensors, a secure and format-compatible file structure for confidential LLM distribution. Built as an extension to the widely adopted Safetensors format, CryptoTensors incorporates tensor-level encryption and embedded access control policies, while preserving critical features such as lazy loading and partial deserialization. It enables transparent decryption and automated key management, supporting flexible licensing and secure model execution with minimal overhead. We implement a proof-of-concept library, benchmark its performance across serialization and runtime scenarios, and validate its compatibility with existing inference frameworks, including Hugging Face Transformers and vLLM. Our results highlight CryptoTensors as a light-weight, efficient, and developer-friendly solution for safeguarding LLM weights in real-world and widespread deployments.

