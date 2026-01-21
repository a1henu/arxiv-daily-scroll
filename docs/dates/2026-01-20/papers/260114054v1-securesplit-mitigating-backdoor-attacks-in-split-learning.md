---
layout: default
title: SecureSplit: Mitigating Backdoor Attacks in Split Learning
---

# SecureSplit: Mitigating Backdoor Attacks in Split Learning
**arXiv**：[2601.14054v1](https://arxiv.org/abs/2601.14054) · [PDF](https://arxiv.org/pdf/2601.14054.pdf)  
**作者**：Zhihao Dou, Dongfei Cui, Weida Wang, Anjun Gao, Yueyang Quan, Mengyao Ma, Viet Vo, Guangdong Bai, Zhuqing Liu, Minghong Fang  

**一句话要点**：提出SecureSplit以解决分割学习中的后门攻击问题

**关键词**：分割学习, 后门攻击, 安全防御, 嵌入过滤, 协作训练

## 3 点简述
- 分割学习易受后门攻击，恶意客户端通过嵌入触发模型漏洞
- 采用维度变换增强良性/中毒嵌入差异，结合多数投票过滤污染嵌入
- 在四个数据集、五种攻击场景和七种防御对比中验证有效性

## 摘要（原文）

> Split Learning (SL) offers a framework for collaborative model training that respects data privacy by allowing participants to share the same dataset while maintaining distinct feature sets. However, SL is susceptible to backdoor attacks, in which malicious clients subtly alter their embeddings to insert hidden triggers that compromise the final trained model. To address this vulnerability, we introduce SecureSplit, a defense mechanism tailored to SL. SecureSplit applies a dimensionality transformation strategy to accentuate subtle differences between benign and poisoned embeddings, facilitating their separation. With this enhanced distinction, we develop an adaptive filtering approach that uses a majority-based voting scheme to remove contaminated embeddings while preserving clean ones. Rigorous experiments across four datasets (CIFAR-10, MNIST, CINIC-10, and ImageNette), five backdoor attack scenarios, and seven alternative defenses confirm the effectiveness of SecureSplit under various challenging conditions.

