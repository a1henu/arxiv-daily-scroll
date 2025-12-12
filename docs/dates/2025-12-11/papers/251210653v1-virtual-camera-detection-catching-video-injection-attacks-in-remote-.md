---
layout: default
title: Virtual camera detection: Catching video injection attacks in remote biometric systems
---

# Virtual camera detection: Catching video injection attacks in remote biometric systems
**arXiv**：[2512.10653v1](https://arxiv.org/abs/2512.10653) · [PDF](https://arxiv.org/pdf/2512.10653.pdf)  
**作者**：Daniyar Kurmankhojayev, Andrei Shadrikov, Dmitrii Gordin, Mikhail Shkorin, Danijar Gabdullin, Aigerim Kambetbayeva, Kanat Kuatov  

**一句话要点**：提出基于机器学习的虚拟摄像头检测方法，以增强远程生物认证系统的视频注入攻击防御。

**关键词**：虚拟摄像头检测, 视频注入攻击, 面部反欺骗, 远程生物认证, 机器学习模型, 元数据分析

## 3 点简述
- 核心问题：视频注入攻击（如深度伪造和虚拟摄像头软件）威胁远程面部识别系统的完整性。
- 方法要点：基于真实用户会话收集的元数据训练机器学习模型，实现虚拟摄像头检测。
- 实验或效果：实证结果显示该方法能有效识别视频注入尝试，降低恶意用户绕过反欺骗系统的风险。

## 摘要（原文）

> Face anti-spoofing (FAS) is a vital component of remote biometric authentication systems based on facial recognition, increasingly used across web-based applications. Among emerging threats, video injection attacks -- facilitated by technologies such as deepfakes and virtual camera software -- pose significant challenges to system integrity. While virtual camera detection (VCD) has shown potential as a countermeasure, existing literature offers limited insight into its practical implementation and evaluation. This study introduces a machine learning-based approach to VCD, with a focus on its design and validation. The model is trained on metadata collected during sessions with authentic users. Empirical results demonstrate its effectiveness in identifying video injection attempts and reducing the risk of malicious users bypassing FAS systems.

