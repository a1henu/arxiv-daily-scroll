---
layout: default
title: A Real-Time Privacy-Preserving Behavior Recognition System via Edge-Cloud Collaboration
---

# A Real-Time Privacy-Preserving Behavior Recognition System via Edge-Cloud Collaboration
**arXiv**：[2601.22938v1](https://arxiv.org/abs/2601.22938) · [PDF](https://arxiv.org/pdf/2601.22938.pdf)  
**作者**：Huan Song, Shuyu Tian, Junyi Hao, Cheng Yuan, Zhenyu Jia, Jiawei Shao, Xuelong Li  

**一句话要点**：提出基于边缘-云协作的隐私保护行为识别系统，以解决高隐私环境中的隐私-安全矛盾。

**关键词**：隐私保护行为识别, 边缘-云协作, AI Flow理论, 不可逆特征映射, 信息瓶颈理论, 异常行为检测

## 3 点简述
- 核心问题：传统RGB监控在隐私敏感环境中存在视觉记录和存储风险，现有隐私保护方法常牺牲语义理解或无法保证数学不可逆性。
- 方法要点：结合AI Flow理论框架，边缘设备通过非线性映射和随机噪声注入将原始图像转换为抽象特征向量，实现源脱敏和不可逆特征映射。
- 实验或效果：系统在边缘实现毫秒级处理，云端基于抽象向量进行异常行为检测，从架构层面切断隐私泄露路径，适用于高敏感公共空间风险管理。

## 摘要（原文）

> As intelligent sensing expands into high-privacy environments such as restrooms and changing rooms, the field faces a critical privacy-security paradox. Traditional RGB surveillance raises significant concerns regarding visual recording and storage, while existing privacy-preserving methods-ranging from physical desensitization to traditional cryptographic or obfuscation techniques-often compromise semantic understanding capabilities or fail to guarantee mathematical irreversibility against reconstruction attacks. To address these challenges, this study presents a novel privacy-preserving perception technology based on the AI Flow theoretical framework and an edge-cloud collaborative architecture. The proposed methodology integrates source desensitization with irreversible feature mapping. Leveraging Information Bottleneck theory, the edge device performs millisecond-level processing to transform raw imagery into abstract feature vectors via non-linear mapping and stochastic noise injection. This process constructs a unidirectional information flow that strips identity-sensitive attributes, rendering the reconstruction of original images impossible. Subsequently, the cloud platform utilizes multimodal family models to perform joint inference solely on these abstract vectors to detect abnormal behaviors. This approach fundamentally severs the path to privacy leakage at the architectural level, achieving a breakthrough from video surveillance to de-identified behavior perception and offering a robust solution for risk management in high-sensitivity public spaces.

