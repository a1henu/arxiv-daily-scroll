---
layout: default
title: Towards Privacy-Preserving LLM Inference via Collaborative Obfuscation (Technical Report)
---

# Towards Privacy-Preserving LLM Inference via Collaborative Obfuscation (Technical Report)
**arXiv**：[2603.01499v1](https://arxiv.org/abs/2603.01499) · [PDF](https://arxiv.org/pdf/2603.01499.pdf)  
**作者**：Yu Lin, Qizhi Zhang, Wenqiang Ruan, Daode Zhang, Jue Hong, Ye Wu, Hanning Xia, Yunlong Mao, Sheng Zhong  

**一句话要点**：提出AloePri方法，通过协同混淆保护云LLM推理中的隐私，满足工业应用需求。

**关键词**：隐私保护推理, 协同混淆, LLM工业应用, 云服务安全, 模型兼容性

## 3 点简述
- 核心问题：现有隐私保护LLM推理方法难以同时满足工业场景的准确性、效率和兼容性要求。
- 方法要点：采用协同混淆技术，联合变换数据和模型参数，以最小化精度损失并确保隐私。
- 实验或效果：在Deepseek-V3.1-Terminus模型上评估，精度损失0.0%~3.5%，效率接近明文推理，能抵抗先进攻击。

## 摘要（原文）

> The rapid development of large language models (LLMs) has driven the widespread adoption of cloud-based LLM inference services, while also bringing prominent privacy risks associated with the transmission and processing of private data in remote inference. For privacy-preserving LLM inference technologies to be practically applied in industrial scenarios, three core requirements must be satisfied simultaneously: (1) Accuracy and efficiency losses should be minimized to mitigate degradation in service experience. (2) The inference process can be run on large-scale clusters consist of heterogeneous legacy xPUs. (3) Compatibility with existing LLM infrastructures should be ensured to reuse their engineering optimizations. To the best of our knowledge, none of the existing privacy-preserving LLM inference methods satisfy all the above constraints while delivering meaningful privacy guarantees. In this paper, we propose AloePri, the first privacy-preserving LLM inference method for industrial applications. AloePri protects both the input and output data by covariant obfuscation, which jointly transforms data and model parameters to achieve better accuracy and privacy. We carefully design the transformation for each model component to ensure inference accuracy and data privacy while keeping full compatibility with existing infrastructures of Language Model as a Service. AloePri has been integrated into an industrial system for the evaluation of mainstream LLMs. The evaluation on Deepseek-V3.1-Terminus model (671B parameters) demonstrates that AloePri causes accuracy loss of 0.0%~3.5% and exhibits efficiency equivalent to that of plaintext inference. Meanwhile, AloePri successfully resists state-of-the-art attacks, with less than 5\% of tokens recovered. To the best of our knowledge, AloePri is the first method to exhibit practical applicability to large-scale models in real-world systems.

