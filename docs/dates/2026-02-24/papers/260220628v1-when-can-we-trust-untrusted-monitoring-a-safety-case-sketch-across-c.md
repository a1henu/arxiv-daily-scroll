---
layout: default
title: When can we trust untrusted monitoring? A safety case sketch across collusion strategies
---

# When can we trust untrusted monitoring? A safety case sketch across collusion strategies
**arXiv**：[2602.20628v1](https://arxiv.org/abs/2602.20628) · [PDF](https://arxiv.org/pdf/2602.20628.pdf)  
**作者**：Nelson Gardner-Challis, Jonathan Bostock, Georgiy Kozhevnikov, Morgan Sinclaire, Joan Velja, Alessandro Abate, Charlie Griffin  

**一句话要点**：提出基于预部署测试的安全案例框架，以评估不可信监控在不同合谋策略下的安全性

**关键词**：不可信监控, AI安全, 合谋策略, 安全案例, 预部署测试, AI控制

## 3 点简述
- 核心问题：不可信监控部署中，如何证明安全性以避免AI误对齐导致灾难性风险
- 方法要点：放宽对AI合谋策略的假设，构建涵盖被动自识别、因果合谋、非因果合谋的分类法
- 实验或效果：识别被动自识别可能更有效的条件，并突出未解决的挑战以推动更稳健评估

## 摘要（原文）

> AIs are increasingly being deployed with greater autonomy and capabilities, which increases the risk that a misaligned AI may be able to cause catastrophic harm. Untrusted monitoring -- using one untrusted model to oversee another -- is one approach to reducing risk. Justifying the safety of an untrusted monitoring deployment is challenging because developers cannot safely deploy a misaligned model to test their protocol directly. In this paper, we develop upon existing methods for rigorously demonstrating safety based on pre-deployment testing. We relax assumptions that previous AI control research made about the collusion strategies a misaligned AI might use to subvert untrusted monitoring. We develop a taxonomy covering passive self-recognition, causal collusion (hiding pre-shared signals), acausal collusion (hiding signals via Schelling points), and combined strategies. We create a safety case sketch to clearly present our argument, explicitly state our assumptions, and highlight unsolved challenges. We identify conditions under which passive self-recognition could be a more effective collusion strategy than those studied previously. Our work builds towards more robust evaluations of untrusted monitoring.

