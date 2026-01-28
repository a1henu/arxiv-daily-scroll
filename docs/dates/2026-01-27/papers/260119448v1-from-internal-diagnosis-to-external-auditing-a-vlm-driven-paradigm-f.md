---
layout: default
title: From Internal Diagnosis to External Auditing: A VLM-Driven Paradigm for Online Test-Time Backdoor Defense
---

# From Internal Diagnosis to External Auditing: A VLM-Driven Paradigm for Online Test-Time Backdoor Defense
**arXiv**：[2601.19448v1](https://arxiv.org/abs/2601.19448) · [PDF](https://arxiv.org/pdf/2601.19448.pdf)  
**作者**：Binyan Xu, Fan Yang, Xilin Dai, Di Tang, Kehuan Zhang  

**一句话要点**：提出PRISM框架，利用通用视觉语言模型作为外部语义审计器，以防御在线测试时后门攻击。

**关键词**：后门防御, 视觉语言模型, 在线测试时审计, 语义安全, 模型无关安全, 原型优化

## 3 点简述
- 核心问题：深度神经网络易受后门攻击，传统内部诊断方法因依赖受害模型参数而脆弱。
- 方法要点：通过混合VLM教师动态优化视觉原型，结合统计边界监控的自适应路由器实时校准阈值。
- 实验或效果：在17个数据集和11种攻击类型上评估，攻击成功率降至<1%，同时提升干净准确率。

## 摘要（原文）

> Deep Neural Networks remain inherently vulnerable to backdoor attacks. Traditional test-time defenses largely operate under the paradigm of internal diagnosis methods like model repairing or input robustness, yet these approaches are often fragile under advanced attacks as they remain entangled with the victim model's corrupted parameters. We propose a paradigm shift from Internal Diagnosis to External Semantic Auditing, arguing that effective defense requires decoupling safety from the victim model via an independent, semantically grounded auditor. To this end, we present a framework harnessing Universal Vision-Language Models (VLMs) as evolving semantic gatekeepers. We introduce PRISM (Prototype Refinement & Inspection via Statistical Monitoring), which overcomes the domain gap of general VLMs through two key mechanisms: a Hybrid VLM Teacher that dynamically refines visual prototypes online, and an Adaptive Router powered by statistical margin monitoring to calibrate gating thresholds in real-time. Extensive evaluation across 17 datasets and 11 attack types demonstrates that PRISM achieves state-of-the-art performance, suppressing Attack Success Rate to <1% on CIFAR-10 while improving clean accuracy, establishing a new standard for model-agnostic, externalized security.

