---
layout: default
title: Protecting the Undeleted in Machine Unlearning
---

# Protecting the Undeleted in Machine Unlearning
**arXiv**：[2602.16697v1](https://arxiv.org/abs/2602.16697) · [PDF](https://arxiv.org/pdf/2602.16697.pdf)  
**作者**：Aloni Cohen, Refael Kohen, Kobbi Nissim, Uri Stemmer  

**一句话要点**：提出新安全定义以保护未删除数据在机器遗忘中的隐私风险

**关键词**：机器遗忘, 隐私保护, 安全定义, 数据重建攻击, 完美重训练

## 3 点简述
- 揭示完美重训练方法对未删除数据的隐私威胁，允许攻击者通过删除请求重建数据集
- 分析现有机器遗忘定义易受攻击或功能受限，如精确求和
- 提出新安全定义，保护未删除数据免受删除操作泄漏，支持公告板、求和等基本功能

## 摘要（原文）

> Machine unlearning aims to remove specific data points from a trained model, often striving to emulate "perfect retraining", i.e., producing the model that would have been obtained had the deleted data never been included. We demonstrate that this approach, and security definitions that enable it, carry significant privacy risks for the remaining (undeleted) data points. We present a reconstruction attack showing that for certain tasks, which can be computed securely without deletions, a mechanism adhering to perfect retraining allows an adversary controlling merely $ω(1)$ data points to reconstruct almost the entire dataset merely by issuing deletion requests. We survey existing definitions for machine unlearning, showing they are either susceptible to such attacks or too restrictive to support basic functionalities like exact summation. To address this problem, we propose a new security definition that specifically safeguards undeleted data against leakage caused by the deletion of other points. We show that our definition permits several essential functionalities, such as bulletin boards, summations, and statistical learning.

