---
layout: default
title: RobPI: Robust Private Inference against Malicious Client
---

# RobPI: Robust Private Inference against Malicious Client
**arXiv**：[2602.19918v1](https://arxiv.org/abs/2602.19918) · [PDF](https://arxiv.org/pdf/2602.19918.pdf)  
**作者**：Jiaqi Xue, Mengxin Zheng, Qian Lou  

**一句话要点**：提出RobPI协议以抵御恶意客户端的私有推理攻击

**关键词**：私有推理, 恶意客户端攻击, 加密噪声注入, 模型安全, 神经网络, 隐私保护

## 3 点简述
- 核心问题：现有私有推理协议假设半诚实威胁模型，但现实中客户端可能恶意操纵输出。
- 方法要点：RobPI通过加密兼容噪声注入logits和特征，增强协议安全性以抵御攻击。
- 实验效果：在多种神经网络和数据集上，RobPI显著降低攻击成功率并增加攻击所需查询次数。

## 摘要（原文）

> The increased deployment of machine learning inference in various applications has sparked privacy concerns. In response, private inference (PI) protocols have been created to allow parties to perform inference without revealing their sensitive data. Despite recent advances in the efficiency of PI, most current methods assume a semi-honest threat model where the data owner is honest and adheres to the protocol. However, in reality, data owners can have different motivations and act in unpredictable ways, making this assumption unrealistic. To demonstrate how a malicious client can compromise the semi-honest model, we first designed an inference manipulation attack against a range of state-of-the-art private inference protocols. This attack allows a malicious client to modify the model output with 3x to 8x fewer queries than current black-box attacks. Motivated by the attacks, we proposed and implemented RobPI, a robust and resilient private inference protocol that withstands malicious clients. RobPI integrates a distinctive cryptographic protocol that bolsters security by weaving encryption-compatible noise into the logits and features of private inference, thereby efficiently warding off malicious-client attacks. Our extensive experiments on various neural networks and datasets show that RobPI achieves ~91.9% attack success rate reduction and increases more than 10x the number of queries required by malicious-client attacks.

