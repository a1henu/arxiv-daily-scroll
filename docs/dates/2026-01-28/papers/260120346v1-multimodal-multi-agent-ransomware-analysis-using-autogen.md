---
layout: default
title: Multimodal Multi-Agent Ransomware Analysis Using AutoGen
---

# Multimodal Multi-Agent Ransomware Analysis Using AutoGen
**arXiv**：[2601.20346v1](https://arxiv.org/abs/2601.20346) · [PDF](https://arxiv.org/pdf/2601.20346.pdf)  
**作者**：Asifullah Khan, Aimen Wadood, Mubashar Iqbal, Umme Zahoora  

**一句话要点**：提出多模态多智能体勒索软件分析框架，结合静态、动态和网络数据提升分类性能。

**关键词**：勒索软件分类, 多模态融合, 智能体架构, 自编码器特征提取, Transformer分类器, 网络安全

## 3 点简述
- 核心问题：传统勒索软件检测方法单一，难以应对复杂威胁，导致分类准确率不足。
- 方法要点：采用多智能体架构，各智能体处理不同模态数据，通过自编码器提取特征并融合，结合Transformer分类器。
- 实验或效果：在大规模数据集上评估，Macro-F1提升至0.936，智能体反馈机制稳定收敛，复合得分约0.88。

## 摘要（原文）

> Ransomware has become one of the most serious cybersecurity threats causing major financial losses and operational disruptions worldwide.Traditional detection methods such as static analysis, heuristic scanning and behavioral analysis often fall short when used alone. To address these limitations, this paper presents multimodal multi agent ransomware analysis framework designed for ransomware classification. Proposed multimodal multiagent architecture combines information from static, dynamic and network sources. Each data type is handled by specialized agent that uses auto encoder based feature extraction. These representations are then integrated through a fusion agent. After that fused representation are used by transformer based classifier. It identifies the specific ransomware family. The agents interact through an interagent feedback mechanism that iteratively refines feature representations by suppressing low confidence information. The framework was evaluated on large scale datasets containing thousands of ransomware and benign samples. Multiple experiments were conducted on ransomware dataset. It outperforms single modality and nonadaptive fusion baseline achieving improvement of up to 0.936 in Macro-F1 for family classification and reducing calibration error. Over 100 epochs, the agentic feedback loop displays a stable monotonic convergence leading to over +0.75 absolute improvement in terms of agent quality and a final composite score of around 0.88 without fine tuning of the language models. Zeroday ransomware detection remains family dependent on polymorphism and modality disruptions. Confidence aware abstention enables reliable real world deployment by favoring conservativeand trustworthy decisions over forced classification. The findings indicate that proposed approach provides a practical andeffective path toward improving real world ransomware defense systems.

