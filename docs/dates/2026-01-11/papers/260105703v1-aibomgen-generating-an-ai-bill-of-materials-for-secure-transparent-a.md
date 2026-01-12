---
layout: default
title: AIBoMGen: Generating an AI Bill of Materials for Secure, Transparent, and Compliant Model Training
---

# AIBoMGen: Generating an AI Bill of Materials for Secure, Transparent, and Compliant Model Training
**arXiv**：[2601.05703v1](https://arxiv.org/abs/2601.05703) · [PDF](https://arxiv.org/pdf/2601.05703.pdf)  
**作者**：Wiebe Vandendriessche, Jordi Thijsman, Laurens D'hooge, Bruno Volckaert, Merlijn Sebrechts  

**一句话要点**：提出AIBoMGen平台以自动化生成AI物料清单，确保模型训练的安全、透明与合规。

**关键词**：AI物料清单, 模型透明度, 安全合规, 自动化生成, 加密验证, 训练平台

## 3 点简述
- 核心问题：AI系统快速发展，缺乏确保透明度、安全性和合规性的工具。
- 方法要点：扩展SBOM为AIBOM，通过自动化平台捕获数据集、模型元数据和环境细节，使用加密哈希和数字签名确保完整性。
- 实验或效果：评估显示AIBoMGen能可靠检测未授权修改，生成AIBOM时性能开销可忽略。

## 摘要（原文）

> The rapid adoption of complex AI systems has outpaced the development of tools to ensure their transparency, security, and regulatory compliance. In this paper, the AI Bill of Materials (AIBOM), an extension of the Software Bill of Materials (SBOM), is introduced as a standardized, verifiable record of trained AI models and their environments. Our proof-of-concept platform, AIBoMGen, automates the generation of signed AIBOMs by capturing datasets, model metadata, and environment details during training. The training platform acts as a neutral, third-party observer and root of trust. It enforces verifiable AIBOM creation for every job. The system uses cryptographic hashing, digital signatures, and in-toto attestations to ensure integrity and protect against threats such as artifact tampering by dishonest model creators. Our evaluation demonstrates that AIBoMGen reliably detects unauthorized modifications to all artifacts and can generate AIBOMs with negligible performance overhead. These results highlight the potential of AIBoMGen as a foundational step toward building secure and transparent AI ecosystems, enabling compliance with regulatory frameworks like the EUs AI Act.

