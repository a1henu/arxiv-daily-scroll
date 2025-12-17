---
layout: default
title: Black-Box Auditing of Quantum Model: Lifted Differential Privacy with Quantum Canaries
---

# Black-Box Auditing of Quantum Model: Lifted Differential Privacy with Quantum Canaries
**arXiv**：[2512.14388v1](https://arxiv.org/abs/2512.14388) · [PDF](https://arxiv.org/pdf/2512.14388.pdf)  
**作者**：Baobao Song, Shiva Raj Pokhrel, Athanasios V. Vasilakos, Tianqing Zhu, Gang Li  

**一句话要点**：提出基于提升量子差分隐私的黑盒审计框架，以量子金丝雀检测量子机器学习模型中的隐私泄露。

**关键词**：量子机器学习, 差分隐私, 隐私审计, 量子金丝雀, 黑盒验证, 隐私泄露检测

## 3 点简述
- 量子机器学习模型可能记忆敏感数据，缺乏实证隐私验证工具。
- 利用量子金丝雀（偏移编码量子态）检测记忆化并量化训练中的隐私泄露。
- 在模拟和物理量子硬件上评估，有效测量实际隐私损失，验证隐私保障。

## 摘要（原文）

> Quantum machine learning (QML) promises significant computational advantages, yet models trained on sensitive data risk memorizing individual records, creating serious privacy vulnerabilities. While Quantum Differential Privacy (QDP) mechanisms provide theoretical worst-case guarantees, they critically lack empirical verification tools for deployed models. We introduce the first black-box privacy auditing framework for QML based on Lifted Quantum Differential Privacy, leveraging quantum canaries (strategically offset-encoded quantum states) to detect memorization and precisely quantify privacy leakage during training. Our framework establishes a rigorous mathematical connection between canary offset and trace distance bounds, deriving empirical lower bounds on privacy budget consumption that bridge the critical gap between theoretical guarantees and practical privacy verification. Comprehensive evaluations across both simulated and physical quantum hardware demonstrate our framework's effectiveness in measuring actual privacy loss in QML models, enabling robust privacy verification in QML systems.

